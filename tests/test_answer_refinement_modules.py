"""Classification remains useful, but cannot stand in for scientific answers."""

import pytest

from biology.answer_refinement.classification import classify_question, is_v1_generated
from biology.answer_refinement.generation import (
    UnsupportedAnswerRepair,
    generate_answer,
)


@pytest.mark.parametrize("prompt,kind", [
    ("Evaluate whether herd immunity alone can control measles at 92% coverage.", "evaluate"),
    ("Design an experiment to test whether auxin transport drives phototropism.", "design"),
    ("Compare innate and adaptive immunity in response speed.", "compare"),
    ("Calculate Hardy-Weinberg allele frequency when q² = 0.16.", "calculate"),
    ("Define apoptosis.", "define"),
    ("A patient presents with hyperglycemia. Explain the insulin response.", "apply"),
    ("Explain how CRISPR-Cas9 creates a double-strand break.", "explain"),
])
def test_question_classification_does_not_author_an_answer(prompt: str, kind: str) -> None:
    assert classify_question(prompt) == kind
    with pytest.raises(UnsupportedAnswerRepair):
        generate_answer(1, "Recall", prompt, "sec:unit_I_atoms_molecules")


def test_supplied_chapter_excerpts_do_not_prove_a_prompt_solution() -> None:
    with pytest.raises(UnsupportedAnswerRepair):
        generate_answer(
            12, "Application", "Calculate q when 16 of 100 individuals have the recessive phenotype.",
            "sec:unit_V_population_genetics", "evolution_genetics",
            ("Allele frequencies sum to one.", "Hardy–Weinberg equilibrium assumes random mating."),
        )


def test_legacy_signature_detection_distinguishes_substantive_calculation() -> None:
    assert is_v1_generated("**Answer.** Expected reasoning: trace the mechanism.")
    assert not is_v1_generated("**Answer.** q² = 0.16, so q = 0.4 and p = 0.6.")


@pytest.mark.parametrize("body", [
    "**Answer (Q1, Recall).** The response should first state the chapter's concrete mechanism.",
    "**Answer (Q1, Recall).** Scholarship standard: name the measured variables.",
    "**Answer (Q1, Recall).** Pitfall to avoid: reporting a number without units.",
])
def test_refinement_recognizes_scaffolds_already_rejected_by_quality_gate(body: str) -> None:
    assert is_v1_generated(body)
