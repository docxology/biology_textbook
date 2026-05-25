"""Repair pedagogy shells on chapters created by the Phase 5 mega-chapter split.

Each split chapter must carry: a unique chapter-metadata badge, an opening
vignette, a Current-Evidence frontier section, a Summary, a Concept Check
prompt, a companion source module reference, and back-matter sections in the
canonical order. This module implements the shell-repair invariants; the thin
CLI lives at ``scripts/repair_split_chapter_shells.py``.
"""

from __future__ import annotations

import re
from pathlib import Path
from typing import Protocol

from biology.enrichment.engine import (
    FRONTIER_SECTION_PATTERN,
    companion_source_section,
    frontier_section,
    insert_before_anchor,
    lab_evidence_section,
)
from biology.enrichment.models import ChapterRecord
from biology.enrichment.records import chapter_records
from biology.quality.patterns import (
    CONCEPT_CHECK_RE,
    OPENING_VIGNETTE_RE,
    SUMMARY_HEADING_RE,
)


class _WriteFn(Protocol):
    def __call__(self, path: Path, text: str) -> None: ...


def _default_writer() -> _WriteFn:
    from textbook_io import write_text_atomic

    return write_text_atomic


# Chapters created by the Phase 5 mega-chapter split. Each value is the legacy
# section title still embedded in stale headings (e.g. "Epigenetics and Gene
# Regulation:" prefixes), used by ``_replace_legacy_titles``.
OLD_TITLES_BY_STEM: dict[str, str] = {
    "chromatin_and_epigenetic_mechanisms": "Epigenetics and Gene Regulation",
    "epigenetic_inheritance_and_disease": "Epigenetics and Gene Regulation",
    "mendelian_principles": "Mendelian Genetics",
    "mendelian_extensions_and_human_genetics": "Mendelian Genetics",
    "host_immunity_and_vaccines": "Infectious Disease",
    "antimicrobial_resistance_and_epidemiology": "Infectious Disease",
    "endocrine_signaling": "Endocrine and Immune Systems",
    "immune_system_defense": "Endocrine and Immune Systems",
    "community_interactions": "Community Ecology",
    "biodiversity_and_food_webs": "Community Ecology",
}

SPLIT_STEMS = frozenset(OLD_TITLES_BY_STEM)

_BADGE_MARKER = "<!-- chapter-metadata-badge -->"
_CURRICULUM_END = "<!-- curriculum-scaffold-end -->"

_ENDOCRINE_SUMMARY_BULLETS = """\
- **Endocrine system:** Hierarchical hypothalamic-pituitary-target gland axes with negative feedback. Three hormone classes: peptide (surface receptors, second messengers), steroid (nuclear receptors, transcription), amino acid derivatives (variable).
- **HPA / HPT / HPG axes:** Stress, thyroid, and reproductive control via CRH–ACTH–cortisol, TRH–TSH–T4/T3, and GnRH–LH/FSH cascades with circadian and feedback regulation.
- **Glucose homeostasis:** Insulin and glucagon balance uptake, glycogen metabolism, and gluconeogenesis; leptin, adiponectin, and GLP-1 provide long-term and incretin modulation.
- **Eicosanoids and disruption:** Arachidonic-acid derivatives mediate inflammation; glucocorticoids and NSAIDs target PLA$_2$ and COX; EDCs perturb hormone signaling during development.
- **Connections:** See \\cref{sec:unit_IX_immune_system_defense} for immune-endocrine coupling and \\cref{sec:unit_III_metabolic_integration} for metabolic integration."""

_IMMUNE_SUMMARY_START = "- **Innate immunity:**"
_IMMUNE_PROHIBITED_PREFIXES = (
    "- **Endocrine",
    "- **HPA",
    "- **HPT",
    "- **HPG",
    "- **Glucose homeostasis",
    "- **Adrenal medulla",
    "- **GH axis",
    "- **Eicosanoids",
    "- **Endocrine disruption",
)

_BACK_MATTER_SECTION_RES = re.compile(
    r"^## (?:Current Evidence and Frontier Biology(?::[^\n]+)?|Summary(?:\b|[\s{:])|"
    r"Review Questions|Further Reading and Source Notes(?::[^\n]+)?|"
    r"Key Terms|Companion Source Module(?::[^\n]+)?)\b.*?"
    r"(?=^## (?:Current Evidence and Frontier Biology|Summary|Review Questions|"
    r"Further Reading and Source Notes|Key Terms|Companion Source Module)\b|\Z)",
    flags=re.MULTILINE | re.DOTALL,
)

_BACK_MATTER_ANCHORS = (
    "## Summary",
    "## Key Terms",
    "## Further Reading and Source Notes:",
    "## Further Reading and Source Notes",
)


