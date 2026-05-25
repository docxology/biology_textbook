#!/usr/bin/env python3
"""Insert chapter-specific source-note sections into configured chapters.

Thin CLI for :mod:`biology.maintenance.further_reading`. Idempotent: chapters
that already carry a Further Reading or Source Notes heading are skipped.
"""

from __future__ import annotations

import sys

from _bootstrap import ensure_project_paths

ensure_project_paths(include_scripts=True)

from biology.maintenance.further_reading import (
    MANUSCRIPT,
    BibEntry,
    apply_further_reading,
    render_section,
)

__all__ = ["BibEntry", "MANUSCRIPT", "apply_further_reading", "main", "render_section"]


def main(argv: list[str] | None = None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    dry_run = "--dry-run" in argv
    result = apply_further_reading(dry_run=dry_run)
    mode = "DRY RUN" if dry_run else "APPLIED"
    marker = "D" if dry_run else "+"
    for path in result.touched:
        print(f"  [{marker}] {path.relative_to(MANUSCRIPT)}")
    print(f"\n[{mode}] further_reading_inserted={result.inserted} skipped={result.skipped}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
