"""Tests for manuscript typography normalization."""

from __future__ import annotations

from biology.maintenance.typography import normalize_arrows_in_file, normalize_arrows_in_text, replace_greek_math_in_text


def test_normalize_arrows_skips_fenced_code() -> None:
    text = "Path A --> B\n```\nx --> y\n```\nDone --> end"
    updated, count = normalize_arrows_in_text(text)
    assert count == 2
    assert "x --> y" in updated
    assert "Path A → B" in updated


def test_replace_greek_math_in_prose_only() -> None:
    text = "Use $\\alpha$ in prose but keep `$\\beta$` inline code."
    updated, count = replace_greek_math_in_text(text)
    assert count == 1
    assert "α" in updated
    assert "$\\beta$" in updated


def test_normalize_arrows_in_file_writes_changes(tmp_path) -> None:
    path = tmp_path / "sample.md"
    path.write_text("Signal A --> B\n", encoding="utf-8")
    count = normalize_arrows_in_file(path)
    assert count == 1
    assert "→" in path.read_text(encoding="utf-8")
