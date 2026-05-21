#!/usr/bin/env python3
"""Synchronize curriculum scaffolds across chapters, labs, and question banks.

This script is intentionally idempotent. It reads ``src/biology/curriculum.py``
and writes the same structured pedagogy layer into every matching textbook
surface:

* chapter Study Blueprint blocks,
* lab evidence/reproducibility checklists,
* question-bank coverage notes,
* generated curriculum-map and instructor appendices,
* table-of-contents-controlled H1 titles and front-matter navigation.
"""

from __future__ import annotations

import argparse
import importlib
import importlib.util
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from types import ModuleType
from typing import Any, Mapping

try:
    from scripts.atomic_io import write_text_atomic
except ModuleNotFoundError:  # pragma: no cover - direct script execution path
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from atomic_io import write_text_atomic  # type: ignore[import-not-found,no-redef]


PROJECT = Path(__file__).resolve().parent.parent
MANUSCRIPT = PROJECT / "manuscript"
SRC = PROJECT / "src"
TEMPLATE_ROOT = PROJECT.parent.parent

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


@dataclass
class SyncReport:
    """Counts of files changed by the synchronization pass."""

    chapters_updated: int = 0
    labs_updated: int = 0
    questions_updated: int = 0
    appendix_updated: bool = False
    instructor_appendix_updated: bool = False
    titles_updated: int = 0
    heading_titles_updated: int = 0
    front_matter_updated: bool = False


