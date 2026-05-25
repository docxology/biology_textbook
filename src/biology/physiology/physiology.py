"""Physiology module.

Covers homeostasis, Poiseuille's law for blood flow, respiratory
mechanics (Bohr effect), thermoregulation, and organ system reference data.
All computations use real physiological equations — no mock methods.
"""

from __future__ import annotations

import math
from dataclasses import dataclass

from textbook_logging import get_logger

logger = get_logger(__name__)

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

NORMAL_BODY_TEMP_K = 310.15  # 37 °C in Kelvin


# ---------------------------------------------------------------------------
# Data Classes
# ---------------------------------------------------------------------------


@dataclass
class BloodFlowResult:
    """Result of Poiseuille flow calculation."""

    volumetric_flow_m3s: float  # Q in m³ s⁻¹
    volumetric_flow_mL_min: float
    reynolds_number: float
    flow_regime: str  # "laminar" or "turbulent"


@dataclass
class RespiratoryResult:
    """Oxygen-hemoglobin dissociation curve point."""

    pO2_mmHg: float
    saturation: float  # SaO2 in [0,1]
    p50_mmHg: float  # pO2 at 50% saturation


@dataclass
class HomeostasisResult:
    """Simple homeostasis model: negative feedback loop."""

    set_point: float
    measured_value: float
    error: float
    corrective_response: float  # proportional to error
    is_within_tolerance: bool


# ---------------------------------------------------------------------------
# Poiseuille's Law — Blood Flow
# ---------------------------------------------------------------------------


def poiseuille_flow(
    pressure_difference_Pa: float,
    radius_m: float,
    length_m: float,
    viscosity_Pa_s: float = 3e-3,
) -> BloodFlowResult:
    """Compute volumetric blood flow using Hagen-Poiseuille law.

    Q = π r⁴ ΔP / (8 η L)

    Args:
        pressure_difference_Pa: ΔP across vessel length (Pa).
        radius_m: Vessel radius (m).
        length_m: Vessel length (m).
        viscosity_Pa_s: Dynamic viscosity of blood (Pa·s; default ≈3 mPa·s).

    Returns:
        BloodFlowResult with flow rate and Reynolds number.

    Raises:
        ValueError: If radius or length are non-positive, or viscosity ≤ 0.
    """
    if radius_m <= 0:
        raise ValueError("radius_m must be positive.")
    if length_m <= 0:
        raise ValueError("length_m must be positive.")
    if viscosity_Pa_s <= 0:
        raise ValueError("viscosity_Pa_s must be positive.")

    Q = (math.pi * radius_m**4 * pressure_difference_Pa) / (8.0 * viscosity_Pa_s * length_m)
    Q_mL_min = Q * 1e6 * 60.0

    # Reynolds number: Re = ρ v D / η; mean velocity v = Q / (π r²)
    density_kg_m3 = 1060.0  # blood density
    mean_velocity = Q / (math.pi * radius_m**2) if radius_m > 0 else 0.0
    Re = (density_kg_m3 * mean_velocity * 2 * radius_m) / viscosity_Pa_s

    regime = "laminar" if Re < 2300 else "turbulent"
    logger.debug(f"Poiseuille: Q={Q_mL_min:.2f} mL/min, Re={Re:.1f}, {regime}")
    return BloodFlowResult(
        volumetric_flow_m3s=Q,
        volumetric_flow_mL_min=Q_mL_min,
        reynolds_number=Re,
        flow_regime=regime,
    )


# ---------------------------------------------------------------------------
# Oxygen–Hemoglobin Dissociation (Hill Equation)
# ---------------------------------------------------------------------------


def oxygen_saturation(
    pO2_mmHg: float,
    p50_mmHg: float = 26.0,
    hill_coefficient: float = 2.7,
) -> RespiratoryResult:
    """Compute hemoglobin oxygen saturation via the Hill equation.

    SaO2 = pO2ⁿ / (p50ⁿ + pO2ⁿ)

    Args:
        pO2_mmHg: Partial pressure of O2 (mmHg).
        p50_mmHg: pO2 at 50% saturation (default 26 mmHg for adult HbA).
        hill_coefficient: n (default 2.7 for cooperative binding).

    Returns:
        RespiratoryResult with saturation [0,1].

    Raises:
        ValueError: If pO2 < 0 or p50 ≤ 0 or n ≤ 0.
    """
    if pO2_mmHg < 0:
        raise ValueError("pO2_mmHg must be non-negative.")
    if p50_mmHg <= 0:
        raise ValueError("p50_mmHg must be positive.")
    if hill_coefficient <= 0:
        raise ValueError("hill_coefficient must be positive.")

    if pO2_mmHg == 0:
        return RespiratoryResult(pO2_mmHg=0.0, saturation=0.0, p50_mmHg=p50_mmHg)

    n = hill_coefficient
    pO2_n = pO2_mmHg**n
    p50_n = p50_mmHg**n
    sat = pO2_n / (p50_n + pO2_n)
    logger.debug(f"O2 sat at pO2={pO2_mmHg}: {sat:.4f}")
    return RespiratoryResult(pO2_mmHg=pO2_mmHg, saturation=sat, p50_mmHg=p50_mmHg)


