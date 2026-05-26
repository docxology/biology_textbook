"""Smoke test that template WIP project resolution finds biology_textbook."""

from __future__ import annotations

import sys
from pathlib import Path


def run_wip_resolver_smoke(cwd: Path | None = None) -> Path:
    """Resolve ``biology_textbook`` through template infrastructure discovery."""
    root_dir = (cwd or Path.cwd()).resolve()
    src = root_dir / "src"
    if str(src) not in sys.path:
        sys.path.insert(0, str(src))

    from textbook_paths import discover_template_root

    template_root = discover_template_root(root_dir)
    if template_root is None:
        raise AssertionError("template infrastructure not found")

    template_str = str(template_root)
    if template_str not in sys.path:
        sys.path.insert(0, template_str)

    from infrastructure.project.discovery import resolve_project_root  # type: ignore[import-not-found]

    project = resolve_project_root(template_root, "biology_textbook")
    if not project.is_dir() or project.name != "biology_textbook":
        raise AssertionError(f"unexpected project root: {project}")
    return project


def main() -> None:
    project = run_wip_resolver_smoke()
    print(project)


if __name__ == "__main__":
    main()
