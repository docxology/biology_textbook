"""Botany module.

Covers plant cell structure, water potential, transpiration (Fick's law),
C3/C4/CAM photosynthesis comparison, plant growth models, and reproductive
biology. All computations use real plant physiology equations — no mock methods.
"""

from __future__ import annotations

import math
from dataclasses import dataclass

from textbook_logging import get_logger

logger = get_logger(__name__)

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------
GAS_CONSTANT = 8.314  # J mol⁻¹ K⁻¹
AVOGADRO = 6.022e23  # mol⁻¹


# ---------------------------------------------------------------------------
# Data Classes
# ---------------------------------------------------------------------------


@dataclass
class WaterPotentialResult:
    """Water potential components for plant cells."""

    osmotic_potential_MPa: float  # ψ_s (solute potential)
    pressure_potential_MPa: float  # ψ_p (turgor pressure)
    water_potential_MPa: float  # ψ = ψ_s + ψ_p


@dataclass
class TranspirationResult:
    """Water loss through stomata via Fick's law."""

    conductance_mol_m2_s: float  # stomatal conductance
    delta_mole_fraction: float  # inside minus outside water vapor (mol/mol)
    flux_mol_m2_s: float  # net transpiration flux
    flux_mmol_m2_s: float


@dataclass
class PhotosynthesisTypeComparison:
    """Comparison of C3, C4, and CAM photosynthesis pathways."""

    pathway: str  # "C3", "C4", or "CAM"
    CO2_fixation_enzyme: str
    first_product: str
    water_use_efficiency: str  # "low", "medium", "high"
    light_saturation_point_µmol_m2_s: float
    optimal_temp_C: float
    photorespiration: bool  # simplified pathway-table flag, not universal absence
    example_plants: list[str]


@dataclass
class PlantGrowthResult:
    """Logistic growth model for plant biomass accumulation."""

    times_days: list[float]
    biomass_g: list[float]
    relative_growth_rate: float  # intrinsic coefficient r; instantaneous RGR = r*(1-W/K)


# ---------------------------------------------------------------------------
# Water Potential
# ---------------------------------------------------------------------------


def water_potential(
    solute_concentration_M: float,
    turgor_pressure_MPa: float,
    temperature_K: float = 298.0,
) -> WaterPotentialResult:
    """Compute plant cell water potential.

    ψ = ψ_s + ψ_p
    ψ_s = -iCRT  (osmotic potential, in MPa)

    Args:
        solute_concentration_M: Molar solute concentration (M).
        turgor_pressure_MPa: Turgor pressure (MPa; positive values).
        temperature_K: Temperature in Kelvin.

    Returns:
        WaterPotentialResult with all components in MPa.

    Raises:
        ValueError: If concentration is non-positive or temperature ≤ 0.
    """
    if not all(math.isfinite(v) for v in (solute_concentration_M, turgor_pressure_MPa, temperature_K)):
        raise ValueError("Water-potential parameters must be finite.")
    if solute_concentration_M <= 0:
        raise ValueError("solute_concentration_M must be positive.")
    if temperature_K <= 0:
        raise ValueError("temperature_K must be positive.")

    # ψ_s = -CRT assuming i=1. M × J mol⁻¹ K⁻¹ × K gives J L⁻¹;
    # 1 J L⁻¹ = 0.001 MPa, so R is scaled by 1e-3 in the MPa calculation.
    osmotic_MPa = -(GAS_CONSTANT * 1e-3 * temperature_K) * solute_concentration_M
    water_pot = osmotic_MPa + turgor_pressure_MPa
    logger.debug(f"Water potential: ψ_s={osmotic_MPa:.4f}, ψ_p={turgor_pressure_MPa:.4f}, ψ={water_pot:.4f} MPa")
    return WaterPotentialResult(
        osmotic_potential_MPa=osmotic_MPa,
        pressure_potential_MPa=turgor_pressure_MPa,
        water_potential_MPa=water_pot,
    )


# ---------------------------------------------------------------------------
# Transpiration — Fick's Law through stomata
# ---------------------------------------------------------------------------


