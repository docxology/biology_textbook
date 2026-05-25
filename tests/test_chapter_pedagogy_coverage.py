"""Regression tests for Tier-2 pedagogy commitments (REVIEW §7)."""

from __future__ import annotations

import re
from pathlib import Path

import pytest

PROJECT = Path(__file__).resolve().parent.parent
MANUSCRIPT = PROJECT / "manuscript"

WORKED_EXAMPLE_HEADING_RE = re.compile(
    r"^#{2,5}\s+Worked Examples?(?:\s|:|\s*$)",
    re.MULTILINE | re.IGNORECASE,
)
WORKED_EXAMPLE_BLOCKQUOTE_RE = re.compile(
    r"^\s*>\s*\*\*Worked Example",
    re.MULTILINE | re.IGNORECASE,
)
CONCEPT_CHECK_RE = re.compile(
    r"^\s*>?\s*\*\*Concept Check(?:\b|\s|\d|\()",
    re.MULTILINE,
)
OBJECTIVE_BLOCK_RE = re.compile(
    r"## Learning Objectives\n(?P<body>.*?)(?:\n<!-- curriculum-scaffold-start -->|\n---|\n## )",
    re.DOTALL,
)
OBJECTIVE_VERB_RE = re.compile(r"^\d+\.\s+(?:\*\*)?([A-Za-z]+)")

RECALL_TIER_VERBS = frozenset(
    {
        "Describe",
        "Explain",
        "State",
        "List",
        "Define",
        "Recall",
        "Name",
        "Identify",
    }
)

QUANTITATIVE_CHAPTER_STEMS = (
    "atoms_molecules",
    "enzymes_and_kinetics",
    "dna_replication_and_cell_cycle",
    "mutations_and_genomics",
    "cell_signaling",
    "phylogenetics",
    "host_immunity_and_vaccines",
    "antimicrobial_resistance_and_epidemiology",
    "endocrine_signaling",
    "immune_system_defense",
    "chromosomal_inheritance",
    "plant_responses",
    "genetic_drift_and_speciation",
    "ecosystem_ecology",
)

CONCEPT_CHECK_DENSE_STEMS = (
    "population_genetics",
    "chromosomal_inheritance",
    "action_potential_synapses",
    "circulation_respiration_homeostasis",
)

BLOOM_DIVERSE_STEMS = (
    "gene_expression",
    "metabolic_integration",
    "nervous_system",
)

SKIP_CHAPTER_NAMES = frozenset({"README.md", "AGENTS.md", "unit_intro.md"})


def _chapter_path(stem: str) -> Path:
    matches = sorted(MANUSCRIPT.rglob(f"{stem}.md"))
    assert len(matches) == 1, f"expected one chapter for {stem}, found {matches}"
    return matches[0]


def _core_chapters() -> list[Path]:
    return [
        path
        for path in sorted(MANUSCRIPT.glob("unit_*/*.md"))
        if path.name not in SKIP_CHAPTER_NAMES
    ]


def _worked_example_count(text: str) -> int:
    return len(WORKED_EXAMPLE_HEADING_RE.findall(text)) + len(
        WORKED_EXAMPLE_BLOCKQUOTE_RE.findall(text)
    )


def _objective_verbs(chapter: Path) -> list[str]:
    match = OBJECTIVE_BLOCK_RE.search(chapter.read_text(encoding="utf-8"))
    assert match is not None, f"{chapter}: missing Learning Objectives block"
    verbs: list[str] = []
    for line in match.group("body").splitlines():
        item = OBJECTIVE_VERB_RE.match(line.strip())
        if item is not None:
            verbs.append(item.group(1))
    return verbs


@pytest.mark.parametrize("stem", QUANTITATIVE_CHAPTER_STEMS)
def test_quantitative_chapters_have_at_least_two_worked_examples(stem: str) -> None:
    chapter = _chapter_path(stem)
    count = _worked_example_count(chapter.read_text(encoding="utf-8"))
    assert count >= 2, f"{chapter.relative_to(MANUSCRIPT)}: {count} worked examples"


@pytest.mark.parametrize("stem", CONCEPT_CHECK_DENSE_STEMS)
def test_named_chapters_have_at_least_three_concept_checks(stem: str) -> None:
    chapter = _chapter_path(stem)
    count = len(CONCEPT_CHECK_RE.findall(chapter.read_text(encoding="utf-8")))
    assert count >= 3, f"{chapter.relative_to(MANUSCRIPT)}: {count} concept checks"


def test_unit_ix_chapters_have_at_least_three_concept_checks() -> None:
    offenders: list[str] = []
    for chapter in sorted((MANUSCRIPT / "unit_IX").glob("*.md")):
        if chapter.name in SKIP_CHAPTER_NAMES:
            continue
        count = len(CONCEPT_CHECK_RE.findall(chapter.read_text(encoding="utf-8")))
        if count < 3:
            offenders.append(f"{chapter.relative_to(MANUSCRIPT)}: {count}")
    assert not offenders


@pytest.mark.parametrize("stem", BLOOM_DIVERSE_STEMS)
def test_flagged_chapters_have_non_recall_learning_objective_verbs(stem: str) -> None:
    chapter = _chapter_path(stem)
    verbs = _objective_verbs(chapter)
    higher_order = [verb for verb in verbs if verb not in RECALL_TIER_VERBS]
    assert len(higher_order) >= 2, f"{chapter.relative_to(MANUSCRIPT)}: verbs={verbs}"


def test_core_chapters_have_at_least_seven_learning_objectives() -> None:
    offenders: list[str] = []
    for chapter in _core_chapters():
        verbs = _objective_verbs(chapter)
        if len(verbs) < 7:
            offenders.append(f"{chapter.relative_to(MANUSCRIPT)}: {len(verbs)} objectives")
    assert not offenders
