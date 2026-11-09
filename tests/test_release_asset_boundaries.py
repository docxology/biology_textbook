"""Renderer export refuses traversal, aliases and altered committed-source bytes."""
from __future__ import annotations

import hashlib
import json
import shutil
from pathlib import Path

import pytest

from biology.pipeline.release_assets import _renderer_sources


@pytest.fixture
def renderer_snapshot(tmp_path: Path) -> Path:
    root = tmp_path / "renderer"
    files = []
    for name in ("LICENSE", "pyproject.toml", "infrastructure/rendering/core.py"):
        path = root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        body = ("synthetic renderer fixture: " + name).encode()
        path.write_bytes(body)
        files.append({"path": name, "bytes": len(body), "sha256": hashlib.sha256(body).hexdigest()})
    (root / "source_manifest.json").write_text(json.dumps({"source_commit": "a" * 40, "files": files}))
    return root

@pytest.mark.parametrize("attack", ["parent", "absolute", "duplicate", "symlink", "hardlink"])
def test_export_refuses_uncontained_or_aliased_members(renderer_snapshot: Path, attack: str) -> None:
    root = renderer_snapshot
    manifest_path = root / "source_manifest.json"
    manifest = json.loads(manifest_path.read_text())
    outside = root.parent / "private.txt"
    body = b"private fixture must not enter an exported renderer"
    outside.write_bytes(body)
    if attack == "duplicate":
        member = dict(manifest["files"][0])
    else:
        name = "../private.txt" if attack == "parent" else str(outside)
        if attack in ("symlink", "hardlink"):
            link = root / "linked.txt"
            if attack == "symlink":
                link.symlink_to(outside)
            else:
                link.hardlink_to(outside)
            name = "linked.txt"
        member = {"path": name, "bytes": len(body), "sha256": hashlib.sha256(body).hexdigest()}
    manifest["files"].append(member)
    manifest_path.write_text(json.dumps(manifest))
    with pytest.raises(ValueError):
        _renderer_sources(root)
    assert outside.read_bytes() == body


def test_export_refuses_bytes_changed_since_snapshot(renderer_snapshot: Path) -> None:
    (renderer_snapshot / "infrastructure/rendering/core.py").write_bytes(b"altered after source capture")
    with pytest.raises(ValueError):
        _renderer_sources(renderer_snapshot)


@pytest.fixture
def export_project(tmp_path: Path, renderer_snapshot: Path) -> Path:
    """Synthetic receipt/artifact inputs test export policy, not PDF-render success."""
    import subprocess

    from biology.pipeline.release_assets import sha256_file, source_state

    root = tmp_path / "project"
    root.mkdir()
    sources = {
        ".gitignore": "output/\n",
        "pyproject.toml": '[project]\nversion = "2.0.0"\n',
        "docs/manuscript/config.yaml": 'book:\n  edition: "1.1"\n',
        "LICENSE": "Synthetic code-license fixture\n",
        "LICENSE-CONTENT": "Synthetic content-license fixture\n",
    }
    for name, body in sources.items():
        path = root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(body)
    for args in (("init", "--initial-branch=main"), ("add", "."), ("-c", "user.name=Fixture", "-c", "user.email=fixture@example.invalid", "commit", "-m", "public fixture")):
        subprocess.run(["git", "-C", str(root), *args], check=True, capture_output=True, stdin=subprocess.DEVNULL)
    pdf = root / "output/pdf/biology_textbook_combined.pdf"
    pdf.parent.mkdir(parents=True)
    pdf.write_bytes(b"synthetic artifact fixture, not a rendered PDF")
    state = source_state(root)
    receipt = root / "output/publication_readiness/receipt.json"
    receipt.parent.mkdir(parents=True)
    receipt.write_text(json.dumps({
        "full": True, "failures": 0, "status": "completed",
        "renderer_manifest_before": sha256_file(renderer_snapshot / "source_manifest.json"),
        "renderer_manifest_after": sha256_file(renderer_snapshot / "source_manifest.json"),
        "source_before": state, "source_after": state,
        "artifacts": {"output/pdf/biology_textbook_combined.pdf": sha256_file(pdf)},
    }))
    return root


