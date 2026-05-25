#!/usr/bin/env python3
"""Normalize glossary anchors and rebuild the appendix term index."""

from __future__ import annotations

import argparse
import sys

from _bootstrap import ensure_project_paths

ensure_project_paths(include_scripts=True)

from biology.maintenance.glossary_links import run_glossary_sync  # noqa: E402


def run(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args(argv)

    exit_code, stats = run_glossary_sync(dry_run=args.dry_run, check=args.check)
    if args.check:
        mode = "CHECK"
    elif args.dry_run:
        mode = "DRY RUN"
    else:
        mode = "APPLIED"
    print(
        f"[{mode}] anchors_updated={stats['anchors_updated']} "
        f"glossary_refs_rewritten={stats['glossary_refs_rewritten']} "
        f"index_terms={stats['index_terms']} "
        f"pending_changes={int(stats['pending_changes'])}"
    )
    if args.check and stats["pending_changes"]:
        print("  pending glossary/index normalization changes", file=sys.stderr)
    return exit_code


if __name__ == "__main__":
    raise SystemExit(run())
