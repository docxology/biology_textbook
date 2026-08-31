"""Project paths for the analysis pipeline."""

from __future__ import annotations

from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[3]
MANUSCRIPT_DIR = PROJECT_ROOT / "docs" / "manuscript"
CONFIG_FILE = MANUSCRIPT_DIR / "config.yaml"
OUTPUT_DIR = PROJECT_ROOT / "output" / "manuscript"
OUTPUT_ROOT = PROJECT_ROOT / "output"

__all__ = [
    "CONFIG_FILE",
    "MANUSCRIPT_DIR",
    "OUTPUT_DIR",
    "OUTPUT_ROOT",
    "PROJECT_ROOT",
]
