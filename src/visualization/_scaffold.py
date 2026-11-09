"""Shared matplotlib scaffold for biology textbook figures."""

from __future__ import annotations

import os

os.environ.setdefault("MPLBACKEND", "Agg")

from pathlib import Path
from tempfile import NamedTemporaryFile

import matplotlib

matplotlib.use("Agg")
from typing import Literal

import matplotlib.pyplot as plt

from textbook_io import require_independent_file_target
from textbook_logging import get_logger
from textbook_visuals import pad_png_to_square

from .cvd import (
    BAR_NEG,
    BAR_POS,
    BLUE,
    GRAY,
    ORANGE,
    PUNNETT_DOMINANT,
    PUNNETT_RECESSIVE,
    PURPLE,
    SERIES2,
    SERIES3,
    SERIES4,
    TEAL,
)

logger = get_logger(__name__)

__all__ = [
    "BAR_NEG",
    "BAR_POS",
    "BLUE",
    "GRAY",
    "ORANGE",
    "PUNNETT_DOMINANT",
    "PUNNETT_RECESSIVE",
    "PURPLE",
    "SERIES2",
    "SERIES3",
    "SERIES4",
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
    """Publish a complete PNG without following output aliases or leaving partial bytes."""
    path = output_dir / filename
    temporary: Path | None = None
    try:
        output_dir.mkdir(parents=True, exist_ok=True)
        require_independent_file_target(path)
        with NamedTemporaryFile(
            dir=output_dir, prefix=f".{path.stem}.", suffix=path.suffix, delete=False,
        ) as handle:
            temporary = Path(handle.name)
        fig.savefig(temporary, dpi=150, bbox_inches="tight")
        if aspect == "square":
            pad_png_to_square(temporary)
        require_independent_file_target(path)
        temporary.replace(path)
    finally:
        plt.close(fig)
        if temporary is not None:
            temporary.unlink(missing_ok=True)
    logger.info(f"Saved figure: {path}")
    return path
