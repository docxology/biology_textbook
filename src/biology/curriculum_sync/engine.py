"""Curriculum sync engine — orchestration and front-matter sync."""

from __future__ import annotations

import importlib
import importlib.util
import sys
from dataclasses import dataclass
from pathlib import Path
from types import ModuleType
from typing import Any

from biology.curriculum_sync.appendices import (
    build_appendix,
    build_front_matter_navigation,
    build_instructor_appendix,
    build_preface_scope_table,
    build_suggested_reading_paths,
    build_textbook_concept_map,
)
from biology.curriculum_sync.paths import MANUSCRIPT, SRC, TEMPLATE_ROOT
from biology.curriculum_sync.sync_blocks import (
    CHAPTER_MARKER,
    CONCEPT_MAP_MARKER,
    LAB_MARKER,
    NAV_MARKER,
    PREFACE_SCOPE_MARKER,
    QUESTION_MARKER,
    READING_PATHS_MARKER,
    _chapter_path,
    _lab_path,
    _question_path,
    _replace_block,
    _write_if_changed,
    normalize_headings,
    sync_chapter,
    sync_h1,
    sync_lab,
    sync_question,
    sync_section_label,
)

__all__ = [
    "CHAPTER_MARKER",
    "CONCEPT_MAP_MARKER",
    "LAB_MARKER",
    "NAV_MARKER",
    "PREFACE_SCOPE_MARKER",
    "QUESTION_MARKER",
    "READING_PATHS_MARKER",
    "SyncReport",
    "_chapter_path",
    "_lab_path",
    "_load_biology_module",
    "_question_path",
    "_write_if_changed",
    "build_appendix",
    "build_instructor_appendix",
    "sync_chapter",
    "sync_front_matter_navigation",
    "sync_heading_titles",
    "sync_lab",
    "sync_preface_scope_table",
    "sync_question",
    "sync_suggested_reading_paths",
    "sync_textbook_concept_map",
    "sync_toc_titles",
]


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


def sync_suggested_reading_paths(book_toc: Any, *, dry_run: bool) -> bool:
    path = MANUSCRIPT / "front_matter.md"
    text = path.read_text(encoding="utf-8")
    block = build_suggested_reading_paths(book_toc)
    if READING_PATHS_MARKER[0] in text and READING_PATHS_MARKER[1] in text:
        replaced, _changed = _replace_block(text, READING_PATHS_MARKER, block)
        return _write_if_changed(path, replaced, dry_run=dry_run)

    heading = "### Suggested reading paths {.unnumbered}"
    next_heading = "\n### Textbook concept map {.unnumbered}"
    heading_pos = text.find(heading)
    next_pos = text.find(next_heading, heading_pos)
    if heading_pos == -1 or next_pos == -1:
        raise ValueError("Could not find suggested reading paths section")
    body_start = heading_pos + len(heading)
    replaced = f"{text[:body_start].rstrip()}\n\n{block}\n\n{text[next_pos:].lstrip()}"
    return _write_if_changed(path, replaced, dry_run=dry_run)


def sync_textbook_concept_map(book_toc: Any, *, dry_run: bool) -> bool:
    path = MANUSCRIPT / "front_matter.md"
    text = path.read_text(encoding="utf-8")
    block = build_textbook_concept_map(book_toc)
    if CONCEPT_MAP_MARKER[0] in text and CONCEPT_MAP_MARKER[1] in text:
        replaced, _changed = _replace_block(text, CONCEPT_MAP_MARKER, block)
        return _write_if_changed(path, replaced, dry_run=dry_run)

    heading = "### Textbook concept map {.unnumbered}"
    next_heading = "\n---"
    heading_pos = text.find(heading)
    next_pos = text.find(next_heading, heading_pos + len(heading))
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
    chapter_titles = {chapter.path: chapter.title for chapter in book_toc.chapters}
    for path in sorted(unnumbered_paths | chapter_paths):
        if path.exists() and normalize_headings(
            path,
            unnumbered=path in unnumbered_paths,
            dry_run=dry_run,
            chapter_title=chapter_titles.get(path),
        ):
            updates += 1
    return updates
