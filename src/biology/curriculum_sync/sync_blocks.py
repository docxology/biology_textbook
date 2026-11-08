"""Curriculum sync engine."""

from __future__ import annotations

import re
from pathlib import Path
from typing import Any

from biology.crossref.helpers import section_reference
from biology.crossref.source import iter_headings, markdown_text, visible_text
from biology.curriculum_sync.paths import MANUSCRIPT
from textbook_io import write_text_atomic

CHAPTER_MARKER = ("<!-- curriculum-scaffold-start -->", "<!-- curriculum-scaffold-end -->")
NAV_MARKER = ("<!-- toc-navigation-start -->", "<!-- toc-navigation-end -->")
READING_PATHS_MARKER = ("<!-- suggested-reading-paths-start -->", "<!-- suggested-reading-paths-end -->")
CONCEPT_MAP_MARKER = ("<!-- textbook-concept-map-start -->", "<!-- textbook-concept-map-end -->")
PREFACE_SCOPE_MARKER = ("<!-- preface-scope-start -->", "<!-- preface-scope-end -->")

HEADING_ATTR_RE = re.compile(r"^(?P<title>.*?)(?:(?:\s+|^)\{(?P<attrs>[^}]*)\})\s*$")
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
    heading = next((item for item in iter_headings(path.read_text(encoding="utf-8")) if item.level == 1), None)
    return heading.title if heading is not None else path.stem.replace("_", " ").title()

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
        raise ValueError("Section headings require an authored descriptive title.")
    return _format_heading(clean, attrs, identifier)

def _replace_first_h1(text: str, title: str) -> tuple[str, bool]:
    heading = next((item for item in iter_headings(text) if item.level == 1), None)
    if heading is not None:
        _toc_safe_heading_title(heading.visible_title)
        current_title, attrs, identifier = _split_heading_parts(_toc_safe_heading_title(heading.title))
        if current_title == title:
            return text, False
        replacement = f"{heading.indent}# {_format_heading(title, attrs, identifier)}"
        updated = text[:heading.start] + replacement + text[heading.end:]
        return updated, updated != text
    return f"# {title}\n\n{text}", True

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
    """Identify the real H1; preserve fenced/comment examples of legacy labels."""
    heading = next((item for item in iter_headings(text) if item.level == 1), None)
    if heading is None:
        return text, False
    _toc_safe_heading_title(heading.visible_title)
    clean, attrs, _existing = _split_heading_parts(_toc_safe_heading_title(heading.title))
    if unnumbered:
        attrs.add(NONNUMBERED_ATTR)
    replacement = f"{heading.indent}# {_format_heading(clean, attrs, label)}"
    updated = text[:heading.start] + replacement + text[heading.end:]
    lines = updated.splitlines(keepends=True)
    visibility = visible_text(updated)
    kept: list[str] = []
    position = 0
    for line in lines:
        visible = visibility[position:position + len(line)]
        position += len(line)
        standalone = None if visible.startswith(("    ", "\t")) else STANDALONE_SEC_LABEL_RE.fullmatch(visible.strip())
        if standalone is None or standalone.group(1) != label:
            kept.append(line)
    result = "".join(kept)
    return result, result != text


def sync_section_label(path: Path, label: str, *, dry_run: bool, unnumbered: bool = True) -> bool:
    """Ensure unnumbered ``sec:`` labels live on the H1 Pandoc identifier."""
    text = path.read_text(encoding="utf-8")
    updated, changed = attach_section_identifier(text, label, unnumbered=unnumbered)
    if not changed:
        return False
    return _write_if_changed(path, updated, dry_run=dry_run)

def _normalize_heading_text(
    original: str, *, unnumbered: bool, chapter_title: str | None = None,
) -> str:
    """Normalize real headings while preserving literal examples and comments."""
    text = original
    alt_view = markdown_text(text, keep_comments=("SOLUTION", "alt"))
    for match in reversed(list(ALT_COMMENT_THEMATIC_BREAK_RE.finditer(alt_view))):
        gap = match.start() + match.group(0).rfind("\n---")
        text = text[:gap] + "\n" + text[gap:]
    for heading in reversed(list(iter_headings(text))):
        _toc_safe_heading_title(heading.visible_title, chapter_title=chapter_title)
        safe_title = _toc_safe_heading_title(heading.title, chapter_title=chapter_title)
        clean_title, attrs, identifier = _split_heading_parts(safe_title)
        if unnumbered:
            attrs.add(NONNUMBERED_ATTR)
        replacement = f"{heading.indent}{'#' * heading.level} {_format_heading(clean_title, attrs, identifier)}"
        text = text[:heading.start] + replacement + text[heading.end:]
    return text


def normalize_headings(
    path: Path,
    *,
    unnumbered: bool,
    dry_run: bool,
    chapter_title: str | None = None,
) -> bool:
    """Normalize Markdown headings so LaTeX numbering and ToC titles stay clean."""
    original = path.read_text(encoding="utf-8")
    try:
        normalized = _normalize_heading_text(original, unnumbered=unnumbered, chapter_title=chapter_title)
    except ValueError as exc:
        raise ValueError(f"{path}: {exc}") from exc
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



