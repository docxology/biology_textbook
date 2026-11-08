#!/usr/bin/env python3
"""Visual contract manifest audit."""

from __future__ import annotations

from _bootstrap import ensure_project_paths

ensure_project_paths()

from biology.visual_contracts import (
    build_manifest,
    check_records,
    render_inline_mermaid_assets,
    write_manifest,
    write_review_matrix,
)
from biology.visual_contracts_cli import main
from biology.visual_contracts_paths import DEFAULT_MANIFEST

__all__ = [
    "DEFAULT_MANIFEST",
    "build_manifest",
    "check_records",
    "main",
    "render_inline_mermaid_assets",
    "write_manifest",
    "write_review_matrix",
]

if __name__ == "__main__":
    raise SystemExit(main())
