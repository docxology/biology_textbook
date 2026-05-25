"""Neuroscience module.

Covers the Hodgkin-Huxley model of action potential, cable equation,
synaptic transmission (EPSP/IPSP), and Hebbian plasticity.
All computations use real differential equations — no mock methods.
"""

from __future__ import annotations

import math
from dataclasses import dataclass

from textbook_logging import get_logger

logger = get_logger(__name__)


# ---------------------------------------------------------------------------
# Data Classes
# ---------------------------------------------------------------------------


@dataclass
class NeuronProperties:
    """Passive membrane properties of a neuron."""

    membrane_capacitance_pF: float  # C_m (pF)
    resting_potential_mV: float  # V_rest
    threshold_potential_mV: float  # V_thresh
    membrane_resistance_MOhm: float  # R_m
    axon_length_mm: float = 100.0
    axon_diameter_µm: float = 10.0


@dataclass
class ActionPotentialResult:
    """Simplified Hodgkin-Huxley action potential time course."""

    times_ms: list[float]
    voltage_mV: list[float]
    peak_voltage_mV: float
    threshold_mV: float
    fired: bool


@dataclass
class SynapticResult:
    """Synaptic potential (EPSP or IPSP) computation."""

    reversal_potential_mV: float
    conductance_peak_nS: float
    membrane_potential_mV: float
    driving_force_mV: float
    peak_current_pA: float
    synaptic_type: str  # "excitatory" or "inhibitory"


@dataclass
class CableResult:
    """Steady-state voltage attenuation along a dendrite (cable equation)."""

    distances_µm: list[float]
    voltages_mV: list[float]
    lambda_µm: float  # space constant


# ---------------------------------------------------------------------------
# Hodgkin-Huxley Simplified Model
# ---------------------------------------------------------------------------


def _alpha_m(voltage_mV: float) -> float:
    d_v = voltage_mV - (-40.0)
    if abs(d_v) < 1e-7:
        return 1.0
    return 0.1 * d_v / (1.0 - math.exp(-d_v / 10.0))


def _beta_m(voltage_mV: float) -> float:
    return 4.0 * math.exp(-(voltage_mV - (-65.0)) / 18.0)


def _alpha_h(voltage_mV: float) -> float:
    return 0.07 * math.exp(-(voltage_mV - (-65.0)) / 20.0)


def _beta_h(voltage_mV: float) -> float:
    return 1.0 / (1.0 + math.exp(-(voltage_mV - (-35.0)) / 10.0))


def _alpha_n(voltage_mV: float) -> float:
    d_v = voltage_mV - (-55.0)
    if abs(d_v) < 1e-7:
        return 0.1
    return 0.01 * d_v / (1.0 - math.exp(-d_v / 10.0))


def _beta_n(voltage_mV: float) -> float:
    return 0.125 * math.exp(-(voltage_mV - (-65.0)) / 80.0)


