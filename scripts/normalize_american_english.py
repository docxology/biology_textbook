#!/usr/bin/env python3
"""Rewrite British spellings to American English in manuscript and docs."""

from __future__ import annotations

import sys

from _bootstrap import ensure_project_paths

ensure_project_paths(include_scripts=True)

from biology.maintenance.american_english import (  # noqa: E402
    MANUSCRIPT,
    iter_target_files,
    normalize_file,
)
from biology.maintenance.models import PROJECT  # noqa: E402


def main(argv: list[str] | None = None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    dry_run = "--dry-run" in argv
    total = 0
    files = 0
    for path in iter_target_files(PROJECT):
        result = normalize_file(path, write=not dry_run)
        if result.replacements:
            files += 1
            total += result.replacements
            print(f"{result.replacements:4d}  {path.relative_to(PROJECT)}")
    mode = "DRY RUN" if dry_run else "APPLIED"
    print(f"[{mode}] replacements={total} files_touched={files}")
    if not dry_run:
        print(f"Manuscript root: {MANUSCRIPT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