def transpiration_flux(
    stomatal_conductance_mol_m2_s: float,
    internal_vapor_mole_fraction: float,
    external_vapor_mole_fraction: float,
) -> TranspirationResult:
    """Compute transpiration flux via Fick's law.

    J = g * (w_internal - w_external), where w is mol H2O / mol air.

    Args:
        stomatal_conductance_mol_m2_s: Stomatal conductance g (mol m⁻² s⁻¹).
        internal_vapor_mole_fraction: Water vapor inside leaf (mol/mol, in [0,1]).
        external_vapor_mole_fraction: Water vapor outside leaf (mol/mol, in [0,1]).

    Returns:
        TranspirationResult with flux in mol m⁻² s⁻¹ and mmol m⁻² s⁻¹.

    Raises:
        ValueError: If conductance is non-positive.
    """
    if not math.isfinite(stomatal_conductance_mol_m2_s):
        raise ValueError("stomatal_conductance_mol_m2_s must be finite.")
    if any(not math.isfinite(w) or not 0 <= w <= 1 for w in (
        internal_vapor_mole_fraction, external_vapor_mole_fraction
    )):
        raise ValueError("Vapor mole fractions must be finite and in [0, 1].")
    if stomatal_conductance_mol_m2_s <= 0:
        raise ValueError("stomatal_conductance_mol_m2_s must be positive.")
    delta_w = internal_vapor_mole_fraction - external_vapor_mole_fraction
    flux = stomatal_conductance_mol_m2_s * delta_w
    logger.debug(f"Transpiration flux: {flux:.4e} mol m⁻² s⁻¹")
    return TranspirationResult(
        conductance_mol_m2_s=stomatal_conductance_mol_m2_s,
        delta_mole_fraction=delta_w,
        flux_mol_m2_s=flux,
        flux_mmol_m2_s=flux * 1000.0,
    )


# ---------------------------------------------------------------------------
# Photosynthesis — Quantum Yield and Light Response
# ---------------------------------------------------------------------------


def photosynthesis_rate(
    photon_flux_µmol_m2_s: float,
    max_rate_µmol_CO2_m2_s: float = 20.0,
    light_saturation_point: float = 800.0,
    dark_respiration_µmol_CO2_m2_s: float = 1.5,
) -> float:
    """Net photosynthesis using a hyperbolic light-response curve.

    A_net = (A_max * I) / (I + K_light) - R_d

    Args:
        photon_flux_µmol_m2_s: Photosynthetically active radiation (PAR).
        max_rate_µmol_CO2_m2_s: Maximum gross photosynthesis rate.
        light_saturation_point: I at which gross A = A_max/2 (µmol m⁻² s⁻¹).
        dark_respiration_µmol_CO2_m2_s: Dark respiration rate.

    Returns:
        Net photosynthesis rate A_net (µmol CO₂ m⁻² s⁻¹).

    Raises:
        ValueError: If photon_flux or rates are negative.
    """
    if not all(math.isfinite(v) for v in (
        photon_flux_µmol_m2_s, max_rate_µmol_CO2_m2_s,
        light_saturation_point, dark_respiration_µmol_CO2_m2_s
    )):
        raise ValueError("Photosynthesis parameters must be finite.")
    if dark_respiration_µmol_CO2_m2_s < 0:
        raise ValueError("dark_respiration must be non-negative.")
    if photon_flux_µmol_m2_s < 0:
        raise ValueError("photon_flux_µmol_m2_s must be non-negative.")
    if max_rate_µmol_CO2_m2_s <= 0:
        raise ValueError("max_rate must be positive.")
    if light_saturation_point <= 0:
        raise ValueError("light_saturation_point must be positive.")

    I, K = photon_flux_µmol_m2_s, light_saturation_point
    fraction = (I / K) / (1.0 + I / K) if I <= K else 1.0 / (1.0 + K / I)
    gross = max_rate_µmol_CO2_m2_s * fraction
    net = gross - dark_respiration_µmol_CO2_m2_s
    logger.debug(f"A_net at PAR={photon_flux_µmol_m2_s}: {net:.4f} µmol CO₂ m⁻² s⁻¹")
    return net


