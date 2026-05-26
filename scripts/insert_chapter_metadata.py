#!/usr/bin/env python3
r"""Insert pedagogical metadata badges into every chapter and populate the
*Course Planning Grid* section of ``manuscript/front_matter.md``.

A chapter "badge" is a single blockquote immediately below the title label
that reports difficulty, reading time, lecture time, and prerequisites:

```
> Level 2/3 · 45 min read · 75 min lecture · Prerequisites: \cref{sec:unit_I_atoms_molecules}
```

Idempotent: an existing badge is refreshed in place.

Run ``uv run python scripts/insert_chapter_metadata.py`` from the project
root (or ``--dry-run`` to preview).
"""

from __future__ import annotations

import importlib
import re
import sys
from dataclasses import dataclass
from pathlib import Path

from _bootstrap import PROJECT, ensure_project_paths

ensure_project_paths(include_scripts=True)

try:
    from scripts.atomic_io import write_text_atomic
except ModuleNotFoundError:  # pragma: no cover - direct script execution path
    from atomic_io import write_text_atomic  # type: ignore[import-not-found,no-redef]

MANUSCRIPT = PROJECT / "manuscript"


def _load_toc():
    """Load the canonical ToC API from ``src/biology/toc.py``."""
    toc = importlib.import_module("biology.toc")
    return toc.load_toc(PROJECT)


_BADGE_MARKER = "<!-- chapter-metadata-badge -->"
_GRID_START = "<!-- course-planning-grid-start -->"
_GRID_END = "<!-- course-planning-grid-end -->"


@dataclass
class InsertReport:
    badges_inserted: int = 0
    badges_updated: int = 0
    badges_already_present: int = 0
    grid_updated: bool = False


# ---------------------------------------------------------------------------
# Chapter badge insertion
# ---------------------------------------------------------------------------

def _format_badge(chapter, chapter_map) -> str:
    meta = chapter.meta
    prereq_links: list[str] = []
    for pid in meta.prerequisites:
        target = chapter_map.get(pid)
        if target is None:
            continue
        # Use bare title as link text; \cref handles formatting in PDF.
        prereq_links.append(f"\\cref{{sec:{pid}}}")
    prereqs = ", ".join(prereq_links) if prereq_links else "none"
    return (f"{_BADGE_MARKER}\n"
            f"> {meta.difficulty_label} · "
            f"{meta.reading_time_min} min read · "
            f"{meta.lecture_time_min} min lecture · "
            f"Prerequisites: {prereqs}")


def insert_badge(path: Path, badge_text: str, report: InsertReport, dry_run: bool = False) -> None:
    if not path.exists():
        print(f"WARN: missing chapter file {path}", file=sys.stderr)
        return
    text = path.read_text(encoding="utf-8")
    if _BADGE_MARKER in text:
        pattern = re.compile(
            re.escape(_BADGE_MARKER) + r"\n> .*(?=\n|$)",
            flags=re.MULTILINE,
        )
        new_text, replacements = pattern.subn(lambda _match: badge_text, text, count=1)
        if replacements and new_text != text:
            if not dry_run:
                write_text_atomic(path, new_text)
            report.badges_updated += 1
        else:
            report.badges_already_present += 1
        return
    # Insert after the chapter label line: the sequence is
    #   # Title
    #   (blank)
    #   \label{sec:...}
    # Put the badge right after the blank line that follows \label{}.
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if line.strip().startswith("\\label{sec:"):
            insert_at = i + 1
            # Skip adjacent blank lines
            while insert_at < len(lines) and lines[insert_at].strip() == "":
                insert_at += 1
            new_lines = lines[:insert_at] + [""] + badge_text.splitlines() + [""] + lines[insert_at:]
            if not dry_run:
                write_text_atomic(path, "\n".join(new_lines) + "\n")
            report.badges_inserted += 1
            return
    print(f"WARN: no \\label{{sec:}} anchor in {path}", file=sys.stderr)


# ---------------------------------------------------------------------------
# Course-planning grid
# ---------------------------------------------------------------------------

# Column layout: wide Unit, medium Chapter, compact Number/Difficulty/Reading/Lecture.
_COURSE_GRID_COLUMN_SPEC = (
    r">{\raggedright\arraybackslash}p{0.34\textwidth}"
    r">{\centering\arraybackslash}p{0.05\textwidth}"
    r">{\raggedright\arraybackslash}p{0.31\textwidth}"
    r">{\centering\arraybackslash}p{0.10\textwidth}"
    r">{\centering\arraybackslash}p{0.10\textwidth}"
    r">{\centering\arraybackslash}p{0.10\textwidth}"
)


