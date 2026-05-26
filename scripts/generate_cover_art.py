#!/usr/bin/env python3
"""Generate the biology textbook cover montage asset."""

from __future__ import annotations

import argparse
from pathlib import Path

from _bootstrap import PROJECT, ensure_project_paths

ensure_project_paths()

from biology.assets.cover_art import DEFAULT_HEIGHT, DEFAULT_WIDTH, generate_cover

DEFAULT_OUTPUT = PROJECT / "manuscript" / "assets" / "cover" / "biology_textbook_cover.png"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args(argv)
    output = generate_cover(args.output, width=DEFAULT_WIDTH, height=DEFAULT_HEIGHT)
    print(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
