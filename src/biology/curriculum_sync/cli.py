"""CLI for curriculum synchronization."""

from __future__ import annotations

import argparse

from biology.curriculum_sync.engine import (
    SyncReport,
    _chapter_path,
    _lab_path,
    _load_biology_module,
    _question_path,
    _write_if_changed,
    build_appendix,
    build_instructor_appendix,
    sync_chapter,
    sync_front_matter_navigation,
    sync_heading_titles,
    sync_lab,
    sync_preface_scope_table,
    sync_question,
    sync_section_reference_commands,
    sync_suggested_reading_paths,
    sync_textbook_concept_map,
    sync_toc_titles,
)
from biology.curriculum_sync.paths import MANUSCRIPT, PROJECT


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Synchronize curriculum scaffolds across manuscript surfaces.")
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
    report.section_refs_updated = sync_section_reference_commands(dry_run=args.dry_run)

    mode = "DRY RUN" if args.dry_run else "APPLIED"
    print(
        f"[{mode}] chapters_updated={report.chapters_updated} "
        f"labs_updated={report.labs_updated} "
        f"questions_updated={report.questions_updated} "
        f"appendix_updated={report.appendix_updated} "
        f"instructor_appendix_updated={report.instructor_appendix_updated} "
        f"titles_updated={report.titles_updated} "
        f"heading_titles_updated={report.heading_titles_updated} "
        f"front_matter_updated={report.front_matter_updated} "
        f"section_refs_updated={report.section_refs_updated}"
    )
    return 0


__all__ = ["main"]
