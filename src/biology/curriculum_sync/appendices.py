"""Curriculum sync engine."""

from __future__ import annotations

from collections.abc import Mapping
from html import escape
from itertools import pairwise
from textwrap import wrap
from typing import Any

from biology.crossref.helpers import section_reference
from biology.curriculum_sync.sync_blocks import (
    _framework_line,
    _join,
    _normalize_heading_text,
)
from biology.maintenance.text_normalize import normalize_text

CHAPTER_MARKER = ("<!-- curriculum-scaffold-start -->", "<!-- curriculum-scaffold-end -->")
NAV_MARKER = ("<!-- toc-navigation-start -->", "<!-- toc-navigation-end -->")
READING_PATHS_MARKER = ("<!-- suggested-reading-paths-start -->", "<!-- suggested-reading-paths-end -->")
CONCEPT_MAP_MARKER = ("<!-- textbook-concept-map-start -->", "<!-- textbook-concept-map-end -->")
PREFACE_SCOPE_MARKER = ("<!-- preface-scope-start -->", "<!-- preface-scope-end -->")



def build_appendix(
    records: tuple[Any, ...],
    chapter_meta: Any,
    alignments: Mapping[str, Any],
    book_toc: Any,
) -> str:
    meta_by_id = {record.chapter_id: record for record in chapter_meta.CHAPTERS}
    chapters_by_id = book_toc.chapters_by_id
    lines = [
        f"# {book_toc.references_by_file['appendix_curriculum_map.md'].title} {{#sec:appendix_curriculum_map .unnumbered}}",
        "",
        "This appendix is generated from `src/biology/curriculum/` and",
        "`src/biology/alignment.py`. It links each chapter to its companion lab,",
        "question bank, model/data skill, misconception probe, transfer task, and",
        "standards/skills alignment so the textbook can be composed into different",
        "course formats without losing pedagogical coherence.",
        "",
    ]
    current_unit: str | None = None
    for record in records:
        meta = meta_by_id[record.chapter_id]
        alignment = alignments[record.chapter_id]
        if meta.unit != current_unit:
            current_unit = meta.unit
            lines.extend(["", f"## Unit {current_unit} {{.unnumbered}}", ""])
        chapter = chapters_by_id[record.chapter_id]
        heading = f"{chapter.display_number} — {chapter.title}"
        lines.extend(
            [
                f"### {heading} {{.unnumbered}}",
                "",
                f"- **Chapter:** {section_reference(f'sec:{record.chapter_id}')}.",
                f"- **Lab:** {section_reference(record.lab_label)}.",
                f"- **Question bank:** {section_reference(record.question_label)}.",
                f"- **Big idea:** {record.big_idea}",
                f"- **Core concepts:** {', '.join(record.core_concepts)}.",
                f"- **Framework alignment:** {_framework_line(alignment)}",
                f"- **Practice cadence:** {_join(alignment.ap_science_practices)}.",
                f"- **Model/data skill:** {record.quantitative_model} {record.data_skill}",
                f"- **Misconception probe:** {record.common_misconception}",
                f"- **Transfer task:** {record.transfer_task}",
                "",
            ]
        )
    return _normalize_heading_text("\n".join(lines).rstrip() + "\n", unnumbered=True)

def build_instructor_appendix(
    records: tuple[Any, ...],
    chapter_meta: Any,
    alignments: Mapping[str, Any],
    book_toc: Any,
) -> str:
    meta_by_id = {record.chapter_id: record for record in chapter_meta.CHAPTERS}
    chapters_by_id = book_toc.chapters_by_id
    lines = [
        f"# {book_toc.references_by_file['appendix_instructor_orchestration.md'].title} {{#sec:appendix_instructor_orchestration .unnumbered}}",
        "",
        "This appendix is generated from the same curriculum and alignment records",
        "that populate chapter Study Blueprints. It gives instructors a compact",
        "sequence for turning the textbook into lectures, labs, quizzes, and transfer",
        "tasks without hand-rebuilding a course map.",
        "",
        "## Reusable Teaching Loop {.unnumbered}",
        "",
        "1. **Launch from a phenomenon.** Begin with a case, dataset, model failure,",
        "or observed pattern that makes the chapter question necessary.",
        "2. **Model the mechanism.** Ask students to draw, compute, simulate, or",
        "annotate the causal structure before reading the full explanation.",
        "3. **Interpret evidence.** Use the companion lab's finite printed packet,",
        "with synthetic and empirical observations identified, to practice analysis and reproducibility.",
        "These paper-based activities do not collect new empirical measurements; synthetic data remain teaching examples.",
        "4. **Check transfer.** Use the question bank to sample recall, application,",
        "data interpretation, and argumentation.",
        "5. **Close the loop.** Return to the transfer task and require a claim,",
        "evidence, reasoning, and uncertainty statement.",
        "",
        "## Chapter Orchestration Matrix {.unnumbered}",
        "",
    ]
    current_unit: str | None = None
    for record in records:
        meta = meta_by_id[record.chapter_id]
        alignment = alignments[record.chapter_id]
        if meta.unit != current_unit:
            current_unit = meta.unit
            lines.extend(["", f"### Unit {current_unit} {{.unnumbered}}", ""])
        chapter = chapters_by_id[record.chapter_id]
        heading = f"{chapter.display_number} — {chapter.title}"
        lines.extend(
            [
                f"#### {heading} {{.unnumbered}}",
                "",
                f"- **Core thread:** {alignment.spiral_thread}",
                f"- **Instructor move:** {alignment.instructor_move}",
                f"- **Formative check:** {alignment.formative_check}",
                f"- **Summative product:** {alignment.summative_product}",
                (
                    f"- **Lab/question pair:** {section_reference(record.lab_label)}; "
                    f"{section_reference(record.question_label)}."
                ),
                f"- **External alignment:** {_framework_line(alignment)}",
                "",
            ]
        )
    return _normalize_heading_text("\n".join(lines).rstrip() + "\n", unnumbered=True)

