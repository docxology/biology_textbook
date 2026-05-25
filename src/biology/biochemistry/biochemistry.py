"""Biochemistry module.

Covers enzyme kinetics (Michaelis-Menten, inhibition), metabolic pathways
(glycolysis, Krebs cycle, electron transport), and thermodynamics of reactions.
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Optional

from textbook_logging import get_logger

from biology.constants import GAS_CONSTANT

logger = get_logger(__name__)

# ---------------------------------------------------------------------------
# Data Classes
# ---------------------------------------------------------------------------


@dataclass
class EnzymeKineticsResult:
    """Michaelis-Menten enzyme kinetics result."""

    substrate_concentration: float  # [S] in µM
    reaction_rate: float  # v in µmol min⁻¹
    Vmax: float
    Km: float
    efficiency: float  # v / Vmax


@dataclass
class MetabolicPathwayStep:
    """A step in a metabolic pathway."""

    name: str
    enzyme: str
    reactants: list[str]
    products: list[str]
    delta_G_prime_kJ: float  # Standard free energy change (kJ mol⁻¹)
    atp_yield: int = 0  # Net ATP produced (negative = consumed)
    nadh_yield: int = 0
    fadh2_yield: int = 0


@dataclass
class GlycolysisResult:
    """Summary of glycolysis energetics."""

    net_atp: int
    net_nadh: int
    steps: list[MetabolicPathwayStep]
    total_delta_G_kJ: float


# ---------------------------------------------------------------------------
# Michaelis-Menten Kinetics
# ---------------------------------------------------------------------------


def michaelis_menten(
    substrate_conc: float,
    Vmax: float,
    Km: float,
) -> EnzymeKineticsResult:
    """Compute reaction rate using the Michaelis-Menten equation.

    v = Vmax * [S] / (Km + [S])

    Args:
        substrate_conc: Substrate concentration [S] (µM).
        Vmax: Maximum reaction rate (µmol min⁻¹).
        Km: Michaelis constant (µM).

    Returns:
        EnzymeKineticsResult with rate and efficiency.

    Raises:
        ValueError: If any parameter is non-positive.
    """
    if substrate_conc < 0:
        raise ValueError("substrate_conc must be non-negative.")
    if Vmax <= 0:
        raise ValueError("Vmax must be positive.")
    if Km <= 0:
        raise ValueError("Km must be positive.")

    v = Vmax * substrate_conc / (Km + substrate_conc)
    efficiency = v / Vmax
    logger.debug(f"MM kinetics: [S]={substrate_conc}, v={v:.4f}, η={efficiency:.4f}")
    return EnzymeKineticsResult(
        substrate_concentration=substrate_conc,
        reaction_rate=v,
        Vmax=Vmax,
        Km=Km,
        efficiency=efficiency,
    )


def competitive_inhibition(
    substrate_conc: float,
    Vmax: float,
    Km: float,
    inhibitor_conc: float,
    Ki: float,
) -> EnzymeKineticsResult:
    """Michaelis-Menten with competitive inhibition.

    v = Vmax * [S] / (α*Km + [S]),  α = 1 + [I]/Ki

    Args:
        substrate_conc: [S] in µM.
        Vmax: Maximum rate (µmol min⁻¹).
        Km: Michaelis constant (µM).
        inhibitor_conc: Inhibitor concentration [I] (µM).
        Ki: Inhibition constant (µM).

    Returns:
        EnzymeKineticsResult under competitive inhibition.

    Raises:
        ValueError: If Ki ≤ 0 or inhibitor_conc < 0.
    """
    if Ki <= 0:
        raise ValueError("Ki must be positive.")
    if inhibitor_conc < 0:
        raise ValueError("inhibitor_conc must be non-negative.")
    alpha = 1.0 + inhibitor_conc / Ki
    apparent_Km = alpha * Km
    return michaelis_menten(substrate_conc, Vmax, apparent_Km)


def enzyme_rate_curve(
    Vmax: float,
    Km: float,
    n_points: int = 50,
    max_conc: Optional[float] = None,
) -> list[EnzymeKineticsResult]:
    """Generate a full Michaelis-Menten curve across [S] range.

    Args:
        Vmax: Maximum reaction rate.
        Km: Michaelis constant.
        n_points: Number of data points.
        max_conc: Maximum substrate concentration (default 10*Km).

    Returns:
        List of EnzymeKineticsResult sorted by [S].
    """
    if max_conc is None:
        max_conc = 10.0 * Km
    if n_points <= 0:
        raise ValueError("n_points must be positive.")
    step = max_conc / n_points
    return [michaelis_menten(i * step, Vmax, Km) for i in range(n_points + 1)]


# ---------------------------------------------------------------------------
# Thermodynamics
# ---------------------------------------------------------------------------


def reaction_free_energy(
    delta_G_standard_kJ: float,
    product_conc: float,
    reactant_conc: float,
    temperature_K: float = 310.0,
) -> float:
    """Compute ΔG using: ΔG = ΔG° + RT ln(Q).

    Args:
        delta_G_standard_kJ: Standard free energy change ΔG°' (kJ mol⁻¹).
        product_conc: Product concentration (M).
        reactant_conc: Reactant concentration (M).
        temperature_K: Temperature in Kelvin.

    Returns:
        ΔG in kJ mol⁻¹.

    Raises:
        ValueError: If concentrations are non-positive.
    """
    if product_conc <= 0 or reactant_conc <= 0:
        raise ValueError("Concentrations must be positive.")
    if temperature_K <= 0:
        raise ValueError("Temperature must be positive.")
    Q = product_conc / reactant_conc
    delta_G_standard_J = delta_G_standard_kJ * 1000.0
    delta_G_J = delta_G_standard_J + GAS_CONSTANT * temperature_K * math.log(Q)
    return delta_G_J / 1000.0


def atp_free_energy(
    atp_conc_mM: float = 3.0,
    adp_conc_mM: float = 1.0,
    pi_conc_mM: float = 10.0,
    temperature_K: float = 310.0,
) -> float:
    """Compute free energy of ATP hydrolysis in cellular conditions.

    ΔG°' = -30.5 kJ/mol; adjusted by Q = [ADP][Pi]/[ATP].

    Args:
        atp_conc_mM: ATP concentration (mM).
        adp_conc_mM: ADP concentration (mM).
        pi_conc_mM: Inorganic phosphate concentration (mM).
        temperature_K: Temperature in Kelvin.

    Returns:
        Actual ΔG of ATP hydrolysis (kJ mol⁻¹), typically -50 to -60 kJ mol⁻¹.
    """
    delta_G0_prime = -30.5  # kJ/mol
    # Convert mM to M for Q calculation
    Q = (adp_conc_mM * pi_conc_mM * 1e-6) / (atp_conc_mM * 1e-3)
    delta_G = delta_G0_prime + (GAS_CONSTANT * temperature_K / 1000.0) * math.log(Q)
    logger.debug(f"ATP ΔG = {delta_G:.2f} kJ/mol")
    return delta_G


# ---------------------------------------------------------------------------
# Glycolysis Summary
# ---------------------------------------------------------------------------

GLYCOLYSIS_STEPS: list[MetabolicPathwayStep] = [
    MetabolicPathwayStep(
        "Hexokinase", "Hexokinase", ["Glucose", "ATP"], ["Glucose-6-phosphate", "ADP"], -16.7, atp_yield=-1
    ),
    MetabolicPathwayStep("Phosphoglucose isomerase", "PGI", ["G-6-P"], ["F-6-P"], +1.7),
    MetabolicPathwayStep("Phosphofructokinase-1", "PFK-1", ["F-6-P", "ATP"], ["F-1,6-BP", "ADP"], -14.2, atp_yield=-1),
    MetabolicPathwayStep("Aldolase", "Aldolase", ["F-1,6-BP"], ["DHAP", "G3P"], +23.9),
    MetabolicPathwayStep("Triose phosphate isomerase", "TPI", ["DHAP"], ["G3P"], +7.5),
    MetabolicPathwayStep(
        "G3P dehydrogenase", "GAPDH", ["2×G3P", "2×NAD⁺"], ["2×1,3-BPG", "2×NADH"], -2 * 6.3, nadh_yield=2
    ),
    MetabolicPathwayStep(
        "Phosphoglycerate kinase", "PGK", ["2×1,3-BPG", "2×ADP"], ["2×3-PG", "2×ATP"], -2 * 18.8, atp_yield=2
    ),
    MetabolicPathwayStep("Phosphoglycerate mutase", "PGM", ["2×3-PG"], ["2×2-PG"], +2 * 4.4),
    MetabolicPathwayStep("Enolase", "Enolase", ["2×2-PG"], ["2×PEP", "2×H₂O"], -2 * 7.5),
    MetabolicPathwayStep("Pyruvate kinase", "PK", ["2×PEP", "2×ADP"], ["2×Pyruvate", "2×ATP"], -2 * 31.4, atp_yield=2),
]


def glycolysis_summary() -> GlycolysisResult:
    """Return the complete glycolysis summary with energetics.

    Returns:
        GlycolysisResult with net ATP, NADH, and steps.
    """
    net_atp = sum(s.atp_yield for s in GLYCOLYSIS_STEPS)
    net_nadh = sum(s.nadh_yield for s in GLYCOLYSIS_STEPS)
    total_dG = sum(s.delta_G_prime_kJ for s in GLYCOLYSIS_STEPS)
    logger.info(f"Glycolysis: net ATP={net_atp}, net NADH={net_nadh}, ΔG_total={total_dG:.1f} kJ/mol")
    return GlycolysisResult(
        net_atp=net_atp,
        net_nadh=net_nadh,
        steps=GLYCOLYSIS_STEPS,
        total_delta_G_kJ=total_dG,
    )


# ---------------------------------------------------------------------------
# Metabolic Integration — ATP Yield by Pathway
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class PathwayATPYield:
    """ATP yield summary for one catabolic pathway.

    ATP yields follow the modern stoichiometry of 2.5 ATP per NADH and 1.5
    ATP per FADH2 reoxidised through the mitochondrial electron-transport
    chain, with the GTP from succinyl-CoA synthetase counted as one ATP.
    Glycolysis and lactic-acid fermentation produce two ATP per glucose by
    substrate-level phosphorylation; the NADH route is accounted only when a
    pathway reoxidises it in the mitochondrion.
    """

    pathway: str
    substrate_level_atp: float
    nadh_count: float
    fadh2_count: float
    oxidative_atp: float
    total_atp: float
    requires_oxygen: bool


def _oxidative_atp(nadh: float, fadh2: float) -> float:
    return nadh * 2.5 + fadh2 * 1.5


def atp_yield_by_pathway() -> tuple[PathwayATPYield, ...]:
    """Tabulate the canonical ATP yields used by the integration figure.

    Numbers follow the textbook stoichiometry: 2 net substrate-level ATP from
    glycolysis, 2 mitochondrial GTP/ATP from the TCA cycle (one per acetyl-
    CoA), and ten NADH plus two FADH2 routed through oxidative
    phosphorylation per glucose. Aerobic respiration sums to ~30-32 ATP; the
    figure uses 30 to reflect the cytosolic NADH shuttle correction.

    Returns:
        Tuple of ``PathwayATPYield`` rows in pedagogical order.
    """
    glycolysis = PathwayATPYield(
        pathway="Glycolysis (substrate level only)",
        substrate_level_atp=2.0,
        nadh_count=2.0,
        fadh2_count=0.0,
        oxidative_atp=0.0,
        total_atp=2.0,
        requires_oxygen=False,
    )
    fermentation = PathwayATPYield(
        pathway="Lactic-acid fermentation",
        substrate_level_atp=2.0,
        nadh_count=0.0,
        fadh2_count=0.0,
        oxidative_atp=0.0,
        total_atp=2.0,
        requires_oxygen=False,
    )
    tca = PathwayATPYield(
        pathway="TCA cycle (per glucose, 2 turns)",
        substrate_level_atp=2.0,
        nadh_count=6.0,
        fadh2_count=2.0,
        oxidative_atp=_oxidative_atp(6.0, 2.0),
        total_atp=2.0 + _oxidative_atp(6.0, 2.0),
        requires_oxygen=True,
    )
    aerobic_total = PathwayATPYield(
        pathway="Aerobic respiration (full)",
        substrate_level_atp=4.0,
        nadh_count=10.0,
        fadh2_count=2.0,
        oxidative_atp=_oxidative_atp(10.0, 2.0),
        total_atp=30.0,  # canonical textbook value with shuttle correction
        requires_oxygen=True,
    )
    rows = (glycolysis, fermentation, tca, aerobic_total)
    logger.debug(
        "ATP yields: %s",
        {row.pathway: row.total_atp for row in rows},
    )
    return rows
