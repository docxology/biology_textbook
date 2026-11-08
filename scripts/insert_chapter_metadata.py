#!/usr/bin/env python3
r"""Insert pedagogical metadata badges and populate the course planning grid."""

from __future__ import annotations

import argparse
import sys

from _bootstrap import PROJECT, ensure_project_paths

ensure_project_paths()

from biology.maintenance.chapter_badges import apply_chapter_metadata


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true", help="Preview changes without writing files")
    args = parser.parse_args(argv)

    report = apply_chapter_metadata(PROJECT, dry_run=args.dry_run)
    mode = "DRY RUN" if args.dry_run else "APPLIED"
    print(
        f"[{mode}] badges_inserted={report.badges_inserted} "
        f"badges_updated={report.badges_updated} "
        f"badges_already_present={report.badges_already_present} "
        f"grid_updated={report.grid_updated}",
        file=sys.stderr,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