def action_potential_hh(
    stimulus_current_µA: float = 10.0,
    t_end_ms: float = 30.0,
    steps: int = 3000,
    V_rest_mV: float = -70.0,
    V_threshold_mV: float = -55.0,
    V_Na_mV: float = 55.0,
    V_K_mV: float = -77.0,
    V_L_mV: float = -54.4,
    g_Na_mS: float = 120.0,
    g_K_mS: float = 36.0,
    g_L_mS: float = 0.3,
    C_m_µF: float = 1.0,
    stimulus_start_ms: float = 5.0,
    stimulus_duration_ms: float = 1.0,
) -> ActionPotentialResult:
    """Run a simplified Hodgkin-Huxley action potential simulation.

    Uses the full HH ODEs with m, n, h gating variables and Euler integration.

    Args:
        stimulus_current_µA: Injected current amplitude (µA/cm²).
        t_end_ms: Simulation duration (ms).
        steps: Number of Euler integration steps.
        V_rest_mV: Resting membrane potential (mV).
        V_threshold_mV: Approximate firing threshold (mV).
        V_Na_mV, V_K_mV, V_L_mV: Reversal potentials (mV).
        g_Na_mS, g_K_mS, g_L_mS: Maximum conductances (mS/cm²).
        C_m_µF: Membrane capacitance (µF/cm²).
        stimulus_start_ms: Stimulus onset (ms).
        stimulus_duration_ms: Stimulus duration (ms).

    Returns:
        ActionPotentialResult with voltage time course.

    Raises:
        ValueError: If t_end_ms ≤ 0 or steps ≤ 0.
    """
    if t_end_ms <= 0:
        raise ValueError("t_end_ms must be positive.")
    if steps <= 0:
        raise ValueError("steps must be positive.")

    dt = t_end_ms / steps

    # Initial conditions at rest (V ≈ V_rest)
    V = V_rest_mV
    m = _alpha_m(V) / (_alpha_m(V) + _beta_m(V))
    h = _alpha_h(V) / (_alpha_h(V) + _beta_h(V))
    n = _alpha_n(V) / (_alpha_n(V) + _beta_n(V))

    times = []
    voltages = []
    peak_V = V
    fired = False

    for i in range(steps):
        t = i * dt
        times.append(t)
        voltages.append(V)

        # Stimulus
        I_stim = stimulus_current_µA if stimulus_start_ms <= t <= (stimulus_start_ms + stimulus_duration_ms) else 0.0

        # Ionic currents
        I_Na = g_Na_mS * (m**3) * h * (V - V_Na_mV)
        I_K = g_K_mS * (n**4) * (V - V_K_mV)
        I_L = g_L_mS * (V - V_L_mV)

        # Membrane equation
        dV_dt = (I_stim - I_Na - I_K - I_L) / C_m_µF
        V = V + dV_dt * dt

        # Update gates
        m = m + (_alpha_m(V) * (1 - m) - _beta_m(V) * m) * dt
        h = h + (_alpha_h(V) * (1 - h) - _beta_h(V) * h) * dt
        n = n + (_alpha_n(V) * (1 - n) - _beta_n(V) * n) * dt

        if V > peak_V:
            peak_V = V
        if V > V_threshold_mV and not fired:
            fired = True

    times.append(t_end_ms)
    voltages.append(V)

    logger.info(f"HH simulation: peak={peak_V:.2f} mV, fired={fired}")
    return ActionPotentialResult(
        times_ms=times,
        voltage_mV=voltages,
        peak_voltage_mV=peak_V,
        threshold_mV=V_threshold_mV,
        fired=fired,
    )


# ---------------------------------------------------------------------------
# Cable Equation — Passive Attenuation
# ---------------------------------------------------------------------------


def cable_voltage_attenuation(
    V0_mV: float,
    axial_resistance_Ohm_cm: float = 100.0,
    membrane_resistance_kOhm_cm2: float = 50.0,
    axon_radius_cm: float = 5e-4,
    max_distance_µm: float = 1000.0,
    n_points: int = 100,
) -> CableResult:
    """Compute steady-state voltage attenuation along a passive dendrite.

    V(x) = V_0 * exp(-x / λ)
    λ = sqrt( r_m / (2 * r_i) ) where r_m and r_i are cm-normalized resistances

    Args:
        V0_mV: Voltage at injection site (mV).
        axial_resistance_Ohm_cm: Axial cytoplasmic resistivity (Ω·cm).
        membrane_resistance_kOhm_cm2: Membrane resistance (kΩ·cm²).
        axon_radius_cm: Fiber radius (cm).
        max_distance_µm: Maximum distance to compute (µm).
        n_points: Number of spatial points.

    Returns:
        CableResult with distance array and voltage array.

    Raises:
        ValueError: If any parameter is non-positive.
    """
    if V0_mV == 0:
        raise ValueError("V0_mV must be non-zero.")
    if axial_resistance_Ohm_cm <= 0:
        raise ValueError("axial_resistance must be positive.")
    if membrane_resistance_kOhm_cm2 <= 0:
        raise ValueError("membrane_resistance must be positive.")
    if axon_radius_cm <= 0:
        raise ValueError("axon_radius_cm must be positive.")
    if n_points <= 0:
        raise ValueError("n_points must be positive.")

    R_m = membrane_resistance_kOhm_cm2 * 1000.0  # Ω·cm²
    R_i = axial_resistance_Ohm_cm
    r = axon_radius_cm

    # Space constant λ (cm)
    lambda_cm = math.sqrt((R_m * r) / (2 * R_i))
    lambda_µm = lambda_cm * 1e4

    distances = [i * max_distance_µm / n_points for i in range(n_points + 1)]
    voltages = [V0_mV * math.exp(-d * 1e-4 / lambda_cm) for d in distances]

    logger.debug(f"Cable equation: λ={lambda_µm:.1f} µm")
    return CableResult(distances_µm=distances, voltages_mV=voltages, lambda_µm=lambda_µm)


