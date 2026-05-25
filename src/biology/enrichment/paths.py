"""Project paths for enrichment."""

from __future__ import annotations

from pathlib import Path

PROJECT = Path(__file__).resolve().parents[3]
MANUSCRIPT = PROJECT / "manuscript"
DOCS = PROJECT / "docs"
