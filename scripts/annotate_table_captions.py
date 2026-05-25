#!/usr/bin/env python3
"""Insert ``Table: … {#tbl:…}`` captions before chapter and lab pipe tables."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from _bootstrap import ensure_project_paths

ensure_project_paths()

from biology.crossref.table_captions import annotate_manuscript


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--manuscript",
        type=Path,
        default=Path(__file__).resolve().parent.parent / "manuscript",
        help="Manuscript root (default: projects/biology_textbook/manuscript)",
    )
    parser.add_argument(
        "--write",
        action="store_true",
        help="Write caption lines into manuscript files (default: dry-run report)",
    )
    args = parser.parse_args(argv)
    manuscript_root = args.manuscript.resolve()
    if not manuscript_root.is_dir():
        print(f"annotate_table_captions: missing manuscript directory: {manuscript_root}", file=sys.stderr)
        return 1

    results, changed = annotate_manuscript(manuscript_root, write=args.write)
    total_tables = sum(len(result.annotations) for result in results)
    low_confidence = sum(len(result.low_confidence) for result in results)
    mode = "write" if args.write else "dry-run"
    print(
        f"annotate_table_captions ({mode}): "
        f"{total_tables} tables in {len(results)} files"
        + (f"; {changed} files updated" if args.write else "")
        + (f"; {low_confidence} low-confidence captions" if low_confidence else "")
    )
    for result in results[:20]:
        rel = result.path.relative_to(manuscript_root)
        print(f"  {rel}: {len(result.annotations)} tables")
    if len(results) > 20:
        print(f"  … and {len(results) - 20} more files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
