"""Biochemistry module.

Covers enzyme kinetics (Michaelis-Menten, inhibition), metabolic pathways
(glycolysis, Krebs cycle, electron transport), and thermodynamics of reactions.
"""

from __future__ import annotations

import math
from dataclasses import dataclass

from biology.constants import GAS_CONSTANT
from textbook_logging import get_logger

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


@dataclass(frozen=True)
class MetabolicPathwayStep:
    """Immutable reaction; energy is per reaction, carrier yields per glucose."""

    name: str
    enzyme: str
    reactants: tuple[str, ...]
    products: tuple[str, ...]
    delta_G_prime_kJ: float  # Approximate standard transformed ΔG°', kJ/mol reaction
    atp_yield: int = 0  # Per glucose (negative = consumed)
    nadh_yield: int = 0  # Per glucose
    fadh2_yield: int = 0  # Per glucose
    reactions_per_glucose: int = 1


@dataclass(frozen=True)
class GlycolysisResult:
    """One-glucose summary using approximate standard transformed energies."""

    net_atp: int
    net_nadh: int
    steps: tuple[MetabolicPathwayStep, ...]
    total_delta_G_kJ: float  # kJ/mol glucose, not cellular ΔG


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
        ValueError: If substrate concentration is negative or non-finite, or
            Vmax or Km is non-positive or non-finite.
    """
    if not math.isfinite(substrate_conc) or substrate_conc < 0:
        raise ValueError("substrate_conc must be finite and non-negative.")
    if not math.isfinite(Vmax) or Vmax <= 0:
        raise ValueError("Vmax must be finite and positive.")
    if not math.isfinite(Km) or Km <= 0:
        raise ValueError("Km must be finite and positive.")

    if substrate_conc <= Km:
        ratio = substrate_conc / Km
        efficiency = ratio / (1.0 + ratio)
    else:
        efficiency = 1.0 / (1.0 + Km / substrate_conc)
    v = Vmax * efficiency
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
        EnzymeKineticsResult with the finite apparent Km under inhibition.

    Raises:
        ValueError: For invalid inputs or an unrepresentable apparent Km.
    """
    if not math.isfinite(Ki) or Ki <= 0:
        raise ValueError("Ki must be finite and positive.")
    if not math.isfinite(inhibitor_conc) or inhibitor_conc < 0:
        raise ValueError("inhibitor_conc must be finite and non-negative.")
    if not math.isfinite(Km) or Km <= 0:
        raise ValueError("Km must be finite and positive.")
    # Scale Km*I/Ki without first overflowing I/Ki or underflowing Km/Ki.
    km_mantissa, km_exponent = math.frexp(Km)
    i_mantissa, i_exponent = math.frexp(inhibitor_conc)
    ki_mantissa, ki_exponent = math.frexp(Ki)
    try:
        inhibition_term = math.ldexp(
            km_mantissa * i_mantissa / ki_mantissa,
            km_exponent + i_exponent - ki_exponent,
        )
    except OverflowError as exc:
        raise ValueError("Apparent Km exceeds the finite model range.") from exc
    apparent_Km = Km + inhibition_term
    if not math.isfinite(apparent_Km):
        raise ValueError("Apparent Km exceeds the finite model range.")
    return michaelis_menten(substrate_conc, Vmax, apparent_Km)


def enzyme_rate_curve(
    Vmax: float,
    Km: float,
    n_points: int = 50,
    max_conc: float | None = None,
) -> list[EnzymeKineticsResult]:
    """Generate a full Michaelis-Menten curve across [S] range.

    Args:
        Vmax: Maximum reaction rate.
        Km: Michaelis constant.
        n_points: Number of data points.
        max_conc: Maximum substrate concentration (default 10*Km).

    Returns:
        List of EnzymeKineticsResult sorted by [S], ending exactly at max_conc.
    """
    if max_conc is None:
        max_conc = 10.0 * Km
    if not isinstance(n_points, int) or isinstance(n_points, bool):
        raise TypeError("n_points must be a positive integer.")
    if n_points <= 0:
        raise ValueError("n_points must be a positive integer.")
    if not math.isfinite(max_conc) or max_conc < 0:
        raise ValueError("max_conc must be finite and non-negative.")
    if max_conc > 0 and n_points > max_conc / math.ulp(max_conc):
        raise ValueError("Concentration step is not representable; reduce n_points.")
    return [
        michaelis_menten(max_conc if i == n_points else (i / n_points) * max_conc, Vmax, Km)
        for i in range(n_points + 1)
    ]


