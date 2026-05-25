#!/usr/bin/env python3
"""Repair pedagogy shells on chapters created by the Phase 5 mega-chapter split."""

from __future__ import annotations

import re
import sys

from _bootstrap import ensure_project_paths

ensure_project_paths()

from biology.enrichment.engine import (  # noqa: E402
    FRONTIER_SECTION_PATTERN,
    companion_source_section,
    frontier_section,
    insert_before_anchor,
    lab_evidence_section,
)
from biology.enrichment.records import chapter_records
from biology.quality.patterns import CONCEPT_CHECK_RE, OPENING_VIGNETTE_RE, SUMMARY_HEADING_RE
from textbook_io import write_text_atomic

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
- **Eicosanoids and disruption:** Arachidonic-acid derivatives mediate inflammation; glucocorticoids and NSAIDs target PLA$_2$ and COX; EDCs perturb hormone signalling during development.
- **Connections:** See \\cref{sec:unit_IX_immune_system_defense} for immune-endocrine coupling and \\cref{sec:unit_III_metabolic_integration} for metabolic integration."""

_IMMUNE_SUMMARY_START = "- **Innate immunity:**"


_BACK_MATTER_SECTION_RES = re.compile(
    r"^## (?:Current Evidence and Frontier Biology(?::[^\n]+)?|Summary(?:\b|[\s{:])|"
    r"Review Questions|Further Reading and Source Notes(?::[^\n]+)?|"
    r"Key Terms|Companion Source Module(?::[^\n]+)?)\b.*?"
    r"(?=^## (?:Current Evidence and Frontier Biology|Summary|Review Questions|"
    r"Further Reading and Source Notes|Key Terms|Companion Source Module)\b|\Z)",
    flags=re.MULTILINE | re.DOTALL,
)


def _dedupe_badges(text: str) -> str:
    if text.count(_BADGE_MARKER) <= 1:
        cleaned = text
    else:
        first = text.find(_BADGE_MARKER)
        rest = text[first + len(_BADGE_MARKER) :]
        rest = rest.replace(_BADGE_MARKER, "")
        cleaned = text[:first] + _BADGE_MARKER + rest
    return re.sub(
        re.escape(_BADGE_MARKER) + r"\n(?:\n)*>",
        _BADGE_MARKER + "\n>",
        cleaned,
        count=1,
    )


def _canonical_back_matter_order(section_map: dict[str, str]) -> str:
    order = (
        "frontier",
        "summary",
        "review",
        "further",
        "key_terms",
        "companion",
    )
    blocks = [section_map[key].strip() for key in order if key in section_map]
    if not blocks:
        return ""
    return "\n\n".join(blocks) + "\n"


def _classify_back_matter_section(heading: str) -> str | None:
    if heading.startswith("## Current Evidence and Frontier Biology"):
        return "frontier"
    if heading.startswith("## Summary"):
        return "summary"
    if heading.startswith("## Review Questions"):
        return "review"
    if heading.startswith("## Further Reading and Source Notes"):
        return "further"
    if heading.startswith("## Key Terms"):
        return "key_terms"
    if heading.startswith("## Companion Source Module"):
        return "companion"
    return None


def _reorder_back_matter(text: str) -> str:
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
    if not ordered:
        return text
    return body + "\n\n---\n\n" + ordered


def _replace_legacy_titles(text: str, *, stem: str, title: str) -> str:
    del stem
    section_prefixes = (
        "Current Evidence and Frontier Biology",
        "Further Reading and Source Notes",
        "Companion Source Module",
    )
    for prefix in section_prefixes:
        text = re.sub(
            rf"^##+ {re.escape(prefix)}: [^\n]+$",
            f"## {prefix}: {title}",
            text,
            flags=re.MULTILINE,
        )
    return text


def _insert_opening_vignette(text: str, title: str) -> str:
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
        lines = [f"- Core ideas from **{title}** are summarised here after completing the chapter."]
    body = "\n".join(lines)
    return f"## Summary\n\n{body}\n"


def _ensure_summary(text: str, *, stem: str, title: str) -> str:
    if SUMMARY_HEADING_RE.search(text):
        if stem == "immune_system_defense":
            return _trim_immune_summary(text)
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


def _trim_immune_summary(text: str) -> str:
    match = SUMMARY_HEADING_RE.search(text)
    if not match:
        return text
    start = match.start()
    end_match = re.search(r"^---\s*$", text[start:], flags=re.MULTILINE)
    end = start + end_match.start() if end_match else len(text)
    block = text[start:end]
    lines = block.splitlines()
    kept = [lines[0], ""]
    for line in lines[2:]:
        if line.startswith(_IMMUNE_SUMMARY_START) or (
            kept
            and kept[-1].startswith("- **")
            and not line.startswith("- **Endocrine")
            and not line.startswith("- **HPA")
            and not line.startswith("- **HPT")
            and not line.startswith("- **HPG")
            and not line.startswith("- **Glucose")
            and not line.startswith("- **Adrenal medulla")
            and not line.startswith("- **GH axis")
            and not line.startswith("- **Eicosanoids")
            and not line.startswith("- **Endocrine disruption")
        ):
            if line.startswith("- **Endocrine"):
                continue
            if line.startswith("- **HPA") or line.startswith("- **HPT") or line.startswith("- **HPG"):
                continue
            if line.startswith("- **Glucose homeostasis"):
                continue
            if line.startswith("- **Adrenal medulla"):
                continue
            if line.startswith("- **GH axis"):
                continue
            if line.startswith("- **Eicosanoids"):
                continue
            if line.startswith("- **Endocrine disruption"):
                continue
            kept.append(line)
    new_block = "\n".join(kept).rstrip() + "\n"
    return text[:start] + new_block + text[end:]


def _ensure_concept_check(text: str, title: str) -> str:
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


def _force_frontier(text: str, record) -> str:
    generated = frontier_section(record).strip() + "\n\n"
    if FRONTIER_SECTION_PATTERN.search(text):
        return FRONTIER_SECTION_PATTERN.sub(lambda _m: generated, text, count=1)
    return insert_before_anchor(
        text,
        generated,
        (
            "## Summary",
            "## Key Terms",
            "## Further Reading and Source Notes:",
            "## Further Reading and Source Notes",
        ),
    )


def _ensure_companion(text: str, record) -> str:
    heading = f"## Companion Source Module: {record.title}"
    if heading in text:
        return text
    section = companion_source_section(record).strip() + "\n"
    return text.rstrip() + "\n\n" + section


def repair_record(record, *, dry_run: bool) -> bool:
    if record.stem not in SPLIT_STEMS:
        return False
    path = record.chapter_path
    original = path.read_text(encoding="utf-8")
    text = original
    text = _dedupe_badges(text)
    text = _replace_legacy_titles(text, stem=record.stem, title=record.title)
    text = _insert_opening_vignette(text, record.title)
    text = _force_frontier(text, record)
    text = _ensure_summary(text, stem=record.stem, title=record.title)
    text = _ensure_concept_check(text, record.title)
    text = _ensure_companion(text, record)
    text = _reorder_back_matter(text)
    text = re.sub(r"\\newpage\s*$", "", text.rstrip()) + "\n"
    if text == original:
        return False
    if not dry_run:
        write_text_atomic(path, text)
    return True


def repair_lab(record, *, dry_run: bool) -> bool:
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
        write_text_atomic(path, new_text)
    return True


def main(argv: list[str] | None = None) -> int:
    dry_run = "--dry-run" in (argv or sys.argv[1:])
    records = chapter_records()
    chapter_changes = sum(repair_record(record, dry_run=dry_run) for record in records)
    lab_changes = sum(repair_lab(record, dry_run=dry_run) for record in records)
    mode = "DRY RUN" if dry_run else "APPLIED"
    print(f"[{mode}] chapters={chapter_changes} labs={lab_changes}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
