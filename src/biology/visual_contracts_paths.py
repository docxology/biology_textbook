"""Path constants for visual contract auditing."""

from __future__ import annotations

from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
TEMPLATE_ROOT = PROJECT_ROOT.parent.parent
SRC_DIR = PROJECT_ROOT / "src"
MANUSCRIPT_DIR = PROJECT_ROOT / "manuscript"
OUTPUT_FIGURES = PROJECT_ROOT / "output" / "figures"
DEFAULT_MANIFEST = OUTPUT_FIGURES / "visual_manifest.json"

__all__ = [
    "DEFAULT_MANIFEST",
    "MANUSCRIPT_DIR",
    "OUTPUT_FIGURES",
    "PROJECT_ROOT",
    "SRC_DIR",
    "TEMPLATE_ROOT",
]
