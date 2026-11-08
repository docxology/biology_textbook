#!/usr/bin/env python3
"""Insert ``\\label{sec:...}`` after every chapter H1 and rewrite prose cross-refs.

Thin CLI for :mod:`biology.crossref.label_insertion`. The script is idempotent:
running it twice leaves the manuscript unchanged.
"""

from __future__ import annotations

import sys

from _bootstrap import ensure_project_paths

ensure_project_paths(include_scripts=True)

from biology.crossref.label_insertion import apply_crossref_labels


def main(argv: list[str] | None = None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    dry_run = "--dry-run" in argv
    report = apply_crossref_labels(dry_run=dry_run)
    mode = "DRY RUN" if dry_run else "APPLIED"
    print(f"[{mode}] {report.summary()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