@pytest.mark.parametrize("change", ["source", "committed-source", "artifact", "renderer", "renderer-bytes", "omitted-runtime", "interrupted-receipt"])
def test_export_refuses_stale_or_incomplete_proof_before_creating_destination(
    export_project: Path, renderer_snapshot: Path, change: str,
) -> None:
    from biology.pipeline.release_assets import build_release_assets

    root = export_project
    if change == "source":
        (root / "unreviewed.py").write_text("unreviewed = True\n")
    elif change == "committed-source":
        import subprocess

        (root / "reviewed.py").write_text("changed = True\n")
        for args in (("add", "reviewed.py"), ("-c", "user.name=Fixture", "-c", "user.email=fixture@example.invalid", "commit", "-m", "new source")):
            subprocess.run(["git", "-C", str(root), *args], check=True, capture_output=True, stdin=subprocess.DEVNULL)
    elif change == "artifact":
        (root / "output/pdf/biology_textbook_combined.pdf").write_bytes(b"different artifact")
    elif change == "renderer":
        manifest = renderer_snapshot / "source_manifest.json"
        record = json.loads(manifest.read_text())
        record["source_commit"] = "b" * 40
        manifest.write_text(json.dumps(record))
    elif change == "renderer-bytes":
        (renderer_snapshot / "infrastructure/rendering/core.py").write_bytes(b"unverified renderer with unchanged manifest")
    elif change == "omitted-runtime":
        (renderer_snapshot / "infrastructure/rendering/extra.lua").write_bytes(b"return {}")
    else:
        receipt = root / "output/publication_readiness/receipt.json"
        value = json.loads(receipt.read_text())
        value["status"] = "running"
        receipt.write_text(json.dumps(value))
    destination = root / "output/release"
    with pytest.raises(ValueError):
        build_release_assets(root, destination, renderer_snapshot)
    assert not destination.exists()


def test_export_cannot_hide_dirty_sources_in_a_config_selected_clean_worktree(
    export_project: Path, renderer_snapshot: Path, tmp_path: Path,
) -> None:
    import subprocess

    from biology.pipeline.release_assets import build_release_assets

    clean_copy = tmp_path / "clean-worktree"
    subprocess.run(["git", "clone", "--no-hardlinks", str(export_project), str(clean_copy)],
                   check=True, capture_output=True, stdin=subprocess.DEVNULL)
    (export_project / "LICENSE").write_text("Unvalidated live license, absent from the recorded commit.\n")
    subprocess.run(["git", "-C", str(export_project), "config", "core.worktree", str(clean_copy)],
                   check=True, capture_output=True, stdin=subprocess.DEVNULL)
    destination = export_project / "output" / "config-worktree-release"
    with pytest.raises(ValueError, match="clean validated main"):
        build_release_assets(export_project, destination, renderer_snapshot)
    assert not destination.exists()


def test_executable_bundle_excludes_private_refs_and_survives_source_removal(
    export_project: Path, renderer_snapshot: Path, tmp_path: Path, monkeypatch: pytest.MonkeyPatch,
) -> None:
    import runpy
    import subprocess
    import zipfile

    from biology.pipeline.release_assets import build_release_assets

    root = export_project
    def git(*args: str) -> str:
        return subprocess.run(["git", "-C", str(root), *args], check=True, capture_output=True, text=True, stdin=subprocess.DEVNULL).stdout.strip()

    public = git("rev-parse", "HEAD")
    git("switch", "--create", "private-unreleased")
    (root / "private.txt").write_text("private fixture must not be exported\n")
    git("add", "private.txt")
    git("-c", "user.name=Fixture", "-c", "user.email=fixture@example.invalid", "commit", "-m", "private fixture")
    private = git("rev-parse", "HEAD")
    git("switch", "main")
    assets = build_release_assets(root, root / "output/release", renderer_snapshot)
    extracted = tmp_path / "extracted"
    with zipfile.ZipFile(assets.executable_bundle) as archive:
        archive.extract("source.bundle", extracted)
        archive.extract("REPRODUCE.py", extracted)
    root.rename(tmp_path / "preserved-source")
    # The bundle advertises only main, not HEAD. Host defaultBranch is unrelated.
    monkeypatch.setenv("GIT_CONFIG_COUNT", "1")
    monkeypatch.setenv("GIT_CONFIG_KEY_0", "init.defaultBranch")
    monkeypatch.setenv("GIT_CONFIG_VALUE_0", "recipient-default-not-main")
    runner = runpy.run_path(str(extracted / "REPRODUCE.py"))
    clone = runner["restore_project"](extracted)
    restored = subprocess.run(["git", "-C", str(clone), "rev-parse", "HEAD"], check=True, capture_output=True, text=True, stdin=subprocess.DEVNULL).stdout.strip()
    private_object = subprocess.run(["git", "-C", str(clone), "cat-file", "-e", private], check=False, capture_output=True, stdin=subprocess.DEVNULL)
    assert restored == public
    assert private_object.returncode != 0
    assert not (clone / "private.txt").exists()


