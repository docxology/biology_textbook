"""Curriculum sync engine."""

from __future__ import annotations

import re
from pathlib import Path
from typing import Any

from biology.crossref.helpers import section_reference
from biology.curriculum_sync.paths import MANUSCRIPT
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
STANDALONE_SEC_LABEL_RE = re.compile(r"^\\label\{(sec:[A-Za-z0-9_\-]+)\}\s*$")
SOURCE_SECTION_TITLES = {
    "Current Evidence and Frontier Biology",
    "Further Reading and Source Notes",
    "Companion Source Module",
}



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

def _split_heading_parts(title: str) -> tuple[str, set[str], str | None]:
    """Return heading title, class attrs, and optional Pandoc identifier (without ``#``)."""
    match = HEADING_ATTR_RE.match(title.strip())
    if match is None:
        return title.strip(), set(), None
    identifier: str | None = None
    attrs: set[str] = set()
    for part in (match.group("attrs") or "").split():
        if part.startswith("#"):
            identifier = part.lstrip("#")
        elif part:
            attrs.add(part)
    return match.group("title").strip(), attrs, identifier


def _split_heading_attrs(title: str) -> tuple[str, set[str]]:
    clean, attrs, _identifier = _split_heading_parts(title)
    return clean, attrs


def _format_heading(title: str, attrs: set[str], identifier: str | None = None) -> str:
    clean_title = title.strip()
    suffix_parts: list[str] = []
    if identifier:
        suffix_parts.append(f"#{identifier}")
    ordered = sorted(attrs, key=lambda attr: (attr != NONNUMBERED_ATTR, attr))
    suffix_parts.extend(ordered)
    if not suffix_parts:
        return clean_title
    return f"{clean_title} {{{' '.join(suffix_parts)}}}"

def _toc_safe_heading_title(title: str, chapter_title: str | None = None) -> str:
    clean, attrs, identifier = _split_heading_parts(title)
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
    if chapter_title is not None and clean in SOURCE_SECTION_TITLES:
        clean = f"{clean}: {chapter_title}"
    if not clean:
        clean = "Additional Island Biogeography Evidence"
    return _format_heading(clean, attrs, identifier)

def _replace_first_h1(text: str, title: str) -> tuple[str, bool]:
    pattern = re.compile(r"^#\s+(.+)$", flags=re.MULTILINE)
    match = pattern.search(text)
    if match is not None:
        current_title, attrs, identifier = _split_heading_parts(match.group(1))
        if current_title == title:
            return text, False
        replacement = f"# {_format_heading(title, attrs, identifier)}"
        new_text = pattern.sub(replacement, text, count=1)
        return new_text, new_text != text
    replacement = f"# {title}"
    return f"{replacement}\n\n{text}", True

def sync_h1(path: Path, title: str, *, dry_run: bool) -> bool:
    text = path.read_text(encoding="utf-8")
    replaced, changed = _replace_first_h1(text, title)
    return changed and _write_if_changed(path, replaced, dry_run=dry_run)

def attach_section_identifier(
    text: str,
    label: str,
    *,
    unnumbered: bool = True,
) -> tuple[str, bool]:
    """Embed ``{#label}`` on the first H1 and remove standalone ``\\label{label}`` lines."""
    lines = text.splitlines()
    new_lines: list[str] = []
    h1_done = False

    for line in lines:
        standalone = STANDALONE_SEC_LABEL_RE.match(line.strip())
        if standalone is not None and standalone.group(1) == label:
            continue
        if not h1_done and line.startswith("# "):
            h1_done = True
            clean, attrs, _existing = _split_heading_parts(line[2:].strip())
            if unnumbered:
                attrs.add(NONNUMBERED_ATTR)
            new_lines.append(f"# {_format_heading(clean, attrs, label)}")
            continue
        new_lines.append(line)

    result = "\n".join(new_lines)
    if text.endswith("\n"):
        result += "\n"
    return result, result != text


def sync_section_label(path: Path, label: str, *, dry_run: bool, unnumbered: bool = True) -> bool:
    """Ensure unnumbered ``sec:`` labels live on the H1 Pandoc identifier."""
    text = path.read_text(encoding="utf-8")
    updated, changed = attach_section_identifier(text, label, unnumbered=unnumbered)
    if not changed:
        return False
    return _write_if_changed(path, updated, dry_run=dry_run)

def normalize_headings(
    path: Path,
    *,
    unnumbered: bool,
    dry_run: bool,
    chapter_title: str | None = None,
) -> bool:
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
        safe_title = _toc_safe_heading_title(raw_title, chapter_title=chapter_title)
        clean_title, attrs, identifier = _split_heading_parts(safe_title)
        if unnumbered:
            attrs.add(NONNUMBERED_ATTR)
        lines.append(f"{hashes} {_format_heading(clean_title, attrs, identifier)}")
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
            f"- **Primary lab:** {section_reference(record.lab_label)}.",
            f"- **Question bank:** {section_reference(record.question_label)}.",
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

