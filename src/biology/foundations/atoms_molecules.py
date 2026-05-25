"""Atomic and bond-energy reference data for Unit I (atoms and molecules).

The Pauling electronegativity and biological bond-energy tables drive the
matplotlib figure that opens the chapter. Both are public-domain reference
values; we list the canonical biological subset only so the figure stays
readable.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class AtomElectronegativity:
    """Pauling electronegativity for a biologically common element."""

    symbol: str
    name: str
    pauling: float


@dataclass(frozen=True)
class BondEnergy:
    """Average bond dissociation energy in kJ/mol."""

    bond: str
    energy_kJ_per_mol: float
    bond_class: str  # "covalent" or "noncovalent"


ATOM_ELECTRONEGATIVITIES: tuple[AtomElectronegativity, ...] = (
    AtomElectronegativity("H", "Hydrogen", 2.20),
    AtomElectronegativity("C", "Carbon", 2.55),
    AtomElectronegativity("N", "Nitrogen", 3.04),
    AtomElectronegativity("O", "Oxygen", 3.44),
    AtomElectronegativity("P", "Phosphorus", 2.19),
    AtomElectronegativity("S", "Sulfur", 2.58),
    AtomElectronegativity("Na", "Sodium", 0.93),
    AtomElectronegativity("K", "Potassium", 0.82),
    AtomElectronegativity("Cl", "Chlorine", 3.16),
    AtomElectronegativity("Ca", "Calcium", 1.00),
)


BIOLOGICAL_BOND_ENERGIES: tuple[BondEnergy, ...] = (
    BondEnergy("C-C", 347.0, "covalent"),
    BondEnergy("C-H", 413.0, "covalent"),
    BondEnergy("C-O", 358.0, "covalent"),
    BondEnergy("C=O", 745.0, "covalent"),
    BondEnergy("O-H", 467.0, "covalent"),
    BondEnergy("N-H", 391.0, "covalent"),
    BondEnergy("P-O", 335.0, "covalent"),
    BondEnergy("Hydrogen bond (O-H..O)", 21.0, "noncovalent"),
    BondEnergy("Van der Waals", 4.0, "noncovalent"),
    BondEnergy("Ionic (Na-Cl in water)", 12.5, "noncovalent"),
)


def electronegativity_difference(
    symbol_a: str,
    symbol_b: str,
    *,
    table: tuple[AtomElectronegativity, ...] = ATOM_ELECTRONEGATIVITIES,
) -> float:
    """Return the unsigned Pauling electronegativity difference for two atoms.

    Args:
        symbol_a: First atomic symbol (case-sensitive).
        symbol_b: Second atomic symbol (case-sensitive).
        table: Lookup table (defaults to the canonical biological set).

    Returns:
        Non-negative electronegativity difference.

    Raises:
        KeyError: If either symbol is not in the table.
    """
    index = {atom.symbol: atom.pauling for atom in table}
    if symbol_a not in index:
        raise KeyError(f"unknown electronegativity symbol: {symbol_a}")
    if symbol_b not in index:
        raise KeyError(f"unknown electronegativity symbol: {symbol_b}")
    return abs(index[symbol_a] - index[symbol_b])


def bond_polarity_class(
    symbol_a: str,
    symbol_b: str,
    *,
    table: tuple[AtomElectronegativity, ...] = ATOM_ELECTRONEGATIVITIES,
) -> str:
    """Classify a bond as nonpolar, polar, or ionic.

    Pauling-style thresholds used in the chapter prose:

    - Difference < 0.5: nonpolar covalent
    - 0.5 <= Difference < 1.7: polar covalent
    - Difference >= 1.7: ionic

    Args:
        symbol_a: First atomic symbol.
        symbol_b: Second atomic symbol.
        table: Lookup table.

    Returns:
        One of ``"nonpolar covalent"``, ``"polar covalent"``, ``"ionic"``.

    Raises:
        KeyError: If either symbol is not present in ``table``.
    """
    delta = electronegativity_difference(symbol_a, symbol_b, table=table)
    if delta < 0.5:
        return "nonpolar covalent"
    if delta < 1.7:
        return "polar covalent"
    return "ionic"
