#!/usr/bin/env python3
"""Repair pedagogy shells on chapters created by the Phase 5 mega-chapter split.

Thin CLI for :mod:`biology.maintenance.chapter_shells`.
"""

from __future__ import annotations

import sys

from _bootstrap import ensure_project_paths

ensure_project_paths()

from biology.maintenance.chapter_shells import repair_split_chapters


def main(argv: list[str] | None = None) -> int:
    dry_run = "--dry-run" in (argv or sys.argv[1:])
    chapter_changes, lab_changes = repair_split_chapters(dry_run=dry_run)
    mode = "DRY RUN" if dry_run else "APPLIED"
    print(f"[{mode}] chapters={chapter_changes} labs={lab_changes}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