def light_response_curve(
    max_rate: float = 20.0,
    light_saturation_point: float = 800.0,
    dark_respiration: float = 1.5,
    n_points: int = 50,
    max_par: float = 2000.0,
) -> list[tuple[float, float]]:
    """Generate a full light-response curve (PAR vs A_net).

    Args:
        max_rate: Maximum gross photosynthesis (µmol CO₂ m⁻² s⁻¹).
        light_saturation_point: Half-saturation PAR.
        dark_respiration: Dark respiration rate.
        n_points: Number of data points.
        max_par: Maximum PAR to plot.

    Returns:
        List of (PAR, A_net) tuples, ending exactly at max_par. Positive PAR
        ranges require a representable nonzero sampling step.
    """
    if not isinstance(n_points, int) or isinstance(n_points, bool):
        raise TypeError("n_points must be a positive integer.")
    if not math.isfinite(max_par) or max_par < 0:
        raise ValueError("max_par must be finite and non-negative.")
    if n_points <= 0:
        raise ValueError("n_points must be positive.")
    if max_par > 0 and n_points > max_par / math.ulp(max_par):
        raise ValueError("PAR step is not representable; reduce n_points.")
    curve = []
    for i in range(n_points + 1):
        par = max_par if i == n_points else (i / n_points) * max_par
        curve.append((par, photosynthesis_rate(par, max_rate, light_saturation_point, dark_respiration)))
    return curve


# ---------------------------------------------------------------------------
# C3 / C4 / CAM Comparison
# ---------------------------------------------------------------------------

PHOTOSYNTHESIS_PATHWAYS: list[PhotosynthesisTypeComparison] = [
    PhotosynthesisTypeComparison(
        pathway="C3",
        CO2_fixation_enzyme="RuBisCO",
        first_product="3-phosphoglycerate (3-PGA)",
        water_use_efficiency="low",
        light_saturation_point_µmol_m2_s=500.0,
        optimal_temp_C=20.0,
        photorespiration=True,
        example_plants=["Wheat", "Rice", "Soybean", "Most trees"],
    ),
    PhotosynthesisTypeComparison(
        pathway="C4",
        CO2_fixation_enzyme="PEP carboxylase",
        first_product="oxaloacetate (OAA)",
        water_use_efficiency="medium",
        light_saturation_point_µmol_m2_s=1500.0,
        optimal_temp_C=35.0,
        photorespiration=False,
        example_plants=["Maize (corn)", "Sugarcane", "Sorghum", "Bermuda grass"],
    ),
    PhotosynthesisTypeComparison(
        pathway="CAM",
        CO2_fixation_enzyme="PEP carboxylase (night)",
        first_product="malate (stored overnight)",
        water_use_efficiency="high",
        light_saturation_point_µmol_m2_s=800.0,
        optimal_temp_C=30.0,
        photorespiration=False,
        example_plants=["Cacti", "Agave", "Pineapple", "Orchids"],
    ),
]


# ---------------------------------------------------------------------------
# Plant Growth Model
# ---------------------------------------------------------------------------