def build_grid(book_toc) -> str:
    units_by_id = book_toc.units_by_id
    lines = [
        r"\begin{table}[htbp]",
        r"\centering",
        r"\footnotesize",
        r"\setlength{\tabcolsep}{2pt}",
        r"\renewcommand{\arraystretch}{1.12}",
        rf"\begin{{tabular}}{{{_COURSE_GRID_COLUMN_SPEC}}}",
        r"\hline",
        r"\textbf{Unit} & \textbf{Number} & \textbf{Chapter} & \textbf{Difficulty} & "
        r"\textbf{Reading} & \textbf{Lecture} \\",
        r"\hline",
    ]
    for chapter in book_toc.chapters:
        c = chapter.meta
        unit = units_by_id[chapter.unit_id]
        lines.append(
            f"{unit.hyperlink_ref} & {chapter.grid_number} & {chapter.hyperlink_ref} & "
            f"{c.difficulty_label} & {c.reading_time_min} min & {c.lecture_time_min} min \\\\"
        )
    totals_reading = sum(chapter.meta.reading_time_min for chapter in book_toc.chapters)
    totals_lecture = sum(chapter.meta.lecture_time_min for chapter in book_toc.chapters)
    hours = totals_reading // 60
    lecture_hours = totals_lecture // 60
    lines.extend(
        [
            r"\hline",
            f" & & \\textbf{{Totals}} & & \\textbf{{{totals_reading} min ({hours} h)}} & "
            f"\\textbf{{{totals_lecture} min ({lecture_hours} h)}} \\\\",
            r"\hline",
            r"\end{tabular}",
            r"\end{table}",
        ]
    )
    return "\n".join(lines)


def update_front_matter_grid(front_matter: Path, grid_md: str, report: InsertReport, dry_run: bool = False) -> None:
    text = front_matter.read_text(encoding="utf-8")
    grid_section = (
        "\n\n## Course Planning Grid {.unnumbered}\n\n"
        "The table below provides a per-chapter difficulty rating (Level 1/3 to Level 3/3), an\n"
        "estimated student reading time, and a suggested lecture allotment. Unit and chapter\n"
        "cells list canonical titles from ``manuscript/config.yaml`` as clickable "
        "``\\hyperref`` links to each section. The grid is\n"
        "auto-generated by ``scripts/insert_chapter_metadata.py`` from the\n"
        "canonical table of contents in ``manuscript/config.yaml`` plus\n"
        "``src/biology/chapter_metadata.py`` — edit those sources and re-run the\n"
        "script to refresh this grid.\n\n"
        f"{_GRID_START}\n{grid_md}\n{_GRID_END}"
    )
    if _GRID_START in text and _GRID_END in text:
        marker_start = text.index(_GRID_START)
        marker_end = text.index(_GRID_END) + len(_GRID_END)
        heading_start = text.rfind("## Course Planning Grid {.unnumbered}", 0, marker_start)
        if heading_start == -1:
            pattern = re.compile(
                re.escape(_GRID_START) + r".*?" + re.escape(_GRID_END), re.DOTALL
            )
            new_text = pattern.sub(f"{_GRID_START}\n{grid_md}\n{_GRID_END}", text)
        else:
            new_text = f"{text[:heading_start].rstrip()}{grid_section}{text[marker_end:]}"
    else:
        # Append before the final "\newpage" if present, else at the end.
        insert_pos = text.rfind("\\newpage")
        if insert_pos == -1:
            new_text = text + f"{grid_section}\n\n\\newpage\n"
        else:
            new_text = text[:insert_pos] + f"{grid_section}\n\n\\newpage\n" + text[insert_pos:]
    if new_text != text and not dry_run:
        write_text_atomic(front_matter, new_text)
    if new_text != text:
        report.grid_updated = True


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main(argv: list[str] | None = None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    dry_run = "--dry-run" in argv
    book_toc = _load_toc()
    chapters = list(book_toc.chapters)
    chapter_map = book_toc.chapters_by_id

    report = InsertReport()

    # 1. Insert badges
    for chapter in chapters:
        insert_badge(chapter.path, _format_badge(chapter, chapter_map), report, dry_run=dry_run)

    # 2. Refresh planning grid
    front_matter = MANUSCRIPT / "front_matter.md"
    update_front_matter_grid(front_matter, build_grid(book_toc), report, dry_run=dry_run)

    mode = "DRY RUN" if dry_run else "APPLIED"
    print(f"[{mode}] badges_inserted={report.badges_inserted} "
          f"badges_updated={report.badges_updated} "
          f"badges_already_present={report.badges_already_present} "
          f"grid_updated={report.grid_updated}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
