#!/usr/bin/env python3
"""Insert references to orphan figure generators into their natural chapters.

Thin CLI for :mod:`biology.pipeline.orphan_figures`. The catalog of insertions
lives in ``src/biology/pipeline/orphan_figures.yaml``. Idempotent: chapters that
already reference the figure PNG are skipped.
"""

from __future__ import annotations

import sys

from _bootstrap import ensure_project_paths

ensure_project_paths(include_scripts=True)

from biology.pipeline.orphan_figures import apply_orphan_figures


def main(argv: list[str] | None = None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    dry_run = "--dry-run" in argv
    result = apply_orphan_figures(dry_run=dry_run)
    mode = "DRY RUN" if dry_run else "APPLIED"
    print(f"[{mode}] figures_inserted={result.inserted}/{result.total}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
