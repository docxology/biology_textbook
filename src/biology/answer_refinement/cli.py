"""CLI for non-writing answer validation and unsupported-repair diagnostics."""

from __future__ import annotations

import sys

from biology.answer_refinement.engine import process_bank
from biology.answer_refinement.paths import QUESTIONS


def main(argv: list[str] | None = None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    banks = sorted(QUESTIONS.rglob("questions_*.md"))
    if not banks:
        print(f"ERROR: no question banks found in {QUESTIONS}", file=sys.stderr)
        return 1
    preserved = 0
    errors = 0
    for bank in banks:
        try:
            _, count = process_bank(bank, dry_run="--dry-run" in argv)
            preserved += count
        except ValueError as exc:
            errors += 1
            print(f"ERROR: {exc}", file=sys.stderr)
    print(f"Validated {len(banks)} banks; preserved {preserved} authored answers; {errors} author actions; no files written.")
    return 1 if errors else 0


def fill_main(argv: list[str] | None = None) -> int:
    """Use the same fail-closed contract for the legacy scaffold CLI."""
    return main(argv)


__all__ = ["fill_main", "main"]
