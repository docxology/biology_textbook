"""Validate reviewed source-owned assessment mappings without inventing pedagogy."""

from __future__ import annotations

from pathlib import Path

from biology.assessment import (
    chapter_learning_objectives,
    parse_lab_alignment,
    parse_question_bank,
)
from biology.toc import load_toc


def sync_all_assessment_metadata(
    project_root: Path, *, check: bool = False, dry_run: bool = False,
) -> tuple[list[Path], int]:
    """Validate the entire source set before returning; never manufacture mappings.

    ``check`` and ``dry_run`` obey the same non-writing validation contract as
    apply. Missing metadata requires an author to review the actual question or
    lab task, not a positional assignment by this tool.
    """
    toc = load_toc(project_root)
    if (
        not toc.chapters
        or {item.chapter.chapter_id for item in toc.questions} != {item.chapter_id for item in toc.chapters}
        or {item.chapter.chapter_id for item in toc.labs} != {item.chapter_id for item in toc.chapters}
        or len(toc.questions) != len(toc.chapters)
        or len(toc.labs) != len(toc.chapters)
    ):
        raise ValueError("Author a complete canonical config with one question bank and lab per chapter")
    for question in toc.questions:
        sync_question_bank(question.path, chapter_learning_objectives(question.chapter.path))
    for lab in toc.labs:
        sync_lab_alignment(lab.path, lab.chapter.title, chapter_learning_objectives(lab.chapter.path))
    return [], 0


def sync_question_bank(path: Path, lo_ids: tuple[str, ...]) -> str:
    """Preserve valid per-item comments byte-for-byte; reject authoring gaps."""
    bank = parse_question_bank(path)
    if [item.number for item in bank.items] != list(range(1, 31)):
        raise ValueError(f"{path}: author reviewed metadata for exactly questions 1–30")
    known = set(lo_ids)
    invalid = bank.assessed_los - known
    missing = known - bank.assessed_los
    if not known or invalid or missing:
        raise ValueError(f"{path}: author semantic LO mappings; invalid={sorted(invalid)}, unassessed={sorted(missing)}")
    if not {"Recall", "Application", "Synthesis"} <= set(bank.difficulty_mix):
        raise ValueError(f"{path}: author a reviewed Recall/Application/Synthesis assessment mix")
    if not {"Analyze", "Evaluate", "Create"} & set(bank.bloom_mix):
        raise ValueError(f"{path}: author higher-order Bloom assessment items")
    return path.read_text(encoding="utf-8")


def sync_lab_alignment(path: Path, chapter_title: str, lo_ids: tuple[str, ...]) -> str:
    """Preserve genuine author-owned outcomes/rubrics and reject unknown LOs."""
    alignment = parse_lab_alignment(path)
    invalid = set(alignment.lo_ids) - set(lo_ids)
    if invalid:
        raise ValueError(f"{path}: author valid {chapter_title} outcome mappings; unknown LOs={sorted(invalid)}")
    return path.read_text(encoding="utf-8")


def write_or_record(path: Path, updated: str, *, write: bool) -> list[Path]:
    """Record a real text change, optionally publishing it atomically."""
    current = path.read_text(encoding="utf-8")
    if current == updated:
        return []
    if write:
        from textbook_io import write_text_atomic

        write_text_atomic(path, updated)
    return [path]


__all__ = ["sync_all_assessment_metadata", "sync_lab_alignment", "sync_question_bank", "write_or_record"]
