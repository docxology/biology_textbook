"""Polymer hierarchy descriptors for the Unit I macromolecules chapter.

Provides a tabulated decomposition of biological polymers into monomer,
polymer, and assembly tiers. The plot draws boxes for each row; the prose
\\cref's the figure when it walks through the hierarchy.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class MacromoleculeTier:
    """One row of the macromolecule hierarchy table."""

    family: str
    monomer: str
    polymer: str
    assembly: str
    example_function: str


MACROMOLECULE_TIERS: tuple[MacromoleculeTier, ...] = (
    MacromoleculeTier(
        family="Proteins",
        monomer="Amino acid",
        polymer="Polypeptide",
        assembly="Folded protein complex",
        example_function="Catalysis, transport, structure",
    ),
    MacromoleculeTier(
        family="Nucleic acids",
        monomer="Nucleotide",
        polymer="Polynucleotide",
        assembly="Double helix or RNP",
        example_function="Information storage and transfer",
    ),
    MacromoleculeTier(
        family="Carbohydrates",
        monomer="Monosaccharide",
        polymer="Polysaccharide",
        assembly="Glycoconjugate or wall",
        example_function="Energy storage, recognition, structure",
    ),
    MacromoleculeTier(
        family="Lipids",
        monomer="Fatty acid / isoprene",
        polymer="Triacylglycerol or phospholipid",
        assembly="Membrane bilayer",
        example_function="Energy, compartmentation, signaling",
    ),
)


def polymer_hierarchy_levels() -> tuple[str, ...]:
    """Return the canonical column labels for the polymer hierarchy figure."""
    return ("Monomer", "Polymer", "Assembly", "Function")
