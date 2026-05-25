"""Shared manuscript traversal and config surface discovery."""

from __future__ import annotations

import re
from pathlib import Path

import yaml

from biology.maintenance.models import ManuscriptSurface, PROJECT

MANUSCRIPT = PROJECT / "manuscript"

__all__ = [
    "configured_chapter_files",
    "configured_chapter_title_by_path",
    "configured_manuscript_surfaces",
    "iter_markdown_headings",
    "iter_prose_lines",
    "load_manuscript_config",
    "manuscript_markdown_files",
    "reference_appendix_path",
]


def manuscript_markdown_files() -> list[Path]:
    return [
        path
        for path in sorted(MANUSCRIPT.rglob("*.md"))
        if path.name not in {"AGENTS.md", "README.md"}
    ]


def load_manuscript_config() -> dict[str, object]:
    return yaml.safe_load((MANUSCRIPT / "config.yaml").read_text(encoding="utf-8")) or {}


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
    return titles


def iter_prose_lines(path: Path) -> list[tuple[int, str]]:
    """Return non-code, non-HTML-comment lines for prose-oriented scans."""
    lines: list[tuple[int, str]] = []
    in_fence = False
    in_comment = False
    for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        stripped = line.strip()
        if stripped.startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        if stripped.startswith("#"):
            continue
        if re.match(r"^>\s*\*\*(?:Ch|Appendix)\s+[A-Za-z0-9.]+", stripped):
            continue
        if "<!--" in stripped:
            in_comment = True
        if not in_comment:
            lines.append((line_no, line))
        if "-->" in stripped:
            in_comment = False
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
