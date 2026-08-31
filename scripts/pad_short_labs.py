#!/usr/bin/env python3
"""Append a Debrief block to every lab under 100 lines."""

from __future__ import annotations

import sys

from _bootstrap import PROJECT, ensure_project_paths

ensure_project_paths()

from biology.maintenance.lab_padding import apply_lab_debrief

LABS = PROJECT / "docs" / "manuscript" / "labs"


def main(argv: list[str] | None = None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    dry_run = "--dry-run" in argv
    touched = 0
    for lab in sorted(LABS.rglob("lab_*.md")):
        if apply_lab_debrief(lab, write=not dry_run):
            touched += 1
            print(f"  [{'D' if dry_run else '+'}] {lab.relative_to(PROJECT / 'manuscript')}: +Debrief block")
    mode = "DRY RUN" if dry_run else "APPLIED"
    print(f"\n[{mode}] labs_padded={touched}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
