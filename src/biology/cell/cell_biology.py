"""Cell biology module.

Covers cell types, organelles, membrane biophysics, and transport mechanisms.
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Optional

from infrastructure.core.logging.utils import get_logger

logger = get_logger(__name__)

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------
FARADAY_CONSTANT = 96485.0  # C mol⁻¹
GAS_CONSTANT = 8.314  # J mol⁻¹ K⁻¹
AVOGADRO = 6.022e23  # mol⁻¹
BOLTZMANN = 1.381e-23  # J K⁻¹


# ---------------------------------------------------------------------------
# Data Classes
# ---------------------------------------------------------------------------


@dataclass
class Organelle:
    """Represents an organelle with its key properties."""

    name: str
    present_in_prokaryotes: bool
    present_in_plant_cells: bool
    present_in_animal_cells: bool
    membrane_bound: bool
    function: str

    def summary(self) -> str:
        """Return a one-line summary."""
        domains = []
        if self.present_in_prokaryotes:
            domains.append("prokaryotes")
        if self.present_in_plant_cells:
            domains.append("plants")
        if self.present_in_animal_cells:
            domains.append("animals")
        return f"{self.name}: found in {', '.join(domains)}. {self.function}"


@dataclass
class IonConcentration:
    """Intracellular and extracellular concentrations of an ion (mM)."""

    ion: str
    charge: int  # e.g. +1 for Na⁺, -1 for Cl⁻
    inside_mM: float
    outside_mM: float


@dataclass
class MembraneTransportResult:
    """Result of a membrane transport calculation."""

    ion: str
    equilibrium_potential_mV: float
    direction: str  # "inward" or "outward" from outside perspective
    driving_force_mV: float


# ---------------------------------------------------------------------------
# Organelle Inventory
# ---------------------------------------------------------------------------

ORGANELLES: list[Organelle] = [
    Organelle("Nucleus", False, True, True, True, "Houses DNA; site of transcription"),
    Organelle("Mitochondria", False, True, True, True, "ATP synthesis via oxidative phosphorylation"),
    Organelle("Chloroplast", False, True, False, True, "Photosynthesis; converts light to chemical energy"),
    Organelle("Ribosome", True, True, True, False, "Protein synthesis (translation)"),
    Organelle("Endoplasmic Reticulum", False, True, True, True, "Protein/lipid synthesis and folding"),
    Organelle("Golgi Apparatus", False, True, True, True, "Protein sorting, modification and secretion"),
    Organelle("Lysosome", False, False, True, True, "Intracellular digestion via hydrolytic enzymes"),
    Organelle("Vacuole", False, True, False, True, "Storage; turgor pressure in plants"),
    Organelle(
        "Cell Wall", True, True, False, False, "Structural support; cellulose in plants, peptidoglycan in bacteria"
    ),
    Organelle("Plasma Membrane", True, True, True, False, "Selective permeability; phospholipid bilayer"),
    Organelle("Centriole", False, False, True, True, "Organises mitotic spindle"),
    Organelle("Peroxisome", False, True, True, True, "Oxidative reactions; fatty acid β-oxidation"),
]


def get_organelles_by_cell_type(cell_type: str) -> list[Organelle]:
    """Return organelles present in the specified cell type.

    Args:
        cell_type: One of 'prokaryote', 'plant', 'animal'.

    Returns:
        List of Organelle objects present in that cell type.

    Raises:
        ValueError: If cell_type is not recognised.
    """
    cell_type = cell_type.lower()
    if cell_type == "prokaryote":
        return [o for o in ORGANELLES if o.present_in_prokaryotes]
    elif cell_type == "plant":
        return [o for o in ORGANELLES if o.present_in_plant_cells]
    elif cell_type == "animal":
        return [o for o in ORGANELLES if o.present_in_animal_cells]
    else:
        raise ValueError(f"Unknown cell_type '{cell_type}'. Use 'prokaryote', 'plant', or 'animal'.")


def count_membrane_bound_organelles(organelles: list[Organelle]) -> int:
    """Count membrane-bound organelles in a list.

    Args:
        organelles: List of Organelle objects.

    Returns:
        Number of membrane-bound organelles.
    """
    return sum(1 for o in organelles if o.membrane_bound)


# ---------------------------------------------------------------------------
# Nernst Equation — Equilibrium Potential
# ---------------------------------------------------------------------------


def nernst_potential(
    ion: IonConcentration,
    temperature_K: float = 310.0,
) -> float:
    """Calculate the Nernst equilibrium potential for an ion.

    E = (RT / zF) * ln([X]_out / [X]_in)

    Args:
        ion: IonConcentration with inside/outside concentrations.
        temperature_K: Temperature in Kelvin (default 310 K = 37 °C).

    Returns:
        Equilibrium potential in millivolts (mV).

    Raises:
        ValueError: If concentrations are non-positive or temperature ≤ 0.
    """
    if temperature_K <= 0:
        raise ValueError(f"temperature_K must be positive, got {temperature_K}")
    if ion.inside_mM <= 0 or ion.outside_mM <= 0:
        raise ValueError("Ion concentrations must be positive (non-zero).")
    if ion.charge == 0:
        raise ValueError("Ion charge must be non-zero.")

    ratio = ion.outside_mM / ion.inside_mM
    E_V = (GAS_CONSTANT * temperature_K) / (ion.charge * FARADAY_CONSTANT) * math.log(ratio)
    E_mV = E_V * 1000.0
    logger.debug(f"Nernst potential for {ion.ion}: {E_mV:.2f} mV")
    return E_mV


def goldman_equation(
    ions: list[IonConcentration],
    permeabilities: list[float],
    temperature_K: float = 310.0,
) -> float:
    """Goldman-Hodgkin-Katz equation for resting membrane potential.

    V_m = (RT/F) * ln(
        (sum P_K*[K]_out + sum P_Na*[Na]_out + sum P_Cl*[Cl]_in) /
        (sum P_K*[K]_in  + sum P_Na*[Na]_in  + sum P_Cl*[Cl]_out)
    )

    Simplified: handles monovalent cations (+1) and anions (-1).

    Args:
        ions: List of IonConcentration.
        permeabilities: Relative membrane permeabilities (same order as ions).
        temperature_K: Temperature in Kelvin.

    Returns:
        Membrane potential in mV.

    Raises:
        ValueError: If lists differ in length or denominator is zero.
    """
    if len(ions) != len(permeabilities):
        raise ValueError("ions and permeabilities must have equal length.")
    if temperature_K <= 0:
        raise ValueError("temperature_K must be positive.")

    numerator = 0.0
    denominator = 0.0
    for ion, P in zip(ions, permeabilities):
        if P < 0:
            raise ValueError(f"Permeability for {ion.ion} must be non-negative.")
        if ion.charge > 0:  # cation
            numerator += P * ion.outside_mM
            denominator += P * ion.inside_mM
        else:  # anion
            numerator += P * ion.inside_mM
            denominator += P * ion.outside_mM

    if denominator == 0:
        raise ValueError("Goldman equation denominator is zero; check concentrations.")

    V_m = (GAS_CONSTANT * temperature_K / FARADAY_CONSTANT) * math.log(numerator / denominator)
    V_mV = V_m * 1000.0
    logger.debug(f"Goldman membrane potential: {V_mV:.2f} mV")
    return V_mV


# ---------------------------------------------------------------------------
# Osmosis — van 't Hoff equation
# ---------------------------------------------------------------------------


def osmotic_pressure(
    solute_concentration_M: float,
    temperature_K: float = 310.0,
    solute_count: int = 1,
) -> float:
    """Calculate osmotic pressure using the van 't Hoff equation.

    π = i * C * R * T

    Args:
        solute_concentration_M: Molar concentration (mol L⁻¹).
        temperature_K: Temperature in Kelvin.
        solute_count: van 't Hoff factor i (default 1 for non-electrolytes).

    Returns:
        Osmotic pressure in Pascals (Pa).

    Raises:
        ValueError: If concentration or temperature is non-positive.
    """
    if solute_concentration_M <= 0:
        raise ValueError("solute_concentration_M must be positive.")
    if temperature_K <= 0:
        raise ValueError("temperature_K must be positive.")
    if solute_count < 1:
        raise ValueError("solute_count (van 't Hoff factor) must be ≥ 1.")

    # Convert M → mol/m³: 1 M = 1000 mol/m³
    C_m3 = solute_concentration_M * 1000.0
    pi_Pa = solute_count * C_m3 * GAS_CONSTANT * temperature_K
    logger.debug(f"Osmotic pressure: {pi_Pa:.1f} Pa at {temperature_K} K")
    return pi_Pa


# ---------------------------------------------------------------------------
# Fick's First Law — Simple Diffusion
# ---------------------------------------------------------------------------


def diffusion_flux(
    diffusion_coefficient_m2s: float,
    concentration_gradient_mol_m4: float,
) -> float:
    """Compute diffusion flux via Fick's First Law: J = -D * (dC/dx).

    Args:
        diffusion_coefficient_m2s: D in m² s⁻¹.
        concentration_gradient_mol_m4: dC/dx in mol m⁻⁴ (can be negative).

    Returns:
        Flux J in mol m⁻² s⁻¹.

    Raises:
        ValueError: If diffusion_coefficient is non-positive.
    """
    if diffusion_coefficient_m2s <= 0:
        raise ValueError("diffusion_coefficient_m2s must be positive.")
    flux = -diffusion_coefficient_m2s * concentration_gradient_mol_m4
    logger.debug(f"Diffusion flux: {flux:.4e} mol m⁻² s⁻¹")
    return flux


# ---------------------------------------------------------------------------
# Default Physiological Ion Set
# ---------------------------------------------------------------------------

PHYSIOLOGICAL_IONS: list[IonConcentration] = [
    IonConcentration("K⁺", +1, inside_mM=140.0, outside_mM=5.0),
    IonConcentration("Na⁺", +1, inside_mM=12.0, outside_mM=145.0),
    IonConcentration("Cl⁻", -1, inside_mM=4.0, outside_mM=110.0),
    IonConcentration("Ca²⁺", +2, inside_mM=0.0001, outside_mM=2.5),
]


def _nernst_input_error(ion: IonConcentration) -> str | None:
    if ion.inside_mM <= 0 or ion.outside_mM <= 0:
        return "ion concentrations must be positive"
    if ion.charge == 0:
        return "ion charge must be non-zero"
    return None


def compute_all_nernst_potentials(
    ions: Optional[list[IonConcentration]] = None,
    temperature_K: float = 310.0,
) -> dict[str, float]:
    """Compute Nernst potentials for a list of ions.

    Args:
        ions: List of IonConcentration objects. Defaults to PHYSIOLOGICAL_IONS.
        temperature_K: Temperature in Kelvin.

    Returns:
        Dict mapping ion name to equilibrium potential in mV.
    """
    if ions is None:
        ions = PHYSIOLOGICAL_IONS
    if temperature_K <= 0:
        raise ValueError(f"temperature_K must be positive, got {temperature_K}")
    result = {}
    for ion in ions:
        error = _nernst_input_error(ion)
        if error is not None:
            logger.warning(f"Skipping {ion.ion}: {error}.")
            continue
        result[ion.ion] = nernst_potential(ion, temperature_K)
    return result


# ---------------------------------------------------------------------------
# Receptor-Ligand Binding and Signalling
# ---------------------------------------------------------------------------


def receptor_occupancy(
    ligand_concentration: float,
    kd: float,
) -> float:
    """Calculate fractional receptor occupancy.

    θ = [L] / ([L] + Kd)

    Args:
        ligand_concentration: Free ligand concentration.
        kd: Dissociation constant (same units as ligand_concentration).

    Returns:
        Fractional occupancy (0.0 to 1.0).

    Raises:
        ValueError: If ligand_concentration is negative or kd is non-positive.
    """
    if ligand_concentration < 0 or kd <= 0:
        raise ValueError("Ligand concentration must be non-negative and Kd must be positive.")
    return ligand_concentration / (ligand_concentration + kd)


def hill_equation(
    ligand_concentration: float,
    kd: float,
    hill_coefficient: float,
) -> float:
    """Calculate fractional occupancy with cooperative binding (Hill equation).

    θ = [L]ⁿ / (Kdⁿ + [L]ⁿ)

    Args:
        ligand_concentration: Free ligand concentration.
        kd: Dissociation constant (same units as ligand_concentration).
        hill_coefficient: Hill coefficient (n).

    Returns:
        Fractional occupancy (0.0 to 1.0).

    Raises:
        ValueError: If ligand_concentration is negative or kd is non-positive.
    """
    if ligand_concentration < 0 or kd <= 0:
        raise ValueError("Ligand concentration must be non-negative and Kd must be positive.")
    if ligand_concentration == 0:
        return 0.0

    l_n = math.pow(ligand_concentration, hill_coefficient)
    k_n = math.pow(kd, hill_coefficient)
    return l_n / (k_n + l_n)


def signal_amplification(amplification_steps: list[float]) -> float:
    """Calculate total signal amplification through a cascade.

    G_total = ∏ A_i

    Args:
        amplification_steps: List of amplification factors for each step.

    Returns:
        Total amplification factor.
    """
    total = 1.0
    for step in amplification_steps:
        total *= step
    return total
