#!/usr/bin/env python3
"""Weave orphan BibTeX entries into the manuscript narrative."""

from __future__ import annotations

import sys

from _bootstrap import PROJECT, ensure_project_paths

ensure_project_paths()

from biology.citations import inject_orphan_citations


def run(argv: list[str] | None = None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    dry_run = "--dry-run" in argv
    report = inject_orphan_citations(PROJECT, dry_run=dry_run, write=not dry_run)
    mode = "DRY RUN" if dry_run else "APPLIED"
    print(
        f"\n[{mode}] inserted={report.inserted} already_cited={report.skipped_already_cited} "
        f"no_anchor={report.skipped_no_anchor} total={report.total}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
