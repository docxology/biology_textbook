"""Curated milestone timeline used by the Unit 0 history chapter.

Each entry is a year-anchored claim that the chapter prose already names. The
``BIOLOGY_MILESTONES`` table is the single source of truth for the matching
matplotlib figure and for the chapter's narrative, so prose and figure cannot
drift apart.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class BiologyMilestone:
    """One milestone in the history of biology."""

    year: int
    event: str
    figure: str
    era: str


BIOLOGY_MILESTONES: tuple[BiologyMilestone, ...] = (
    BiologyMilestone(1665, "Cells named in cork sections", "Hooke", "early modern"),
    BiologyMilestone(1735, "Binomial classification of life", "Linnaeus", "early modern"),
    BiologyMilestone(1838, "Cell theory of multicellular life", "Schleiden & Schwann", "nineteenth century"),
    BiologyMilestone(1859, "Natural selection published", "Darwin", "nineteenth century"),
    BiologyMilestone(1866, "Laws of particulate inheritance", "Mendel", "nineteenth century"),
    BiologyMilestone(1928, "Penicillin antibiotic discovered", "Fleming", "early twentieth century"),
    BiologyMilestone(1944, "DNA carries genetic information", "Avery, MacLeod, McCarty", "mid twentieth century"),
    BiologyMilestone(1953, "DNA double-helix structure", "Watson, Crick, Franklin, Wilkins", "mid twentieth century"),
    BiologyMilestone(1972, "Endosymbiotic theory of eukaryotes", "Margulis", "late twentieth century"),
    BiologyMilestone(1983, "PCR amplification of DNA", "Mullis", "late twentieth century"),
    BiologyMilestone(2003, "Human genome reference draft completed", "HGP consortium", "early twenty-first century"),
    BiologyMilestone(2012, "CRISPR-Cas9 programmable editing", "Doudna & Charpentier", "early twenty-first century"),
    BiologyMilestone(2020, "AlphaFold structure prediction", "DeepMind", "early twenty-first century"),
)


def milestones_by_era() -> dict[str, list[BiologyMilestone]]:
    """Group milestones into chronological eras for the figure legend.

    Returns:
        Ordered mapping from era label to milestones in that era, preserving
        insertion order from ``BIOLOGY_MILESTONES``.
    """
    grouped: dict[str, list[BiologyMilestone]] = {}
    for milestone in BIOLOGY_MILESTONES:
        grouped.setdefault(milestone.era, []).append(milestone)
    return grouped
