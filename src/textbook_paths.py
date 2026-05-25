"""Path discovery helpers for standalone and template-hosted checkouts."""

from __future__ import annotations

import os
import sys
from pathlib import Path

PROJECT = Path(__file__).resolve().parent.parent
SRC = PROJECT / "src"
SCRIPTS_DIR = PROJECT / "scripts"


def ensure_project_paths(*, include_scripts: bool = False) -> Path:
    """Insert ``src/``, optional ``scripts/``, and template root on ``sys.path``."""
    if include_scripts:
        scripts_str = str(SCRIPTS_DIR)
        if scripts_str not in sys.path:
            sys.path.insert(0, scripts_str)

    src_str = str(SRC)
    if src_str not in sys.path:
        sys.path.insert(0, src_str)

    template_root = discover_template_root(PROJECT)
    if template_root is not None:
        template_str = str(template_root)
        if template_str not in sys.path:
            sys.path.insert(0, template_str)

    return PROJECT


def template_root() -> Path | None:
    """Return the discovered template repository root, if any."""
    return discover_template_root(PROJECT)


def is_template_root(path: Path) -> bool:
    """Return true when ``path`` looks like the template repository root."""
    return (
        (path / "infrastructure" / "validation").is_dir()
        and (path / "infrastructure" / "rendering").is_dir()
    )


def discover_template_root(start: Path) -> Path | None:
    """Find a nearby template root without assuming a fixed checkout layout."""
    env_value = os.environ.get("BIOLOGY_TEXTBOOK_TEMPLATE_ROOT")
    if env_value:
        env_path = Path(env_value).expanduser().resolve()
        if is_template_root(env_path):
            return env_path

    current = start.resolve()
    if current.is_file():
        current = current.parent

    visited: set[Path] = set()
    for ancestor in (current, *current.parents):
        if ancestor in visited:
            continue
        visited.add(ancestor)
        if is_template_root(ancestor):
            return ancestor
        try:
            children = sorted(path for path in ancestor.iterdir() if path.is_dir())
        except OSError:
            children = []
        for child in children:
            if child in visited:
                continue
            visited.add(child)
            if is_template_root(child):
                return child
        if ancestor == ancestor.home():
            break
    return None