# ---------------------------------------------------------------------------
# Synaptic Transmission
# ---------------------------------------------------------------------------


def synaptic_current(
    reversal_potential_mV: float,
    membrane_potential_mV: float,
    peak_conductance_nS: float,
    synapse_type: str = "excitatory",
) -> SynapticResult:
    """Compute synaptic driving force and peak current.

    I_syn = g_peak * (V_m - E_rev)

    Args:
        reversal_potential_mV: E_rev (e.g. 0 mV for AMPA, -70 mV for GABA-A).
        membrane_potential_mV: Current membrane voltage.
        peak_conductance_nS: Maximum synaptic conductance (nS).
        synapse_type: "excitatory" or "inhibitory".

    Returns:
        SynapticResult with driving force and peak current.

    Raises:
        ValueError: If peak_conductance ≤ 0.
    """
    if peak_conductance_nS <= 0:
        raise ValueError("peak_conductance_nS must be positive.")

    driving_force = membrane_potential_mV - reversal_potential_mV
    # Current in pA: g (nS) × V (mV) = nS × mV = pA  (1 nS × 1 mV = 1 pA)
    peak_current = peak_conductance_nS * driving_force

    logger.debug(f"Synapse ({synapse_type}): DF={driving_force:.1f} mV, I={peak_current:.2f} pA")
    return SynapticResult(
        reversal_potential_mV=reversal_potential_mV,
        conductance_peak_nS=peak_conductance_nS,
        membrane_potential_mV=membrane_potential_mV,
        driving_force_mV=driving_force,
        peak_current_pA=peak_current,
        synaptic_type=synapse_type,
    )


# ---------------------------------------------------------------------------
# Hebbian Plasticity
# ---------------------------------------------------------------------------


def hebbian_weight_update(
    current_weight: float,
    pre_activity: float,
    post_activity: float,
    learning_rate: float = 0.01,
    weight_max: float = 1.0,
    weight_min: float = 0.0,
) -> float:
    """Apply Hebb's rule: Δw = η * x_pre * x_post  (normalized BCM variant).

    Args:
        current_weight: Synaptic weight w ∈ [weight_min, weight_max].
        pre_activity: Presynaptic firing rate (normalized [0,1]).
        post_activity: Postsynaptic firing rate (normalized [0,1]).
        learning_rate: η.
        weight_max, weight_min: Clipping bounds.

    Returns:
        Updated synaptic weight.

    Raises:
        ValueError: If learning_rate is non-positive.
    """
    if learning_rate <= 0:
        raise ValueError("learning_rate must be positive.")
    delta_w = learning_rate * pre_activity * post_activity
    new_weight = max(weight_min, min(weight_max, current_weight + delta_w))
    return new_weight


# ---------------------------------------------------------------------------
# Brain Region Reference Data
# ---------------------------------------------------------------------------

BRAIN_REGIONS: dict[str, dict] = {
    "Cerebral Cortex": {
        "lobes": ["Frontal", "Parietal", "Temporal", "Occipital"],
        "neuron_count_billions": 16,
        "functions": ["cognition", "voluntary movement", "sensory processing", "language"],
    },
    "Cerebellum": {
        "neuron_count_billions": 70,
        "functions": ["motor coordination", "balance", "procedural learning"],
    },
    "Hippocampus": {
        "neuron_count_millions": 40,
        "functions": ["spatial navigation", "episodic memory consolidation"],
    },
    "Amygdala": {
        "neuron_count_millions": 12,
        "functions": ["fear processing", "emotional memory", "threat detection"],
    },
    "Hypothalamus": {
        "functions": ["homeostasis", "hunger/satiety", "thirst", "circadian rhythms", "hormone regulation"],
        "linked_structures": ["pituitary gland"],
    },
    "Brainstem": {
        "parts": ["Midbrain", "Pons", "Medulla oblongata"],
        "functions": ["vital reflexes (breathing, heart rate)", "cranial nerve nuclei", "reticular formation"],
    },
    "Basal Ganglia": {
        "parts": ["Striatum", "Globus pallidus", "Substantia nigra", "Subthalamic nucleus"],
        "functions": ["action selection", "procedural learning", "reward signaling"],
    },
}