def dedupe_badges(text: str) -> str:
    """Collapse duplicate chapter-metadata badge markers down to one."""
    if text.count(_BADGE_MARKER) <= 1:
        cleaned = text
    else:
        first = text.find(_BADGE_MARKER)
        rest = text[first + len(_BADGE_MARKER) :].replace(_BADGE_MARKER, "")
        cleaned = text[:first] + _BADGE_MARKER + rest
    return re.sub(
        re.escape(_BADGE_MARKER) + r"\n(?:\n)*>",
        _BADGE_MARKER + "\n>",
        cleaned,
        count=1,
    )


def _canonical_back_matter_order(section_map: dict[str, str]) -> str:
    order = ("frontier", "summary", "review", "further", "key_terms", "companion")
    blocks = [section_map[key].strip() for key in order if key in section_map]
    return "\n\n".join(blocks) + "\n" if blocks else ""


def _classify_back_matter_section(heading: str) -> str | None:
    mapping = {
        "## Current Evidence and Frontier Biology": "frontier",
        "## Summary": "summary",
        "## Review Questions": "review",
        "## Further Reading and Source Notes": "further",
        "## Key Terms": "key_terms",
        "## Companion Source Module": "companion",
    }
    for prefix, key in mapping.items():
        if heading.startswith(prefix):
            return key
    return None


def reorder_back_matter(text: str) -> str:
    """Sort back-matter sections into the canonical order."""
    matches = list(_BACK_MATTER_SECTION_RES.finditer(text))
    if len(matches) < 2:
        return text
    first = matches[0].start()
    body = text[:first].rstrip()
    section_map: dict[str, str] = {}
    for match in matches:
        block = match.group(0).strip()
        heading = block.splitlines()[0]
        key = _classify_back_matter_section(heading)
        if key and key not in section_map:
            section_map[key] = block
    ordered = _canonical_back_matter_order(section_map)
    return body + "\n\n---\n\n" + ordered if ordered else text


def replace_legacy_titles(text: str, *, title: str) -> str:
    """Rewrite stale ``: <old title>`` suffixes on back-matter sections."""
    for prefix in (
        "Current Evidence and Frontier Biology",
        "Further Reading and Source Notes",
        "Companion Source Module",
    ):
        text = re.sub(
            rf"^##+ {re.escape(prefix)}: [^\n]+$",
            f"## {prefix}: {title}",
            text,
            flags=re.MULTILINE,
        )
    return text


def insert_opening_vignette(text: str, title: str) -> str:
    """Add a one-paragraph opening vignette if none is already present."""
    if OPENING_VIGNETTE_RE.search(text):
        return text
    anchor = text.find(_CURRICULUM_END)
    if anchor == -1:
        anchor = text.find("\n---\n")
    if anchor == -1:
        return text
    insert_at = text.find("\n", anchor)
    if insert_at == -1:
        return text
    block = (
        "\n\n---\n\n"
        f"> **Opening Vignette — {title}**\n"
        ">\n"
        f"> This chapter connects {title.lower()} to measurable evidence: models, datasets, "
        "and experiments that can strengthen or weaken each claim.\n"
    )
    return text[: insert_at + 1] + block + text[insert_at + 1 :]


def _summary_from_objectives(text: str, title: str) -> str:
    lines: list[str] = []
    in_lo = False
    for line in text.splitlines():
        if line.startswith("## Learning Objectives"):
            in_lo = True
            continue
        if in_lo and line.startswith("## "):
            break
        if in_lo and re.match(r"^\d+\.\s+", line):
            item = re.sub(r"^\d+\.\s+", "", line).strip()
            item = re.sub(r"\[\*\*([^*]+)\*\*\]\([^)]+\)", r"**\1**", item)
            item = re.sub(r"\\cite[tp]?\{[^}]+\}", "", item).strip()
            if item:
                lines.append(f"- {item}")
        if len(lines) >= 8:
            break
    if not lines:
        lines = [f"- Core ideas from **{title}** are summarized here after completing the chapter."]
    return f"## Summary\n\n{chr(10).join(lines)}\n"


def ensure_summary(text: str, *, stem: str, title: str) -> str:
    """Ensure each chapter has a Summary section (chapter-specific where required)."""
    if SUMMARY_HEADING_RE.search(text):
        if stem == "immune_system_defense":
            return trim_immune_summary(text)
        return text
    if stem == "endocrine_signaling":
        section = f"## Summary\n\n{_ENDOCRINE_SUMMARY_BULLETS}\n"
    else:
        section = _summary_from_objectives(text, title)
    return insert_before_anchor(
        text,
        section,
        (
            "## Key Terms",
            "## Review Questions",
            "## Further Reading and Source Notes:",
            "## Further Reading and Source Notes",
            "## Companion Source Module",
        ),
    )


