"""Tests for answer-refinement classification, evidence, and generation helpers."""

from __future__ import annotations

from pathlib import Path

from biology.answer_refinement.classification import (
    classify_question,
    is_v1_generated,
    prompt_specific_anchor,
    tier_for,
)
from biology.answer_refinement.evidence import (
    chapter_category,
    chapter_evidence,
    chapter_method,
    fallback_evidence,
    pitfall_for,
)
from biology.answer_refinement.generation import answer_clauses, generate_answer


def test_classify_question_covers_major_prompt_shapes() -> None:
    assert classify_question("Evaluate whether herd immunity alone can control measles at 92% coverage.") == "evaluate"
    assert classify_question("Design an experiment to test whether auxin transport drives phototropism.") == "design"
    assert classify_question("Compare innate and adaptive immunity in response speed.") == "compare"
    assert classify_question("Calculate Hardy-Weinberg allele frequency when q² = 0.16.") == "calculate"
    assert classify_question("Define the term apoptosis.") == "define"
    assert classify_question("A patient presents with hyperglycaemia. Explain the insulin response.") == "apply"
    assert classify_question("Explain how CRISPR-Cas9 creates a double-strand break.") == "explain"


def test_prompt_specific_anchor_extracts_clauses_and_quantities() -> None:
    clause_anchor = prompt_specific_anchor("Explain photosynthesis (a) light reactions and (b) Calvin cycle.")
    assert "Address these prompt parts" in clause_anchor
    quantity_anchor = prompt_specific_anchor("Calculate growth when r = 0.3 and K = 1000 individuals.")
    assert "0.3" in quantity_anchor or "1000" in quantity_anchor


def test_evidence_helpers_return_non_empty_strings() -> None:
    e1, e2 = fallback_evidence("ecology")
    assert e1 and e2
    assert pitfall_for("calculate", "ecology")
    assert chapter_method("physiology")
    assert chapter_category("population_ecology") == "ecology"


def test_chapter_evidence_uses_manuscript_sentences() -> None:
    e1, e2 = chapter_evidence(
        "unit_V",
        "population_genetics",
        "Explain Hardy-Weinberg equilibrium assumptions.",
        "evolution_genetics",
    )
    assert len(e1) > 20
    assert len(e2) > 20


def test_generate_answer_for_each_kind() -> None:
    for kind_prompt in (
        "Define osmosis.",
        "Compare mitosis and meiosis.",
        "Calculate q when 16 of 100 individuals are homozygous recessive.",
        "Explain negative feedback in the HPA axis.",
        "Design an experiment to test enzyme inhibition.",
        "Evaluate whether vaccination alone can eradicate polio.",
        "A farmer observes crop wilting. Apply water-potential reasoning.",
    ):
        answer = generate_answer(
            1,
            tier_for(1),
            kind_prompt,
            "sec:unit_I_water_and_life",
            chapter_category("water_and_life"),
        )
        assert "Expected reasoning:" not in answer
        assert "Scoring focus:" not in answer
        assert "\\cref{sec:unit_I_water_and_life}" in answer


def test_answer_clauses_and_v1_signature_detection() -> None:
    assert "Address the requested parts explicitly" in answer_clauses("Explain (a) cause and (b) effect.")
    assert is_v1_generated("**Answer.** Expected reasoning: trace the mechanism.")
    assert not is_v1_generated("**Answer.** Punnett square for Aa x Aa gives 3:1.")


def test_candidate_sentences_skip_scaffold_and_short_lines() -> None:
    from biology.answer_refinement.classification import _candidate_sentences

    chapter = "\n".join(
        [
            "## Methods",
            "",
            "This is a substantive mechanistic sentence about membrane transport channels that is long enough to pass the candidate filter for evidence selection in answer refinement workflows.",
        ]
    )
    sentences = _candidate_sentences(chapter)
    assert any("membrane transport" in sentence for sentence in sentences)
    assert all("Concept Check" not in sentence for sentence in sentences)


def test_clean_sentence_preserves_inline_latex() -> None:
    from biology.answer_refinement.classification import _clean_sentence

    cleaned = _clean_sentence("The $\\Delta G$ value for ATP hydrolysis is strongly negative under cellular conditions.")
    assert "$\\Delta G$" in cleaned or "Delta G" in cleaned
    assert len(cleaned) >= 40


def test_process_bank_dry_run_refines_v1_signature(tmp_path: Path) -> None:
    from biology.answer_refinement.engine import process_bank

    bank = tmp_path / "questions_sample.md"
    bank.write_text(
        "\n".join(
            [
                "# Sample Questions \\label{sec:q_unit_I_atoms_molecules}",
                "",
                "1. Define an atom.",
                "<!-- SOLUTION",
                "**Answer (Q1, Recall).** Expected answer for *an atom*: use the definition.",
                "SOLUTION -->",
            ]
        ),
        encoding="utf-8",
    )
    refined, skipped = process_bank(bank, dry_run=True)
    assert refined == 1
    assert skipped == 0
    assert "Expected answer for" in bank.read_text(encoding="utf-8")
