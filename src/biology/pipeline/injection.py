"""Inject ordered manuscript sources into output/manuscript for rendering."""

from __future__ import annotations

import logging
import re
import shutil
import tempfile
from pathlib import Path

from biology.crossref.source import visible_text
from biology.maintenance.manuscript_spans import protected_spans
from biology.maintenance.manuscript_walker import require_manuscript_source
from biology.pipeline.numbering import section_numbering_directives
from biology.pipeline.paths import MANUSCRIPT_DIR, OUTPUT_DIR, PROJECT_ROOT
from textbook_io import write_text_atomic
from textbook_paths import require_project_output_directory

logger = logging.getLogger(__name__)

SOLUTION_BLOCK_RE = re.compile(
    r"<!--[ \t]*SOLUTION[ \t]*\n(.*?)\n[ \t]*SOLUTION[ \t]*-->",
    re.DOTALL,
)

INSTRUCTOR_WATERMARK_LATEX = """
% Instructor edition watermark (injected by biology_analysis.py when export.watermark_instructor is true)
\\usepackage{draftwatermark}
\\SetWatermarkText{INSTRUCTOR EDITION}
\\SetWatermarkFontSize{32pt}
\\SetWatermarkScale{1.0}
\\SetWatermarkColor[gray]{0.88}
"""

_UNICODE_MATH_FOR_LATEX = {
    "≤": r"$\leq$",
    "≲": r"$\lesssim$",
    "∝": r"$\propto$",
    "⇌": r"$\rightleftharpoons$",
    "⋅": r"$\cdot$",
    "∘": r"$\circ$",
    "𝜑": r"$\varphi$",
    "𝜌": r"$\rho$",
}


def normalize_unicode_math_for_latex(text: str) -> str:
    """Normalize prose symbols without changing equations, code, or diagrams."""
    spans = protected_spans(text)
    parts: list[str] = []
    cursor = 0
    for start, end in spans:
        if start < cursor:
            if end > cursor:
                parts.append(text[cursor:end])
                cursor = end
            continue
        prose = text[cursor:start]
        for char, latex in _UNICODE_MATH_FOR_LATEX.items():
            prose = prose.replace(char, latex)
        parts.extend((prose, text[start:end]))
        cursor = end
    prose = text[cursor:]
    for char, latex in _UNICODE_MATH_FOR_LATEX.items():
        prose = prose.replace(char, latex)
    parts.append(prose)
    return "".join(parts)


def instructor_preamble_text(preamble: str, *, watermark_instructor: bool) -> str:
    """Return preamble text, optionally appending the instructor watermark block."""
    if not watermark_instructor:
        return preamble
    if "draftwatermark" in preamble:
        return preamble
    block_start = preamble.find("```latex\n")
    if block_start == -1:
        return preamble + INSTRUCTOR_WATERMARK_LATEX
    block_end = preamble.find("\n```", block_start + 1)
    if block_end == -1:
        return preamble
    return preamble[:block_end] + INSTRUCTOR_WATERMARK_LATEX + preamble[block_end:]


def clear_stale_slide_artifacts() -> None:
    """Remove stale generated slide files before a fresh WIP render."""
    slides_dir = require_project_output_directory(PROJECT_ROOT, PROJECT_ROOT / "output" / "slides")
    slides_dir.mkdir(parents=True, exist_ok=True)
    removed = 0
    for path in slides_dir.iterdir():
        if path.is_file():
            path.unlink()
            removed += 1
    if removed:
        logger.info("Cleared %d stale slide artifact(s) from %s", removed, slides_dir)


def reveal_solutions(text: str) -> str:
    """Reveal real answer blocks without changing examples or adjacent questions."""
    parts: list[str] = []
    cursor = 0
    for match in SOLUTION_BLOCK_RE.finditer(visible_text(text)):
        parts.append(text[cursor:match.start()])
        body = normalize_unicode_math_for_latex(text[match.start(1):match.end(1)].strip("\n"))
        quoted = "\n".join(f"> {line}" if line.strip() else ">" for line in body.splitlines())
        # A following metadata comment otherwise becomes a lazy continuation of
        # this quote, absorbing the next numbered question into the answer.
        parts.append(f"\n\n{quoted}\n\n")
        cursor = match.end()
    parts.append(text[cursor:])
    return "".join(parts)


