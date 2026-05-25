"""Shared image helpers for generated textbook visuals."""

from __future__ import annotations

from pathlib import Path

from PIL import Image


def pad_png_to_square(path: Path, *, background: tuple[int, int, int, int] = (255, 255, 255, 255)) -> Path:
    """Pad a PNG image onto a square white canvas in place.

    The plotted or rendered content is not resampled; padding is added equally
    on both sides of the shorter dimension. This keeps source generators
    deterministic while making rendered assets easier to place in the compact
    PDF layout.
    """
    path = Path(path)
    if path.suffix.lower() != ".png" or not path.exists():
        return path
    with Image.open(path) as image:
        rgba = image.convert("RGBA")
        width, height = rgba.size
        if width == height:
            return path
        side = max(width, height)
        canvas = Image.new("RGBA", (side, side), background)
        x = (side - width) // 2
        y = (side - height) // 2
        canvas.paste(rgba, (x, y), rgba)
        canvas.save(path)
    return path


__all__ = ["pad_png_to_square"]
