"""Chapter metadata — difficulty, duration, prerequisites.

Defines one :class:`ChapterMeta` record per chapter (Unit 0 + Units I–X). The
data is hand-tuned to reflect the cognitive and mathematical load of each
chapter, based on: line count, math density, number of named mechanisms, and
the instructor's judgement of how well a first-year biology student will
navigate it.

Difficulty scale (applied uniformly):

* Level 1/3 — foundational; accessible to any first-year student.
* Level 2/3 — intermediate; assumes earlier chapters; mathematical detail.
* Level 3/3 — advanced; substantial quantitative content or conceptual leap.

Duration is an estimated *reading* time (minutes), not lecture time. For
instructor use we also supply a suggested *lecture* time.

This module is imported by:

* :mod:`scripts.insert_chapter_metadata` — writes a one-line badge row at
  the top of each chapter file.
* :mod:`scripts.generate_course_planning_grid` — produces the table inserted
  into ``manuscript/front_matter.md``.
* :mod:`tests.test_metadata_completeness` — asserts every chapter in
  ``config.yaml`` has a corresponding :class:`ChapterMeta` record.
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True)
class ChapterMeta:
    """Metadata for one chapter, lab, or question bank."""

    chapter_id: str  # e.g. "unit_I_water_and_life"
    number: int  # sequential chapter number (1..N); 0 for Unit 0
    unit: str  # "0" | "I" | … | "X"
    difficulty: int  # 1, 2, or 3
    reading_time_min: int  # estimated student reading time
    lecture_time_min: int  # suggested single-lecture allotment
    prerequisites: tuple[str, ...] = field(default_factory=tuple)

    @property
    def star_badge(self) -> str:
        """Return the legacy star-rating string for compatibility tests.

        Examples:
            difficulty=1 -> '★☆☆'
            difficulty=2 -> '★★☆'
            difficulty=3 -> '★★★'
        """
        return "★" * self.difficulty + "☆" * (3 - self.difficulty)

    @property
    def difficulty_label(self) -> str:
        """Return a PDF-safe, screen-reader-friendly difficulty label."""
        return f"Level {self.difficulty}/3"


# ---------------------------------------------------------------------------
# Chapter records — order follows config.yaml
# ---------------------------------------------------------------------------

CHAPTERS: list[ChapterMeta] = [
    # Unit 0 — Systems Science
    ChapterMeta("unit_0_systems_science", 0, "0", 2, 35, 50),
    ChapterMeta("unit_0_complex_adaptive_systems", 0, "0", 2, 35, 50, ("unit_0_systems_science",)),
    ChapterMeta(
        "unit_0_active_inference", 0, "0", 3, 45, 75, ("unit_0_systems_science", "unit_0_complex_adaptive_systems")
    ),
    ChapterMeta(
        "unit_0_history_philosophy_biology",
        0,
        "0",
        2,
        80,
        100,
        ("unit_0_systems_science", "unit_0_complex_adaptive_systems", "unit_0_active_inference"),
    ),
    # Unit I — Chemistry of Life
    ChapterMeta("unit_I_atoms_molecules", 1, "I", 1, 40, 50),
    ChapterMeta("unit_I_water_and_life", 2, "I", 1, 40, 50, ("unit_I_atoms_molecules",)),
    ChapterMeta("unit_I_macromolecules", 3, "I", 2, 55, 75, ("unit_I_atoms_molecules", "unit_I_water_and_life")),
    ChapterMeta("unit_I_enzymes_and_kinetics", 4, "I", 3, 60, 75, ("unit_I_macromolecules",)),
    # Unit II — Cell
    ChapterMeta("unit_II_cell_theory", 5, "II", 1, 45, 50, ("unit_I_macromolecules",)),
    ChapterMeta("unit_II_cell_structure", 6, "II", 2, 50, 75, ("unit_II_cell_theory",)),
    ChapterMeta("unit_II_membrane_transport", 7, "II", 2, 50, 75, ("unit_II_cell_structure", "unit_I_water_and_life")),
    ChapterMeta(
        "unit_II_cell_signaling", 8, "II", 3, 55, 75, ("unit_II_membrane_transport", "unit_I_enzymes_and_kinetics")
    ),
    # Unit III — Energy & Metabolism
    ChapterMeta(
        "unit_III_bioenergetics_and_respiration",
        9,
        "III",
        3,
        60,
        100,
        ("unit_II_cell_structure", "unit_I_enzymes_and_kinetics"),
    ),
    ChapterMeta("unit_III_photosynthesis", 10, "III", 2, 55, 75, ("unit_III_bioenergetics_and_respiration",)),
    ChapterMeta(
        "unit_III_metabolic_integration",
        11,
        "III",
        3,
        60,
        100,
        ("unit_III_bioenergetics_and_respiration", "unit_III_photosynthesis"),
    ),
    # Unit IV — Molecular Genetics
    ChapterMeta(
        "unit_IV_dna_replication_and_cell_cycle",
        12,
        "IV",
        2,
        55,
        75,
        ("unit_I_macromolecules", "unit_II_cell_structure"),
    ),
    ChapterMeta("unit_IV_gene_expression", 13, "IV", 2, 60, 100, ("unit_IV_dna_replication_and_cell_cycle",)),
    ChapterMeta("unit_IV_mutations_and_genomics", 14, "IV", 2, 55, 75, ("unit_IV_gene_expression",)),
    ChapterMeta(
        "unit_IV_chromatin_and_epigenetic_mechanisms", 15, "IV", 3, 28, 40, ("unit_IV_gene_expression",)
    ),
    ChapterMeta(
        "unit_IV_epigenetic_inheritance_and_disease",
        16,
        "IV",
        3,
        28,
        40,
        ("unit_IV_chromatin_and_epigenetic_mechanisms",),
    ),
    # Unit V — Classical Genetics
    ChapterMeta(
        "unit_V_mendelian_principles", 17, "V", 2, 35, 55, ("unit_IV_dna_replication_and_cell_cycle",)
    ),
    ChapterMeta(
        "unit_V_mendelian_extensions_and_human_genetics",
        18,
        "V",
        2,
        35,
        55,
        ("unit_V_mendelian_principles",),
    ),
    ChapterMeta("unit_V_chromosomal_inheritance", 19, "V", 2, 60, 75, ("unit_V_mendelian_principles",)),
    ChapterMeta(
        "unit_V_population_genetics",
        20,
        "V",
        3,
        75,
        100,
        ("unit_V_mendelian_principles", "unit_V_chromosomal_inheritance"),
    ),
    # Unit VI — Evolution
    ChapterMeta("unit_VI_evolution_and_selection", 21, "VI", 2, 60, 75, ("unit_V_population_genetics",)),
    ChapterMeta("unit_VI_genetic_drift_and_speciation", 22, "VI", 3, 60, 75, ("unit_VI_evolution_and_selection",)),
    ChapterMeta("unit_VI_phylogenetics", 23, "VI", 3, 60, 100, ("unit_VI_genetic_drift_and_speciation",)),
    # Unit VII — Microbiology
    ChapterMeta("unit_VII_bacteria_archaea_viruses", 24, "VII", 2, 65, 75, ("unit_II_cell_structure",)),
    ChapterMeta("unit_VII_microbial_ecology", 25, "VII", 2, 60, 75, ("unit_VII_bacteria_archaea_viruses",)),
    ChapterMeta("unit_VII_host_immunity_and_vaccines", 26, "VII", 2, 30, 40, ("unit_VII_bacteria_archaea_viruses",)),
    ChapterMeta(
        "unit_VII_antimicrobial_resistance_and_epidemiology",
        27,
        "VII",
        2,
        35,
        45,
        ("unit_VII_host_immunity_and_vaccines",),
    ),
    # Unit VIII — Botany
    ChapterMeta("unit_VIII_plant_structure_and_water", 28, "VIII", 2, 55, 75, ("unit_II_membrane_transport",)),
    ChapterMeta("unit_VIII_plant_reproduction", 29, "VIII", 2, 55, 75, ("unit_VIII_plant_structure_and_water",)),
    ChapterMeta("unit_VIII_plant_responses", 30, "VIII", 2, 55, 75, ("unit_VIII_plant_reproduction",)),
    # Unit IX — Zoology / Physiology
    ChapterMeta(
        "unit_IX_circulation_respiration_homeostasis",
        31,
        "IX",
        3,
        60,
        100,
        ("unit_II_membrane_transport", "unit_III_bioenergetics_and_respiration"),
    ),
    ChapterMeta("unit_IX_nervous_system", 32, "IX", 3, 55, 75, ("unit_IX_circulation_respiration_homeostasis",)),
    ChapterMeta("unit_IX_action_potential_synapses", 33, "IX", 3, 55, 100, ("unit_IX_nervous_system",)),
    ChapterMeta(
        "unit_IX_endocrine_signaling", 34, "IX", 2, 30, 40, ("unit_IX_circulation_respiration_homeostasis",)
    ),
    ChapterMeta(
        "unit_IX_immune_system_defense", 35, "IX", 2, 30, 40, ("unit_IX_endocrine_signaling",)
    ),
    # Unit X — Ecology
    ChapterMeta("unit_X_population_ecology", 36, "X", 3, 75, 100, ("unit_V_population_genetics",)),
    ChapterMeta("unit_X_community_interactions", 37, "X", 2, 45, 55, ("unit_X_population_ecology",)),
    ChapterMeta(
        "unit_X_biodiversity_and_food_webs", 38, "X", 2, 40, 50, ("unit_X_community_interactions",)
    ),
    ChapterMeta(
        "unit_X_ecosystem_ecology",
        39,
        "X",
        2,
        65,
        75,
        ("unit_X_community_interactions", "unit_X_biodiversity_and_food_webs", "unit_III_photosynthesis"),
    ),
    ChapterMeta("unit_X_biomes_and_conservation", 40, "X", 2, 70, 75, ("unit_X_ecosystem_ecology",)),
]


CHAPTERS_BY_ID: dict[str, ChapterMeta] = {chapter.chapter_id: chapter for chapter in CHAPTERS}


# ---------------------------------------------------------------------------
# Lookup helpers
# ---------------------------------------------------------------------------


def by_id(chapter_id: str) -> ChapterMeta | None:
    """Look up a chapter's metadata by its unique ``chapter_id``.

    Args:
        chapter_id: The ID string defined in ``ChapterMeta.chapter_id``
            (e.g. ``unit_I_water_and_life``).

    Returns:
        The matching :class:`ChapterMeta`, or ``None`` if no chapter has that ID.
    """
    return CHAPTERS_BY_ID.get(chapter_id)


def by_unit(unit: str) -> list[ChapterMeta]:
    """Return all chapters belonging to a given unit.

    Args:
        unit: The unit tag (e.g. ``unit_I``, ``unit_0``).

    Returns:
        List of :class:`ChapterMeta` objects in that unit, in definition order.
    """
    return [c for c in CHAPTERS if c.unit == unit]


__all__ = ["ChapterMeta", "CHAPTERS", "CHAPTERS_BY_ID", "by_id", "by_unit"]
