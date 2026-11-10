"""Source-bound standalone release assets; no remote publication or registry writes."""
from __future__ import annotations

import hashlib
import json
import os
import stat
import subprocess
import tomllib
import zipfile
from dataclasses import dataclass
from pathlib import Path, PurePosixPath
from typing import IO

import yaml

from textbook_io import write_text_atomic
from textbook_paths import require_project_output_directory

_GIT_CONTEXT_VARIABLES = (
    "GIT_DIR", "GIT_WORK_TREE", "GIT_COMMON_DIR", "GIT_INDEX_FILE",
    "GIT_OBJECT_DIRECTORY", "GIT_ALTERNATE_OBJECT_DIRECTORIES", "GIT_NAMESPACE", "GIT_PREFIX",
)


def _git(root: Path, *args: str) -> str:
    # Bind the explicit project/worktree, including when local Git config names
    # another worktree. Preserve unrelated configuration, auth and transport.
    env = os.environ.copy()
    for name in _GIT_CONTEXT_VARIABLES:
        env.pop(name, None)
    env["GIT_OPTIONAL_LOCKS"] = "0"
    # A cached fsmonitor changed-path set cannot certify source cleanliness.
    result = subprocess.run(
        ["git", "-c", "core.fsmonitor=false", "-C", str(root), f"--work-tree={root.resolve()}", *args], stdin=subprocess.DEVNULL,
        capture_output=True, text=True, check=True,
        env=env,
    )
    return result.stdout.strip()


def source_state(root: Path) -> dict[str, str | bool]:
    """Capture Git identity and cleanliness, including unignored untracked sources."""
    return {
        "commit": _git(root, "rev-parse", "--verify", "HEAD"),
        "tree": _git(root, "rev-parse", "HEAD^{tree}"),
        "clean": not _git(root, "status", "--porcelain", "--untracked-files=all"),
    }


def sha256_file(path: Path) -> str:
    with path.open("rb") as stream:
        return hashlib.file_digest(stream, "sha256").hexdigest()


def _verified_copy(source: IO[bytes], target: IO[bytes], expected: str) -> None:
    digest = hashlib.sha256()
    while block := source.read(1024 * 1024):
        target.write(block)
        digest.update(block)
    if digest.hexdigest() != expected:
        raise ValueError("Artifact bytes changed or do not match their recorded SHA-256")


def _renderer_sources(root: Path) -> tuple[dict, list[tuple[str, Path, str]]]:
    """Verify the complete shipped tree, not only the manifest's chosen subset.

    No cache/code/resource exceptions are made: an unlisted file could satisfy an
    import or resource read during validation but disappear from the release ZIP.
    Bounds cover the installed committed snapshot without unbounded reads.
    """
    if root.is_symlink() or not root.is_dir():
        raise ValueError("The renderer root must be an independent directory")
    root = root.resolve()
    manifest_path = root / "source_manifest.json"
    manifest_stat = manifest_path.lstat()
    if not stat.S_ISREG(manifest_stat.st_mode) or manifest_stat.st_nlink != 1 or manifest_stat.st_size > 4 * 1024 * 1024:
        raise ValueError("The renderer manifest must be a bounded independent regular file")
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    entries = manifest["files"]
    if not isinstance(entries, list) or not 1 <= len(entries) <= 10000:
        raise ValueError("Renderer manifest file count is outside the supported bounds")
    members: list[tuple[str, Path, str]] = []
    seen: set[str] = set()
    total = 0
    for item in entries:
        name = item["path"]
        relative = PurePosixPath(name)
        path = root / relative
        if not name or "\\" in name or relative.as_posix() != name or relative.is_absolute() or ".." in relative.parts or name in seen or name == "source_manifest.json":
            raise ValueError("Unsafe or duplicate renderer manifest member")
        for parent in path.parents:
            if parent == root:
                break
            if parent.is_symlink():
                raise ValueError("Renderer directory aliases cannot certify source custody")
        member_stat = path.lstat()
        if not stat.S_ISREG(member_stat.st_mode) or not path.resolve().is_relative_to(root) or member_stat.st_nlink != 1:
            raise ValueError("Renderer members must be independent contained regular files")
        total += member_stat.st_size
        if member_stat.st_size > 64 * 1024 * 1024 or total > 512 * 1024 * 1024:
            raise ValueError("Renderer source size is outside the supported bounds")
        if member_stat.st_size != item["bytes"] or sha256_file(path) != item["sha256"]:
            raise ValueError("Renderer snapshot no longer matches its committed-source manifest")
        seen.add(name)
        members.append((name, path, item["sha256"]))
    actual: set[str] = set()

    def reject_unreadable(error: OSError) -> None:
        raise error

    for directory_count, (directory, directories, files) in enumerate(
        os.walk(root, followlinks=False, onerror=reject_unreadable), start=1,
    ):
        if directory_count > 10000:
            raise ValueError("Renderer directory count is outside the supported bounds")
        base = Path(directory)
        for name in directories:
            if (base / name).is_symlink():
                raise ValueError("Renderer directory aliases cannot certify source custody")
        for name in files:
            path = base / name
            info = path.lstat()
            if not stat.S_ISREG(info.st_mode) or info.st_nlink != 1:
                raise ValueError("Renderer tree contains a non-independent regular file")
            actual.add(path.relative_to(root).as_posix())
            if len(actual) > 10001:
                raise ValueError("Renderer tree file count is outside the supported bounds")
    if actual != seen | {"source_manifest.json"}:
        raise ValueError("Renderer manifest must cover the complete shipped runtime tree")
    if not {"LICENSE", "pyproject.toml"} <= seen or not any(name.startswith("infrastructure/rendering/") for name in seen):
        raise ValueError("A licensed committed rendering snapshot is required")
    members.append(("source_manifest.json", manifest_path, sha256_file(manifest_path)))
    return manifest, members