@pytest.mark.parametrize("name", [
    "infrastructure/validation/content/validator_math.py",
    "infrastructure/rendering/filters/equations.lua",
    "infrastructure/rendering/templates/header.tex",
    "infrastructure/rendering/__pycache__/core.cpython-315.pyc",
])
def test_export_refuses_unlisted_runtime_files(renderer_snapshot: Path, name: str) -> None:
    path = renderer_snapshot / name
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(b"unlisted runtime fixture")
    with pytest.raises(ValueError, match="complete shipped runtime tree"):
        _renderer_sources(renderer_snapshot)


def test_export_refuses_omitted_member_still_present_on_disk(renderer_snapshot: Path) -> None:
    manifest_path = renderer_snapshot / "source_manifest.json"
    manifest = json.loads(manifest_path.read_text())
    manifest["files"] = [item for item in manifest["files"] if item["path"] != "infrastructure/rendering/core.py"]
    manifest_path.write_text(json.dumps(manifest))
    with pytest.raises(ValueError, match="complete shipped runtime tree"):
        _renderer_sources(renderer_snapshot)


@pytest.mark.parametrize("alias", ["output", "release-parent", "release"])
def test_export_refuses_output_alias_without_touching_target(
    export_project: Path, renderer_snapshot: Path, tmp_path: Path, alias: str,
) -> None:
    from biology.pipeline.release_assets import build_release_assets

    root = export_project
    unrelated = tmp_path / "unrelated"
    unrelated.mkdir()
    sentinel = unrelated / "sentinel"
    sentinel.write_bytes(b"preserve unrelated output")
    if alias == "output":
        (root / "output").rename(root / "preserved-output")
        (root / "output").symlink_to(unrelated, target_is_directory=True)
        destination = root / "output/release"
    elif alias == "release-parent":
        (root / "output/alias").symlink_to(unrelated, target_is_directory=True)
        destination = root / "output/alias/release"
    else:
        destination = root / "output/release"
        destination.symlink_to(unrelated, target_is_directory=True)
    with pytest.raises(ValueError):
        build_release_assets(root, destination, renderer_snapshot)
    assert sentinel.read_bytes() == b"preserve unrelated output"
    assert sorted(path.name for path in unrelated.iterdir()) == ["sentinel"]


def test_export_preserves_occupied_destination(export_project: Path, renderer_snapshot: Path) -> None:
    from biology.pipeline.release_assets import build_release_assets

    destination = export_project / "output/release"
    destination.mkdir()
    sentinel = destination / "sentinel"
    sentinel.write_bytes(b"existing release")
    with pytest.raises(FileExistsError):
        build_release_assets(export_project, destination, renderer_snapshot)
    assert sentinel.read_bytes() == b"existing release"


@pytest.mark.parametrize("relation", ["equal", "descendant"])
def test_export_refuses_output_in_renderer_before_writing(
    export_project: Path, renderer_snapshot: Path, relation: str,
) -> None:
    from biology.pipeline.release_assets import build_release_assets

    renderer = export_project / "output" / "renderer"
    shutil.copytree(renderer_snapshot, renderer)
    before = {path.relative_to(renderer): path.read_bytes()
              for path in renderer.rglob("*") if path.is_file()}
    destination = renderer if relation == "equal" else renderer / "releases" / "candidate"
    with pytest.raises(ValueError, match="renderer"):
        build_release_assets(export_project, destination, renderer)
    assert {path.relative_to(renderer): path.read_bytes()
            for path in renderer.rglob("*") if path.is_file()} == before
    if relation == "descendant":
        assert not destination.exists()


