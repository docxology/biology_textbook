"""Tests for template WIP resolver smoke gate."""

from __future__ import annotations

from pathlib import Path

from biology.quality.wip_resolver_smoke import run_wip_resolver_smoke


def test_run_wip_resolver_smoke_finds_biology_textbook() -> None:
    project_root = Path(__file__).resolve().parent.parent
    resolved = run_wip_resolver_smoke(project_root)
    assert resolved.name == "biology_textbook"
    assert resolved.is_dir()


def test_run_wip_resolver_smoke_raises_when_template_missing(tmp_path: Path, monkeypatch) -> None:
    import pytest

    monkeypatch.setattr("textbook_paths.discover_template_root", lambda _cwd: None)
    with pytest.raises(AssertionError, match="template infrastructure not found"):
        run_wip_resolver_smoke(tmp_path)

def test_run_wip_resolver_smoke_raises_when_no_candidate_root_resolves(
    tmp_path: Path, monkeypatch
) -> None:
    """A shadow root that does not resolve this tree must fail closed."""
    import pytest

    fake_template = tmp_path / "template"
    (fake_template / "infrastructure" / "validation").mkdir(parents=True)
    (fake_template / "infrastructure" / "rendering").mkdir(parents=True)
    monkeypatch.setattr(
        "textbook_paths.discover_template_root", lambda _cwd: fake_template
    )
    monkeypatch.setattr("textbook_paths.PROJECT", tmp_path / "nowhere")
    with pytest.raises(AssertionError, match="unexpected project root"):
        run_wip_resolver_smoke(tmp_path)
