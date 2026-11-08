"""Cell biology module.

Covers cell types, organelles, membrane biophysics, and transport mechanisms.
"""

from __future__ import annotations

import math
from dataclasses import dataclass

from biology.constants import FARADAY_CONSTANT, GAS_CONSTANT
from textbook_logging import get_logger

logger = get_logger(__name__)

# Re-export constants for backward-compatible imports from this module.
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
    # OpenStax Biology 2e §4.3, centrosome: nine microtubule triplets, not a membrane.
    # https://openstax.org/books/biology-2e/pages/4-3-eukaryotic-cells
    Organelle("Centriole", False, False, True, False, "Non-membranous microtubule barrel; organizes spindle"),
    Organelle("Peroxisome", False, True, True, True, "Oxidative reactions; fatty acid β-oxidation"),
]


def get_organelles_by_cell_type(cell_type: str) -> list[Organelle]:
    """Return organelles present in the specified cell type.

    Args:
        cell_type: One of 'prokaryote', 'plant', 'animal'.

    Returns:
        List of Organelle objects present in that cell type.

    Raises:
        ValueError: If cell_type is not recognized.
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
    if not math.isfinite(temperature_K) or temperature_K <= 0:
        raise ValueError("temperature_K must be finite and positive.")
    if any(not math.isfinite(c) or c <= 0 for c in (ion.inside_mM, ion.outside_mM)):
        raise ValueError("Ion concentrations must be finite and positive.")
    if not math.isfinite(ion.charge) or ion.charge == 0:
        raise ValueError("Ion charge must be finite and non-zero.")

    log_ratio = math.log(ion.outside_mM) - math.log(ion.inside_mM)
    E_V = (GAS_CONSTANT * temperature_K / FARADAY_CONSTANT / ion.charge) * log_ratio
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
    if not math.isfinite(temperature_K) or temperature_K <= 0:
        raise ValueError("temperature_K must be finite and positive.")

    numerator_logs: list[float] = []
    denominator_logs: list[float] = []
    for ion, P in zip(ions, permeabilities):
        if ion.charge not in (-1, 1):
            raise ValueError("Simplified Goldman equation supports only charges -1 and +1.")
        if not math.isfinite(P) or P < 0:
            raise ValueError("Permeabilities must be finite and non-negative.")
        if any(not math.isfinite(c) or c < 0 for c in (ion.inside_mM, ion.outside_mM)):
            raise ValueError("Ion concentrations must be finite and non-negative.")
        top, bottom = ((ion.outside_mM, ion.inside_mM) if ion.charge == 1
                       else (ion.inside_mM, ion.outside_mM))
        if P > 0:
            if top > 0:
                numerator_logs.append(math.log(P) + math.log(top))
            if bottom > 0:
                denominator_logs.append(math.log(P) + math.log(bottom))
    if not numerator_logs or not denominator_logs:
        raise ValueError("Goldman numerator and denominator must both be positive.")
    # Log-sum-exp preserves the quotient without overflowing P*concentration.
    top_max, bottom_max = max(numerator_logs), max(denominator_logs)
    log_top = top_max + math.log(math.fsum(math.exp(x - top_max) for x in numerator_logs))
    log_bottom = bottom_max + math.log(math.fsum(math.exp(x - bottom_max) for x in denominator_logs))
    V_m = (GAS_CONSTANT * temperature_K / FARADAY_CONSTANT) * (log_top - log_bottom)
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
    if not math.isfinite(solute_concentration_M) or solute_concentration_M <= 0:
        raise ValueError("solute_concentration_M must be finite and positive.")
    if not math.isfinite(temperature_K) or temperature_K <= 0:
        raise ValueError("temperature_K must be finite and positive.")
    if not math.isfinite(solute_count) or solute_count < 1:
        raise ValueError("solute_count (van 't Hoff factor) must be finite and ≥ 1.")

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
    if not math.isfinite(diffusion_coefficient_m2s) or diffusion_coefficient_m2s <= 0:
        raise ValueError("diffusion_coefficient_m2s must be finite and positive.")
    if not math.isfinite(concentration_gradient_mol_m4):
        raise ValueError("concentration gradient must be finite.")
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
    if any(not math.isfinite(c) or c <= 0 for c in (ion.inside_mM, ion.outside_mM)):
        return "ion concentrations must be finite and positive"
    if not math.isfinite(ion.charge) or ion.charge == 0:
        return "ion charge must be finite and non-zero"
    return None


def compute_all_nernst_potentials(
    ions: list[IonConcentration] | None = None,
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
    if not math.isfinite(temperature_K) or temperature_K <= 0:
        raise ValueError("temperature_K must be finite and positive.")
    result = {}
    for ion in ions:
        error = _nernst_input_error(ion)
        if error is not None:
            logger.warning(f"Skipping {ion.ion}: {error}.")
            continue
        result[ion.ion] = nernst_potential(ion, temperature_K)
    return result


# ---------------------------------------------------------------------------
# Receptor-Ligand Binding and Signaling
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
    if not math.isfinite(ligand_concentration) or not math.isfinite(kd) or ligand_concentration < 0 or kd <= 0:
        raise ValueError("Ligand concentration must be finite/non-negative and Kd finite/positive.")
    if ligand_concentration <= kd:
        ratio = ligand_concentration / kd
        return ratio / (1.0 + ratio)
    return 1.0 / (1.0 + kd / ligand_concentration)


def hill_equation(
    ligand_concentration: float,
    kd: float,
    hill_coefficient: float,
) -> float:
    """Evaluate a phenomenological Hill fractional-occupancy model.

    θ = [L]ⁿ / (K_halfⁿ + [L]ⁿ), where ``kd`` supplies K_half.

    Args:
        ligand_concentration: Free ligand concentration.
        kd: Half-occupancy concentration (same units as ligand_concentration).
            It is not generally a microscopic dissociation constant; the simple
            one-site binding interpretation applies when hill_coefficient is 1.
        hill_coefficient: Hill coefficient (n).

    Returns:
        Fractional occupancy (0.0 to 1.0).

    Raises:
        ValueError: If inputs are non-finite, ligand_concentration is negative,
            or kd or hill_coefficient is non-positive.
    """
    if not math.isfinite(ligand_concentration) or not math.isfinite(kd) or ligand_concentration < 0 or kd <= 0:
        raise ValueError("Ligand concentration must be finite/non-negative and Kd finite/positive.")
    if not math.isfinite(hill_coefficient) or hill_coefficient <= 0:
        raise ValueError("hill_coefficient must be finite and positive.")
    if ligand_concentration == 0:
        return 0.0
    log_ratio = hill_coefficient * (math.log(ligand_concentration) - math.log(kd))
    if log_ratio >= 0:
        return 1.0 / (1.0 + math.exp(-log_ratio))
    ratio = math.exp(log_ratio)
    return ratio / (1.0 + ratio)


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


# ---------------------------------------------------------------------------
# Organelle Size Reference Data (representative linear dimensions in micrometres)
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class OrganelleSize:
    """Representative linear dimension for a cellular structure.

    Rows span macromolecular structures, organelles, and whole cells from
    multiple taxa. Values are diameters unless the name specifies length;
    ``diameter_um`` stores either dimension as an order-of-magnitude landmark,
    not a precise measurement or a universal size for that structure.
    """

    name: str
    diameter_um: float
    category: str  # e.g. "prokaryotic cell", "organelle", "macromolecule"


ORGANELLE_SIZES: tuple[OrganelleSize, ...] = (
    OrganelleSize("Ribosome", 0.025, "macromolecular"),
    OrganelleSize("Microtubule (diameter)", 0.025, "macromolecular"),
    OrganelleSize("Centriole (diameter)", 0.20, "organelle"),
    OrganelleSize("Lysosome", 0.50, "organelle"),
    OrganelleSize("Peroxisome", 0.60, "organelle"),
    OrganelleSize("Mitochondrion (length)", 2.0, "organelle"),
    OrganelleSize("Chloroplast (length)", 6.0, "organelle"),
    OrganelleSize("Nucleus", 6.0, "organelle"),
    OrganelleSize("E. coli cell (length)", 2.0, "prokaryotic cell"),
    OrganelleSize("Animal cell (typical)", 20.0, "eukaryotic cell"),
    OrganelleSize("Plant cell (typical)", 50.0, "eukaryotic cell"),
)


def organelle_size_table() -> tuple[OrganelleSize, ...]:
    """Return the canonical organelle-size reference table.

    Returns:
        Tuple of ``OrganelleSize`` rows sorted in increasing linear dimension so the
        log-scale figure renders monotonically.
    """
    return tuple(sorted(ORGANELLE_SIZES, key=lambda row: row.diameter_um))
