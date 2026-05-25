#!/usr/bin/env python3
"""Embedded enrichment pass for the biology textbook."""

from __future__ import annotations

from _bootstrap import ensure_project_paths

ensure_project_paths()

from biology.enrichment.cli import main

if __name__ == "__main__":
    raise SystemExit(main())