def trim_immune_summary(text: str) -> str:
    """Strip endocrine bullets accidentally left in the immune-defense Summary."""
    match = SUMMARY_HEADING_RE.search(text)
    if not match:
        return text
    start = match.start()
    end_match = re.search(r"^---\s*$", text[start:], flags=re.MULTILINE)
    end = start + end_match.start() if end_match else len(text)
    block = text[start:end]
    lines = block.splitlines()
    kept: list[str] = [lines[0], ""]
    for line in lines[2:]:
        is_innate_start = line.startswith(_IMMUNE_SUMMARY_START)
        is_prohibited = any(line.startswith(prefix) for prefix in _IMMUNE_PROHIBITED_PREFIXES)
        in_bullet_continuation = bool(kept) and kept[-1].startswith("- **") and not is_prohibited
        if is_innate_start or in_bullet_continuation:
            if is_prohibited:
                continue
            kept.append(line)
    new_block = "\n".join(kept).rstrip() + "\n"
    return text[:start] + new_block + text[end:]


def ensure_concept_check(text: str, title: str) -> str:
    """Add a closing Concept Check prompt if one is missing."""
    if CONCEPT_CHECK_RE.search(text):
        return text
    check = (
        f"> **Concept Check:** State one claim from **{title}** and the observation "
        "that would most strongly challenge it.\n"
    )
    anchor = text.rfind("\n---\n")
    if anchor == -1:
        return text.rstrip() + "\n\n" + check
    return text[:anchor].rstrip() + "\n\n" + check + "\n" + text[anchor:]


def force_frontier(text: str, record: ChapterRecord) -> str:
    """Regenerate the Current-Evidence frontier block from the catalog."""
    generated = frontier_section(record).strip() + "\n\n"
    if FRONTIER_SECTION_PATTERN.search(text):
        return FRONTIER_SECTION_PATTERN.sub(lambda _m: generated, text, count=1)
    return insert_before_anchor(text, generated, _BACK_MATTER_ANCHORS)


def ensure_companion(text: str, record: ChapterRecord) -> str:
    """Append the canonical Companion Source Module section if missing."""
    heading = f"## Companion Source Module: {record.title}"
    if heading in text:
        return text
    section = companion_source_section(record).strip() + "\n"
    return text.rstrip() + "\n\n" + section


def repair_record(record: ChapterRecord, *, dry_run: bool = False, write_fn: _WriteFn | None = None) -> bool:
    """Repair shell invariants for one split chapter. Return True when content changed."""
    if record.stem not in SPLIT_STEMS:
        return False
    path = record.chapter_path
    original = path.read_text(encoding="utf-8")
    text = original
    text = dedupe_badges(text)
    text = replace_legacy_titles(text, title=record.title)
    text = insert_opening_vignette(text, record.title)
    text = force_frontier(text, record)
    text = ensure_summary(text, stem=record.stem, title=record.title)
    text = ensure_concept_check(text, record.title)
    text = ensure_companion(text, record)
    text = reorder_back_matter(text)
    text = re.sub(r"\\newpage\s*$", "", text.rstrip()) + "\n"
    if text == original:
        return False
    if not dry_run:
        writer = write_fn or _default_writer()
        writer(path, text)
    return True


def repair_lab(record: ChapterRecord, *, dry_run: bool = False, write_fn: _WriteFn | None = None) -> bool:
    """Append the Paper-Based Evidence Upgrade section to companion labs."""
    if record.stem not in SPLIT_STEMS:
        return False
    path = record.lab_path
    if not path.exists():
        return False
    text = path.read_text(encoding="utf-8")
    if "## Paper-Based Evidence Upgrade" in text:
        return False
    section = lab_evidence_section(record).strip() + "\n"
    new_text = insert_before_anchor(
        text,
        section,
        ("## Analysis Questions", "## Additional Analysis Questions", "## Debrief and Reflection"),
    )
    if new_text == text:
        return False
    if not dry_run:
        writer = write_fn or _default_writer()
        writer(path, new_text)
    return True


def repair_split_chapters(*, dry_run: bool = False, write_fn: _WriteFn | None = None) -> tuple[int, int]:
    """Repair every split chapter and lab. Return ``(chapter_changes, lab_changes)``."""
    records = chapter_records()
    chapter_changes = sum(repair_record(r, dry_run=dry_run, write_fn=write_fn) for r in records)
    lab_changes = sum(repair_lab(r, dry_run=dry_run, write_fn=write_fn) for r in records)
    return chapter_changes, lab_changes


__all__ = [
    "OLD_TITLES_BY_STEM",
    "SPLIT_STEMS",
    "dedupe_badges",
    "ensure_companion",
    "ensure_concept_check",
    "ensure_summary",
    "force_frontier",
    "insert_opening_vignette",
    "reorder_back_matter",
    "repair_lab",
    "repair_record",
    "repair_split_chapters",
    "replace_legacy_titles",
    "trim_immune_summary",
]
