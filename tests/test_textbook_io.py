"""Tests for shared textbook_io helpers."""

from __future__ import annotations

from pathlib import Path

import pytest

from textbook_io import write_text_atomic


def test_write_text_atomic_cleans_temp_file_when_replace_fails(tmp_path: Path) -> None:
    # A regular temporary file cannot replace a nonempty directory on disk.
    target = tmp_path / "chapter.md"
    target.mkdir()
    original = target / "original.md"
    original.write_bytes(b"original\n")
    neighbor = tmp_path / ".chapter.md.neighbor.tmp"
    neighbor.write_bytes(b"neighbor\n")
    before = set(tmp_path.iterdir())

    with pytest.raises(OSError):
        write_text_atomic(target, "draft\n")

    assert original.read_bytes() == b"original\n"
    assert neighbor.read_bytes() == b"neighbor\n"
    assert set(tmp_path.iterdir()) == before


def test_encoding_failure_preserves_target_and_only_removes_owned_temp(tmp_path: Path) -> None:
    target = tmp_path / "chapter.md"
    target.write_bytes(b"original\n")
    neighbor = tmp_path / ".chapter.md.neighbor.tmp"
    neighbor.write_bytes(b"neighbor\n")
    before = set(tmp_path.iterdir())

    with pytest.raises(UnicodeEncodeError):
        write_text_atomic(target, "prefix then μ\n", encoding="ascii")

    assert target.read_bytes() == b"original\n"
    assert neighbor.read_bytes() == b"neighbor\n"
    assert set(tmp_path.iterdir()) == before
