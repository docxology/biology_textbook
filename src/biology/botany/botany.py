"""Botany module.

Covers plant cell structure, water potential, transpiration (Fick's law),
C3/C4/CAM photosynthesis comparison, plant growth models, and reproductive
biology. All computations use real plant physiology equations — no mock methods.
"""

from __future__ import annotations

from dataclasses import dataclass

from infrastructure.core.logging.utils import get_logger

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
    delta_concentration_mol_m3: float  # vapour concentration gradient
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
    photorespiration: bool
    example_plants: list[str]


@dataclass
class PlantGrowthResult:
    """Logistic growth model for plant biomass accumulation."""

    times_days: list[float]
    biomass_g: list[float]
    relative_growth_rate: float  # RGR (g g⁻¹ day⁻¹)


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
    internal_vapor_conc_mol_m3: float,
    external_vapor_conc_mol_m3: float,
) -> TranspirationResult:
    """Compute transpiration flux via Fick's law.

    J = g * (C_internal - C_external)

    Args:
        stomatal_conductance_mol_m2_s: Stomatal conductance g (mol m⁻² s⁻¹).
        internal_vapor_conc_mol_m3: Water vapour inside leaf (mol m⁻³).
        external_vapor_conc_mol_m3: Water vapour in atmosphere (mol m⁻³).

    Returns:
        TranspirationResult with flux in mol m⁻² s⁻¹ and mmol m⁻² s⁻¹.

    Raises:
        ValueError: If conductance is non-positive.
    """
    if stomatal_conductance_mol_m2_s <= 0:
        raise ValueError("stomatal_conductance_mol_m2_s must be positive.")
    delta_C = internal_vapor_conc_mol_m3 - external_vapor_conc_mol_m3
    flux = stomatal_conductance_mol_m2_s * delta_C
    logger.debug(f"Transpiration flux: {flux:.4e} mol m⁻² s⁻¹")
    return TranspirationResult(
        conductance_mol_m2_s=stomatal_conductance_mol_m2_s,
        delta_concentration_mol_m3=delta_C,
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
        light_saturation_point: I at which A = A_max/2 (µmol m⁻² s⁻¹).
        dark_respiration_µmol_CO2_m2_s: Dark respiration rate.

    Returns:
        Net photosynthesis rate A_net (µmol CO₂ m⁻² s⁻¹).

    Raises:
        ValueError: If photon_flux or rates are negative.
    """
    if photon_flux_µmol_m2_s < 0:
        raise ValueError("photon_flux_µmol_m2_s must be non-negative.")
    if max_rate_µmol_CO2_m2_s <= 0:
        raise ValueError("max_rate must be positive.")
    if light_saturation_point <= 0:
        raise ValueError("light_saturation_point must be positive.")

    gross = (max_rate_µmol_CO2_m2_s * photon_flux_µmol_m2_s) / (photon_flux_µmol_m2_s + light_saturation_point)
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
        List of (PAR, A_net) tuples.
    """
    if n_points <= 0:
        raise ValueError("n_points must be positive.")
    step = max_par / n_points
    return [
        (i * step, photosynthesis_rate(i * step, max_rate, light_saturation_point, dark_respiration))
        for i in range(n_points + 1)
    ]


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

    Relative Growth Rate (RGR) = (1/W) * dW/dt

    Args:
        initial_biomass_g: Initial dry mass (g).
        relative_growth_rate: RGR (g g⁻¹ day⁻¹).
        carrying_capacity_g: Maximum biomass (g).
        duration_days: Simulation duration (days).
        steps: Number of time steps.

    Returns:
        PlantGrowthResult with time series.
    """
    if initial_biomass_g <= 0:
        raise ValueError("initial_biomass_g must be positive.")
    if relative_growth_rate <= 0:
        raise ValueError("relative_growth_rate must be positive.")
    if carrying_capacity_g <= initial_biomass_g:
        raise ValueError("carrying_capacity_g must exceed initial_biomass_g.")
    if duration_days <= 0:
        raise ValueError("duration_days must be positive.")

    dt = duration_days / steps
    times = [0.0]
    biomass = [initial_biomass_g]
    W = initial_biomass_g

    for _ in range(steps):
        dW = relative_growth_rate * W * (1.0 - W / carrying_capacity_g)
        W = max(0.0, W + dW * dt)
        times.append(times[-1] + dt)
        biomass.append(W)

    logger.debug(f"Plant growth: final biomass={biomass[-1]:.2f} g at day {duration_days}")
    return PlantGrowthResult(times_days=times, biomass_g=biomass, relative_growth_rate=relative_growth_rate)