def plant_biomass_growth(
    initial_biomass_g: float,
    relative_growth_rate: float,
    carrying_capacity_g: float,
    duration_days: float,
    steps: int = 100,
) -> PlantGrowthResult:
    """Simulate plant biomass accumulation using a logistic growth model.

    Instantaneous RGR = (1/W)*dW/dt = r*(1-W/K), not the constant r.

    Uses forward Euler through ecology.logistic_growth with the same explicit
    rate*dt admissibility bound. Increase steps for accuracy; no clipping.

    Args:
        initial_biomass_g: Initial dry mass (g).
        relative_growth_rate: Intrinsic logistic coefficient r (day⁻¹).
        carrying_capacity_g: Maximum biomass (g).
        duration_days: Simulation duration (days).
        steps: Number of time steps.

    Returns:
        PlantGrowthResult with time series.
    """
    if not all(math.isfinite(v) for v in (
        initial_biomass_g, relative_growth_rate, carrying_capacity_g, duration_days
    )):
        raise ValueError("Biomass parameters must be finite.")
    if initial_biomass_g <= 0:
        raise ValueError("initial_biomass_g must be positive.")
    if relative_growth_rate <= 0:
        raise ValueError("relative_growth_rate must be positive.")
    if carrying_capacity_g <= initial_biomass_g:
        raise ValueError("carrying_capacity_g must exceed initial_biomass_g.")
    if duration_days <= 0:
        raise ValueError("duration_days must be positive.")

    from biology.ecology import logistic_growth

    result = logistic_growth(
        initial_biomass_g, relative_growth_rate, carrying_capacity_g, duration_days, steps
    )
    times, biomass = result.times, result.populations

    logger.debug(f"Plant growth: final biomass={biomass[-1]:.2f} g at day {duration_days}")
    return PlantGrowthResult(times_days=times, biomass_g=biomass, relative_growth_rate=relative_growth_rate)


# ---------------------------------------------------------------------------
# Plant Reproduction — Pollen Tube Growth Curve
# ---------------------------------------------------------------------------


@dataclass
class PollenTubeGrowthResult:
    """Length-vs-time profile for a growing pollen tube."""

    times_min: list[float]
    lengths_um: list[float]
    elongation_rate_um_per_min: float
    saturation_length_um: float


def pollen_tube_growth(
    *,
    max_length_um: float = 1500.0,
    growth_rate_um_per_min: float = 12.0,
    duration_min: float = 240.0,
    initial_length_um: float = 50.0,
    steps: int = 240,
) -> PollenTubeGrowthResult:
    """Simulate pollen tube length over time using a saturating growth model.

    Sample the exact saturating-linear law dL/dt = v*(1-L/L_max):
    L(t) = L_max - (L_max-L0)*exp(-v*t/L_max).
    Here v has units um/min, not 1/min. This phenomenological model has
    no explicit resource pool and does not establish a slowing mechanism.

    Args:
        max_length_um: Positive saturation length L_max, at least initial_length_um.
        growth_rate_um_per_min: Low-length elongation speed v (must be positive).
        duration_min: Simulated duration (minutes, must be positive).
        initial_length_um: Initial pollen-tube length in [0, L_max].
        steps: Positive integer interval count; duration/steps must be representable.

    Returns:
        PollenTubeGrowthResult with ``steps + 1`` (time, length) samples.

    Raises:
        TypeError: If steps is not an integer (excluding bool).
        ValueError: If any argument is out of range.
    """
    if not all(math.isfinite(v) for v in (
        max_length_um, initial_length_um, growth_rate_um_per_min, duration_min
    )):
        raise ValueError("Pollen growth parameters must be finite.")
    if not isinstance(steps, int) or isinstance(steps, bool):
        raise TypeError("steps must be a positive integer.")
    if max_length_um <= 0 or initial_length_um < 0:
        raise ValueError("max_length_um must be positive and initial_length_um non-negative.")
    if initial_length_um > max_length_um:
        raise ValueError("initial_length_um must not exceed max_length_um.")
    if growth_rate_um_per_min <= 0:
        raise ValueError("growth_rate_um_per_min must be positive.")
    if duration_min <= 0 or steps <= 0:
        raise ValueError("duration_min and steps must be positive.")

    if steps > duration_min / math.ulp(duration_min):
        raise ValueError("Sampling time step is not representable; reduce steps.")
    times = [duration_min if i == steps else (i / steps) * duration_min for i in range(steps + 1)]
    lengths = [
        initial_length_um if t == 0 else
        initial_length_um + (max_length_um - initial_length_um)
        * -math.expm1(-(growth_rate_um_per_min / max_length_um) * t)
        for t in times
    ]
    logger.debug(
        "Pollen tube growth: final length=%.1f um at %.0f min", lengths[-1], duration_min
    )
    return PollenTubeGrowthResult(
        times_min=times,
        lengths_um=lengths,
        elongation_rate_um_per_min=growth_rate_um_per_min,
        saturation_length_um=max_length_um,
    )
