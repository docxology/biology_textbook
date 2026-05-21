"""Standards and skills alignment for the biology textbook.

This module is the curriculum layer above ``biology.curriculum``.  It maps
each chapter to widely used biology-education frameworks while keeping the
project's internal chapter/lab/question identifiers as the source of truth.

Reference frameworks used for the labels:

* College Board AP Biology Course and Exam Description, effective fall 2025.
* AAAS/NSF Vision and Change core concepts and competencies.
* NGSS high-school life-science topic organization.
* BioSkills Guide categories elaborating Vision and Change competencies.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from typing import Iterable, Mapping

from .curriculum import CURRICULUM


VISION_CHANGE_CONCEPTS: tuple[str, ...] = (
    "Evolution",
    "Structure and function",
    "Information flow, exchange, and storage",
    "Pathways and transformations of energy and matter",
    "Systems",
)

VISION_CHANGE_COMPETENCIES: tuple[str, ...] = (
    "Process of science",
    "Quantitative reasoning",
    "Modeling and simulation",
    "Interdisciplinary nature of science",
    "Communication and collaboration",
    "Science and society",
)

AP_BIOLOGY_BIG_IDEAS: tuple[str, ...] = (
    "Evolution",
    "Energetics",
    "Information Storage and Transmission",
    "Systems Interactions",
)

AP_BIOLOGY_PRACTICES: tuple[str, ...] = (
    "Concept Explanation",
    "Visual Representations",
    "Questions and Methods",
    "Representing and Describing Data",
    "Statistical Tests and Data Analysis",
    "Argumentation",
)

NGSS_HS_LS_TOPICS: tuple[str, ...] = (
    "Structure and Function",
    "Inheritance and Variation of Traits",
    "Matter and Energy in Organisms and Ecosystems",
    "Interdependent Relationships in Ecosystems",
    "Natural Selection and Evolution",
)

BIOSKILLS_CATEGORIES: tuple[str, ...] = VISION_CHANGE_COMPETENCIES


@dataclass(frozen=True)
class UnitAlignment:
    """Default framework alignment for a unit of the textbook."""

    vision_change_concepts: tuple[str, ...]
    vision_change_competencies: tuple[str, ...]
    ap_big_ideas: tuple[str, ...]
    ap_science_practices: tuple[str, ...]
    ngss_topics: tuple[str, ...]
    bioskills: tuple[str, ...]
    spiral_thread: str


@dataclass(frozen=True)
class AlignmentRecord:
    """Framework alignment and instructor orchestration for one chapter."""

    chapter_id: str
    vision_change_concepts: tuple[str, ...]
    vision_change_competencies: tuple[str, ...]
    ap_big_ideas: tuple[str, ...]
    ap_science_practices: tuple[str, ...]
    ngss_topics: tuple[str, ...]
    bioskills: tuple[str, ...]
    spiral_thread: str
    instructor_move: str
    formative_check: str
    summative_product: str


def _u(
    vision_change_concepts: tuple[str, ...],
    vision_change_competencies: tuple[str, ...],
    ap_big_ideas: tuple[str, ...],
    ap_science_practices: tuple[str, ...],
    ngss_topics: tuple[str, ...],
    bioskills: tuple[str, ...],
    spiral_thread: str,
) -> UnitAlignment:
    return UnitAlignment(
        vision_change_concepts=vision_change_concepts,
        vision_change_competencies=vision_change_competencies,
        ap_big_ideas=ap_big_ideas,
        ap_science_practices=ap_science_practices,
        ngss_topics=ngss_topics,
        bioskills=bioskills,
        spiral_thread=spiral_thread,
    )


UNIT_ALIGNMENTS: Mapping[str, UnitAlignment] = {
    "unit_0": _u(
        ("Systems", "Structure and function"),
        ("Modeling and simulation", "Quantitative reasoning", "Process of science"),
        ("Systems Interactions",),
        ("Questions and Methods", "Representing and Describing Data", "Argumentation"),
        ("Structure and Function", "Interdependent Relationships in Ecosystems"),
        ("Modeling and simulation", "Process of science", "Quantitative reasoning"),
        "Use systems diagrams, uncertainty, and feedback as recurring sense-making tools.",
    ),
    "unit_I": _u(
        ("Structure and function", "Pathways and transformations of energy and matter"),
        ("Quantitative reasoning", "Interdisciplinary nature of science"),
        ("Energetics", "Systems Interactions"),
        ("Concept Explanation", "Statistical Tests and Data Analysis", "Argumentation"),
        ("Matter and Energy in Organisms and Ecosystems", "Structure and Function"),
        ("Quantitative reasoning", "Interdisciplinary nature of science"),
        "Connect chemical structure, water, polymers, and catalysis to biological mechanism.",
    ),
    "unit_II": _u(
        ("Structure and function", "Systems", "Information flow, exchange, and storage"),
        ("Modeling and simulation", "Process of science"),
        ("Systems Interactions", "Information Storage and Transmission"),
        ("Visual Representations", "Questions and Methods", "Argumentation"),
        ("Structure and Function",),
        ("Modeling and simulation", "Process of science"),
        "Revisit boundaries, compartments, and signals as causal models of cellular work.",
    ),
    "unit_III": _u(
        ("Pathways and transformations of energy and matter", "Systems"),
        ("Quantitative reasoning", "Modeling and simulation"),
        ("Energetics", "Systems Interactions"),
        ("Representing and Describing Data", "Statistical Tests and Data Analysis"),
        ("Matter and Energy in Organisms and Ecosystems",),
        ("Quantitative reasoning", "Modeling and simulation"),
        "Track matter, electrons, and free energy through pathways and ecosystems.",
    ),
    "unit_IV": _u(
        ("Information flow, exchange, and storage", "Structure and function"),
        ("Process of science", "Quantitative reasoning", "Science and society"),
        ("Information Storage and Transmission", "Systems Interactions"),
        ("Concept Explanation", "Questions and Methods", "Argumentation"),
        ("Inheritance and Variation of Traits", "Structure and Function"),
        ("Process of science", "Science and society", "Quantitative reasoning"),
        "Connect sequence, regulation, genome integrity, and phenotype through evidence.",
    ),
    "unit_V": _u(
        ("Information flow, exchange, and storage", "Evolution"),
        ("Quantitative reasoning", "Process of science", "Modeling and simulation"),
        ("Information Storage and Transmission", "Evolution"),
        ("Statistical Tests and Data Analysis", "Representing and Describing Data"),
        ("Inheritance and Variation of Traits", "Natural Selection and Evolution"),
        ("Quantitative reasoning", "Process of science"),
        "Use probability and population reasoning to connect inheritance to evolution.",
    ),
    "unit_VI": _u(
        ("Evolution", "Systems"),
        ("Modeling and simulation", "Quantitative reasoning", "Communication and collaboration"),
        ("Evolution", "Systems Interactions"),
        ("Visual Representations", "Statistical Tests and Data Analysis", "Argumentation"),
        ("Natural Selection and Evolution", "Interdependent Relationships in Ecosystems"),
        ("Modeling and simulation", "Quantitative reasoning", "Communication and collaboration"),
        "Return to variation, evidence, and historical inference across evolutionary scales.",
    ),
    "unit_VII": _u(
        ("Evolution", "Systems", "Structure and function"),
        ("Science and society", "Process of science", "Modeling and simulation"),
        ("Evolution", "Systems Interactions"),
        ("Questions and Methods", "Representing and Describing Data", "Argumentation"),
        ("Structure and Function", "Interdependent Relationships in Ecosystems"),
        ("Science and society", "Process of science", "Modeling and simulation"),
        "Use microbes to integrate evolution, ecology, host response, and public decisions.",
    ),
    "unit_VIII": _u(
        ("Structure and function", "Pathways and transformations of energy and matter", "Systems"),
        ("Interdisciplinary nature of science", "Process of science"),
        ("Energetics", "Systems Interactions"),
        ("Visual Representations", "Questions and Methods", "Argumentation"),
        ("Structure and Function", "Matter and Energy in Organisms and Ecosystems"),
        ("Interdisciplinary nature of science", "Process of science"),
        "Read plant form as an engineered compromise among transport, energy, and reproduction.",
    ),
    "unit_IX": _u(
        ("Structure and function", "Systems"),
        ("Modeling and simulation", "Quantitative reasoning", "Science and society"),
        ("Systems Interactions", "Energetics"),
        ("Visual Representations", "Statistical Tests and Data Analysis", "Argumentation"),
        ("Structure and Function",),
        ("Modeling and simulation", "Quantitative reasoning", "Science and society"),
        "Spiral homeostasis from organ systems to neural, endocrine, and immune decisions.",
    ),
    "unit_X": _u(
        ("Systems", "Evolution", "Pathways and transformations of energy and matter"),
        ("Modeling and simulation", "Science and society", "Communication and collaboration"),
        ("Systems Interactions", "Evolution", "Energetics"),
        ("Representing and Describing Data", "Statistical Tests and Data Analysis", "Argumentation"),
        (
            "Interdependent Relationships in Ecosystems",
            "Matter and Energy in Organisms and Ecosystems",
            "Natural Selection and Evolution",
        ),
        ("Modeling and simulation", "Science and society", "Communication and collaboration"),
        "Use ecological models to connect populations, interactions, matter, climate, and decisions.",
    ),
}


def _unit_key(chapter_id: str) -> str:
    parts = chapter_id.split("_", 2)
    if len(parts) != 3:
        raise ValueError(f"Unexpected chapter id: {chapter_id}")
    return f"{parts[0]}_{parts[1]}"


def _fragment(text: str) -> str:
    return text.strip().rstrip(".")


def _lower_initial(text: str) -> str:
    fragment = _fragment(text)
    return f"{fragment[:1].lower()}{fragment[1:]}"


def _make_alignment(record: object) -> AlignmentRecord:
    chapter_id = getattr(record, "chapter_id")
    defaults = UNIT_ALIGNMENTS[_unit_key(chapter_id)]
    data_skill = getattr(record, "data_skill")
    quantitative_model = getattr(record, "quantitative_model")
    assessment_focus = getattr(record, "assessment_focus")
    transfer_task = getattr(record, "transfer_task")
    return AlignmentRecord(
        chapter_id=chapter_id,
        vision_change_concepts=defaults.vision_change_concepts,
        vision_change_competencies=defaults.vision_change_competencies,
        ap_big_ideas=defaults.ap_big_ideas,
        ap_science_practices=defaults.ap_science_practices,
        ngss_topics=defaults.ngss_topics,
        bioskills=defaults.bioskills,
        spiral_thread=defaults.spiral_thread,
        instructor_move=(
            "Launch from a phenomenon, have students model it with "
            f"{_fragment(quantitative_model)}, then test the model through data."
        ),
        formative_check=(
            f"Ask students to {_lower_initial(data_skill)} and then answer: {_lower_initial(assessment_focus)}."
        ),
        summative_product=transfer_task,
    )


ALIGNMENTS: tuple[AlignmentRecord, ...] = tuple(_make_alignment(record) for record in CURRICULUM)
ALIGNMENTS_BY_ID: Mapping[str, AlignmentRecord] = {record.chapter_id: record for record in ALIGNMENTS}


def by_id(chapter_id: str) -> AlignmentRecord | None:
    """Return alignment metadata for ``chapter_id`` if it exists."""
    return ALIGNMENTS_BY_ID.get(chapter_id)


def require(chapter_id: str) -> AlignmentRecord:
    """Return alignment metadata or raise a clear error for missing IDs."""
    try:
        return ALIGNMENTS_BY_ID[chapter_id]
    except KeyError as exc:
        raise KeyError(f"No alignment record for {chapter_id!r}") from exc


def framework_counts(records: Iterable[AlignmentRecord] = ALIGNMENTS) -> dict[str, dict[str, int]]:
    """Count how often framework labels appear across alignment records."""
    vision_change: Counter[str] = Counter()
    ap_big_ideas: Counter[str] = Counter()
    ap_practices: Counter[str] = Counter()
    ngss_topics: Counter[str] = Counter()
    bioskills: Counter[str] = Counter()
    for record in records:
        vision_change.update(record.vision_change_concepts)
        ap_big_ideas.update(record.ap_big_ideas)
        ap_practices.update(record.ap_science_practices)
        ngss_topics.update(record.ngss_topics)
        bioskills.update(record.bioskills)
    return {
        "vision_change_concepts": dict(vision_change),
        "ap_big_ideas": dict(ap_big_ideas),
        "ap_science_practices": dict(ap_practices),
        "ngss_topics": dict(ngss_topics),
        "bioskills": dict(bioskills),
    }


__all__ = [
    "ALIGNMENTS",
    "ALIGNMENTS_BY_ID",
    "AP_BIOLOGY_BIG_IDEAS",
    "AP_BIOLOGY_PRACTICES",
    "AlignmentRecord",
    "BIOSKILLS_CATEGORIES",
    "NGSS_HS_LS_TOPICS",
    "UnitAlignment",
    "UNIT_ALIGNMENTS",
    "VISION_CHANGE_COMPETENCIES",
    "VISION_CHANGE_CONCEPTS",
    "by_id",
    "framework_counts",
    "require",
]