@pytest.mark.parametrize("operation", ["state", "restore"])
def test_explicit_source_and_restore_ignore_ambient_git_repository(
    export_project: Path, tmp_path: Path, monkeypatch: pytest.MonkeyPatch, operation: str,
) -> None:
    import runpy
    import subprocess

    from biology.pipeline.release_assets import _reproduction_runner, source_state

    def git(*args: str) -> str:
        return subprocess.run(["git", *args], check=True, capture_output=True, text=True,
                              stdin=subprocess.DEVNULL).stdout.strip()

    expected = source_state(export_project)
    unrelated = tmp_path / "unrelated-git"
    git("clone", "--no-hardlinks", str(export_project), str(unrelated))
    (unrelated / "UNRELATED.md").write_text("Do not bind or alter this independent repository.\n")
    git("-C", str(unrelated), "add", "UNRELATED.md")
    git("-C", str(unrelated), "-c", "user.name=Fixture", "-c", "user.email=fixture@example.invalid",
        "commit", "-m", "unrelated fixture")
    extraction = tmp_path / "extraction"
    extraction.mkdir()
    git("-C", str(export_project), "bundle", "create", str(extraction / "source.bundle"), "refs/heads/main")
    before = {path.relative_to(unrelated): path.read_bytes()
              for path in unrelated.rglob("*") if path.is_file()}
    for name, value in {"GIT_DIR": unrelated / ".git", "GIT_WORK_TREE": unrelated,
                        "GIT_COMMON_DIR": unrelated / ".git", "GIT_INDEX_FILE": unrelated / ".git/index"}.items():
        monkeypatch.setenv(name, str(value))
    if operation == "state":
        assert source_state(export_project) == expected
    else:
        runner = extraction / "REPRODUCE.py"
        runner.write_text(_reproduction_runner(str(expected["commit"])))
        namespace = runpy.run_path(str(runner))
        restored = namespace["restore_project"](extraction)
        assert (restored / "pyproject.toml").read_bytes() == (export_project / "pyproject.toml").read_bytes()
        assert not (restored / "UNRELATED.md").exists()
    assert {path.relative_to(unrelated): path.read_bytes()
            for path in unrelated.rglob("*") if path.is_file()} == before




@pytest.mark.parametrize("occupied", ["directory", "dangling-symlink"])
def test_runner_refuses_occupied_restoration_target(tmp_path: Path, occupied: str) -> None:
    import runpy

    from biology.pipeline.release_assets import _reproduction_runner

    target = tmp_path / "biology_textbook"
    if occupied == "directory":
        target.mkdir()
        (target / "sentinel").write_text("preserve")
    else:
        target.symlink_to(tmp_path / "absent")
    runner_path = tmp_path / "REPRODUCE.py"
    runner_path.write_text(_reproduction_runner("a" * 40))
    runner = runpy.run_path(str(runner_path))
    with pytest.raises(FileExistsError):
        runner["restore_project"](tmp_path)
    if occupied == "directory":
        assert (target / "sentinel").read_text() == "preserve"
    else:
        assert target.is_symlink()


