"""Real disposable source/renderer fixtures exercise custody, not native PDF success.

The bounded fixture graph executes a Python renderer and writes actual artifact
bytes. Only graph selection and project/template paths are injected; Git state,
manifest verification, receipt writes and release export remain real.
"""
from __future__ import annotations

import hashlib
import json
import os
import shutil
import subprocess
import sys
import zipfile
from pathlib import Path

import pytest

from biology.pipeline.release_assets import (
    build_release_assets,
    sha256_file,
    source_state,
)
from biology.quality import publication_gate as gate


@pytest.fixture
def publication_fixture(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> tuple[Path, Path]:
    root = tmp_path / "project"
    root.mkdir()
    # Losing this fixture's .git must not discover the enclosing checkout.
    monkeypatch.setenv("GIT_CEILING_DIRECTORIES", str(tmp_path))
    for name, body in {
        ".gitignore": "output/\n",
        "pyproject.toml": '[project]\nversion = "2.0.0"\n',
        "docs/manuscript/config.yaml": 'book:\n  edition: "1.1"\n',
        "LICENSE": "Synthetic code-license fixture\n",
        "LICENSE-CONTENT": "Synthetic content-license fixture\n",
    }.items():
        path = root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(body)
    for args in (("init", "--initial-branch=main"), ("add", "."), ("-c", "user.name=Fixture", "-c", "user.email=fixture@example.invalid", "-c", "commit.gpgsign=false", "commit", "-m", "fixture")):
        subprocess.run(["git", "-C", str(root), *args], check=True, capture_output=True, stdin=subprocess.DEVNULL)
    renderer = tmp_path / "renderer"
    files = []
    for name, payload in {
        "LICENSE": b"Synthetic renderer license fixture\n",
        "pyproject.toml": b'[project]\nname = "fixture-renderer"\n',
        "infrastructure/rendering/core.py": b'def render():\n    return b"synthetic rendered artifact, not a PDF"\n',
        "infrastructure/validation/content/validator_math.py": b"valid = True\n",
        "infrastructure/rendering/filters/equations.lua": b"return {}\n",
        "infrastructure/rendering/templates/header.tex": b"% synthetic fixture resource\n",
    }.items():
        path = renderer / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(payload)
        files.append({"path": name, "bytes": len(payload), "sha256": hashlib.sha256(payload).hexdigest()})
    (renderer / "source_manifest.json").write_text(json.dumps({"source_commit": "a" * 40, "files": files}))
    pdf = root / "output/pdf/biology_textbook_combined.pdf"
    pdf.parent.mkdir(parents=True)
    pdf.write_bytes(b"old synthetic artifact")
    state = source_state(root)
    review = root / "output/publication_readiness"
    review.mkdir()
    digest = sha256_file(renderer / "source_manifest.json")
    (review / "receipt.json").write_text(json.dumps({
        "full": True, "status": "completed", "failures": 0,
        "source_before": state, "source_after": state,
        "renderer_manifest_before": digest, "renderer_manifest_after": digest,
        "artifacts": {"output/pdf/biology_textbook_combined.pdf": sha256_file(pdf)},
    }))
    monkeypatch.setattr(gate, "PROJECT", root)
    monkeypatch.setenv("BIOLOGY_TEXTBOOK_TEMPLATE_ROOT", str(renderer))
    monkeypatch.setattr(gate, "DEFAULT_REVIEW_ARTIFACT_DIR", review)
    return root, renderer


def _fixture_graph(monkeypatch: pytest.MonkeyPatch, root: Path, renderer: Path, tail: str = "") -> None:
    receipt = root / "output/publication_readiness/receipt.json"
    marker = root / "output/executed"
    pdf = root / "output/pdf/biology_textbook_combined.pdf"
    code = (
        "import json, runpy; from pathlib import Path; "
        f"assert json.loads(Path({str(receipt)!r}).read_text())['status'] == 'running'; "
        f"render = runpy.run_path({str(renderer / 'infrastructure/rendering/core.py')!r})['render']; "
        f"Path({str(pdf)!r}).write_bytes(render()); "
        f"Path({str(marker)!r}).touch(); " + tail
    )
    steps = [gate.CommandStep("fixture-render", (sys.executable, "-c", code), root)]
    monkeypatch.setattr(gate, "build_command_steps", lambda **kwargs: steps)
    monkeypatch.setattr(gate, "build_python_steps", lambda **kwargs: [])


@pytest.mark.parametrize("alias", ["output", "review", "receipt", "figures", "pdf"])
def test_gate_refuses_output_aliases_and_preserves_unrelated_targets(
    publication_fixture: tuple[Path, Path], tmp_path: Path, alias: str,
) -> None:
    root, _ = publication_fixture
    unrelated = tmp_path / "unrelated"
    unrelated.mkdir()
    sentinel = unrelated / "receipt.json"
    sentinel.write_bytes(b"unrelated receipt must survive")
    if alias == "receipt":
        target = root / "output/publication_readiness/receipt.json"
        target.unlink()
        target.symlink_to(sentinel)
    else:
        target = root / {"output": "output", "review": "output/publication_readiness", "figures": "output/figures", "pdf": "output/pdf"}[alias]
        if target.exists():
            target.rename(tmp_path / "preserved-output")
        target.symlink_to(unrelated, target_is_directory=True)
    with pytest.raises(ValueError):
        gate.run_publication_gate(full=True)
    assert sentinel.read_bytes() == b"unrelated receipt must survive"
    assert sorted(path.name for path in unrelated.iterdir()) == ["receipt.json"]


def test_gate_refuses_nonoutput_receipt_directory_without_writing(
    publication_fixture: tuple[Path, Path], tmp_path: Path,
) -> None:
    unrelated = tmp_path / "unrelated"
    unrelated.mkdir()
    with pytest.raises(ValueError):
        gate.run_publication_gate(full=True, artifact_dir=unrelated)
    assert not list(unrelated.iterdir())


@pytest.mark.parametrize("failure", ["invalid-selection", "missing-git", "missing-manifest", "tampered-renderer", "omitted-module"])
def test_preflight_failure_invalidates_old_pass_before_any_step(
    publication_fixture: tuple[Path, Path], monkeypatch: pytest.MonkeyPatch, tmp_path: Path, failure: str,
) -> None:
    root, renderer = publication_fixture
    _fixture_graph(monkeypatch, root, renderer)
    manifest_path = renderer / "source_manifest.json"
    original_manifest = manifest_path.read_bytes()
    core = renderer / "infrastructure/rendering/core.py"
    original_core = core.read_bytes()
    missing_path = tmp_path / "preserved-manifest.json"
    with monkeypatch.context() as ambient:
        if failure == "invalid-selection":
            ambient.setenv("BIOLOGY_TEXTBOOK_TEMPLATE_ROOT", str(tmp_path / "absent-renderer"))
        elif failure == "missing-git":
            ambient.setenv("PATH", str(tmp_path / "no-executables"))
        elif failure == "missing-manifest":
            manifest_path.rename(missing_path)
        elif failure == "tampered-renderer":
            core.write_bytes(b'def render():\n    return b"unverified"\n')
        else:
            manifest = json.loads(original_manifest)
            manifest["files"] = [item for item in manifest["files"] if not item["path"].endswith("validator_math.py")]
            manifest_path.write_text(json.dumps(manifest))
        with pytest.raises((OSError, ValueError)):
            gate.run_publication_gate(full=True)
    receipt = json.loads((root / "output/publication_readiness/receipt.json").read_text())
    assert receipt["status"] == "interrupted"
    assert receipt["failures"] == 1
    assert not (root / "output/executed").exists()
    # Restoring the transient prerequisite must not revive the preceding PASS.
    if missing_path.exists():
        missing_path.rename(manifest_path)
    else:
        manifest_path.write_bytes(original_manifest)
    core.write_bytes(original_core)
    with pytest.raises(ValueError, match="passing full publication receipt"):
        build_release_assets(root, root / "output/release", renderer)
    assert not (root / "output/release").exists()


@pytest.mark.parametrize("change", ["renderer-code", "unlisted-resource", "postflight-git"])
def test_postflight_exception_leaves_interrupted_nonpassing_evidence(
    publication_fixture: tuple[Path, Path], monkeypatch: pytest.MonkeyPatch, change: str,
) -> None:
    root, renderer = publication_fixture
    if change == "renderer-code":
        target = renderer / "infrastructure/rendering/core.py"
        tail = f"Path({str(target)!r}).write_bytes(b'changed after render')"
    elif change == "unlisted-resource":
        target = renderer / "infrastructure/rendering/templates/unlisted.tex"
        tail = f"Path({str(target)!r}).write_bytes(b'unlisted after render')"
    else:
        tail = f"Path({str(root / '.git')!r}).rename({str(root / 'output/preserved-git')!r})"
    _fixture_graph(monkeypatch, root, renderer, tail)
    with pytest.raises((OSError, ValueError, subprocess.CalledProcessError)):
        gate.run_publication_gate(full=True)
    receipt = json.loads((root / "output/publication_readiness/receipt.json").read_text())
    assert (root / "output/executed").is_file()
    assert receipt["status"] == "interrupted"
    assert receipt["failures"] == 1


def test_changed_manifest_identity_cannot_finish_with_a_pass(
    publication_fixture: tuple[Path, Path], monkeypatch: pytest.MonkeyPatch,
) -> None:
    root, renderer = publication_fixture
    manifest = renderer / "source_manifest.json"
    tail = (
        f"path = Path({str(manifest)!r}); record = json.loads(path.read_text()); "
        "record['source_commit'] = 'b' * 40; path.write_text(json.dumps(record))"
    )
    _fixture_graph(monkeypatch, root, renderer, tail)
    assert gate.run_publication_gate(full=True) == 1
    receipt = json.loads((root / "output/publication_readiness/receipt.json").read_text())
    assert receipt["status"] == "completed"
    assert receipt["failures"] == 1
    assert receipt["renderer_manifest_before"] != receipt["renderer_manifest_after"]
    with pytest.raises(ValueError, match="passing full publication receipt"):
        build_release_assets(root, root / "output/release", renderer)


def test_verified_fixture_gate_and_independent_export_keep_all_renderer_members(
    publication_fixture: tuple[Path, Path], monkeypatch: pytest.MonkeyPatch, tmp_path: Path,
) -> None:
    root, renderer = publication_fixture
    _fixture_graph(monkeypatch, root, renderer)
    assert gate.run_publication_gate(full=True) == 0
    receipt = json.loads((root / "output/publication_readiness/receipt.json").read_text())
    assert receipt["status"] == "completed"
    assert receipt["renderer_manifest_before"] == receipt["renderer_manifest_after"]
    assets = build_release_assets(root, root / "output/release", renderer)
    extracted = tmp_path / "independent-renderer"
    with zipfile.ZipFile(assets.executable_bundle) as archive:
        for name in archive.namelist():
            if name.startswith("renderer/"):
                archive.extract(name, extracted)
    from biology.pipeline.release_assets import _renderer_sources

    _, members = _renderer_sources(extracted / "renderer")
    assert {name for name, _, _ in members} == {
        path.relative_to(renderer).as_posix() for path in renderer.rglob("*") if path.is_file()
    }
    assert (root / "output/pdf/biology_textbook_combined.pdf").read_bytes() == b"synthetic rendered artifact, not a PDF"


@pytest.mark.parametrize("selection", ["missing", "non-template"])
def test_actual_cli_invalid_selection_invalidates_fixture_pass_and_blocks_export_after_restore(
    publication_fixture: tuple[Path, Path], monkeypatch: pytest.MonkeyPatch, tmp_path: Path, selection: str,
) -> None:
    root, renderer = publication_fixture
    source = Path(gate.__file__).resolve().parents[2]
    shutil.copytree(source, root / "src", ignore=shutil.ignore_patterns("__pycache__", "*.pyc", "*.egg-info"))
    scripts = root / "scripts"
    scripts.mkdir()
    for name in ("_bootstrap.py", "audit_publication_readiness.py"):
        shutil.copyfile(source.parent / "scripts" / name, scripts / name)
    for args in (("add", "."), ("-c", "user.name=Fixture", "-c", "user.email=fixture@example.invalid", "-c", "commit.gpgsign=false", "commit", "-m", "actual CLI fixture")):
        subprocess.run(["git", "-C", str(root), *args], check=True, capture_output=True, stdin=subprocess.DEVNULL)

    # Establish exporter acceptance using the real bounded fixture graph. These
    # artifact bytes exercise custody; they are deliberately not a native PDF.
    _fixture_graph(monkeypatch, root, renderer)
    assert gate.run_publication_gate(full=True) == 0
    build_release_assets(root, root / "output/release-before", renderer)
    state = source_state(root)
    pdf = root / "output/pdf/biology_textbook_combined.pdf"
    artifact = pdf.read_bytes()
    assert artifact == b"synthetic rendered artifact, not a PDF"
    marker = root / "output/executed"
    marker.unlink()
    receipt_path = root / "output/publication_readiness/receipt.json"
    invalid = tmp_path / "invalid-renderer"
    if selection == "non-template":
        invalid.mkdir()
    with monkeypatch.context() as ambient:
        ambient.setenv("BIOLOGY_TEXTBOOK_TEMPLATE_ROOT", str(invalid))
        result = subprocess.run(
            [sys.executable, str(scripts / "audit_publication_readiness.py"), "--check", "--full"],
            cwd=root, env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"},
            capture_output=True, text=True, check=False, stdin=subprocess.DEVNULL,
        )
    assert result.returncode != 0
    receipt = json.loads(receipt_path.read_text())
    assert receipt["full"] is True
    assert receipt["status"] == "interrupted", result.stderr
    assert receipt["failures"] == 1
    assert receipt["error_type"] == "ValueError"
    assert not marker.exists()
    assert source_state(root) == state
    assert pdf.read_bytes() == artifact
    # The valid selection is restored, but the failed attempt remains decisive.
    assert os.environ["BIOLOGY_TEXTBOOK_TEMPLATE_ROOT"] == str(renderer)
    with pytest.raises(ValueError, match="passing full publication receipt"):
        build_release_assets(root, root / "output/release-after", renderer)
    assert not (root / "output/release-after").exists()