@dataclass(frozen=True)
class ReleaseAssets:
    version: str
    edition: str
    source_commit: str
    pdf: Path
    executable_bundle: Path
    checksums: Path
    provenance: Path


def build_release_assets(
    project: Path, destination: Path, renderer_root: Path, *, receipt: Path | None = None,
) -> ReleaseAssets:
    """Export validated main without overwriting assets or relying on another checkout.

    The executable ZIP includes a self-contained Git bundle of main, the frozen
    licensed renderer, its receipt, the instructor PDF and a real native runner.
    Failed construction leaves its new partial directory for inspection.
    """
    project = project.resolve()
    destination = require_project_output_directory(project, destination)
    if destination.is_relative_to(renderer_root.resolve()):
        raise ValueError("Release output must not be inside the frozen renderer snapshot")
    state = source_state(project)
    if not state["clean"] or state["commit"] != _git(project, "rev-parse", "refs/heads/main"):
        raise ValueError("Release assets require clean validated main")
    evidence = json.loads((receipt or project / "output/publication_readiness/receipt.json").read_text())
    if evidence.get("full") is not True or type(evidence.get("failures")) is not int or evidence["failures"] != 0 or evidence.get("status") != "completed":
        raise ValueError("A passing full publication receipt is required")
    if evidence.get("source_before") != state or evidence.get("source_after") != state:
        raise ValueError("Publication evidence belongs to different or dirty source")
    commit = str(state["commit"])
    metadata = tomllib.loads(_git(project, "show", f"{commit}:pyproject.toml"))["project"]
    config = yaml.safe_load(_git(project, "show", f"{commit}:docs/manuscript/config.yaml"))
    version = metadata["version"]
    edition = str(config["book"]["edition"])
    source_pdf = project / "output/pdf/biology_textbook_combined.pdf"
    expected_pdf = evidence.get("artifacts", {}).get("output/pdf/biology_textbook_combined.pdf")
    if not expected_pdf or sha256_file(source_pdf) != expected_pdf:
        raise ValueError("The instructor PDF is absent or differs from the validated artifact")
    renderer_manifest, renderer_members = _renderer_sources(renderer_root)
    renderer_digest = sha256_file(renderer_root / "source_manifest.json")
    if evidence.get("renderer_manifest_before") != renderer_digest or evidence.get("renderer_manifest_after") != renderer_digest:
        raise ValueError("The renderer snapshot differs from the one in the full validation receipt")
    destination.mkdir(parents=True, exist_ok=False)
    pdf = destination / source_pdf.name
    with source_pdf.open("rb") as source, pdf.open("xb") as target:
        _verified_copy(source, target, expected_pdf)
    source_bundle = destination / "source.bundle"
    _git(project, "bundle", "create", str(source_bundle), "refs/heads/main")
    _git(project, "bundle", "verify", str(source_bundle))
    if _git(project, "bundle", "list-heads", str(source_bundle), "refs/heads/main").split() != [commit, "refs/heads/main"]:
        raise ValueError("Main changed while capturing the validated Git bundle")
    provenance_data = {
        "schema": 1, "software_version": version, "manuscript_edition": edition,
        "source_commit": commit, "source_tree": state["tree"],
        "renderer_commit": renderer_manifest["source_commit"],
        "pdf_sha256": expected_pdf, "source_bundle_sha256": sha256_file(source_bundle),
        "licenses": {"code": "Apache-2.0", "manuscript": "CC-BY-4.0"},
        "zenodo_deposition": "No deposition for this edition is asserted",
        "verification": evidence,
    }
    provenance = destination / "release-provenance.json"
    write_text_atomic(provenance, json.dumps(provenance_data, indent=2) + "\n")
    runner = _reproduction_runner(commit)
    instructions = (
        f"# Biology Textbook v{version} — instructor edition {edition}\n\n"
        "Run `python3 REPRODUCE.py` in this extracted directory. It refuses an occupied "
        "`biology_textbook` destination, clones the included independent Git bundle, installs "
        "the locked Python/Node dependencies, and runs the complete native publication gate.\n\n"
        "Bootstrap pins npm's CLI prefix and uses the shipped standalone uv workspace root; "
        "a containing workspace supplies neither the lock nor the installation target.\n\n"
        "Prerequisites: Git, uv, a compatible Node/npm, Pandoc, XeLaTeX and Chrome/Chromium. "
        "The repository's optional .puppeteer.json currently targets macOS system Chrome; "
        "adjust that documented host configuration on other platforms. Dependencies may "
        "need network access; standard UV_OFFLINE/npm offline/cache settings are honored. "
        "No Docker execution or byte-identical cross-platform PDF is claimed.\n\n"
        "For same-host byte comparisons, preserve SOURCE_DATE_EPOCH and "
        "TEMPLATE_DETERMINISTIC from release-provenance.json's verification.runtime; "
        "different build-time inputs are not the same reproducibility experiment.\n\n"
        "The earlier template-only Docker wrapper is intentionally not retained. All required "
        "project sources and the committed rendering library are supplied here. The receipt "
        "is source-bound evidence, not an externally signed certification.\n"
    )
    executable_bundle = destination / f"biology_textbook_v{version}_executable_bundle.zip"
    with zipfile.ZipFile(executable_bundle, "x", compression=zipfile.ZIP_DEFLATED) as archive:
        files = [("source.bundle", source_bundle, sha256_file(source_bundle)),
                 ("artifacts/pdf/" + pdf.name, pdf, expected_pdf),
                 ("release-provenance.json", provenance, sha256_file(provenance))]
        files.extend(("renderer/" + name, path, digest) for name, path, digest in renderer_members)
        for name, path, digest in files:
            with path.open("rb") as source, archive.open(name, "w") as target:
                _verified_copy(source, target, digest)
        archive.writestr("REPRODUCE.py", runner)
        archive.writestr("README.md", instructions)
        archive.write(project / "LICENSE", "LICENSE")
        archive.write(project / "LICENSE-CONTENT", "LICENSE-CONTENT")
    checksums = destination / "SHA256SUMS"
    write_text_atomic(checksums, "".join(
        f"{sha256_file(path)}  {path.name}\n"
        for path in (pdf, executable_bundle, provenance, source_bundle)
    ))
    return ReleaseAssets(version, edition, commit, pdf, executable_bundle, checksums, provenance)


