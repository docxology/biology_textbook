"""Embedded enrichment engine for the biology textbook.

Frontier biology, lab evidence, and audit-matrix logic live here. Companion
source surfaces are delegated to :mod:`biology.enrichment.companion` and
question-bank answer keys to :mod:`biology.enrichment.answer_keys`; the public
names from those modules are re-exported here so existing callers continue to
import from a single facade.
"""

from __future__ import annotations

import re
from functools import partial

from biology.citations import citation_command_count
from biology.enrichment.answer_keys import (
    ANSWER_SIGNATURES,
    answer_key,
    common_pitfall,
    evidence_target,
    prompt_cues,
    refine_question_banks,
    scholarship_check,
)
from biology.enrichment.catalog import (
    EXTRA_FRONTIER_BY_STEM,
    FIGURE_BY_STEM,
    FOCUS_BY_STEM,
    FRONTIER_BY_UNIT,
    SOURCE_PRACTICE_BY_UNIT,
)
from biology.enrichment.companion import (
    companion_source_section,
    normalize_companion_source_modules,
)
from biology.enrichment.models import ChapterRecord
from biology.enrichment.paths import DOCS, MANUSCRIPT, PROJECT
from biology.maintenance.text_normalize import normalize_text
from textbook_io import write_text_atomic


# ---------------------------------------------------------------------------
# Frontier biology — per-chapter and per-unit
# ---------------------------------------------------------------------------


def frontier_section(record: ChapterRecord) -> str:
    """Return the canonical frontier-biology section body for one chapter."""

    unit_claim, unit_move = FRONTIER_BY_UNIT[record.unit_id]
    focus = FOCUS_BY_STEM[record.stem]
    source_practice = SOURCE_PRACTICE_BY_UNIT[record.unit_id]
    extra = EXTRA_FRONTIER_BY_STEM.get(record.stem, "")
    extra_block = f"\n\n{extra}" if extra else ""
    figure = FIGURE_BY_STEM.get(record.stem)
    figure_block = ""
    if figure is not None:
        figure_title, mermaid, alt, caption = figure
        figure_block = f"""
### Current Evidence Map: {figure_title}

```mermaid
{mermaid}
```
<!-- alt: {alt} -->
*{caption}*
"""
    title = f"## Current Evidence and Frontier Biology: {record.title}"
    return f"""
{title}

For **{record.title}**, frontier biology belongs inside the evidence logic of
the chapter. {unit_claim} The core reading question is this: {focus}

- **What to verify:** identify the observation, model, assay, or dataset that
  would make the claim stronger or weaker.
- **What to qualify:** state the scale, organism, cell type, environmental
  condition, or population where the claim is expected to hold.
- **What to compare:** test at least one alternative explanation, baseline, or
  null model before treating the pattern as causal.
- **What to cite:** distinguish primary evidence, review synthesis, public
  dataset, and institutional guidance; for recent or numeric claims, prefer
  the source closest to the measurement and state what has changed since it was
  published.

{unit_move}

**Source practice:** {source_practice}{extra_block}
{figure_block}
"""


FRONTIER_SECTION_PATTERN = re.compile(
    r"^## Current Evidence and Frontier Biology(?::[^\n]+)?\n.*?"
    r"(?=^## (?:Summary|Key Terms|Further Reading|Companion Source Module)(?::|\s|\{|$)|\Z)",
    flags=re.DOTALL | re.MULTILINE,
)

_FRONTIER_SECTION_RE = FRONTIER_SECTION_PATTERN


UNIT_THREAD_BY_UNIT: dict[str, str] = {
    unit: f"""
## Current Evidence Thread

Use this unit as an evidence trail rather than a list of topics. {claim} As you
move through the chapters, keep a two-column note: **claim** on the left,
**evidence that would change my confidence** on the right. By the end of the
unit, each major idea should be tied to a measurement, model, citation, or
paper-based lab decision.
"""
    for unit, (claim, _move) in FRONTIER_BY_UNIT.items()
}


def insert_before_anchor(text: str, section: str, anchors: tuple[str, ...]) -> str:
    """Insert ``section`` before the earliest matching anchor in ``text``."""

    lines = [line.strip() for line in section.strip().splitlines() if line.strip()]
    marker = lines[0] if lines else ""
    if marker and marker in text:
        return text
    positions = [text.find(anchor) for anchor in anchors if text.find(anchor) != -1]
    if not positions:
        return text.rstrip() + "\n\n" + section.strip() + "\n"
    pos = min(positions)
    return text[:pos].rstrip() + "\n\n" + section.strip() + "\n\n" + text[pos:].lstrip()


def _constant_replacement(_match: re.Match[str], *, replacement: str) -> str:
    return replacement


