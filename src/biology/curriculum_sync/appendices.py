"""Curriculum sync engine."""

from __future__ import annotations

import importlib
import importlib.util
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from types import ModuleType
from typing import Any, Mapping

from biology.curriculum_sync.paths import MANUSCRIPT, SRC, TEMPLATE_ROOT
from biology.curriculum_sync.sync_blocks import _framework_line, _join
from textbook_io import write_text_atomic


CHAPTER_MARKER = ("<!-- curriculum-scaffold-start -->", "<!-- curriculum-scaffold-end -->")
LAB_MARKER = ("<!-- lab-evidence-checklist-start -->", "<!-- lab-evidence-checklist-end -->")
QUESTION_MARKER = ("<!-- question-coverage-start -->", "<!-- question-coverage-end -->")
NAV_MARKER = ("<!-- toc-navigation-start -->", "<!-- toc-navigation-end -->")
READING_PATHS_MARKER = ("<!-- suggested-reading-paths-start -->", "<!-- suggested-reading-paths-end -->")
CONCEPT_MAP_MARKER = ("<!-- textbook-concept-map-start -->", "<!-- textbook-concept-map-end -->")
PREFACE_SCOPE_MARKER = ("<!-- preface-scope-start -->", "<!-- preface-scope-end -->")
HEADING_RE = re.compile(r"^(?P<hashes>#{1,6})(?P<space>\s*)(?P<title>.*)$")

HEADING_ATTR_RE = re.compile(r"^(?P<title>.*?)(?:\s+\{(?P<attrs>[^}]*)\})\s*$")
MANUAL_HEADING_NUMBER_RE = re.compile(r"^\d+(?:\.\d+)*\.?\s+(?P<title>\S.*)$")
ALT_COMMENT_THEMATIC_BREAK_RE = re.compile(
    r"(<!--\s*alt:\s*.*?\s*-->)\n---",
    flags=re.DOTALL,
)
NONNUMBERED_ATTR = ".unnumbered"
SOURCE_SECTION_TITLES = {
    "Current Evidence and Frontier Biology",
    "Further Reading and Source Notes",
    "Companion Source Module",
}



def build_appendix(
    records: tuple[Any, ...],
    chapter_meta: Any,
    alignments: Mapping[str, Any],
    book_toc: Any,
) -> str:
    meta_by_id = {record.chapter_id: record for record in chapter_meta.CHAPTERS}
    chapters_by_id = book_toc.chapters_by_id
    lines = [
        f"# {book_toc.references_by_file['appendix_curriculum_map.md'].title} {{.unnumbered}}",
        "",
        "\\label{sec:appendix_curriculum_map}",
        "",
        "This appendix is generated from `src/biology/curriculum.py` and",
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
                f"- **Chapter:** \\cref{{sec:{record.chapter_id}}}.",
                f"- **Lab:** \\cref{{{record.lab_label}}}.",
                f"- **Question bank:** \\cref{{{record.question_label}}}.",
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
    return "\n".join(lines).rstrip() + "\n"

def build_instructor_appendix(
    records: tuple[Any, ...],
    chapter_meta: Any,
    alignments: Mapping[str, Any],
    book_toc: Any,
) -> str:
    meta_by_id = {record.chapter_id: record for record in chapter_meta.CHAPTERS}
    chapters_by_id = book_toc.chapters_by_id
    lines = [
        f"# {book_toc.references_by_file['appendix_instructor_orchestration.md'].title} {{.unnumbered}}",
        "",
        "\\label{sec:appendix_instructor_orchestration}",
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
        "3. **Gather evidence.** Use the companion lab as the measurement and",
        "reproducibility surface for the chapter.",
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
                f"- **Lab/question pair:** \\cref{{{record.lab_label}}}; "
                f"\\cref{{{record.question_label}}}.",
                f"- **External alignment:** {_framework_line(alignment)}",
                "",
            ]
        )
    return "\n".join(lines).rstrip() + "\n"