def build_front_matter_navigation(book_toc: Any) -> str:
    lines = [
        NAV_MARKER[0],
        "The textbook is organized from systems-level orientation through molecular,",
        "cellular, organismal, evolutionary, and ecological scales. The entries below",
        "are generated from `docs/manuscript/config.yaml` so navigation stays aligned with",
        "the rendered table of contents.",
        "",
    ]
    for unit in book_toc.units:
        chapter_list = "; ".join(chapter.hyperlink_ref for chapter in unit.chapters)
        lines.append(f"- **{unit.hyperlink_display_title}:** {chapter_list}.")
    lines.extend(
        [
            "- **Laboratory activities:** the laboratory appendix collects one companion lab per chapter",
            "in the chapters' canonical order, after the core chapter sequence.",
            "- **Question banks:** a separate question-bank appendix collects one 30-item bank per chapter",
            "in the same canonical order, after the laboratory sequence.",
        ]
    )
    for reference in book_toc.references:
        lines.append(
            f"- **{reference.hyperlink_ref}:** reference material generated or ordered from the same manifest."
        )
    lines.extend(
        [
            "- **Source modules:** `src/biology/<domain>/` contains the tested Python",
            "implementations for the quantitative models used throughout the book.",
            NAV_MARKER[1],
        ]
    )
    return "\n".join(lines)

def _unit_ref(book_toc: Any, unit_id: str) -> str:
    return book_toc.units_by_id[unit_id].hyperlink_ref

def _chapter_ref(book_toc: Any, chapter_id: str) -> str:
    return book_toc.chapters_by_id[chapter_id].hyperlink_ref

def build_suggested_reading_paths(book_toc: Any) -> str:
    """Return the generated suggested reading paths table."""
    rows = [
        READING_PATHS_MARKER[0],
        "| Path | Emphasis | Notes |",
        "| ---- | -------- | ----- |",
        (
            "| **AP / first-year survey** | "
            f"{_unit_ref(book_toc, 'unit_I')}; {_unit_ref(book_toc, 'unit_II')}; "
            f"{_unit_ref(book_toc, 'unit_III')}; selected genetics/evolution chapters; "
            f"{_unit_ref(book_toc, 'unit_X')} | "
            "Skim the systems orientation; prioritize metabolism and genetics core narratives. |"
        ),
        (
            "| **Pre-health / majors** | "
            f"{_unit_ref(book_toc, 'unit_I')} through {_unit_ref(book_toc, 'unit_IX')}; "
            f"{_unit_ref(book_toc, 'unit_X')}; systems orientation as setup | "
            "Add labs for quantitative skills; pair each physiology chapter with its Python bridge. |"
        ),
        (
            "| **Ecology / environmental focus** | "
            f"{_unit_ref(book_toc, 'unit_I')} and {_unit_ref(book_toc, 'unit_II')} as review; "
            f"{_chapter_ref(book_toc, 'unit_III_photosynthesis')}; "
            f"{_unit_ref(book_toc, 'unit_VI')}; {_unit_ref(book_toc, 'unit_VII')}; "
            f"{_unit_ref(book_toc, 'unit_X')} | "
            "Emphasize population models, biogeochemistry, and conservation metrics in `biology.ecology.ecology`. |"
        ),
        (
            "| **Computation-first** | "
            f"{_unit_ref(book_toc, 'unit_0')} plus any later unit | "
            "Read “Bridge to computation” blocks first, then narrative; run `scripts/generate_figures.py`. |"
        ),
        READING_PATHS_MARKER[1],
    ]
    return "\n".join(rows)