_FRONTIER_BOILERPLATE_MARKER = (
    "This chapter's frontier is not a separate topic bolted onto the end"
)


def _expected_frontier_heading(title: str) -> str:
    return f"## Current Evidence and Frontier Biology: {title}"


def _substantive_frontier_section(existing: str, generated: str, *, title: str) -> bool:
    """Return True when the on-disk frontier should be preserved over catalog output."""

    expected_heading = _expected_frontier_heading(title)
    first_line = existing.splitlines()[0].strip() if existing.strip() else ""
    if first_line and first_line != expected_heading:
        return False
    if existing.strip() == generated.strip():
        return True
    if _FRONTIER_BOILERPLATE_MARKER in existing:
        return False
    generic_physiology = (
        "Interpret physiological data by separating baseline variation"
    )
    if generic_physiology in existing:
        return False
    return len(existing.strip()) > len(generated.strip())


def enrich_chapters(records: list[ChapterRecord], dry_run: bool) -> int:
    """Insert or refresh the frontier section in each chapter."""

    changed = 0
    for record in records:
        path = record.chapter_path
        text = path.read_text(encoding="utf-8")
        section = frontier_section(record).strip() + "\n\n"
        generated = section.strip()
        if _FRONTIER_SECTION_RE.search(text):
            match = _FRONTIER_SECTION_RE.search(text)
            if match is None:
                continue
            existing = match.group(0).strip()
            if _substantive_frontier_section(existing, generated, title=record.title):
                continue
            replacer = partial(_constant_replacement, replacement=section)
            new_text = _FRONTIER_SECTION_RE.sub(replacer, text, count=1)
        else:
            new_text = insert_before_anchor(
                text,
                frontier_section(record),
                (
                    "## Summary",
                    "## Key Terms",
                    "## Further Reading and Source Notes:",
                    "## Further Reading and Source Notes",
                ),
            )
        if new_text != text:
            new_text = normalize_text(new_text).text
        if new_text != text:
            changed += 1
            if not dry_run:
                write_text_atomic(path, new_text)
    return changed


def refresh_chapter_scholarship_bullets(records: list[ChapterRecord], dry_run: bool) -> int:
    """Append the "What to cite" bullet to any frontier section missing it."""

    changed = 0
    marker = (
        "- **What to compare:** test at least one alternative explanation, baseline, or\n"
        "  null model before treating the pattern as causal.\n"
    )
    insertion = (
        "- **What to cite:** distinguish primary evidence, review synthesis, public\n"
        "  dataset, and institutional guidance; for recent or numeric claims, prefer\n"
        "  the source closest to the measurement and state what has changed since it was\n"
        "  published.\n"
    )
    for record in records:
        path = record.chapter_path
        text = path.read_text(encoding="utf-8")
        if "- **What to cite:**" in text or marker not in text:
            continue
        new_text = text.replace(marker, marker + insertion, 1)
        if new_text != text:
            changed += 1
            if not dry_run:
                write_text_atomic(path, new_text)
    return changed


def enrich_unit_intros(dry_run: bool) -> int:
    """Insert the current evidence thread into each unit introduction."""

    changed = 0
    for unit_id, section in UNIT_THREAD_BY_UNIT.items():
        path = MANUSCRIPT / unit_id / "unit_intro.md"
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        new_text = insert_before_anchor(
            text,
            section,
            ("## Computational Toolbox", "## Connections Across the Textbook", "## Chapter Roadmap"),
        )
        if new_text != text:
            changed += 1
            if not dry_run:
                write_text_atomic(path, new_text)
    return changed


# ---------------------------------------------------------------------------
# Lab evidence upgrade — paper-based reproducibility pass
# ---------------------------------------------------------------------------


def lab_evidence_section(record: ChapterRecord) -> str:
    """Return the paper-based evidence upgrade block for one lab."""

    focus = FOCUS_BY_STEM[record.stem]
    return f"""
## Paper-Based Evidence Upgrade

Before answering the analysis questions, annotate the paper dataset for
**{record.title}** with a reproducibility pass:

| Evidence check | Student action |
| --- | --- |
| Control logic | Mark the comparison that functions as the baseline, negative control, or reference case. |
| Uncertainty | Circle the row, card, diagram feature, or model assumption most likely to change the conclusion. |
| Model comparison | State whether a simpler rule, null model, or alternative mechanism could explain the same pattern. |
| Decision threshold | Write the minimum evidence that would make you revise the interpretation. |
| Reproducibility | Record the exact scoring rule another group would need to reproduce your classification. |

Focus note: {focus} Keep required work paper-based; any material-handling or
equipment version belongs only in an optional extension.
"""


