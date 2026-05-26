"""Tests for ``biology.answer_refinement.solution_scaffolds``."""

from __future__ import annotations

from pathlib import Path

from biology.answer_refinement.solution_scaffolds import (
    insert_solution_scaffolds,
    process_question_bank,
    scaffold_block,
)


def test_scaffold_block_includes_tier_and_anchor() -> None:
    block = scaffold_block(5, "What is ATP?")
    assert "Q5" in block
    assert "Recall" in block
    assert "What is ATP?" in block
    assert block.startswith("<!-- SOLUTION")


def test_process_question_bank_is_idempotent(tmp_path: Path) -> None:
    bank = tmp_path / "questions_demo.md"
    bank.write_text(
        "<!-- assess: unit -->\n\n"
        "1. First question?\n\n"
        "2. Second question?\n",
        encoding="utf-8",
    )
    first_pass = process_question_bank(bank, dry_run=False, write=True)
    text_after_first = bank.read_text(encoding="utf-8")
    assert first_pass == 2
    assert "<!-- assess:" in text_after_first
    assert text_after_first.index("<!-- assess:") < text_after_first.index("<!-- SOLUTION")

    second_pass = process_question_bank(bank, dry_run=False, write=True)
    assert second_pass == 0
    assert bank.read_text(encoding="utf-8") == text_after_first


def test_insert_solution_scaffolds_dry_run_counts(tmp_path: Path) -> None:
    questions = tmp_path / "questions" / "unit_I"
    questions.mkdir(parents=True)
    bank = questions / "questions_demo.md"
    bank.write_text("1. Question one?\n\n2. Question two?\n", encoding="utf-8")
    report = insert_solution_scaffolds(tmp_path / "questions", dry_run=True, write=False)
    assert report.scaffolds_inserted == 2
    assert report.files_touched == 1
    assert bank.read_text(encoding="utf-8") == "1. Question one?\n\n2. Question two?\n"
