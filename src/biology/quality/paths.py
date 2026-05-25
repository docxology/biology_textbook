"""Filesystem paths for textbook quality auditing."""

from __future__ import annotations

from pathlib import Path

PROJECT = Path(__file__).resolve().parents[3]
MANUSCRIPT = PROJECT / "manuscript"
QUALITY_ADVISORIES = MANUSCRIPT / "quality_advisories.yaml"

__all__ = ["MANUSCRIPT", "PROJECT", "QUALITY_ADVISORIES"]
