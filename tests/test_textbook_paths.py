"""Behavioral boundaries for explicitly selected rendering dependencies."""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

from textbook_paths import (
    SCRIPTS_DIR,
    SRC,
    discover_template_root,
    ensure_project_paths,
)


@pytest.fixture(autouse=True)
def clear_integration_selection(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("BIOLOGY_TEXTBOOK_TEMPLATE_ROOT", raising=False)


def template_checkout(path: Path) -> Path:
    (path / "infrastructure" / "validation").mkdir(parents=True)
    (path / "infrastructure" / "rendering").mkdir(parents=True)
    return path


def test_unrelated_neighbor_never_enters_import_resolution(tmp_path: Path) -> None:
    project = tmp_path / "biology_textbook"
    project.mkdir()
    template_checkout(tmp_path / "template")
    assert discover_template_root(project) is None


def test_actual_enclosing_template_is_recognized(tmp_path: Path) -> None:
    template = template_checkout(tmp_path / "template")
    project = template / "projects" / "biology_textbook"
    project.mkdir(parents=True)
    assert discover_template_root(project) == template


def test_explicit_dependency_is_authoritative(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    enclosing = template_checkout(tmp_path / "enclosing")
    project = enclosing / "projects" / "biology_textbook"
    project.mkdir(parents=True)
    selected = template_checkout(tmp_path / "selected")
    monkeypatch.setenv("BIOLOGY_TEXTBOOK_TEMPLATE_ROOT", str(selected))
    assert discover_template_root(project) == selected


def test_invalid_explicit_dependency_cannot_fall_back(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    enclosing = template_checkout(tmp_path / "enclosing")
    monkeypatch.setenv("BIOLOGY_TEXTBOOK_TEMPLATE_ROOT", str(tmp_path / "missing"))
    with pytest.raises(ValueError, match="BIOLOGY_TEXTBOOK_TEMPLATE_ROOT"):
        discover_template_root(enclosing)


def test_project_imports_precede_selected_dependency(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    selected = template_checkout(tmp_path / "selected")
    monkeypatch.setenv("BIOLOGY_TEXTBOOK_TEMPLATE_ROOT", str(selected))
    original = list(sys.path)
    try:
        sys.path[:] = [str(selected), *[p for p in sys.path if p != str(selected)]]
        ensure_project_paths(include_scripts=True)
        ensure_project_paths(include_scripts=True)
        assert sys.path.index(str(SRC)) < sys.path.index(str(selected))
        assert sys.path.index(str(SCRIPTS_DIR)) < sys.path.index(str(selected))
        assert sys.path.count(str(SRC)) == 1
    finally:
        sys.path[:] = original


def test_local_only_bootstrap_defers_invalid_selection_without_fallback(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch,
) -> None:
    missing = tmp_path / "missing"
    monkeypatch.setenv("BIOLOGY_TEXTBOOK_TEMPLATE_ROOT", str(missing))
    original = list(sys.path)
    try:
        ensure_project_paths(include_scripts=True, include_template=False)
        assert sys.path[:2] == [str(SRC), str(SCRIPTS_DIR)]
        assert str(missing) not in sys.path
        with pytest.raises(ValueError, match="BIOLOGY_TEXTBOOK_TEMPLATE_ROOT"):
            ensure_project_paths()
    finally:
        sys.path[:] = original