def oxygen_dissociation_curve(
    p50_mmHg: float = 26.0,
    n_points: int = 100,
    max_pO2: float = 150.0,
) -> list[RespiratoryResult]:
    """Generate an O2-Hb dissociation curve across pO2 range.

    Args:
        p50_mmHg: pO2 at 50% saturation.
        n_points: Number of data points.
        max_pO2: Maximum pO2 in mmHg.

    Returns:
        List of RespiratoryResult.
    """
    if n_points <= 0:
        raise ValueError("n_points must be positive.")
    step = max_pO2 / n_points
    return [oxygen_saturation(i * step, p50_mmHg) for i in range(n_points + 1)]


# ---------------------------------------------------------------------------
# Homeostasis Model
# ---------------------------------------------------------------------------


def homeostasis_response(
    set_point: float,
    measured_value: float,
    gain: float = 1.0,
    tolerance: float = 0.05,
) -> HomeostasisResult:
    """Simulate a proportional negative-feedback homeostatic response.

    corrective_response = -gain * (measured_value - set_point)

    Args:
        set_point: Target value (e.g., 37.0 °C).
        measured_value: Current measured value.
        gain: Proportionality constant (default 1.0).
        tolerance: Acceptable deviation from set_point.

    Returns:
        HomeostasisResult with error and corrective response.
    """
    error = measured_value - set_point
    correction = -gain * error
    within = abs(error) <= tolerance
    logger.debug(f"Homeostasis: error={error:.4f}, correction={correction:.4f}")
    return HomeostasisResult(
        set_point=set_point,
        measured_value=measured_value,
        error=error,
        corrective_response=correction,
        is_within_tolerance=within,
    )


# ---------------------------------------------------------------------------
# Organ System Reference Data
# ---------------------------------------------------------------------------

ORGAN_SYSTEMS: dict[str, dict] = {
    "Cardiovascular": {
        "organs": ["Heart", "Arteries", "Veins", "Capillaries"],
        "function": "Circulation of blood; transport of O2, nutrients, waste",
        "cardiac_output_L_min": 5.0,
        "heart_rate_bpm": 72,
    },
    "Respiratory": {
        "organs": ["Lungs", "Trachea", "Bronchi", "Diaphragm"],
        "function": "Gas exchange (O2/CO2); acid-base balance",
        "tidal_volume_mL": 500,
        "breathing_rate_breaths_min": 15,
    },
    "Nervous": {
        "organs": ["Brain", "Spinal Cord", "Peripheral Nerves"],
        "function": "Integration, sensing, motor control",
        "neurons_billions": 86,
        "synapses_trillions": 100,
    },
    "Digestive": {
        "organs": ["Mouth", "Esophagus", "Stomach", "Small Intestine", "Large Intestine", "Liver", "Pancreas"],
        "function": "Mechanical and chemical digestion; nutrient absorption",
        "transit_time_hours": 24,
    },
    "Endocrine": {
        "organs": ["Hypothalamus", "Pituitary", "Thyroid", "Adrenal glands", "Pancreas", "Gonads"],
        "function": "Hormonal signaling; metabolic regulation",
    },
    "Immune": {
        "organs": ["Bone marrow", "Thymus", "Lymph nodes", "Spleen"],
        "function": "Defense against pathogens; immune memory",
    },
    "Musculoskeletal": {
        "organs": ["Skeletal muscles (~640)", "Bones (206)", "Joints", "Tendons", "Ligaments"],
        "function": "Movement, support, mineral storage",
    },
    "Renal/Urinary": {
        "organs": ["Kidneys", "Ureters", "Bladder", "Urethra"],
        "function": "Waste filtration; fluid/electrolyte balance; blood pressure",
        "daily_filtration_L": 180,
        "daily_urine_L": 1.5,
    },
    "Integumentary": {
        "organs": ["Skin", "Hair", "Nails", "Sweat glands"],
        "function": "Barrier, thermoregulation, sensory reception",
        "surface_area_m2": 2.0,
    },
    "Reproductive": {
        "organs": ["Gonads", "Accessory glands", "Ducts"],
        "function": "Production of gametes; fertilization; gestation",
    },
}
