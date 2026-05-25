"""Tests for shared figure post-processing helpers."""

from __future__ import annotations

from pathlib import Path

import pytest

pytest.importorskip("PIL")

from textbook_visuals import pad_png_to_square


def test_pad_png_to_square_expands_non_square_image(tmp_path: Path) -> None:
    from PIL import Image

    path = tmp_path / "wide.png"
    Image.new("RGBA", (200, 100), (255, 0, 0, 255)).save(path)
    pad_png_to_square(path)
    with Image.open(path) as image:
        assert image.size[0] == image.size[1] == 200