def build_preface_scope_table(book_toc: Any) -> str:
    """Return the generated preface scope table."""
    lines = [
        PREFACE_SCOPE_MARKER[0],
        "| Instructional block | Core chapters |",
        "| ---- | ------------- |",
    ]
    for unit in book_toc.units:
        chapter_list = "; ".join(chapter.hyperlink_ref for chapter in unit.chapters)
        lines.append(f"| **{unit.hyperlink_ref}** | {chapter_list} |")
    lines.append(PREFACE_SCOPE_MARKER[1])
    return "\n".join(lines)

def build_textbook_concept_map(book_toc: Any) -> str:
    """Group canonical unit labels into an explicitly editorial relationship map."""
    groups = (
        ("mechanisms", "Models and cellular mechanisms", ("unit_I", "unit_II", "unit_III")),
        ("inheritance", "Information, inheritance and change", ("unit_IV", "unit_V", "unit_VI")),
        ("environments", "Organisms and environments", ("unit_VII", "unit_VIII", "unit_IX", "unit_X")),
    )
    units = {unit.unit_id: unit for unit in book_toc.units}
    relationships = (
        ("unit_I", "unit_II", "---|molecular interactions|"),
        ("unit_II", "unit_III", "---|membrane gradients|"),
        ("unit_IV", "unit_V", "---|inheritance|"),
        ("unit_V", "unit_VI", "---|allele frequencies|"),
        ("unit_VII", "unit_X", "---|nutrient cycling|"),
        ("unit_VIII", "unit_X", "---|primary production|"),
        ("unit_IX", "unit_X", "---|organisms in environments|"),
    )
    lines = [
        CONCEPT_MAP_MARKER[0],
        "Unit labels come from `docs/manuscript/config.yaml`. The groups and connections",
        "below are editorial selections, not a derived prerequisite or causal graph.",
        "",
        "```mermaid",
        "---",
        "config:",
        "  layout: dagre",
        "---",
        "graph TD",
    ]
    active_groups = []
    for group, title, identifiers in groups:
        members = [units[key] for key in identifiers if key in units]
        if not members:
            continue
        active_groups.append(group)
        lines.extend([f'    subgraph {group}["{title}"]', "        direction LR"])
        for unit in members:
            title_lines = "<br/>".join(escape(part) for part in wrap(unit.title, width=24))
            lines.append(f'        {unit.unit_id}["Unit {escape(unit.label)}<br/>{title_lines}"]')
        for source, target, connector in relationships:
            if source in identifiers and target in identifiers and source in units and target in units:
                lines.append(f"        {source} {connector} {target}")
        lines.append("    end")
        lines.append(f"    style {group} fill:#fafafa,stroke:#526777,color:#17212b")
    lens = units.get("unit_0")
    if lens is not None:
        title_lines = "<br/>".join(escape(part) for part in wrap(lens.title, width=24))
        lines.append(f'    unit_0["Unit {escape(lens.label)}<br/>{title_lines}"]')
        if "mechanisms" in active_groups:
            lines.append('    unit_0 -.-|"optional systems lens"| mechanisms')
    for source, target in pairwise(active_groups):
        lines.append(f"    {source} --- {target}")
    lines.extend([
        "    classDef topic fill:#eef5fa,stroke:#0077bb,color:#111111",
        "    classDef lens fill:#f4f4f4,stroke:#666666,color:#111111,stroke-dasharray:4 3",
    ])
    for unit in book_toc.units:
        lines.append(f"    class {unit.unit_id} {'lens' if unit.unit_id == 'unit_0' else 'topic'}")
    caption = (
        "Textbook relationship map: models and cellular mechanisms, inheritance and evolutionary change, "
        "and organisms in environments are complementary topic groups. Dotted connections indicate an "
        "example optional systems lens; solid connections identify selected relationships, not required "
        "reading order or measured causation. Labels are config-derived; grouping and links are authored "
        "in `src/biology/curriculum_sync/appendices.py`. Omitted links do not imply independence."
    )
    alt = (
        "Grouped panels organize the displayed unit topics; solid links identify selected relationships, "
        "not prerequisites or measured causes."
    )
    if lens is not None and "mechanisms" in active_groups:
        alt += " A dotted link adds an optional systems lens."
    lines.extend([
        "```", "", f"<!-- alt: {alt} -->", "",
        f"*{caption}*", "", CONCEPT_MAP_MARKER[1],
    ])
    return normalize_text("\n".join(lines)).text

