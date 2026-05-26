"""Tests for short-lab debrief padding."""

from __future__ import annotations

from biology.maintenance.lab_padding import append_debrief_if_short, apply_lab_debrief


def test_append_debrief_if_short_adds_block() -> None:
    text = "\\label{sec:lab_unit_I_atoms}\n\nShort lab body.\n"
    updated = append_debrief_if_short(text, min_lines=100)
    assert updated is not None
    assert "## Debrief and Reflection" in updated
    assert "\\cref{sec:unit_I_atoms}" in updated


def test_append_debrief_if_short_skips_existing_block() -> None:
    text = "## Debrief and Reflection\n\nAlready present."
    assert append_debrief_if_short(text) is None


def test_apply_lab_debrief_writes_block(tmp_path) -> None:
    path = tmp_path / "lab.md"
    path.write_text("\\label{sec:lab_unit_I_atoms}\n\nShort.\n", encoding="utf-8")
    assert apply_lab_debrief(path) is True
    assert "## Debrief and Reflection" in path.read_text(encoding="utf-8")