def _cover_members(cover: Path) -> list[Path]:
    """Admit every recursive cover member before any source bytes are copied."""
    members: list[Path] = []

    def visit(path: Path, ancestors: frozenset[Path]) -> None:
        require_manuscript_source(path, MANUSCRIPT_DIR, project_root=PROJECT_ROOT)
        if path.is_dir():
            resolved = path.resolve()
            if resolved in ancestors:
                raise ValueError(f"Cyclic cover directory alias: {path}")
            members.append(path)
            for child in sorted(path.iterdir()):
                visit(child, ancestors | {resolved})
        elif path.is_file():
            members.append(path)
        else:
            raise ValueError(f"Cover member is not a regular file or directory: {path}")

    require_manuscript_source(cover, MANUSCRIPT_DIR, project_root=PROJECT_ROOT)
    if cover.exists():
        if not cover.is_dir():
            raise ValueError(f"Cover source is not a directory: {cover}")
        visit(cover, frozenset())
    return members


def inject_chapters_for_rendering(
    chapters: list[Path],
    *,
    include_solutions: bool = False,
    watermark_instructor: bool = False,
) -> None:
    """Stage a complete fresh tree before replacing the previous injection."""
    if not chapters:
        raise ValueError("Cannot inject an empty manuscript")
    require_project_output_directory(PROJECT_ROOT, OUTPUT_DIR)
    source_root = MANUSCRIPT_DIR.resolve()
    if OUTPUT_DIR.resolve().is_relative_to(source_root) or source_root.is_relative_to(OUTPUT_DIR.resolve()):
        raise ValueError(f"Injection destination overlaps manuscript sources: {OUTPUT_DIR}")
    for source in chapters:
        require_manuscript_source(source, MANUSCRIPT_DIR, project_root=PROJECT_ROOT)
        if not source.is_file():
            raise FileNotFoundError(f"Selected manuscript source is missing: {source}")
    if len({source.resolve() for source in chapters}) != len(chapters):
        raise ValueError("Cannot inject duplicate manuscript sources")

    auxiliary: list[Path] = []
    for name in ("config.yaml", "references.bib", "preamble.md"):
        source = require_manuscript_source(MANUSCRIPT_DIR / name, MANUSCRIPT_DIR, project_root=PROJECT_ROOT)
        if source.exists():
            if not source.is_file():
                raise ValueError(f"Auxiliary source is not a regular file: {source}")
            auxiliary.append(source)
    cover_members = _cover_members(MANUSCRIPT_DIR / "assets" / "cover")

    OUTPUT_DIR.parent.mkdir(parents=True, exist_ok=True)
    stage = Path(tempfile.mkdtemp(prefix=".manuscript-stage-", dir=OUTPUT_DIR.parent))
    backup = stage.with_name(stage.name + ".previous")
    try:
        prefix_width = max(2, len(str(len(chapters))))
        directives = section_numbering_directives(chapters)
        for index, source in enumerate(chapters, start=1):
            destination = stage / f"{index:0{prefix_width}d}_{source.name}"
            content = normalize_unicode_math_for_latex(source.read_text(encoding="utf-8"))
            if include_solutions:
                content = reveal_solutions(content)
            directive = directives.get(source.resolve())
            if directive is not None:
                content = f"{directive}\n\n{content}"
            if "<!-- render:skip-beamer -->" not in content:
                content = "<!-- render:skip-beamer -->\n\n" + content
            write_text_atomic(destination, content)
            shutil.copystat(source, destination)

        for source in auxiliary:
            if source.name == "preamble.md":
                write_text_atomic(
                    stage / source.name,
                    instructor_preamble_text(
                        source.read_text(encoding="utf-8"),
                        watermark_instructor=watermark_instructor and include_solutions,
                    ),
                )
            else:
                shutil.copy2(source, stage / source.name)
        for source in cover_members:
            destination = stage / source.relative_to(MANUSCRIPT_DIR)
            if source.is_dir():
                destination.mkdir(parents=True, exist_ok=True)
            else:
                shutil.copy2(source, destination)

        if OUTPUT_DIR.exists():
            OUTPUT_DIR.rename(backup)
        try:
            stage.rename(OUTPUT_DIR)
        except BaseException:
            if backup.exists() and not OUTPUT_DIR.exists():
                backup.rename(OUTPUT_DIR)
            raise
        if backup.exists():
            shutil.rmtree(backup)
    finally:
        if stage.exists():
            shutil.rmtree(stage)
    edition = "instructor" if include_solutions else "student"
    logger.info("Injected %d chapter files into %s (%s edition)", len(chapters), OUTPUT_DIR, edition)


__all__ = [
    "clear_stale_slide_artifacts",
    "inject_chapters_for_rendering",
    "instructor_preamble_text",
    "normalize_unicode_math_for_latex",
    "reveal_solutions",
]
