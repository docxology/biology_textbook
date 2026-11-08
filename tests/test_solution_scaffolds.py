"""Missing solutions require authorship, not automatic release placeholders."""

from pathlib import Path

import pytest

from biology.answer_refinement.generation import UnsupportedAnswerRepair
from biology.answer_refinement.solution_scaffolds import (
    insert_solution_scaffolds,
    process_question_bank,
    scaffold_block,
)


def test_scaffold_block_explicitly_refuses_missing_real_answer() -> None:
    with pytest.raises(UnsupportedAnswerRepair, match="Q5"):
        scaffold_block(5, "Calculate the probability of aa from Aa × Aa.")


@pytest.mark.parametrize("dry_run,write", [(False, True), (True, True), (False, False)])
def test_missing_answer_never_inserts_placeholder(tmp_path: Path, dry_run: bool, write: bool) -> None:
    bank = tmp_path / "questions_demo.md"
    original = "# Questions {#sec:q_unit_V_population_genetics}\n\n1. Calculate the probability of aa from Aa × Aa.\n"
    bank.write_text(original, encoding="utf-8")
    with pytest.raises(UnsupportedAnswerRepair, match="Q1"):
        process_question_bank(bank, dry_run=dry_run, write=write)
    assert bank.read_text(encoding="utf-8") == original


def test_directory_validation_cannot_partially_insert_scaffolds(tmp_path: Path) -> None:
    questions = tmp_path / "questions"
    questions.mkdir()
    first = questions / "questions_a.md"
    second = questions / "questions_b.md"
    first.write_text("# Questions {#sec:q_unit_V_population_genetics}\n1. Calculate P(aa) from Aa × Aa.\n<!-- SOLUTION\n**Answer (Q1, Application).** Each parent transmits a with probability 1/2, so P(aa) = 1/4.\nSOLUTION -->\n", encoding="utf-8")
    second.write_text("# Questions {#sec:q_unit_V_population_genetics}\n1. Explain genetic drift.\n", encoding="utf-8")
    before = {path: path.read_bytes() for path in (first, second)}
    with pytest.raises(UnsupportedAnswerRepair):
        insert_solution_scaffolds(questions)
    assert {path: path.read_bytes() for path in before} == before


def test_empty_bank_directory_is_not_a_silent_noop(tmp_path: Path) -> None:
    with pytest.raises(ValueError):
        insert_solution_scaffolds(tmp_path)
