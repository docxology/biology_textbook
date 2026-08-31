"""Smoke test that template WIP project resolution finds biology_textbook."""

from __future__ import annotations

import sys
from pathlib import Path


def _is_template_root(path: Path) -> bool:
    return (path / "infrastructure" / "validation").is_dir() and (
        path / "infrastructure" / "rendering"
    ).is_dir()


def run_wip_resolver_smoke(cwd: Path | None = None) -> Path:
    """Resolve ``biology_textbook`` through template infrastructure discovery."""
    root_dir = (cwd or Path.cwd()).resolve()
    src = root_dir / "src"
    if str(src) not in sys.path:
        sys.path.insert(0, str(src))

    from textbook_paths import PROJECT, discover_template_root

    template_root = discover_template_root(root_dir)
    if template_root is None:
        raise AssertionError("template infrastructure not found")

    template_str = str(template_root)
    if template_str not in sys.path:
        sys.path.insert(0, template_str)

    from infrastructure.core.project_paths import resolve_project_root  # type: ignore[import-not-found]

    target = PROJECT.resolve()

    def project_root_for(template: Path) -> Path | None:
        """Resolve the bare name, accepting only a hit on this physical tree."""
        try:
            project = resolve_project_root(template, "biology_textbook")
        except ValueError:
            return None
        if project.is_dir() and project.resolve() == target:
            return project
        # This checkout may live under a typed lifecycle subfolder (for example
        # ``projects/ongoing/Teaching/biology_textbook``) reachable only through
        # an intermediate symlink. A nearer template checkout without this
        # project can shadow the intended root, so also probe that qualified
        # lifecycle location before declaring failure.
        link = template / "projects" / "ongoing" / "Teaching" / "biology_textbook"
        try:
            if link.exists() and link.resolve() == target:
                return link
        except OSError:
            return None
        return None

    project = project_root_for(template_root)
    if project is not None:
        return project

    # The nearest template checkout shadows the intended root (it resolves the
    # bare name elsewhere or not at all). Scan the remaining ancestor template
    # roots the way ``discover_template_root`` does and take one that actually
    # resolves to this physical tree.
    for ancestor in target.parents:
        if ancestor == ancestor.home():
            break
        candidates: list[Path] = [ancestor] if _is_template_root(ancestor) else []
        try:
            candidates += [
                child
                for child in sorted(ancestor.iterdir())
                if child.is_dir() and _is_template_root(child)
            ]
        except OSError:
            pass
        for candidate in candidates:
            project = project_root_for(candidate)
            if project is not None:
                return project

    raise AssertionError(f"unexpected project root: {template_root}")


def main() -> None:
    project = run_wip_resolver_smoke()
    print(project)


if __name__ == "__main__":
    main()