def _load_module(name: str, path: Path) -> ModuleType:
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Could not load {name} from {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def _load_biology_module(name: str) -> ModuleType:
    for path in (SRC, TEMPLATE_ROOT):
        if str(path) not in sys.path:
            sys.path.insert(0, str(path))
    return importlib.import_module(f"biology.{name}")


def _chapter_path(chapter_id: str) -> Path:
    parts = chapter_id.split("_", 2)
    if len(parts) != 3:
        raise ValueError(f"Unexpected chapter id: {chapter_id}")
    unit_dir = f"{parts[0]}_{parts[1]}"
    return MANUSCRIPT / unit_dir / f"{parts[2]}.md"


def _lab_path(chapter_id: str) -> Path:
    parts = chapter_id.split("_", 2)
    if len(parts) != 3:
        raise ValueError(f"Unexpected chapter id: {chapter_id}")
    unit_dir = f"{parts[0]}_{parts[1]}"
    return MANUSCRIPT / "labs" / unit_dir / f"lab_{parts[2]}.md"


def _question_path(chapter_id: str) -> Path:
    parts = chapter_id.split("_", 2)
    if len(parts) != 3:
        raise ValueError(f"Unexpected chapter id: {chapter_id}")
    unit_dir = f"{parts[0]}_{parts[1]}"
    return MANUSCRIPT / "questions" / unit_dir / f"questions_{parts[2]}.md"


def _title(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    match = re.search(r"^#\s+(.+)$", text, flags=re.MULTILINE)
    return match.group(1).strip() if match else path.stem.replace("_", " ").title()


def _replace_block(text: str, marker: tuple[str, str], block: str) -> tuple[str, bool]:
    start, end = marker
    single_block = re.escape(start) + r".*?" + re.escape(end)
    pattern = re.compile(r"(?:" + single_block + r"\s*)+", flags=re.DOTALL)
    if pattern.search(text):
        new_text = pattern.sub(lambda _match: f"{block}\n\n", text)
        return new_text, True
    return text, False


def _write_if_changed(path: Path, text: str, *, dry_run: bool) -> bool:
    old = path.read_text(encoding="utf-8") if path.exists() else ""
    if text == old:
        return False
    if not dry_run:
        write_text_atomic(path, text)
    return True


def _split_heading_attrs(title: str) -> tuple[str, set[str]]:
    match = HEADING_ATTR_RE.match(title.strip())
    if match is None:
        return title.strip(), set()
    attrs = {part for part in (match.group("attrs") or "").split() if part}
    return match.group("title").strip(), attrs


def _format_heading(title: str, attrs: set[str]) -> str:
    clean_title = title.strip()
    if not attrs:
        return clean_title
    ordered = sorted(attrs, key=lambda attr: (attr != NONNUMBERED_ATTR, attr))
    return f"{clean_title} {{{' '.join(ordered)}}}"


def _toc_safe_heading_title(title: str) -> str:
    clean, attrs = _split_heading_attrs(title)
    while True:
        match = MANUAL_HEADING_NUMBER_RE.match(clean)
        if match is None:
            break
        clean = match.group("title").strip()
    clean = clean.strip()
    if clean == "Bridge to computation":
        clean = "Computational Bridge"
    elif clean == "Source Code Module":
        clean = "Companion Source Module"
    elif clean == "Procedure":
        clean = "Experimental Procedure"
    elif clean == "Additional Analysis Questions":
        clean = "Extension Analysis Questions"
    elif clean == "Further Reading":
        clean = "Further Reading and Source Notes"
    if not clean:
        clean = "Additional Island Biogeography Evidence"
    return _format_heading(clean, attrs)


def _replace_first_h1(text: str, title: str) -> tuple[str, bool]:
    pattern = re.compile(r"^#\s+(.+)$", flags=re.MULTILINE)
    match = pattern.search(text)
    if match is not None:
        current_title, attrs = _split_heading_attrs(match.group(1))
        if current_title == title:
            return text, False
        replacement = f"# {_format_heading(title, attrs)}"
        new_text = pattern.sub(replacement, text, count=1)
        return new_text, new_text != text
    replacement = f"# {title}"
    return f"{replacement}\n\n{text}", True


def sync_h1(path: Path, title: str, *, dry_run: bool) -> bool:
    text = path.read_text(encoding="utf-8")
    replaced, changed = _replace_first_h1(text, title)
    return changed and _write_if_changed(path, replaced, dry_run=dry_run)


def sync_section_label(path: Path, label: str, *, dry_run: bool) -> bool:
    """Ensure a ``sec:`` label is present immediately below the first H1."""
    text = path.read_text(encoding="utf-8")
    label_line = f"\\label{{{label}}}"
    if label_line in text:
        return False
    lines = text.splitlines()
    for index, line in enumerate(lines):
        if line.startswith("# "):
            insert_at = index + 1
            while insert_at < len(lines) and lines[insert_at].strip() == "":
                insert_at += 1
            new_lines = lines[: insert_at] + ["", label_line] + lines[insert_at:]
            return _write_if_changed(path, "\n".join(new_lines) + "\n", dry_run=dry_run)
    return _write_if_changed(path, f"# {path.stem}\n\n{label_line}\n\n{text}", dry_run=dry_run)


def normalize_headings(path: Path, *, unnumbered: bool, dry_run: bool) -> bool:
    """Normalize Markdown headings so LaTeX numbering and ToC titles stay clean."""
    original = path.read_text(encoding="utf-8")
    text = ALT_COMMENT_THEMATIC_BREAK_RE.sub(r"\1\n\n---", original)
    lines: list[str] = []
    in_fence = False
    in_yaml_front_matter = False
    yaml_delimiters_seen = 0
    for line_no, line in enumerate(text.splitlines(), start=1):
        if line.strip() == "---" and (line_no == 1 or in_yaml_front_matter):
            yaml_delimiters_seen += 1
            in_yaml_front_matter = yaml_delimiters_seen == 1
            lines.append(line)
            continue
        if in_yaml_front_matter:
            lines.append(line)
            continue
        stripped = line.lstrip()
        if stripped.startswith("```"):
            in_fence = not in_fence
            lines.append(line)
            continue
        if in_fence:
            lines.append(line)
            continue
        match = HEADING_RE.match(line)
        if match is None:
            lines.append(line)
            continue
        hashes = match.group("hashes")
        raw_title = match.group("title").strip()
        if not raw_title and not match.group("space"):
            lines.append(line)
            continue
        clean_title, attrs = _split_heading_attrs(_toc_safe_heading_title(raw_title))
        if unnumbered:
            attrs.add(NONNUMBERED_ATTR)
        lines.append(f"{hashes} {_format_heading(clean_title, attrs)}")
    normalized = "\n".join(lines)
    if text.endswith("\n"):
        normalized += "\n"
    return normalized != original and _write_if_changed(path, normalized, dry_run=dry_run)


def _join(values: tuple[str, ...]) -> str:
    return ", ".join(values)


def _framework_line(alignment: Any) -> str:
    return (
        f"Vision & Change: {_join(alignment.vision_change_concepts)}; "
        f"AP Biology: {_join(alignment.ap_big_ideas)}; "
        f"NGSS-style topics: {_join(alignment.ngss_topics)}."
    )


def _chapter_block(record: Any, alignment: Any) -> str:
    concepts = ", ".join(record.core_concepts)
    return "\n".join(
        [
            CHAPTER_MARKER[0],
            "### Study Blueprint",
            "",
            f"- **Big idea:** {record.big_idea}",
            f"- **Core concepts:** {concepts}.",
            f"- **Framework alignment:** {_framework_line(alignment)}",
            f"- **Model or quantitative lens:** {record.quantitative_model}",
            f"- **Data skill:** {record.data_skill}",
            f"- **Practice cadence:** {_join(alignment.ap_science_practices)}.",
            f"- **Common misconception to repair:** {record.common_misconception}",
            f"- **Primary lab:** \\cref{{{record.lab_label}}}.",
            f"- **Question bank:** \\cref{{{record.question_label}}}.",
            f"- **Transfer task:** {record.transfer_task}",
            f"- **Bridge to computation:** `{record.bridge_api}`.",
            CHAPTER_MARKER[1],
        ]
    )


def _lab_block(record: Any, alignment: Any) -> str:
    return "\n".join(
        [
            LAB_MARKER[0],
            "## Evidence and Reproducibility Checklist {.unnumbered}",
            "",
            f"- **Primary evidence goal:** {record.lab_focus}",
            f"- **Data skill to practice:** {record.data_skill}",
            f"- **BioSkills emphasis:** {_join(alignment.bioskills)}.",
            "- **Control logic:** identify at least one positive control, one negative control, "
            "or one baseline comparison before interpreting results.",
            "- **Measurement discipline:** record units, uncertainty, sample size, and any "
            "discarded observation with a reason.",
            "- **Mechanistic link:** connect one result directly to the parent chapter's big "
            "idea before writing the conclusion.",
            "- **Reproducibility check:** state one procedural detail that another group "
            "would need in order to reproduce the result.",
            LAB_MARKER[1],
        ]
    )


def _question_block(record: Any, alignment: Any) -> str:
    return "\n".join(
        [
            QUESTION_MARKER[0],
            "## Instructor Use and Coverage Notes {.unnumbered}",
            "",
            f"- **Coverage target:** {record.assessment_focus}",
            f"- **Model/data emphasis:** {record.quantitative_model}",
            f"- **Assessment alignment:** {_join(alignment.ap_science_practices)}.",
            f"- **Misconception probe:** {record.common_misconception}",
            f"- **Transfer product:** {alignment.summative_product}",
            "- **Grading focus:** award full credit for mechanism, evidence, boundary "
            "conditions, and units when a calculation is required.",
            "- **Suggested use:** draw one recall item, one application item, and one "
            "synthesis item when building a short quiz from this bank.",
            QUESTION_MARKER[1],
        ]
    )


def sync_chapter(path: Path, record: Any, alignment: Any, *, dry_run: bool) -> bool:
    text = path.read_text(encoding="utf-8")
    block = _chapter_block(record, alignment)
    replaced, changed = _replace_block(text, CHAPTER_MARKER, block)
    if not changed:
        anchor = replaced.find("\n---", replaced.find("## Learning Objectives"))
        if anchor == -1:
            anchor = replaced.find("\n## ", replaced.find("## Learning Objectives") + 1)
        if anchor == -1:
            anchor = len(replaced)
        replaced = f"{replaced[:anchor].rstrip()}\n\n{block}\n\n{replaced[anchor:].lstrip()}"
    return _write_if_changed(path, replaced, dry_run=dry_run)


def sync_lab(path: Path, record: Any, alignment: Any, *, dry_run: bool) -> bool:
    text = path.read_text(encoding="utf-8")
    block = _lab_block(record, alignment)
    replaced, changed = _replace_block(text, LAB_MARKER, block)
    if not changed:
        anchor = replaced.find("\n## Analysis Questions")
        if anchor == -1:
            anchor = replaced.find("\n## Debrief")
        if anchor == -1:
            anchor = len(replaced)
        replaced = f"{replaced[:anchor].rstrip()}\n\n{block}\n\n{replaced[anchor:].lstrip()}"
    return _write_if_changed(path, replaced, dry_run=dry_run)


def sync_question(path: Path, record: Any, alignment: Any, *, dry_run: bool) -> bool:
    text = path.read_text(encoding="utf-8")
    block = _question_block(record, alignment)
    replaced, changed = _replace_block(text, QUESTION_MARKER, block)
    if not changed:
        anchor = replaced.find("\n## Questions")
        if anchor == -1:
            anchor = replaced.find("\n1. ")
        if anchor == -1:
            anchor = len(replaced)
        replaced = f"{replaced[:anchor].rstrip()}\n\n{block}\n\n{replaced[anchor:].lstrip()}"
    return _write_if_changed(path, replaced, dry_run=dry_run)


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
        heading = chapter.title
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
        heading = chapter.title
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


def sync_suggested_reading_paths(book_toc: Any, *, dry_run: bool) -> bool:
    path = MANUSCRIPT / "front_matter.md"
    text = path.read_text(encoding="utf-8")
    block = build_suggested_reading_paths(book_toc)
    if READING_PATHS_MARKER[0] in text and READING_PATHS_MARKER[1] in text:
        replaced, _changed = _replace_block(text, READING_PATHS_MARKER, block)
        return _write_if_changed(path, replaced, dry_run=dry_run)

    heading = "### Suggested reading paths {.unnumbered}"
    next_heading = "\n### Notation and conventions {.unnumbered}"
    heading_pos = text.find(heading)
    next_pos = text.find(next_heading, heading_pos)
    if heading_pos == -1 or next_pos == -1:
        raise ValueError("Could not find suggested reading paths section")
    body_start = heading_pos + len(heading)
    replaced = f"{text[:body_start].rstrip()}\n\n{block}\n\n{text[next_pos:].lstrip()}"
    return _write_if_changed(path, replaced, dry_run=dry_run)


def build_textbook_concept_map(book_toc: Any) -> str:
    """Return the generated front-matter concept map block."""
    summaries = {
        "unit_0": "feedback, emergence,<br/>active inference, systems",
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


def sync_textbook_concept_map(book_toc: Any, *, dry_run: bool) -> bool:
    path = MANUSCRIPT / "front_matter.md"
    text = path.read_text(encoding="utf-8")
    block = build_textbook_concept_map(book_toc)
    if CONCEPT_MAP_MARKER[0] in text and CONCEPT_MAP_MARKER[1] in text:
        replaced, _changed = _replace_block(text, CONCEPT_MAP_MARKER, block)
        return _write_if_changed(path, replaced, dry_run=dry_run)

    heading = "### Textbook Concept Map {.unnumbered}"
    next_heading = "\n### Accessing source materials {.unnumbered}"
    heading_pos = text.find(heading)
    next_pos = text.find(next_heading, heading_pos)
    if heading_pos == -1 or next_pos == -1:
        raise ValueError("Could not find textbook concept map section")
    body_start = heading_pos + len(heading)
    replaced = f"{text[:body_start].rstrip()}\n\n{block}\n\n{text[next_pos:].lstrip()}"
    return _write_if_changed(path, replaced, dry_run=dry_run)


def sync_preface_scope_table(book_toc: Any, *, dry_run: bool) -> bool:
    path = MANUSCRIPT / "preface.md"
    text = path.read_text(encoding="utf-8")
    block = build_preface_scope_table(book_toc)
    if PREFACE_SCOPE_MARKER[0] in text and PREFACE_SCOPE_MARKER[1] in text:
        replaced, _changed = _replace_block(text, PREFACE_SCOPE_MARKER, block)
        return _write_if_changed(path, replaced, dry_run=dry_run)

    heading = "## Scope and Organisation {.unnumbered}"
    next_divider = "\n---"
    heading_pos = text.find(heading)
    divider_pos = text.find(next_divider, heading_pos + len(heading))
    if heading_pos == -1 or divider_pos == -1:
        raise ValueError("Could not find preface scope section")
    replaced_section = (
        f"{heading}\n\n"
        "The textbook proceeds from atoms to ecosystems, following the standard introductory course arc.\n"
        "The table below is generated from `manuscript/config.yaml`; unit and chapter titles are\n"
        "semantic references resolved from the canonical manuscript labels.\n\n"
        f"{block}"
    )
    replaced = f"{text[:heading_pos].rstrip()}\n\n{replaced_section}{text[divider_pos:]}"
    return _write_if_changed(path, replaced, dry_run=dry_run)


def sync_front_matter_navigation(book_toc: Any, *, dry_run: bool) -> bool:
    path = MANUSCRIPT / "front_matter.md"
    text = path.read_text(encoding="utf-8")
    block = build_front_matter_navigation(book_toc)
    if NAV_MARKER[0] in text and NAV_MARKER[1] in text:
        replaced, _changed = _replace_block(text, NAV_MARKER, block)
        return _write_if_changed(path, replaced, dry_run=dry_run)

    heading = "### How to Navigate This Book {.unnumbered}"
    next_heading = "\n### Suggested reading paths {.unnumbered}"
    heading_pos = text.find(heading)
    next_pos = text.find(next_heading, heading_pos)
    if heading_pos == -1 or next_pos == -1:
        raise ValueError("Could not find front-matter navigation section")
    body_start = heading_pos + len(heading)
    replaced = f"{text[:body_start].rstrip()}\n\n{block}\n\n{text[next_pos:].lstrip()}"
    return _write_if_changed(path, replaced, dry_run=dry_run)


def sync_toc_titles(book_toc: Any, *, dry_run: bool) -> int:
    updates = 0
    for unit in book_toc.units:
        if unit.intro_path.exists() and sync_h1(unit.intro_path, unit.intro_title, dry_run=dry_run):
            updates += 1
        if unit.intro_path.exists() and sync_section_label(
            unit.intro_path, unit.section_label, dry_run=dry_run
        ):
            updates += 1
        for chapter in unit.chapters:
            if sync_h1(chapter.path, chapter.title, dry_run=dry_run):
                updates += 1
    for lab in book_toc.labs:
        if sync_h1(lab.path, lab.title, dry_run=dry_run):
            updates += 1
    for question in book_toc.questions:
        if sync_h1(question.path, question.title, dry_run=dry_run):
            updates += 1
    for reference in book_toc.references:
        if sync_h1(reference.path, reference.title, dry_run=dry_run):
            updates += 1
    return updates


def sync_heading_titles(book_toc: Any, *, dry_run: bool) -> int:
    """Normalize all ToC-visible Markdown headings."""
    updates = 0
    unnumbered_paths = {
        MANUSCRIPT / "front_matter.md",
        MANUSCRIPT / "preface.md",
        *(unit.intro_path for unit in book_toc.units),
        *(lab.path for lab in book_toc.labs),
        *(question.path for question in book_toc.questions),
        *(reference.path for reference in book_toc.references),
    }
    chapter_paths = {chapter.path for chapter in book_toc.chapters}
    for path in sorted(unnumbered_paths | chapter_paths):
        if path.exists() and normalize_headings(path, unnumbered=path in unnumbered_paths, dry_run=dry_run):
            updates += 1
    return updates


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true", help="Report changes without writing files")
    args = parser.parse_args(argv)

    curriculum = _load_biology_module("curriculum")
    chapter_meta = _load_biology_module("chapter_metadata")
    alignment_module = _load_biology_module("alignment")
    toc_module = _load_biology_module("toc")
    book_toc = toc_module.load_toc(PROJECT)
    records = tuple(curriculum.CURRICULUM)
    alignments = {record.chapter_id: record for record in alignment_module.ALIGNMENTS}
    report = SyncReport()

    for record in records:
        alignment = alignments[record.chapter_id]
        chapter = _chapter_path(record.chapter_id)
        lab = _lab_path(record.chapter_id)
        question = _question_path(record.chapter_id)
        for path in (chapter, lab, question):
            if not path.exists():
                raise FileNotFoundError(path)
        if sync_chapter(chapter, record, alignment, dry_run=args.dry_run):
            report.chapters_updated += 1
        if sync_lab(lab, record, alignment, dry_run=args.dry_run):
            report.labs_updated += 1
        if sync_question(question, record, alignment, dry_run=args.dry_run):
            report.questions_updated += 1

    appendix = MANUSCRIPT / "appendices" / "appendix_curriculum_map.md"
    if _write_if_changed(
        appendix,
        build_appendix(records, chapter_meta, alignments, book_toc),
        dry_run=args.dry_run,
    ):
        report.appendix_updated = True
    instructor_appendix = MANUSCRIPT / "appendices" / "appendix_instructor_orchestration.md"
    if _write_if_changed(
        instructor_appendix,
        build_instructor_appendix(records, chapter_meta, alignments, book_toc),
        dry_run=args.dry_run,
    ):
        report.instructor_appendix_updated = True
    report.titles_updated = sync_toc_titles(book_toc, dry_run=args.dry_run)
    report.heading_titles_updated = sync_heading_titles(book_toc, dry_run=args.dry_run)
    report.front_matter_updated = sync_front_matter_navigation(book_toc, dry_run=args.dry_run)
    if sync_suggested_reading_paths(book_toc, dry_run=args.dry_run):
        report.front_matter_updated = True
    if sync_textbook_concept_map(book_toc, dry_run=args.dry_run):
        report.front_matter_updated = True
    if sync_preface_scope_table(book_toc, dry_run=args.dry_run):
        report.front_matter_updated = True

    mode = "DRY RUN" if args.dry_run else "APPLIED"
    print(
        f"[{mode}] chapters_updated={report.chapters_updated} "
        f"labs_updated={report.labs_updated} "
        f"questions_updated={report.questions_updated} "
        f"appendix_updated={report.appendix_updated} "
        f"instructor_appendix_updated={report.instructor_appendix_updated} "
        f"titles_updated={report.titles_updated} "
        f"heading_titles_updated={report.heading_titles_updated} "
        f"front_matter_updated={report.front_matter_updated}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
