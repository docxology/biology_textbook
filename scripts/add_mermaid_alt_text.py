#!/usr/bin/env python3
"""Normalize inline Mermaid alt text and captions.

The manuscript uses inline Mermaid fences for many explanatory diagrams. This
script is the maintenance point for their accessibility metadata:

* one ``<!-- alt: ... -->`` comment immediately after each Mermaid fence;
* one italic caption immediately after the alt comment;
* no generic filler phrases or duplicate alt comments.

Run without flags to rewrite manuscript files in place. Run with ``--check`` to
fail if any Mermaid block would be changed.
"""

from __future__ import annotations

import argparse

from _bootstrap import PROJECT, ensure_project_paths

ensure_project_paths(include_scripts=True)

from biology.maintenance.text_normalize import (  # noqa: E402
    FileResult,
    _alt_from_caption,
    _metadata_is_weak,
    normalize_all,
    normalize_text,
)

MANUSCRIPT = PROJECT / "manuscript"

__all__ = [
    "FileResult",
    "_alt_from_caption",
    "_metadata_is_weak",
    "normalize_text",
    "normalize_all",
]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check",
        action="store_true",
        help="report files that would change and return a non-zero status",
    )
    args = parser.parse_args()

    results = normalize_all(manuscript=MANUSCRIPT, write=not args.check)
    changed = [result for result in results if result.changed]
    block_count = sum(result.blocks for result in results)

    if changed:
        verb = "would update" if args.check else "updated"
        for result in changed:
            rel = result.path.relative_to(MANUSCRIPT)
            print(f"{verb}: {rel} ({result.blocks} Mermaid block(s))")
    print(f"Checked {block_count} inline Mermaid block(s) across {len(results)} manuscript file(s).")

    if args.check and changed:
        print("Mermaid alt/caption metadata is not normalized; run this script without --check.")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
