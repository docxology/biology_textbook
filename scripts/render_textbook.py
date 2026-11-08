#!/usr/bin/env python3
"""Render a freshly hydrated textbook without running template-root recipes."""

import argparse

from _bootstrap import ensure_project_paths

ensure_project_paths()

from biology.pipeline.rendering import render_textbook


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.parse_args(argv)
    print(render_textbook())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