def build_front_matter_navigation(book_toc: Any) -> str:
    lines = [
        NAV_MARKER[0],
        "The textbook is organized from systems-level orientation through molecular,",
        "cellular, organismal, evolutionary, and ecological scales. The entries below",
        "are generated from `manuscript/config.yaml` so navigation stays aligned with",
        "the rendered table of contents.",
        "",
    ]
    for unit in book_toc.units:
        chapter_list = "; ".join(chapter.name_ref for chapter in unit.chapters)
        lines.append(f"- **{unit.name_ref}:** {chapter_list}.")
    lines.extend(
        [
            "- **Laboratory activities:** one companion lab follows each chapter in the",
            "same canonical order.",
            "- **Question banks:** one 30-item question bank follows each chapter in the",
            "same canonical order.",
        ]
    )
    for reference in book_toc.references:
        lines.append(
            f"- **{reference.name_ref}:** reference material generated or ordered from the same manifest."
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
    return book_toc.units_by_id[unit_id].name_ref

def _chapter_ref(book_toc: Any, chapter_id: str) -> str:
    return book_toc.chapters_by_id[chapter_id].name_ref

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
            "Skim the systems orientation; prioritise metabolism and genetics core narratives. |"
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
            "Emphasise population models, biogeochemistry, conservation metrics in `ecology.py`. |"
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
        chapter_list = "; ".join(chapter.name_ref for chapter in unit.chapters)
        lines.append(f"| **{unit.name_ref}** | {chapter_list} |")
    lines.append(PREFACE_SCOPE_MARKER[1])
    return "\n".join(lines)

def build_textbook_concept_map(book_toc: Any) -> str:
    """Return the generated front-matter concept map block."""
    summaries = {
        "unit_0": "feedback, emergence,<br/>active inference, history",
        "unit_I": "atoms, bonds, water,<br/>macromolecules, enzymes",
        "unit_II": "organelles, membranes,<br/>signalling, transport",
        "unit_III": "respiration, photosynthesis,<br/>ATP, chemiosmosis",
        "unit_IV": "DNA, transcription,<br/>translation, genomics",
        "unit_V": "Mendelian, chromosomal,<br/>population genetics",
        "unit_VI": "selection, drift,<br/>speciation, phylogenetics",
        "unit_VII": "bacteria, viruses,<br/>microbiome, disease",
        "unit_VIII": "structure, reproduction,<br/>responses, hormones",
        "unit_IX": "circulation, nervous system,<br/>endocrine, immune",
        "unit_X": "populations, communities,<br/>ecosystems, conservation",
    }
    styles = {
        "unit_0": "#34495e",
        "unit_I": "#4a90d9",
        "unit_II": "#8e44ad",
        "unit_III": "#e67e22",
        "unit_IV": "#e74c3c",
        "unit_V": "#c0392b",
        "unit_VI": "#27ae60",
        "unit_VII": "#16a085",
        "unit_VIII": "#2ecc71",
        "unit_IX": "#3498db",
        "unit_X": "#1abc9c",
    }
    node_ids = {
        "unit_0": "U0",
        "unit_I": "I",
        "unit_II": "II",
        "unit_III": "III",
        "unit_IV": "IV",
        "unit_V": "V",
        "unit_VI": "VI",
        "unit_VII": "VII",
        "unit_VIII": "VIII",
        "unit_IX": "IX",
        "unit_X": "X",
    }
    dependency_edges = (
        ("unit_0", "unit_I", "-.->|conceptual lens|"),
        ("unit_0", "unit_II", "-.->|conceptual lens|"),
        ("unit_0", "unit_X", "-.->|conceptual lens|"),
        ("unit_0", "unit_IX", "-.->|conceptual lens|"),
        ("unit_I", "unit_II", "-->"),
        ("unit_I", "unit_III", "-->"),
        ("unit_II", "unit_III", "-->"),
        ("unit_II", "unit_IV", "-->"),
        ("unit_III", "unit_IV", "-->"),
        ("unit_IV", "unit_V", "-->"),
        ("unit_V", "unit_VI", "-->"),
        ("unit_VI", "unit_VII", "-->"),
        ("unit_I", "unit_VII", "-->"),
        ("unit_II", "unit_VIII", "-->"),
        ("unit_III", "unit_VIII", "-->"),
        ("unit_IV", "unit_IX", "-->"),
        ("unit_II", "unit_IX", "-->"),
        ("unit_VI", "unit_X", "-->"),
        ("unit_VII", "unit_X", "-->"),
        ("unit_VIII", "unit_X", "-->"),
        ("unit_IX", "unit_X", "-->"),
    )
    lines = [
        CONCEPT_MAP_MARKER[0],
        "The instructional blocks form an interdependent architecture. The diagram",
        "below shows primary dependency paths and integrative threads.",
        "",
        "```mermaid",
        "graph TD",
    ]
    for unit in book_toc.units:
        summary = summaries[unit.unit_id]
        node = node_ids[unit.unit_id]
        lines.append(f'    {node}["{unit.display_title}<br/>{summary}"]')
    lines.append("")
    for source, target, arrow in dependency_edges:
        lines.append(f"    {node_ids[source]} {arrow} {node_ids[target]}")
    lines.append("")
    for unit in book_toc.units:
        lines.append(f"    style {node_ids[unit.unit_id]} fill:{styles[unit.unit_id]},color:#fff")
    lines.extend(
        [
            "```",
            "",
            "<!-- alt: Graph showing generated dependency map derived from manuscript/config.yaml: "
            "dashed links show the systems orientation as a conceptual lens, and solid arrows show "
            "dependencies through the canonical unit sequence. -->",
            "",
            "*Generated dependency map derived from `manuscript/config.yaml`: dashed links show "
            "the systems orientation as a conceptual lens, and solid arrows show dependencies "
            "through the canonical unit sequence.*",
            "",
            CONCEPT_MAP_MARKER[1],
        ]
    )
    return "\n".join(lines)

