"""Path discovery helpers for standalone and template-hosted checkouts."""

from __future__ import annotations

import os
import sys
from pathlib import Path

PROJECT = Path(__file__).resolve().parent.parent
SRC = PROJECT / "src"
SCRIPTS_DIR = PROJECT / "scripts"


def ensure_project_paths(*, include_scripts: bool = False, include_template: bool = True) -> Path:
    """Keep local imports first; optionally discover the integration dependency.

    Receipt-owning entry points defer integration discovery until their running
    evidence is persisted by passing ``include_template=False`` during startup.
    """
    selected_paths = [str(SRC)]
    if include_scripts:
        selected_paths.append(str(SCRIPTS_DIR))
    for path in reversed(selected_paths):
        while path in sys.path:
            sys.path.remove(path)
        sys.path.insert(0, path)

    template_root = discover_template_root(PROJECT) if include_template else None
    if template_root is not None:
        template_str = str(template_root)
        if template_str not in sys.path:
            sys.path.append(template_str)

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
    """Find an enclosing template or an explicit integration dependency.

    Unrelated neighboring repositories never participate in import resolution.
    An invalid explicit selection is an error, not permission to choose another.
    """
    env_value = os.environ.get("BIOLOGY_TEXTBOOK_TEMPLATE_ROOT")
    if env_value:
        env_path = Path(env_value).expanduser().resolve()
        if not is_template_root(env_path):
            raise ValueError(f"Invalid BIOLOGY_TEXTBOOK_TEMPLATE_ROOT: {env_path}")
        return env_path
    current = start.resolve()
    if current.is_file():
        current = current.parent
    for ancestor in (current, *current.parents):
        if is_template_root(ancestor):
            return ancestor
    return None


def require_project_output_directory(project_root: Path, directory: Path) -> Path:
    """Admit only independent directories beneath the project's output root.

    Inspect lexical ancestors before resolving them: an output symlink must
    never turn artifact replacement or stale-file cleanup into source deletion.
    This check creates nothing and rejects aliases even within the project.
    """
    root = project_root.resolve()
    output = root / "output"
    target = Path(os.path.abspath(directory))
    if not target.is_relative_to(output):
        raise ValueError(f"Generated output must remain beneath {output}: {directory}")
    current = output
    for component in (None, *target.relative_to(output).parts):
        if component is not None:
            current = current / component
        if current.is_symlink() or (current.exists() and not current.is_dir()):
            raise ValueError(f"Generated output has an aliased or non-directory ancestor: {current}")
    return target
