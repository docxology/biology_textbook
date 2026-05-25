"""Tests for answer scaffold filling and enrichment answer keys."""

from __future__ import annotations

from pathlib import Path

import pytest

from biology.answer_refinement.scaffolds import generate_answer, process_bank
from biology.enrichment.answer_keys import (
    answer_key,
    common_pitfall,
    evidence_target,
    prompt_cues,
    refine_question_banks,
    scholarship_check,
)
from biology.enrichment.models import ChapterRecord


def test_generate_answer_includes_chapter_reference() -> None:
    body = generate_answer(
        3,
        "Recall",
        "Define osmosis and explain why it matters for cells.",
        "sec:unit_II_membrane_transport",
    )
    assert "**Answer (Q3, Recall).**" in body
    assert "\\cref{sec:unit_II_membrane_transport}" in body
    assert "osmosis" in body.lower()


def test_process_bank_fills_instructor_scaffold_dry_run(tmp_path: Path) -> None:
    bank = tmp_path / "questions_demo.md"
    bank.write_text(
        "# Questions\n\\label{sec:q_unit_I_demo}\n\n"
        "1. Define osmosis.\n\n"
        "<!-- SOLUTION\n"
        "**Answer (Q1, Recall).** [INSTRUCTOR SCAFFOLD — fill before release]\n"
        "SOLUTION -->\n",
        encoding="utf-8",
    )
    filled = process_bank(bank, dry_run=True)
    assert filled == 1
    assert "[INSTRUCTOR SCAFFOLD" in bank.read_text(encoding="utf-8")


def test_answer_key_helpers_cover_prompt_specifics() -> None:
    record = ChapterRecord(
        unit_id="unit_I",
        unit_title="Unit I",
        file="water_and_life.md",
        title="Water and Life",
    )
    question = "Calculate the water potential when Ψ_s = -0.8 MPa and Ψ_p = 0.3 MPa."
    key = answer_key(12, question, record)
    assert "water potential" in key.lower()
    assert "\\cref{sec:unit_I_water_and_life}" in key
    assert scholarship_check("quantitative")
    assert "units" in common_pitfall("quantitative", question)
    assert "MPa" in prompt_cues(question) or "carry through" in prompt_cues(question)
    assert "definition" in evidence_target("definition", record)


def test_process_bank_writes_scaffold_when_applied(tmp_path: Path) -> None:
    bank = tmp_path / "questions_demo.md"
    bank.write_text(
        "# Questions\n\\label{sec:q_unit_I_demo}\n\n"
        "1. Define osmosis.\n\n"
        "<!-- SOLUTION\n"
        "**Answer (Q1, Recall).** [INSTRUCTOR SCAFFOLD — fill before release]\n"
        "SOLUTION -->\n",
        encoding="utf-8",
    )
    filled = process_bank(bank, dry_run=False)
    assert filled == 1
    updated = bank.read_text(encoding="utf-8")
    assert "[INSTRUCTOR SCAFFOLD" not in updated
    assert "\\cref{sec:unit_I_demo}" in updated


def test_refine_question_banks_rewrites_generic_signature_dry_run(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    manuscript = tmp_path / "manuscript"
    bank = manuscript / "questions" / "unit_I" / "questions_water_and_life.md"
    bank.parent.mkdir(parents=True)
    bank.write_text(
        "# Questions\n\\label{sec:q_unit_I_water_and_life}\n\n"
        "1. Define water potential.\n\n"
        "<!-- SOLUTION\n"
        "**Answer.** Expected answer for *water potential*: use the definition.\n"
        "SOLUTION -->\n",
        encoding="utf-8",
    )
    monkeypatch.setattr("biology.enrichment.paths.MANUSCRIPT", manuscript)
    monkeypatch.setattr("biology.enrichment.models.MANUSCRIPT", manuscript)
    record = ChapterRecord(
        unit_id="unit_I",
        unit_title="Unit I",
        file="water_and_life.md",
        title="Water and Life",
    )
    changed_files, changed_blocks = refine_question_banks([record], dry_run=True)
    assert changed_files == 1
    assert changed_blocks == 1
    assert "Expected answer for" in bank.read_text(encoding="utf-8")


def test_refine_question_banks_persists_rewrite_when_applied(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    manuscript = tmp_path / "manuscript"
    bank = manuscript / "questions" / "unit_I" / "questions_water_and_life.md"
    bank.parent.mkdir(parents=True)
    bank.write_text(
        "# Questions\n\\label{sec:q_unit_I_water_and_life}\n\n"
        "1. Define water potential.\n\n"
        "<!-- SOLUTION\n"
        "**Answer.** Expected answer for *water potential*: use the definition.\n"
        "SOLUTION -->\n",
        encoding="utf-8",
    )
    monkeypatch.setattr("biology.enrichment.paths.MANUSCRIPT", manuscript)
    monkeypatch.setattr("biology.enrichment.models.MANUSCRIPT", manuscript)
    record = ChapterRecord(
        unit_id="unit_I",
        unit_title="Unit I",
        file="water_and_life.md",
        title="Water and Life",
    )
    changed_files, changed_blocks = refine_question_banks([record], dry_run=False)
    assert changed_files == 1
    assert changed_blocks == 1
    assert "Expected answer for" not in bank.read_text(encoding="utf-8")
