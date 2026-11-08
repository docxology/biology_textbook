#!/usr/bin/env python3
"""Check XeLaTeX/PDF logs for render regressions."""

from __future__ import annotations

import argparse
from pathlib import Path

from _bootstrap import ensure_project_paths

ensure_project_paths()

from biology.quality.pdf_log import run_pdf_log_check


def run(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("log", type=Path, help="Path to a XeLaTeX or combined manuscript log")
    parser.add_argument("--max-overfull-pt", type=float, default=50.0)
    parser.add_argument("--max-overfull-vbox-pt", type=float, default=350.0)
    parser.add_argument(
        "--allow-missing-glyphs",
        action="store_true",
        help="Do not fail on XeLaTeX 'Missing character' warnings (instructor solution keys)",
    )
    args = parser.parse_args(argv)
    return run_pdf_log_check(
        args.log,
        max_overfull_pt=args.max_overfull_pt,
        max_overfull_vbox_pt=args.max_overfull_vbox_pt,
        allow_missing_glyphs=args.allow_missing_glyphs,
    )


if __name__ == "__main__":
    raise SystemExit(run())
