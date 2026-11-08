"""Molecular building blocks, polymers and nonpolymer lipid assemblies."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class MacromoleculeTier:
    """One row of the macromolecule hierarchy table."""

    family: str
    building_blocks: str
    molecule: str
    assembly: str
    example_function: str
    is_polymer: bool


MACROMOLECULE_TIERS: tuple[MacromoleculeTier, ...] = (
    MacromoleculeTier(
        family="Proteins",
        building_blocks="Amino acid",
        molecule="Polypeptide",
        assembly="Folded protein complex",
        example_function="Catalysis, transport, structure",
        is_polymer=True,
    ),
    MacromoleculeTier(
        family="Nucleic acids",
        building_blocks="Nucleotide",
        molecule="Polynucleotide",
        assembly="Double helix or RNP",
        example_function="Information storage and transfer",
        is_polymer=True,
    ),
    MacromoleculeTier(
        family="Carbohydrates",
        building_blocks="Monosaccharide",
        molecule="Polysaccharide",
        assembly="Glycoconjugate or wall",
        example_function="Energy storage, recognition, structure",
        is_polymer=True,
    ),
    # Representative glycerophospholipid, not a repeating-unit polymer.
    # https://openstax.org/books/biology-2e/pages/3-3-lipids
    MacromoleculeTier(
        family="Lipids",
        building_blocks="Glycerol, fatty acids,\nphosphate + head group",
        molecule="Phospholipid\n(nonpolymer)",
        assembly="Self-assembled bilayer",
        example_function="Compartmentation, signaling",
        is_polymer=False,
    ),
)


def polymer_hierarchy_levels() -> tuple[str, ...]:
    """Column labels allowing both polymer and nonpolymer molecular paths."""
    return ("Building blocks", "Molecule", "Assembly", "Function")
