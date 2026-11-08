"""Shared manuscript traversal and config surface discovery."""

from __future__ import annotations

import re
from pathlib import Path

import yaml

from biology.crossref.source import visible_text
from biology.maintenance.models import PROJECT, ManuscriptSurface

MANUSCRIPT = PROJECT / "docs" / "manuscript"

__all__ = [
    "configured_chapter_files",
    "configured_chapter_title_by_path",
    "configured_manuscript_surfaces",
    "iter_markdown_headings",
    "iter_prose_lines",
    "load_manuscript_config",
    "manuscript_markdown_files",
    "reference_appendix_path",
    "require_manuscript_source",
]


def require_manuscript_source(
    path: Path, manuscript_root: Path, *, project_root: Path | None = None,
) -> Path:
    """Admit a source without opening bytes, including its directory aliases.

    Internal file aliases are supported, but neither lexical traversal nor a
    resolved target may leave the selected manuscript (or its project).
    Missing paths remain available to callers that diagnose authoring gaps.
    """
    root = manuscript_root.absolute()
    resolved_root = root.resolve()
    if root.is_symlink() or (
        project_root is not None and not resolved_root.is_relative_to(project_root.resolve())
    ):
        raise ValueError(f"Manuscript directory escapes project or is aliased: {root}")
    source = path.absolute()
    if not source.is_relative_to(root) or ".." in source.relative_to(root).parts:
        raise ValueError(f"Source escapes manuscript directory: {path}")
    for ancestor in (source, *source.parents):
        if not ancestor.resolve().is_relative_to(resolved_root):
            raise ValueError(f"Source escapes manuscript directory: {path}")
        if ancestor == root:
            break
    return path


def manuscript_markdown_files(
    manuscript_root: Path | None = None, *, project_root: Path | None = None,
) -> list[Path]:
    """Discover all Markdown only after admitting the entire recursive tree."""
    root = MANUSCRIPT if manuscript_root is None else manuscript_root
    project = PROJECT if manuscript_root is None and project_root is None else project_root
    require_manuscript_source(root, root, project_root=project)
    files: list[Path] = []

    def visit(directory: Path, ancestors: frozenset[Path]) -> None:
        resolved = directory.resolve()
        if resolved in ancestors:
            raise ValueError(f"Cyclic manuscript directory alias: {directory}")
        for path in sorted(directory.iterdir()):
            require_manuscript_source(path, root, project_root=project)
            if path.is_dir():
                visit(path, ancestors | {resolved})
            elif path.suffix == ".md" and path.name not in {"AGENTS.md", "README.md"}:
                if not path.is_file():
                    raise FileNotFoundError(f"Manuscript source is missing: {path}")
                files.append(path)

    visit(root, frozenset())
    return files


def load_manuscript_config() -> dict[str, object]:
    config_path = require_manuscript_source(MANUSCRIPT / "config.yaml", MANUSCRIPT, project_root=PROJECT)
    return yaml.safe_load(config_path.read_text(encoding="utf-8")) or {}


def reference_appendix_path(filename: str) -> Path:
    if filename == "glossary.md":
        return MANUSCRIPT / "glossary.md"
    return MANUSCRIPT / "appendices" / filename


def configured_manuscript_surfaces() -> list[ManuscriptSurface]:
    """Return all config-registered student-facing manuscript surfaces."""
    config = load_manuscript_config()
    surfaces: list[ManuscriptSurface] = []

    front_matter = config.get("front_matter", {})
    if isinstance(front_matter, dict):
        for entry in front_matter.get("files", []):
            if isinstance(entry, dict) and isinstance(entry.get("file"), str):
                surfaces.append(ManuscriptSurface("front_matter", MANUSCRIPT / entry["file"]))

    units = config.get("units", [])
    if not isinstance(units, list):
        units = []
    for unit in units:
        if not isinstance(unit, dict):
            continue
        directory = unit.get("directory", unit.get("id"))
        if not isinstance(directory, str):
            continue
        surfaces.append(ManuscriptSurface("unit_intro", MANUSCRIPT / directory / "unit_intro.md"))
        chapters = unit.get("chapters", [])
        if not isinstance(chapters, list):
            continue
        for chapter in chapters:
            if not isinstance(chapter, dict) or chapter.get("enabled", True) is False:
                continue
            filename = chapter.get("file")
            if isinstance(filename, str):
                surfaces.append(ManuscriptSurface("chapter", MANUSCRIPT / directory / filename))

    appendices = config.get("appendices", {})
    if isinstance(appendices, dict):
        for category, base_dir in (("lab", "labs"), ("question", "questions")):
            bundles = appendices.get(f"{category}s", [])
            if not isinstance(bundles, list):
                continue
            for bundle in bundles:
                if not isinstance(bundle, dict) or not isinstance(bundle.get("unit"), str):
                    continue
                files = bundle.get("files", [])
                if not isinstance(files, list):
                    continue
                for entry in files:
                    if isinstance(entry, dict) and isinstance(entry.get("file"), str):
                        surfaces.append(
                            ManuscriptSurface(
                                category,
                                MANUSCRIPT / base_dir / bundle["unit"] / entry["file"],
                            )
                        )

        references = appendices.get("reference", [])
        if isinstance(references, list):
            for entry in references:
                if isinstance(entry, dict) and isinstance(entry.get("file"), str):
                    surfaces.append(
                        ManuscriptSurface("appendix", reference_appendix_path(entry["file"]))
                    )

    for surface in surfaces:
        require_manuscript_source(surface.path, MANUSCRIPT, project_root=PROJECT)
    return surfaces


def configured_chapter_files() -> list[Path]:
    return [surface.path for surface in configured_manuscript_surfaces() if surface.category == "chapter"]


def configured_chapter_title_by_path() -> dict[Path, str]:
    config = load_manuscript_config()
    titles: dict[Path, str] = {}
    units = config.get("units", [])
    if not isinstance(units, list):
        return titles
    for unit in units:
        if not isinstance(unit, dict):
            continue
        directory = unit.get("directory", unit.get("id"))
        if not isinstance(directory, str):
            continue
        chapters = unit.get("chapters", [])
        if not isinstance(chapters, list):
            continue
        for chapter in chapters:
            if not isinstance(chapter, dict) or chapter.get("enabled", True) is False:
                continue
            filename = chapter.get("file")
            title = chapter.get("title")
            if isinstance(filename, str) and isinstance(title, str):
                titles[MANUSCRIPT / directory / filename] = title
    for path in titles:
        require_manuscript_source(path, MANUSCRIPT, project_root=PROJECT)
    return titles


def iter_prose_lines(path: Path) -> list[tuple[int, str]]:
    """Return rendered prose, including instructor solutions but excluding examples."""
    lines: list[tuple[int, str]] = []
    visible = visible_text(path.read_text(encoding="utf-8"))
    for line_no, line in enumerate(visible.splitlines(), start=1):
        line = re.sub(r"<!--\s*SOLUTION\b|\bSOLUTION\s*-->", "", line)
        stripped = line.strip()
        if stripped.startswith("#"):
            continue
        if re.match(r"^>\s*\*\*(?:Ch|Appendix)\s+[A-Za-z0-9.]+", stripped):
            continue
        lines.append((line_no, line))
    return lines


def iter_markdown_headings(path: Path) -> list[tuple[int, str]]:
    """Return Markdown heading lines outside fenced code blocks."""
    headings: list[tuple[int, str]] = []
    in_fence = False
    for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        stripped = line.strip()
        if stripped.startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        if stripped.startswith("#"):
            headings.append((line_no, line))
    return headings
