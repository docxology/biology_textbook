"""Tests for question-bank answer refinement heuristics."""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path


SCRIPT = Path(__file__).resolve().parent.parent / "scripts" / "refine_generated_answers.py"
spec = importlib.util.spec_from_file_location("refine_generated_answers", SCRIPT)
assert spec is not None
module = importlib.util.module_from_spec(spec)
sys.modules["refine_generated_answers"] = module
assert spec.loader is not None
spec.loader.exec_module(module)


def test_subject_phrase_removes_command_prefix() -> None:
    assert module.subject_phrase("State Mendel's two laws. Give the biological basis.") == "Mendel's two laws"
    assert module.subject_phrase("What is a Punnett square? Draw and solve: Aa x Aa.") == "a Punnett square"


def test_classify_probability_and_chi_square_as_calculate() -> None:
    assert module.classify_question("What is the probability their first child will have PKU?") == "calculate"
    assert module.classify_question("A chi-square analysis gives χ² = 2.6. Should the null be rejected?") == "calculate"


def test_current_generated_answer_signatures_are_refinable() -> None:
    body = "**Answer.** Give the canonical definition of *What is a Punnett square*."
    assert module.is_v1_generated(body)
    current_body = "**Answer.** Expected answer for *water potential*: use the definition. Prompt cues to cover: Write."
    assert module.is_v1_generated(current_body)
    latest_body = "**Answer.** Define *a biome* in one precise sentence. Required clauses: a) climate."
    assert module.is_v1_generated(latest_body)
    just_regenerated_body = "**Answer.** A complete response should trace *MRSA* from cause to outcome."
    assert module.is_v1_generated(just_regenerated_body)
    expected_reasoning_body = "**Answer.** Expected reasoning: trace *MRSA* from cause to outcome."
    assert module.is_v1_generated(expected_reasoning_body)
    formulaic_body = (
        "**Answer.** Trace *MRSA* from initiating condition through mechanism to observable outcome. "
        "Scoring focus: identify the taxon."
    )
    assert module.is_v1_generated(formulaic_body)
    hand_written = "**Answer.** Punnett square for X^H X^h x X^H Y: gametes from mother..."
    assert not module.is_v1_generated(hand_written)


def test_regenerated_answers_do_not_use_expected_reasoning_scaffold() -> None:
    answer = module.generate_answer(
        12,
        "Application",
        "Calculate the allele frequency if 16 of 100 individuals are recessive.",
        "sec:unit_V_population_genetics",
        "evolution_genetics",
    )
    assert "Expected reasoning:" not in answer
    assert "Scoring focus:" not in answer
    assert "Chapter anchor:" in answer
    assert "\\cref{sec:unit_V_population_genetics}" in answer
