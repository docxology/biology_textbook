"""Shared matplotlib scaffold for biology textbook figures."""

from __future__ import annotations

import os

os.environ.setdefault("MPLBACKEND", "Agg")

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

from typing import Literal

from textbook_logging import get_logger
from textbook_visuals import pad_png_to_square

from .cvd import (
    BAR_NEG,
    BAR_POS,
    GRAY,
    ORANGE,
    PUNNETT_DOMINANT,
    PUNNETT_RECESSIVE,
    PURPLE,
    SERIES2,
    SERIES3,
    TEAL,
)

logger = get_logger(__name__)

__all__ = [
    "BAR_NEG",
    "BAR_POS",
    "GRAY",
    "ORANGE",
    "PUNNETT_DOMINANT",
    "PUNNETT_RECESSIVE",
    "PURPLE",
    "SERIES2",
    "SERIES3",
    "TEAL",
    "_save_figure",
    "get_logger",
    "logger",
]


def _save_figure(
    fig: plt.Figure,
    output_dir: Path,
    filename: str,
    *,
    aspect: Literal["square", "landscape"] = "square",
) -> Path:
    """Save a matplotlib figure to disk and close it."""
    output_dir.mkdir(parents=True, exist_ok=True)
    path = output_dir / filename
    fig.savefig(path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    if aspect == "square":
        pad_png_to_square(path)
    logger.info(f"Saved figure: {path}")
    return path
