"""Unsupported repair is explicit and never damages authored solutions."""

from pathlib import Path

import pytest

from biology.answer_refinement.engine import process_bank as refine_bank
from biology.answer_refinement.generation import UnsupportedAnswerRepair
from biology.answer_refinement.scaffolds import generate_answer
from biology.answer_refinement.scaffolds import process_bank as fill_bank

_REVIEWED = """# Questions {#sec:q_unit_V_population_genetics .unnumbered}

1. Under Hardy–Weinberg assumptions, 16 of 100 individuals are recessive. Calculate p and q.
<!-- SOLUTION
**Answer (Q1, Application).** q² = 16/100 = 0.16, so q = 0.4 and p = 1 − q = 0.6.
1. The square root is appropriate because the recessive phenotype has genotype aa.
2. The genotype frequencies are 0.36, 0.48 and 0.16, which sum to one.
SOLUTION -->
"""


@pytest.mark.parametrize("repair", [refine_bank, fill_bank])
@pytest.mark.parametrize("dry_run", [False, True])
def test_reviewed_solution_and_its_numbered_reasoning_are_preserved(tmp_path: Path, repair, dry_run: bool) -> None:
    bank = tmp_path / "questions_population_genetics.md"
    bank.write_text(_REVIEWED, encoding="utf-8")
    before = bank.read_bytes()
    repair(bank, dry_run=dry_run)
    assert bank.read_bytes() == before
    assert refine_bank(bank, dry_run=True) == (0, 1)


@pytest.mark.parametrize("legacy", [
    "**Answer (Q2, Recall).** [INSTRUCTOR SCAFFOLD — fill before release]",
    "**Answer (Q2, Recall).** Expected reasoning: trace the mechanism.",
])
@pytest.mark.parametrize("repair", [refine_bank, fill_bank])
@pytest.mark.parametrize("dry_run", [False, True])
def test_unsupported_later_item_refuses_without_partial_write(tmp_path: Path, legacy: str, repair, dry_run: bool) -> None:
    bank = tmp_path / "questions_population_genetics.md"
    original = _REVIEWED + f"\n2. Explain genetic drift.\n<!-- SOLUTION\n{legacy}\nSOLUTION -->\n"
    bank.write_text(original, encoding="utf-8")
    before = bank.read_bytes()
    with pytest.raises(UnsupportedAnswerRepair, match="Q2"):
        repair(bank, dry_run=dry_run)
    assert bank.read_bytes() == before


def test_generation_refuses_to_substitute_guidance_for_actual_calculation() -> None:
    with pytest.raises(UnsupportedAnswerRepair, match="Q12"):
        generate_answer(12, "Application", "Calculate q when q² = 0.16.", "sec:unit_V_population_genetics")


@pytest.mark.parametrize("text", ["# Questions\n1. Explain drift.\n", "# Questions {#sec:q_unit_V_population_genetics}\n"])
def test_malformed_or_empty_bank_is_not_a_silent_success(tmp_path: Path, text: str) -> None:
    bank = tmp_path / "questions_population_genetics.md"
    bank.write_text(text, encoding="utf-8")
    with pytest.raises(ValueError):
        refine_bank(bank)
    assert bank.read_text(encoding="utf-8") == text


def test_substantive_handwritten_evidence_and_pitfall_labels_are_not_scaffolds(tmp_path: Path) -> None:
    bank = tmp_path / "questions_population_genetics.md"
    original = _REVIEWED.replace(
        "\nSOLUTION -->",
        "\n\nCommon pitfall: recessive phenotype frequency is q², not q.\n"
        "Evidence anchor: 16/100 = 0.16 supports q = 0.4, not q = 0.16.\nSOLUTION -->",
    )
    bank.write_text(original, encoding="utf-8")
    assert refine_bank(bank) == (0, 1)
    assert fill_bank(bank) == 0
    assert bank.read_text(encoding="utf-8") == original
