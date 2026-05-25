"""Tests for shared textbook_io helpers."""

from __future__ import annotations

from pathlib import Path

import pytest

from textbook_io import write_text_atomic


def test_write_text_atomic_cleans_temp_file_when_replace_fails(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    target = tmp_path / "chapter.md"

    def failing_replace(*_args: object, **_kwargs: object) -> None:
        raise OSError("replace failed")

    monkeypatch.setattr("textbook_io.os.replace", failing_replace)

    with pytest.raises(OSError, match="replace failed"):
        write_text_atomic(target, "draft\n")

    assert not target.exists()
    assert not list(tmp_path.glob(".*.tmp"))
