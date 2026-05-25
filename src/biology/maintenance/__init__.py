"""Shared manuscript maintenance primitives for quality and sync engines."""

from biology.maintenance.chapter_shells import repair_split_chapters
from biology.maintenance.further_reading import (
    BibEntry,
    apply_further_reading,
    render_section,
)
from biology.maintenance.manuscript_walker import (
    configured_chapter_files,
    configured_chapter_title_by_path,
    configured_manuscript_surfaces,
    iter_markdown_headings,
    iter_prose_lines,
    load_manuscript_config,
    manuscript_markdown_files,
    reference_appendix_path,
)
from biology.maintenance.models import Finding, ManuscriptSurface, PROJECT

__all__ = [
    "BibEntry",
    "Finding",
    "ManuscriptSurface",
    "PROJECT",
    "apply_further_reading",
    "configured_chapter_files",
    "configured_chapter_title_by_path",
    "configured_manuscript_surfaces",
    "iter_markdown_headings",
    "iter_prose_lines",
    "load_manuscript_config",
    "manuscript_markdown_files",
    "reference_appendix_path",
    "render_section",
    "repair_split_chapters",
]
