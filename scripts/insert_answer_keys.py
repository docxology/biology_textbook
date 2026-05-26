#!/usr/bin/env python3
"""Insert instructor-edition answer keys into every question bank."""

from __future__ import annotations

import argparse
import sys

from _bootstrap import ensure_project_paths

ensure_project_paths(include_scripts=True)

from biology.answer_refinement.paths import QUESTIONS
from biology.answer_refinement.solution_scaffolds import insert_solution_scaffolds


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true", help="Preview scaffold insertions without writing")
    args = parser.parse_args(argv)

    report = insert_solution_scaffolds(QUESTIONS, dry_run=args.dry_run, write=not args.dry_run)
    mode = "DRY RUN" if args.dry_run else "APPLIED"
    print(f"\n[{mode}] scaffolds_inserted={report.scaffolds_inserted} files_touched={report.files_touched}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
