"""CLI for embedded enrichment."""

from __future__ import annotations

import argparse

from biology.enrichment.engine import (
    enrich_chapters,
    enrich_labs,
    enrich_unit_intros,
    normalize_companion_source_modules,
    refresh_chapter_scholarship_bullets,
    refine_question_banks,
    write_audit_matrix,
)
from biology.enrichment.records import chapter_records


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Embedded enrichment pass for the biology textbook.")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args(argv)

    records = chapter_records()
    matrix = write_audit_matrix(records, args.dry_run)
    unit_intros = enrich_unit_intros(args.dry_run)
    chapters = enrich_chapters(records, args.dry_run)
    scholarship_bullets = refresh_chapter_scholarship_bullets(records, args.dry_run)
    companion_modules = normalize_companion_source_modules(records, args.dry_run)
    labs = enrich_labs(records, args.dry_run)
    question_files, question_blocks = refine_question_banks(records, args.dry_run)
    mode = "DRY RUN" if args.dry_run else "APPLIED"
    print(
        f"[{mode}] matrix={matrix} unit_intros={unit_intros} chapters={chapters} "
        f"scholarship_bullets={scholarship_bullets} companion_modules={companion_modules} labs={labs} "
        f"question_files={question_files} question_blocks={question_blocks}"
    )
    return 0


__all__ = ["main"]
