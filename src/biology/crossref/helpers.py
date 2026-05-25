"""Helper utilities for cross-reference id suggestion and block detection."""

from __future__ import annotations

import re
from pathlib import Path

from biology.crossref.patterns import GENERATED_BLOCK_MARKERS


def slugify(text: str) -> str:
    """Produce a filesystem/URL-safe slug suitable for a crossref id."""
    slug = text.strip().lower()
    slug = re.sub(r"[^a-z0-9]+", "-", slug)
    slug = re.sub(r"-+", "-", slug).strip("-")
    return slug or "untitled"


def unit_tag(path: Path) -> str:
    """Extract the unit tag (e.g. ``unit_I``) from a manuscript path."""
    for part in path.parts:
        if part.startswith("unit_"):
            return part
    return "front"


def file_stem(path: Path) -> str:
    stem = path.stem
    for prefix in ("lab_", "questions_"):
        if stem.startswith(prefix):
            stem = stem[len(prefix) :]
            break
    return stem


def suggest_id(kind: str, path: Path, descriptor: str, ordinal: int = 0) -> str:
    """Suggest a canonical crossref id for ``kind`` at ``path``."""
    unit = unit_tag(path)
    stem = file_stem(path)
    tail = slugify(descriptor) if descriptor else f"item-{ordinal}"
    return f"{unit}-{stem}-{tail}"


def is_unnumbered_section_id(sec_id: str) -> bool:
    """Return True when a ``sec:…`` id labels an unnumbered ``\\section*`` surface."""
    if sec_id in {"glossary"}:
        return True
    if sec_id.startswith(("lab_", "q_", "appendix_")):
        return True
    return sec_id.endswith("_unit_intro")


def section_reference(label: str) -> str:
    """Return ``\\nameref`` for unnumbered sections and ``\\cref`` for numbered chapters."""
    normalized = label if label.startswith("sec:") else f"sec:{label}"
    sec_id = normalized.removeprefix("sec:")
    if is_unnumbered_section_id(sec_id):
        return f"\\nameref{{{normalized}}}"
    return f"\\cref{{{normalized}}}"


_UNNUMBERED_SEC_CREF_RE = re.compile(r"\\([Cc])ref\{(sec:[^}]+)\}")


def normalize_unnumbered_section_crefs(text: str) -> str:
    """Rewrite ``\\cref{sec:lab_…}`` (etc.) to ``\\nameref`` for starred sections."""
    def _replace(match: re.Match[str]) -> str:
        label = match.group(2)
        sec_id = label.removeprefix("sec:")
        if is_unnumbered_section_id(sec_id):
            return f"\\nameref{{{label}}}"
        return match.group(0)

    return _UNNUMBERED_SEC_CREF_RE.sub(_replace, text)


def generated_block_lines(text: str) -> set[int]:
    """Line numbers owned by generated manuscript marker blocks."""
    line_starts: list[int] = []
    offset = 0
    for line in text.splitlines(keepends=True):
        line_starts.append(offset)
        offset += len(line)
    generated: set[int] = set()
    for start_marker, end_marker in GENERATED_BLOCK_MARKERS:
        start = text.find(start_marker)
        end = text.find(end_marker, start)
        if start == -1 or end == -1:
            continue
        end += len(end_marker)
        for line_no, line_start in enumerate(line_starts, start=1):
            if start <= line_start < end:
                generated.add(line_no)
    return generated


__all__ = [
    "file_stem",
    "generated_block_lines",
    "is_unnumbered_section_id",
    "normalize_unnumbered_section_crefs",
    "section_reference",
    "slugify",
    "suggest_id",
    "unit_tag",
]