def enrich_labs(records: list[ChapterRecord], dry_run: bool) -> int:
    """Insert the paper-based evidence upgrade into each companion lab."""

    changed = 0
    for record in records:
        path = record.lab_path
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        new_text = insert_before_anchor(
            text,
            lab_evidence_section(record),
            ("## Analysis Questions", "## Additional Analysis Questions", "## Debrief and Reflection"),
        )
        if new_text != text:
            changed += 1
            if not dry_run:
                write_text_atomic(path, new_text)
    return changed


# ---------------------------------------------------------------------------
# Audit matrix
# ---------------------------------------------------------------------------


def count_pattern(text: str, pattern: str) -> int:
    """Return the multiline match count of ``pattern`` in ``text``."""

    return len(re.findall(pattern, text, flags=re.MULTILINE))


def write_audit_matrix(records: list[ChapterRecord], dry_run: bool) -> int:
    """Refresh the embedded enrichment audit matrix in ``docs/``."""

    lines = [
        "# Embedded Enrichment Audit Matrix",
        "",
        "Generated by `scripts/enrich_embedded_textbook.py`. This matrix is a planning and review surface; canonical ordering remains `manuscript/config.yaml`.",
        "",
        "| Unit | Surface | Path | Current evidence | Embedded pass target |",
        "| --- | --- | --- | --- | --- |",
    ]
    for record in records:
        chapter_text = record.chapter_path.read_text(encoding="utf-8")
        h2_count = count_pattern(chapter_text, r"^##\s+")
        citation_count = citation_command_count(chapter_text)
        mermaid_count = count_pattern(chapter_text, r"^```mermaid")
        chapter_evidence = (
            f"{len(chapter_text):,} chars; "
            f"{h2_count} H2; "
            f"{citation_count} citations; "
            f"{mermaid_count} Mermaid"
        )
        lines.append(
            f"| {record.unit_id} | Chapter | `{record.chapter_path.relative_to(PROJECT)}` | {chapter_evidence} | Current evidence/frontier box; accessibility and citation review |"
        )
        if record.lab_path.exists():
            lab_text = record.lab_path.read_text(encoding="utf-8")
            lines.append(
                f"| {record.unit_id} | Lab | `{record.lab_path.relative_to(PROJECT)}` | {len(lab_text):,} chars | Paper-based evidence upgrade, controls, uncertainty, reproducibility |"
            )
        if record.question_path.exists():
            question_text = record.question_path.read_text(encoding="utf-8")
            solution_count = count_pattern(question_text, r"<!-- SOLUTION")
            lines.append(
                f"| {record.unit_id} | Questions | `{record.question_path.relative_to(PROJECT)}` | {solution_count} solution blocks | Prompt-specific answer keys, evidence use, scholarship checks |"
            )
    glossary_text = (MANUSCRIPT / "glossary.md").read_text(encoding="utf-8")
    glossary_anchor_count = count_pattern(glossary_text, r"\{#gl:")
    lines.extend(
        [
            f"| all | Glossary | `manuscript/glossary.md` | {glossary_anchor_count} anchors | Semantic references, qualified definitions, first-use closure |",
            "| all | Appendices | `manuscript/appendices/*.md` | reference appendices | Accessibility, semantic references, no hard-coded rendered numbers |",
            "",
            "## Review Defaults",
            "",
            "- Preserve 44 chapters, 44 labs, and 44 question banks.",
            "- Add embedded improvements only; do not add new renderable chapter surfaces.",
            "- Cite or qualify recent and numeric claims.",
            "- Keep required labs paper-based; optional material extensions stay clearly optional.",
            "- Use `\\cref{...}` and generated figure/equation labels instead of hard-coded rendered numbers.",
        ]
    )
    out = DOCS / "embedded_enrichment_audit_matrix.md"
    text = "\n".join(lines) + "\n"
    old = out.read_text(encoding="utf-8") if out.exists() else ""
    if text == old:
        return 0
    if not dry_run:
        write_text_atomic(out, text)
    return 1


__all__ = [
    "ANSWER_SIGNATURES",
    "FRONTIER_SECTION_PATTERN",
    "UNIT_THREAD_BY_UNIT",
    "answer_key",
    "common_pitfall",
    "companion_source_section",
    "count_pattern",
    "enrich_chapters",
    "enrich_labs",
    "enrich_unit_intros",
    "evidence_target",
    "frontier_section",
    "insert_before_anchor",
    "lab_evidence_section",
    "normalize_companion_source_modules",
    "prompt_cues",
    "refine_question_banks",
    "refresh_chapter_scholarship_bullets",
    "scholarship_check",
    "write_audit_matrix",
]
