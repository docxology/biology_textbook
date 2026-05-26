"""Helper utilities for cross-reference id suggestion and block detection."""

from __future__ import annotations

import re
from functools import lru_cache
from pathlib import Path
from typing import Any

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


_HYPERREF_ESCAPE_RE = re.compile(r"([\\#%&_$~^{}])")


def escape_hyperref_text(text: str) -> str:
    """Escape characters that break ``\\hyperref`` display arguments."""
    return _HYPERREF_ESCAPE_RE.sub(r"\\\1", text)


def section_hyperlink(label: str, display: str) -> str:
    """Return a forward-safe clickable PDF link with explicit display text."""
    normalized = label if label.startswith("sec:") else f"sec:{label}"
    escaped = escape_hyperref_text(display)
    return f"\\hyperref[{normalized}]{{{escaped}}}"


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


_NAMEREF_RE = re.compile(r"\\nameref\{(?P<label>sec:[^}]+)\}")


def build_nameref_plain_map(book_toc: Any) -> dict[str, str]:
    """Map ``sec:…`` labels to plain titles for early front-matter references."""
    mapping: dict[str, str] = {}
    for unit in book_toc.units:
        mapping[unit.section_label] = unit.plain_ref
        for chapter in unit.chapters:
            mapping[chapter.section_label] = chapter.plain_ref
    for reference in book_toc.references:
        mapping[reference.section_label] = reference.plain_ref
    return mapping


def replace_namerefs_with_plain_titles(text: str, book_toc: Any) -> str:
    """Replace ``\\nameref{sec:…}`` with canonical TOC titles (no forward-ref warnings)."""
    mapping = build_nameref_plain_map(book_toc)
    return _NAMEREF_RE.sub(lambda match: mapping.get(match.group("label"), match.group(0)), text)


def collect_plain_ref_variants(book_toc: Any) -> tuple[str, ...]:
    """Return canonical TOC plain titles (longest first) for structural-ref audits."""
    variants: set[str] = set()
    for unit in book_toc.units:
        variants.add(unit.plain_ref)
        variants.add(unit.display_title)
        variants.add(f"{unit.display_title}:")
        variants.add(f"{unit.plain_ref}:")
        for chapter in unit.chapters:
            variants.add(chapter.plain_ref)
    for reference in book_toc.references:
        variants.add(reference.plain_ref)
        if not reference.plain_ref.endswith(":"):
            variants.add(f"{reference.plain_ref}:")
    return tuple(sorted(variants, key=len, reverse=True))


@lru_cache(maxsize=1)
def cached_plain_ref_variants() -> tuple[str, ...]:
    """Load and cache plain TOC title variants for validator stripping."""
    from biology.toc import load_toc

    return collect_plain_ref_variants(load_toc())


def strip_canonical_plain_refs(line: str, plain_refs: tuple[str, ...] | None = None) -> str:
    """Remove canonical TOC plain titles so structural-ref patterns ignore them."""
    refs = cached_plain_ref_variants() if plain_refs is None else plain_refs
    result = line
    for ref in refs:
        if ref:
            result = result.replace(ref, "")
    return result


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
    "build_nameref_plain_map",
    "cached_plain_ref_variants",
    "collect_plain_ref_variants",
    "file_stem",
    "generated_block_lines",
    "is_unnumbered_section_id",
    "normalize_unnumbered_section_crefs",
    "replace_namerefs_with_plain_titles",
    "escape_hyperref_text",
    "section_hyperlink",
    "section_reference",
    "slugify",
    "strip_canonical_plain_refs",
    "suggest_id",
    "unit_tag",
]