def test_reproduction_bootstrap_preserves_containing_workspace_dependencies(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch,
) -> None:
    """Real npm may clean only this checkout, even inside another workspace."""
    import os
    import runpy
    import subprocess
    import sys

    from biology.pipeline.release_assets import _reproduction_runner

    if not shutil.which("uv") or not shutil.which("npm"):
        pytest.skip("Native uv and npm are required for the bootstrap containment regression")
    for name in tuple(os.environ):
        if name.upper().startswith("NPM_CONFIG_") and name.upper() not in {"NPM_CONFIG_CACHE", "NPM_CONFIG_OFFLINE"}:
            monkeypatch.delenv(name)
    npm_config = tmp_path / "empty-npmrc"
    npm_config.write_text("")
    monkeypatch.setenv("NPM_CONFIG_USERCONFIG", str(npm_config))
    monkeypatch.setenv("NPM_CONFIG_GLOBALCONFIG", str(tmp_path / "absent-global-npmrc"))
    monkeypatch.setenv("NPM_CONFIG_OFFLINE", "true")
    outer = tmp_path / "outer"
    project = outer / "release" / "biology_textbook"
    sibling = outer / "sibling"
    project.mkdir(parents=True)
    sibling.mkdir()
    for directory, metadata in (
        (outer, {"name": "outer-fixture", "version": "1.0.0", "private": True,
                 "workspaces": ["release/biology_textbook", "sibling"]}),
        (project, {"name": "restored-textbook-fixture", "version": "1.0.0", "private": True}),
        (sibling, {"name": "unrelated-sibling-fixture", "version": "1.0.0", "private": True}),
    ):
        (directory / "package.json").write_text(json.dumps(metadata))
    (project / "pyproject.toml").write_text(
        '[project]\nname="bootstrap-fixture"\nversion="1.0.0"\nrequires-python=">=3.11"\n'
        '[project.optional-dependencies]\ndev=[]\n'
    )
    for command in (
        ["uv", "lock", "--project", str(project), "--no-config", "--offline", "--python", sys.executable],
        ["npm", "--prefix", str(project), "install", "--package-lock-only", "--ignore-scripts", "--no-audit", "--no-fund"],
        ["npm", "--prefix", str(outer), "install", "--package-lock-only", "--ignore-scripts", "--no-audit", "--no-fund"],
    ):
        subprocess.run(command, cwd=project, check=True, capture_output=True, text=True,
                       stdin=subprocess.DEVNULL, timeout=60)
    sentinels = []
    for directory in (outer, sibling, project):
        sentinel = directory / "node_modules" / "preserve-fixture" / "sentinel"
        sentinel.parent.mkdir(parents=True)
        sentinel.write_bytes(b"existing local dependency work")
        sentinels.append(sentinel)
    prior_lock = (outer / "package-lock.json").read_bytes()
    runner_path = tmp_path / "REPRODUCE.py"
    runner_path.write_text(_reproduction_runner("a" * 40))
    runner = runpy.run_path(str(runner_path))
    runner["bootstrap_project"](project, tmp_path / "renderer-not-used-by-bootstrap")
    assert not sentinels[2].exists(), "The real scoped npm ci must actually clean its own stale installation"
    assert sentinels[0].read_bytes() == b"existing local dependency work"
    assert sentinels[1].read_bytes() == b"existing local dependency work"
    assert (outer / "package-lock.json").read_bytes() == prior_lock


def test_standalone_lock_ignores_an_untrusted_containing_uv_workspace(tmp_path: Path) -> None:
    """The real standalone metadata must select its own valid frozen lock."""
    import subprocess
    import sys

    if not shutil.which("uv"):
        pytest.skip("Native uv is required for the standalone lock-root regression")
    source = Path(__file__).resolve().parents[1]
    outer = tmp_path / "outer-uv-workspace"
    project = outer / "release" / "biology_textbook"
    project.mkdir(parents=True)
    for name in ("pyproject.toml", "uv.lock"):
        shutil.copyfile(source / name, project / name)
    (outer / "pyproject.toml").write_text(
        '[project]\nname="unrelated-outer-fixture"\nversion="1.0.0"\nrequires-python=">=3.11"\n'
        '[tool.uv.workspace]\nmembers=["release/*"]\n'
    )
    outside_lock = outer / "uv.lock"
    outside_lock.write_bytes(b"untrusted malformed ancestor lock [\n")
    own_before = (project / "uv.lock").read_bytes()
    outside_before = outside_lock.read_bytes()
    def validate(directory: Path) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            ["uv", "lock", "--project", str(directory), "--no-config", "--locked", "--offline", "--python", sys.executable],
            check=False, stdin=subprocess.DEVNULL, capture_output=True, text=True, timeout=60,
        )
    control = validate(outer)
    assert control.returncode != 0, "The untrusted outer lock must be a genuine rejecting control"
    result = validate(project)
    assert result.returncode == 0, result.stderr
    assert (project / "uv.lock").read_bytes() == own_before
    assert outside_lock.read_bytes() == outside_before
