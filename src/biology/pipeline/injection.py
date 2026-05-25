"""Inject ordered manuscript sources into output/manuscript for rendering."""

from __future__ import annotations

import logging
import re
import shutil
from pathlib import Path

from textbook_io import write_text_atomic

from biology.pipeline.numbering import section_numbering_directives
from biology.pipeline.paths import MANUSCRIPT_DIR, OUTPUT_DIR, PROJECT_ROOT

logger = logging.getLogger(__name__)

SOLUTION_BLOCK_RE = re.compile(
    r"<!--\s*SOLUTION\s*\n(.*?)\n\s*SOLUTION\s*-->",
    re.DOTALL,
)


def clear_stale_slide_artifacts() -> None:
    """Remove stale generated slide files before a fresh WIP render."""
    slides_dir = PROJECT_ROOT / "output" / "slides"
    slides_dir.mkdir(parents=True, exist_ok=True)
    removed = 0
    for path in slides_dir.iterdir():
        if path.is_file():
            path.unlink()
            removed += 1
    if removed:
        logger.info("Cleared %d stale slide artifact(s) from %s", removed, slides_dir)


def reveal_solutions(text: str) -> str:
    """Reveal instructor solution blocks as blockquoted markdown."""

    def repl(match: re.Match[str]) -> str:
        body = match.group(1).strip("\n")
        return "\n".join(f"> {line}" if line.strip() else ">" for line in body.splitlines())

    return SOLUTION_BLOCK_RE.sub(repl, text)


def inject_chapters_for_rendering(chapters: list[Path], *, include_solutions: bool = False) -> None:
    """Copy all chapters into OUTPUT_DIR with sequential numeric prefixes."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    for existing in OUTPUT_DIR.glob("*.md"):
        existing.unlink()

    prefix_width = max(2, len(str(len(chapters))))
    numbering_directives = section_numbering_directives(chapters)

    for index, src in enumerate(chapters, start=1):
        dest = OUTPUT_DIR / f"{index:0{prefix_width}d}_{src.name}"
        content = src.read_text(encoding="utf-8")
        if include_solutions:
            content = reveal_solutions(content)
        directive = numbering_directives.get(src.resolve())
        if directive is not None:
            content = f"{directive}\n\n{content}"
        if "<!-- render:skip-beamer -->" not in content:
            content = "<!-- render:skip-beamer -->\n\n" + content
        write_text_atomic(dest, content)
        shutil.copystat(src, dest)
        logger.info("  Injected [%02d] %s → %s", index, src.name, dest.name)

    for aux in ("config.yaml", "references.bib", "preamble.md"):
        src = MANUSCRIPT_DIR / aux
        if src.exists():
            shutil.copy2(src, OUTPUT_DIR / aux)
            logger.info("  Copied auxiliary file: %s", aux)

    cover_assets = MANUSCRIPT_DIR / "assets" / "cover"
    if cover_assets.exists():
        dest_assets = OUTPUT_DIR / "assets" / "cover"
        dest_assets.mkdir(parents=True, exist_ok=True)
        for src in cover_assets.iterdir():
            if src.is_file():
                shutil.copy2(src, dest_assets / src.name)
        logger.info("  Copied cover assets: %s → %s", cover_assets, dest_assets)

    edition = "instructor" if include_solutions else "student"
    logger.info("Injected %d chapter files into %s (%s edition)", len(chapters), OUTPUT_DIR, edition)


__all__ = [
    "clear_stale_slide_artifacts",
    "inject_chapters_for_rendering",
    "reveal_solutions",
]
