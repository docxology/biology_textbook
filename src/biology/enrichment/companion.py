"""Companion source module generation and normalization."""

from __future__ import annotations

import re

from biology.enrichment.catalog import (
    COMPANION_INTRO_BY_STEM,
    COMPANION_SOURCE_BY_STEM,
    _COMPANION_NOTE_LINE_RE,
    _COMPANION_SECTION_RE,
    _INLINE_COMPANION_NOTE_RE,
)
from biology.enrichment.models import ChapterRecord
from textbook_io import write_text_atomic


def _companion_source_table_caption(record: ChapterRecord) -> str:
    tbl_id = f"{record.unit_id}_{record.stem}_companion_source_surfaces"
    return f": Companion source surfaces for {record.title}. {{#tbl:{tbl_id}}}"


def _caption_companion_source_table(record: ChapterRecord, body: str) -> str:
    """Add the stable pandoc caption expected by table-crossref checks."""

    lines = body.splitlines()
    for idx, line in enumerate(lines):
        if not line.lstrip().startswith("|"):
            continue
        previous = lines[idx - 1].strip() if idx else ""
        if previous.startswith(":") and "{#tbl:" in previous:
            return body
        lines.insert(idx, _companion_source_table_caption(record))
        return "\n".join(lines)
    return body


def companion_source_section(record: ChapterRecord) -> str:
    intro = COMPANION_INTRO_BY_STEM.get(
        record.stem,
        (
            f"**{record.title}** should leave a reproducible trail from a biological claim to\n"
            "the code, figure, diagram, or paper-based activity that can test it. Use the\n"
            "surfaces below to inspect the chapter's assumptions, rerun the relevant model,\n"
            "or compare the manuscript explanation with companion labs and figures."
        ),
    )
    body = COMPANION_SOURCE_BY_STEM.get(
        record.stem,
        "| Surface | Use it for |\n"
        "| --- | --- |\n"
        "| `src/biology/` | Connect the chapter concept to a tested model or data structure. |\n\n"
        "**Reproducibility check:** name the input, output, assumption, and evidence limit before using code as support.",
    )
    body = _caption_companion_source_table(record, body)
    return f"""
---

## Companion Source Module: {record.title}

{intro}

{body}
"""


def _normalize_companion_heading(text: str, title: str) -> str:
    return re.sub(
        r"(?m)^#{2,3}\s+Companion Source Module(?::[^\n{]+)?(?:\s+\{[^}]*\})?\s*$",
        f"## Companion Source Module: {title}",
        text,
    )


def normalize_companion_source_modules(records: list[ChapterRecord], dry_run: bool) -> int:
    changed = 0
    for record in records:
        path = record.chapter_path
        text = path.read_text(encoding="utf-8")
        new_text = _COMPANION_SECTION_RE.sub("", text)
        new_text = _COMPANION_NOTE_LINE_RE.sub("", new_text)
        new_text = _INLINE_COMPANION_NOTE_RE.sub("", new_text)
        new_text = re.sub(r"\n---\s*\n\s*\n---\s*\n", "\n---\n", new_text)
        new_text = re.sub(r"\n---\s*\n\s*(?=---\s*\n)", "\n", new_text)
        new_text = re.sub(r"\n{4,}", "\n\n\n", new_text).rstrip()
        rebuilt = f"{new_text}\n\n{companion_source_section(record).strip()}\n"
        rebuilt_normalized = _normalize_companion_heading(rebuilt, record.title)
        existing_normalized = _normalize_companion_heading(text, record.title)
        if rebuilt_normalized == existing_normalized:
            continue
        if rebuilt != text:
            changed += 1
            if not dry_run:
                write_text_atomic(path, rebuilt)
    return changed


__all__ = ["companion_source_section", "normalize_companion_source_modules"]
