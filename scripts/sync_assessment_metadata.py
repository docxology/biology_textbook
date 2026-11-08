#!/usr/bin/env python3
"""Synchronize question-bank and lab assessment metadata from the canonical TOC."""

from __future__ import annotations

import argparse
import sys

from _bootstrap import PROJECT, ensure_project_paths

ensure_project_paths()

from biology.assessment_sync import sync_all_assessment_metadata


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--check", action="store_true", help="Exit non-zero if files are not synchronized")
    mode.add_argument("--dry-run", action="store_true", help="Preview synchronized files without writing changes")
    args = parser.parse_args()

    changed, check_exit = sync_all_assessment_metadata(
        PROJECT,
        check=args.check,
        dry_run=args.dry_run,
    )

    if changed:
        action = "out of sync" if args.check else "would update" if args.dry_run else "updated"
        for path in changed:
            print(f"assessment metadata {action}: {path.relative_to(PROJECT)}", file=sys.stderr)
        return check_exit
    print("assessment metadata synchronized")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
