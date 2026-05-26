"""Tests for parent-chapter cross-reference insertion."""

from __future__ import annotations

from pathlib import Path

from biology.crossref.parent_chapter_links import (
    apply_parent_chapter_cref,
    derive_parent_section_label,
    insert_parent_chapter_cref,
)


def test_derive_parent_section_label_from_lab_path() -> None:
    path = Path("manuscript/labs/unit_I/lab_atoms_molecules.md")
    assert derive_parent_section_label(path) == "sec:unit_I_atoms_molecules"


def test_insert_parent_chapter_cref_is_idempotent() -> None:
    path = Path("manuscript/questions/unit_II/questions_cell_theory.md")
    text = "\\label{sec:questions_unit_II_cell_theory}\n\nFirst paragraph."
    updated = insert_parent_chapter_cref(text, path)
    assert updated is not None
    assert "\\cref{sec:unit_II_cell_theory}" in updated
    assert insert_parent_chapter_cref(updated, path) is None


def test_apply_parent_chapter_cref_writes_file(tmp_path) -> None:
    path = tmp_path / "manuscript" / "labs" / "unit_I" / "lab_atoms.md"
    path.parent.mkdir(parents=True)
    path.write_text("\\label{sec:lab_unit_I_atoms}\n\nBody.\n", encoding="utf-8")
    assert apply_parent_chapter_cref(path) is True
    assert "\\cref{sec:unit_I_atoms}" in path.read_text(encoding="utf-8")
