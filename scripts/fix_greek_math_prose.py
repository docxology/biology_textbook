#!/usr/bin/env python3
"""Replace ``$\\greek$`` in prose with the Unicode codepoint."""

from __future__ import annotations

import sys

from _bootstrap import PROJECT, ensure_project_paths

ensure_project_paths()

from biology.maintenance.typography import replace_greek_math_in_file

MANUSCRIPT = PROJECT / "manuscript"
SKIP_NAMES = frozenset({"README.md", "AGENTS.md", "preamble.md"})


def main(argv: list[str] | None = None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    dry_run = "--dry-run" in argv
    total = 0
    files = 0
    for md in MANUSCRIPT.rglob("*.md"):
        if md.name in SKIP_NAMES:
            continue
        count = replace_greek_math_in_file(md, write=not dry_run)
        if count:
            files += 1
            total += count
    mode = "DRY RUN" if dry_run else "APPLIED"
    print(f"[{mode}] greek_replaced={total} files_touched={files}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
