"""LaTeX section-numbering directives for injected manuscript files."""

from __future__ import annotations

from pathlib import Path

from biology.pipeline.paths import MANUSCRIPT_DIR

UNIT_ZERO_NUMBERING_DIRECTIVE = (
    "% Unit 0 chapters render as 0.1, 0.2, ... without shifting Unit I.\n"
    "\\setcounter{section}{0}\n"
    "\\renewcommand{\\thesection}{0.\\arabic{section}}"
)
MAIN_NUMBERING_DIRECTIVE = (
    "% Reset main chapter numbering after Unit 0.\n"
    "\\setcounter{section}{0}\n"
    "\\renewcommand{\\thesection}{\\arabic{section}}"
)

_SKIP_NAMES = frozenset({"README.md", "AGENTS.md", "unit_intro.md"})


def section_numbering_directives(chapters: list[Path]) -> dict[Path, str]:
    """Return raw-LaTeX numbering directives keyed by source file path."""
    resolved = [path.resolve() for path in chapters]
    chapter_set = set(resolved)
    directives: dict[Path, str] = {}

    first_unit_zero_chapter = next(
        (
            path
            for path in resolved
            if path.parent == (MANUSCRIPT_DIR / "unit_0").resolve()
            and path.name not in _SKIP_NAMES
        ),
        None,
    )
    if first_unit_zero_chapter is not None:
        directives[first_unit_zero_chapter] = UNIT_ZERO_NUMBERING_DIRECTIVE

    first_main_chapter = next(
        (
            path
            for path in resolved
            if path.parent.name.startswith("unit_")
            and path.parent.name != "unit_0"
            and path.name not in _SKIP_NAMES
        ),
        None,
    )
    if first_main_chapter is not None:
        unit_intro = first_main_chapter.parent / "unit_intro.md"
        reset_target = unit_intro if unit_intro in chapter_set else first_main_chapter
        directives[reset_target] = MAIN_NUMBERING_DIRECTIVE

    return directives


__all__ = [
    "MAIN_NUMBERING_DIRECTIVE",
    "UNIT_ZERO_NUMBERING_DIRECTIVE",
    "section_numbering_directives",
]
