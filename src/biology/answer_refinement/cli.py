"""CLI for answer refinement."""

from __future__ import annotations

import sys

from biology.answer_refinement.engine import process_bank
from biology.answer_refinement.paths import MANUSCRIPT, QUESTIONS


def main(argv: list[str] | None = None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    dry_run = "--dry-run" in argv
    total_refined = 0
    total_skipped = 0
    files = 0
    for bank in sorted(QUESTIONS.rglob("questions_*.md")):
        refined, skipped = process_bank(bank, dry_run=dry_run)
        if refined or skipped:
            files += 1
        if refined:
            total_refined += refined
            print(
                f"  [{'D' if dry_run else '+'}] {bank.relative_to(MANUSCRIPT)}: "
                f"refined {refined}, preserved {skipped} hand-written"
            )
        total_skipped += skipped
    mode = "DRY RUN" if dry_run else "APPLIED"
    print(f"\n[{mode}] refined={total_refined}  hand_written_preserved={total_skipped}  files_touched={files}")
    return 0


__all__ = ["main"]
