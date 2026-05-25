#!/usr/bin/env python3
"""Replace stale notebook-based lab sections with tested, self-contained snippets.

The textbook labs are paper-first activities. Optional computation should run
against this project's ``src/biology`` modules without requiring hidden
notebooks, CSV files, or dependencies outside ``pyproject.toml``.
"""

from __future__ import annotations

import sys

from _bootstrap import ensure_project_paths

ensure_project_paths(include_scripts=True)

from biology.maintenance.lab_workflows import WORKFLOWS, normalise_lab


def main(argv: list[str] | None = None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    dry_run = "--dry-run" in argv
    changed = 0
    for workflow in WORKFLOWS:
        if normalise_lab(workflow, dry_run=dry_run):
            changed += 1
            marker = "D" if dry_run else "+"
            print(f"  [{marker}] {workflow.relative_path} -> {workflow.source_module}")
    mode = "DRY RUN" if dry_run else "APPLIED"
    print(f"\n[{mode}] labs_normalised={changed}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
