#!/usr/bin/env python3
"""Polish existing pandoc table captions across the biology textbook manuscript."""

from __future__ import annotations

import argparse
from pathlib import Path

from _bootstrap import ensure_project_paths

ensure_project_paths()

from biology.crossref.table_captions import polish_manuscript_captions


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--manuscript",
        type=Path,
        default=Path(__file__).resolve().parents[1] / "docs" / "manuscript",
        help="Manuscript root (default: projects/biology_textbook/manuscript)",
    )
    parser.add_argument(
        "--write",
        action="store_true",
        help="Apply caption polish to manuscript files (default: dry run)",
    )
    args = parser.parse_args()
    changed, examined = polish_manuscript_captions(args.manuscript, write=args.write)
    mode = "updated" if args.write else "would update"
    print(f"{mode} {changed} file(s); examined {examined} caption(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
