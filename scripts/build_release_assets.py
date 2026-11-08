#!/usr/bin/env python3
"""Build source-bound PDF and executable ZIP assets from validated clean main."""
from __future__ import annotations

import argparse
from dataclasses import asdict
from pathlib import Path

from _bootstrap import ensure_project_paths

ensure_project_paths()

from biology.pipeline.release_assets import build_release_assets
from textbook_paths import PROJECT


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", required=True, type=Path)
    parser.add_argument("--renderer-root", required=True, type=Path)
    args = parser.parse_args(argv)
    assets = build_release_assets(PROJECT, args.output_dir, args.renderer_root)
    for name, value in asdict(assets).items():
        print(f"{name}: {value}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
