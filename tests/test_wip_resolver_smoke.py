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
