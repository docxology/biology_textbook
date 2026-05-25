"""Tests for checkout path discovery helpers."""

from __future__ import annotations

import sys
from pathlib import Path

from textbook_paths import (
    PROJECT,
    SCRIPTS_DIR,
    SRC,
    discover_template_root,
    ensure_project_paths,
    is_template_root,
    template_root,
)


def test_discovers_template_root_from_sibling_checkout(tmp_path: Path) -> None:
    project = tmp_path / "projects" / "passive" / "biology_textbook"
    project.mkdir(parents=True)
    template = tmp_path / "template"
    (template / "infrastructure" / "validation").mkdir(parents=True)
    (template / "infrastructure" / "rendering").mkdir(parents=True)

    assert discover_template_root(project) == template


def test_is_template_root_requires_validation_and_rendering(tmp_path: Path) -> None:
    root = tmp_path / "template"
    root.mkdir()
    assert not is_template_root(root)
    (root / "infrastructure" / "validation").mkdir(parents=True)
    assert not is_template_root(root)
    (root / "infrastructure" / "rendering").mkdir(parents=True)
    assert is_template_root(root)


def test_discover_template_root_honours_env_override(tmp_path: Path, monkeypatch) -> None:
    project = tmp_path / "biology_textbook"
    project.mkdir()
    template = tmp_path / "template"
    (template / "infrastructure" / "validation").mkdir(parents=True)
    (template / "infrastructure" / "rendering").mkdir(parents=True)
    monkeypatch.setenv("BIOLOGY_TEXTBOOK_TEMPLATE_ROOT", str(template))

    assert discover_template_root(project) == template


def test_ensure_project_paths_inserts_src_scripts_and_template(tmp_path: Path, monkeypatch) -> None:
    template = tmp_path / "template"
    (template / "infrastructure" / "validation").mkdir(parents=True)
    (template / "infrastructure" / "rendering").mkdir(parents=True)
    monkeypatch.setenv("BIOLOGY_TEXTBOOK_TEMPLATE_ROOT", str(template))
    for path in (str(SRC), str(SCRIPTS_DIR), str(template)):
        while path in sys.path:
            sys.path.remove(path)

    returned = ensure_project_paths(include_scripts=True)

    assert returned == PROJECT
    assert str(SRC) in sys.path
    assert str(SCRIPTS_DIR) in sys.path
    assert str(template) in sys.path
    ensure_project_paths(include_scripts=True)
    assert sys.path.count(str(SRC)) == 1


def test_project_constants_point_at_active_checkout() -> None:
    assert PROJECT.name == "biology_textbook"
    assert SRC == PROJECT / "src"
    assert SCRIPTS_DIR == PROJECT / "scripts"
    discovered = template_root()
    assert discovered is None or is_template_root(discovered)