# ---------------------------------------------------------------------------
# Thermodynamics
# ---------------------------------------------------------------------------


def reaction_free_energy(
    delta_G_standard_kJ: float,
    product_conc: float,
    reactant_conc: float,
    temperature_K: float = 310.0,
) -> float:
    """Compute fixed-convention 1:1 ideal-dilute reaction free energy.

    Uses Q = product_conc / reactant_conc for a 1:1 reaction, not an
    arbitrary stoichiometric quotient. Supply the standard transformed energy
    for the same temperature and biochemical convention; this helper does not
    calculate pH/metal speciation or nonideal activity corrections.

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
    if any(not math.isfinite(c) or c <= 0 for c in (product_conc, reactant_conc)):
        raise ValueError("Concentrations must be finite and positive.")
    if not math.isfinite(temperature_K) or temperature_K <= 0:
        raise ValueError("Temperature must be finite and positive.")
    if not math.isfinite(delta_G_standard_kJ):
        raise ValueError("Standard free energy must be finite.")
    log_Q = math.log(product_conc) - math.log(reactant_conc)
    return delta_G_standard_kJ + (GAS_CONSTANT * temperature_K / 1000.0) * log_Q


def atp_free_energy(
    atp_conc_mM: float = 3.0,
    adp_conc_mM: float = 1.0,
    pi_conc_mM: float = 10.0,
    temperature_K: float = 310.0,
) -> float:
    """Compute model ATP-hydrolysis free energy under ideal dilute activities.

    Fixes ΔG°' at -30.5 kJ/mol and uses Q = a_ADP*a_Pi/a_ATP with a 1 M
    standard state. This is not a pH/Mg-speciation or physiological-activity model.

    Args:
        atp_conc_mM: ATP concentration (mM).
        adp_conc_mM: ADP concentration (mM).
        pi_conc_mM: Inorganic phosphate concentration (mM).
        temperature_K: Temperature in Kelvin.

    Returns:
        Model ΔG of ATP hydrolysis (kJ mol⁻¹); no fixed cellular range is implied.
    """
    if any(not math.isfinite(c) or c <= 0 for c in (atp_conc_mM, adp_conc_mM, pi_conc_mM)):
        raise ValueError("ATP, ADP and phosphate concentrations must be finite and positive.")
    if not math.isfinite(temperature_K) or temperature_K <= 0:
        raise ValueError("Temperature must be finite and positive.")
    delta_G0_prime = -30.5  # kJ/mol
    log_Q = math.log(adp_conc_mM) + math.log(pi_conc_mM) - math.log(atp_conc_mM) - math.log(1000.0)
    delta_G = delta_G0_prime + (GAS_CONSTANT * temperature_K / 1000.0) * log_Q
    logger.debug(f"ATP ΔG = {delta_G:.2f} kJ/mol")
    return delta_G


# ---------------------------------------------------------------------------
# Glycolysis Summary
# ---------------------------------------------------------------------------

# UC Davis BIS 2A, "1.11: Glycolysis", Table 1 (2022 revision),
# https://bio.libretexts.org/@go/page/8434 (bibliography: ucdavis2022glycolysis).
# Approximate teaching ΔG°' values, NOT measured cellular ΔG. Values are
# per reaction; steps 6–10 occur twice per glucose, TPI occurs once.
GLYCOLYSIS_STEPS: tuple[MetabolicPathwayStep, ...] = (
    MetabolicPathwayStep(
        "Hexokinase", "Hexokinase", ("Glucose", "ATP"), ("Glucose-6-phosphate", "ADP"), -16.7, atp_yield=-1
    ),
    MetabolicPathwayStep("Phosphoglucose isomerase", "PGI", ("G-6-P",), ("F-6-P",), 1.67),
    MetabolicPathwayStep("Phosphofructokinase-1", "PFK-1", ("F-6-P", "ATP"), ("F-1,6-BP", "ADP"), -14.2, atp_yield=-1),
    MetabolicPathwayStep("Aldolase", "Aldolase", ("F-1,6-BP",), ("DHAP", "G3P"), 23.9),
    MetabolicPathwayStep("Triose phosphate isomerase", "TPI", ("DHAP",), ("G3P",), 7.56),
    MetabolicPathwayStep(
        "G3P dehydrogenase", "GAPDH", ("G3P", "NAD⁺", "Pi"), ("1,3-BPG", "NADH", "H⁺"),
        6.30, nadh_yield=2, reactions_per_glucose=2
    ),
    MetabolicPathwayStep(
        "Phosphoglycerate kinase", "PGK", ("1,3-BPG", "ADP"), ("3-PG", "ATP"),
        -18.9, atp_yield=2, reactions_per_glucose=2
    ),
    MetabolicPathwayStep("Phosphoglycerate mutase", "PGM", ("3-PG",), ("2-PG",), 4.4, reactions_per_glucose=2),
    MetabolicPathwayStep("Enolase", "Enolase", ("2-PG",), ("PEP", "H₂O"), 1.8, reactions_per_glucose=2),
    MetabolicPathwayStep(
        "Pyruvate kinase", "PK", ("PEP", "ADP"), ("Pyruvate", "ATP"),
        -31.7, atp_yield=2, reactions_per_glucose=2
    ),
)


def glycolysis_summary() -> GlycolysisResult:
    """Return one-glucose yields and approximate standard transformed ΔG°'.

    Energies follow the UC Davis teaching table, not cellular concentrations.
    Reaction multiplicities weight energy only; carrier yields are already
    per glucose.
    """
    net_atp = sum(s.atp_yield for s in GLYCOLYSIS_STEPS)
    net_nadh = sum(s.nadh_yield for s in GLYCOLYSIS_STEPS)
    total_dG = math.fsum(s.delta_G_prime_kJ * s.reactions_per_glucose for s in GLYCOLYSIS_STEPS)
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
    shuttle_adjustment_atp: float = 0.0  # Included in oxidative_atp, not an extra stack


def _oxidative_atp(nadh: float, fadh2: float) -> float:
    return nadh * 2.5 + fadh2 * 1.5


def atp_yield_by_pathway() -> tuple[PathwayATPYield, ...]:
    """Tabulate the canonical ATP yields used by the integration figure.

    Numbers follow the textbook stoichiometry: 2 net substrate-level ATP from
    glycolysis, 2 mitochondrial GTP/ATP from the TCA cycle (one per acetyl-
    CoA), and ten NADH plus two FADH2 routed through oxidative
    phosphorylation per glucose. The glycerol-3-phosphate shuttle delivers
    the two cytosolic NADH electron pairs at FAD-linked yield: oxidative ATP
    = 10*2.5 + 2*1.5 - 2 = 26; full respiration = 4 + 26 = 30.

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
        pathway="Aerobic respiration (glycerol-3-phosphate shuttle)",
        substrate_level_atp=4.0,
        nadh_count=10.0,
        fadh2_count=2.0,
        oxidative_atp=_oxidative_atp(10.0, 2.0) - 2.0,
        total_atp=4.0 + _oxidative_atp(10.0, 2.0) - 2.0,
        requires_oxygen=True,
        shuttle_adjustment_atp=-2.0,
    )
    rows = (glycolysis, fermentation, tca, aerobic_total)
    logger.debug(
        "ATP yields: %s",
        {row.pathway: row.total_atp for row in rows},
    )
    return rows
