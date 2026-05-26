"""Tests for cover art generation."""

from __future__ import annotations

from biology.assets.cover_art import DEFAULT_HEIGHT, DEFAULT_WIDTH, generate_cover


def test_generate_cover_writes_png(tmp_path) -> None:
    output = tmp_path / "cover.png"
    path = generate_cover(output, width=400, height=300)
    data = path.read_bytes()
    assert data[:8] == b"\x89PNG\r\n\x1a\n"
    assert path.stat().st_size > 10_000
    assert DEFAULT_WIDTH == 2400
    assert DEFAULT_HEIGHT == 1800