def _reproduction_runner(commit: str) -> str:
    return f'''"""Execute the complete standalone textbook reproduction, without another checkout."""
import os
import pathlib
import subprocess


def restore_project(here):
    project = here / "biology_textbook"
    if project.exists() or project.is_symlink():
        raise FileExistsError("Preserve the existing biology_textbook directory; use a fresh extraction")
    git_env = os.environ.copy()
    for name in {_GIT_CONTEXT_VARIABLES!r}:
        git_env.pop(name, None)
    git_env["GIT_OPTIONAL_LOCKS"] = "0"
    subprocess.run(["git", "clone", "--branch", "main", "--no-hardlinks", str(here / "source.bundle"), str(project)], env=git_env, check=True, stdin=subprocess.DEVNULL)
    actual = subprocess.run(["git", "-C", str(project), "rev-parse", "HEAD"], env=git_env, check=True, stdin=subprocess.DEVNULL, capture_output=True, text=True).stdout.strip()
    if actual != {commit!r}:
        raise ValueError("Bundled Git source does not match the validated release commit")
    return project


def reproduction_environment(project, renderer):
    env = os.environ.copy()
    for name in {_GIT_CONTEXT_VARIABLES!r}:
        env.pop(name, None)
    # Keep offline/index/cache policy, never inherited project/interpreter selectors.
    python_policy = {{"UV_PYTHON_CACHE_DIR", "UV_PYTHON_INSTALL_MIRROR", "UV_PYTHON_DOWNLOADS"}}
    for name in tuple(env):
        if (
            name.startswith(("PYTHON", "VIRTUAL_ENV", "CONDA", "_OLD_VIRTUAL", "UV_VENV"))
            or (name.startswith("UV_PYTHON") and name not in python_policy)
            or name in {{
                "UV_PROJECT", "UV_WORKING_DIR", "UV_WORKING_DIRECTORY", "UV_PROJECT_ENVIRONMENT",
                "UV_ENV_FILE", "UV_MANAGED_PYTHON", "UV_NO_MANAGED_PYTHON", "UV_SYSTEM_PYTHON",
                "UV_NO_PROJECT", "UV_NO_SYNC", "UV_FROZEN", "UV_ACTIVE", "UV_CONFIG_FILE",
                "__PYVENV_LAUNCHER__",
            }}
        ):
            env.pop(name)
    local = project / "output" / "reproduction"
    env.update({{
        "BIOLOGY_TEXTBOOK_TEMPLATE_ROOT": str(renderer),
        "UV_PROJECT_ENVIRONMENT": str(project / ".venv"), "UV_NO_ENV_FILE": "1",
        "TMPDIR": str(local / "tmp"), "MPLCONFIGDIR": str(local / "mpl"),
        "TEXMFVAR": str(local / "texmf-var"), "TEXMFCONFIG": str(local / "texmf-config"),
        "TEXMFCACHE": str(local / "texmf-cache"), "XDG_CACHE_HOME": str(local / "xdg-cache"),
        "PYTHONPYCACHEPREFIX": str(local / "pycache"), "PYTHONDONTWRITEBYTECODE": "1",
        "UV_LINK_MODE": "copy", "UV_PYTHON_INSTALL_DIR": str(local / "python"),
    }})
    env.setdefault("UV_CACHE_DIR", str(local / "uv-cache"))
    env.setdefault("NPM_CONFIG_CACHE", str(local / "npm-cache"))
    return env


def bootstrap_project(project, renderer):
    env = reproduction_environment(project, renderer)
    local = project / "output" / "reproduction"
    for name in ("tmp", "mpl", "texmf-var", "texmf-config", "texmf-cache", "xdg-cache", "pycache"):
        (local / name).mkdir(parents=True, exist_ok=True)
    for command in (["uv", "sync", "--project", str(project), "--no-config", "--locked", "--extra", "dev"], ["npm", "--prefix", str(project), "ci", "--ignore-scripts"]):
        subprocess.run(command, cwd=project, env=env, check=True, stdin=subprocess.DEVNULL)
    return env


def main():
    here = pathlib.Path(__file__).resolve().parent
    project = restore_project(here)
    env = bootstrap_project(project, here / "renderer")
    env["PATH"] = str(project / "node_modules" / ".bin") + os.pathsep + str(project / ".venv" / "bin") + os.pathsep + env["PATH"]
    subprocess.run([str(project / ".venv" / "bin" / "python"), "scripts/audit_publication_readiness.py", "--check", "--full"], cwd=project, env=env, check=True, stdin=subprocess.DEVNULL)


if __name__ == "__main__":
    main()
'''
