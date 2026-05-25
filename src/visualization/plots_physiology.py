"""Domain matplotlib figure generators."""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from visualization._scaffold import (
    BAR_POS,
    GRAY,
    ORANGE,
    SERIES2,
    SERIES3,
    TEAL,
    _save_figure,
)


def plot_oxygen_dissociation(
    output_dir: Path,
) -> Path:
    """Plot O2-Hb dissociation curves at different physiological conditions.

    Args:
        output_dir: Directory to save PNG.

    Returns:
        Path to saved PNG.
    """
    from biology.physiology import oxygen_dissociation_curve

    fig, ax = plt.subplots(figsize=(9, 6))

    configs: list[tuple[float, str, str, str]] = [
        (26.0, "Normal (37°C, pH 7.4)", SERIES3[0], "-"),
        (32.0, "Right-shifted (fever / exercise)", SERIES3[1], "--"),
        (20.0, "Left-shifted (fetal HbF)", SERIES3[2], "-."),
    ]

    for p50, label, color, ls in configs:
        curve = oxygen_dissociation_curve(p50_mmHg=p50, n_points=150)
        pO2s = [r.pO2_mmHg for r in curve]
        sats = [r.saturation * 100 for r in curve]
        ax.plot(pO2s, sats, color=color, linewidth=2.5, linestyle=ls, label=label)

    ax.set_xlabel("pO₂ (mmHg)", fontsize=14)
    ax.set_ylabel("Haemoglobin Saturation (%)", fontsize=14)
    ax.set_title("Oxygen-Haemoglobin Dissociation Curves", fontsize=15)
    ax.legend(fontsize=12)
    ax.set_xlim(0, 150)
    ax.set_ylim(0, 100)
    ax.axvline(100, color=GRAY, linestyle=":", linewidth=1, alpha=0.6, label="Alveolar pO₂")
    ax.axvline(40, color=ORANGE, linestyle=":", linewidth=1, alpha=0.6, label="Tissue pO₂")
    ax.tick_params(labelsize=12)
    fig.tight_layout()
    return _save_figure(fig, output_dir, "oxygen_dissociation_curve.png")


# ---------------------------------------------------------------------------
# Biochemistry — Michaelis-Menten curve
# ---------------------------------------------------------------------------


def plot_michaelis_menten(
    output_dir: Path,
    Vmax: float = 10.0,
    Km: float = 5.0,
) -> Path:
    """Plot Michaelis-Menten saturation curve with competitive inhibition overlay.

    Args:
        output_dir: Directory to save PNG.
        Vmax: Maximum reaction rate.
        Km: Michaelis constant.

    Returns:
        Path to saved PNG.
    """
    from biology.biochemistry import michaelis_menten, competitive_inhibition

    s_values = [i * 0.5 for i in range(61)]  # 0 to 30 µM

    v_normal = [michaelis_menten(s, Vmax, Km).reaction_rate for s in s_values]
    v_inhibited = [competitive_inhibition(s, Vmax, Km, inhibitor_conc=10.0, Ki=5.0).reaction_rate for s in s_values]

    fig, ax = plt.subplots(figsize=(9, 5))
    ax.plot(s_values, v_normal, color=SERIES2[0], linewidth=2.5, label="No inhibitor")
    ax.plot(
        s_values,
        v_inhibited,
        color=SERIES2[1],
        linewidth=2.5,
        linestyle="--",
        label="Competitive inhibitor ([I]=10 µM, Kᵢ=5 µM)",
    )
    ax.axhline(Vmax, color=TEAL, linewidth=1.5, linestyle=":", alpha=0.8, label=f"Vmax = {Vmax}")
    ax.axhline(Vmax / 2, color=ORANGE, linewidth=1.0, linestyle=":", alpha=0.8, label=f"Vmax/2 = {Vmax / 2}")
    ax.axvline(Km, color=ORANGE, linewidth=1.0, linestyle=":", alpha=0.8, label=f"Km = {Km} µM")
    ax.set_xlabel("[S] Substrate Concentration (µM)", fontsize=14)
    ax.set_ylabel("Reaction Rate v (µmol min⁻¹)", fontsize=14)
    ax.set_title("Michaelis-Menten Kinetics", fontsize=15)
    ax.legend(fontsize=11)
    ax.tick_params(labelsize=12)
    fig.tight_layout()
    return _save_figure(fig, output_dir, "michaelis_menten.png")


# ---------------------------------------------------------------------------
# Neuroscience — Action potential
# ---------------------------------------------------------------------------


def plot_action_potential(
    output_dir: Path,
) -> Path:
    """Plot Hodgkin-Huxley action potential simulation.

    Args:
        output_dir: Directory to save PNG.

    Returns:
        Path to saved PNG.
    """
    from biology.neuroscience import action_potential_hh

    result = action_potential_hh(stimulus_current_µA=10.0, t_end_ms=30.0, steps=3000)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(result.times_ms, result.voltage_mV, color=BAR_POS, linewidth=2.0)
    ax.axhline(
        result.threshold_mV,
        color=ORANGE,
        linewidth=1.2,
        linestyle="--",
        alpha=0.7,
        label=f"Threshold ≈ {result.threshold_mV} mV",
    )
    ax.axhline(-70, color="gray", linewidth=1.0, linestyle=":", alpha=0.5, label="Resting potential")
    ax.set_xlabel("Time (ms)", fontsize=14)
    ax.set_ylabel("Membrane Potential (mV)", fontsize=14)
    ax.set_title("Hodgkin-Huxley Action Potential Simulation", fontsize=15)
    ax.legend(fontsize=12)
    ax.tick_params(labelsize=12)
    fig.tight_layout()
    return _save_figure(fig, output_dir, "action_potential.png")


def plot_poiseuille_flow(
    output_dir: Path,
) -> Path:
    """Plot Hagen-Poiseuille flow rate sensitivity to vessel radius."""
    from biology.physiology import poiseuille_flow

    radii_um = np.linspace(5.0, 50.0, 80)
    delta_p = 1000.0
    length_m = 0.02
    flows = [
        poiseuille_flow(delta_p, r * 1e-6, length_m).volumetric_flow_mL_min for r in radii_um
    ]

    fig, ax = plt.subplots(figsize=(9, 5))
    ax.plot(radii_um, flows, color=BAR_POS, linewidth=2.4)
    ax.set_xlabel("Vessel radius (µm)", fontsize=13)
    ax.set_ylabel("Volumetric flow Q (mL min⁻¹)", fontsize=13)
    ax.set_title("Poiseuille Law — Flow Scales with r⁴", fontsize=15)
    ax.tick_params(labelsize=11)
    fig.tight_layout()
    return _save_figure(fig, output_dir, "poiseuille_flow.png")


def plot_glycolysis_summary(
    output_dir: Path,
) -> Path:
    """Bar summary of ATP and NADH yields per glycolysis step."""
    from biology.biochemistry import glycolysis_summary

    result = glycolysis_summary()
    labels = [step.name for step in result.steps]
    atp = [step.atp_yield for step in result.steps]
    nadh = [step.nadh_yield for step in result.steps]

    x = np.arange(len(labels))
    width = 0.35
    fig, ax = plt.subplots(figsize=(11, 5))
    ax.bar(x - width / 2, atp, width, label="ATP yield", color=SERIES2[0], edgecolor="black", linewidth=0.6)
    ax.bar(x + width / 2, nadh, width, label="NADH yield", color=SERIES2[1], edgecolor="black", linewidth=0.6)
    ax.set_xticks(x)
    ax.set_xticklabels(labels, rotation=35, ha="right", fontsize=9)
    ax.set_ylabel("Net yield per step", fontsize=13)
    ax.set_title(f"Glycolysis Energetics (net ATP = {result.net_atp}, net NADH = {result.net_nadh})", fontsize=14)
    ax.legend(fontsize=10, frameon=False)
    ax.tick_params(labelsize=10)
    fig.tight_layout()
    return _save_figure(fig, output_dir, "glycolysis_summary.png")


def plot_homeostasis_feedback(
    output_dir: Path,
) -> Path:
    """Simulated proportional correction of a temperature deviation toward set point."""
    from biology.physiology import homeostasis_response

    set_point = 37.0
    gain = 0.35
    measured = 39.5
    history_meas: list[float] = []
    history_corr: list[float] = []
    for _ in range(12):
        response = homeostasis_response(set_point, measured, gain=gain, tolerance=0.2)
        history_meas.append(measured)
        history_corr.append(response.corrective_response)
        measured += response.corrective_response

    steps = list(range(len(history_meas)))
    fig, ax = plt.subplots(figsize=(9, 5))
    ax.plot(steps, history_meas, color=SERIES2[0], linewidth=2.2, marker="o", label="Measured temperature")
    ax.axhline(set_point, color=ORANGE, linestyle="--", linewidth=1.2, label=f"Set point = {set_point:g} °C")
    ax2 = ax.twinx()
    ax2.bar(steps, history_corr, alpha=0.35, color=TEAL, label="Corrective response")
    ax.set_xlabel("Feedback iteration", fontsize=13)
    ax.set_ylabel("Temperature (°C)", fontsize=13)
    ax2.set_ylabel("Correction (°C)", fontsize=12)
    ax.set_title("Proportional Homeostatic Feedback", fontsize=15)
    ax.legend(loc="upper right", fontsize=10, frameon=False)
    ax.tick_params(labelsize=11)
    fig.tight_layout()
    return _save_figure(fig, output_dir, "homeostasis_feedback.png")


def plot_atp_yield_comparison(output_dir: Path) -> Path:
    """Stacked bar chart of ATP yield by catabolic pathway.

    Shows substrate-level ATP and oxidative-phosphorylation ATP for
    glycolysis, lactic-acid fermentation, the TCA cycle, and full aerobic
    respiration. Anaerobic pathways have zero oxidative ATP; full aerobic
    respiration is dominated by the oxidative contribution.

    Args:
        output_dir: Directory to save PNG.

    Returns:
        Path to the saved PNG.
    """
    from biology.biochemistry import atp_yield_by_pathway

    rows = list(atp_yield_by_pathway())
    labels = [row.pathway for row in rows]
    substrate = np.array([row.substrate_level_atp for row in rows])
    oxidative = np.array([row.oxidative_atp for row in rows])

    x = np.arange(len(rows))
    fig, ax = plt.subplots(figsize=(11, 5.5))
    ax.bar(
        x,
        substrate,
        label="Substrate-level ATP",
        color=SERIES2[0],
        edgecolor="black",
        linewidth=0.6,
    )
    ax.bar(
        x,
        oxidative,
        bottom=substrate,
        label="Oxidative phosphorylation ATP",
        color=SERIES2[1],
        edgecolor="black",
        linewidth=0.6,
    )
    totals = [row.total_atp for row in rows]
    for idx, total in enumerate(totals):
        ax.text(
            idx,
            total + 0.6,
            f"{total:.1f}",
            ha="center",
            va="bottom",
            fontsize=10,
            fontweight="bold",
        )

    ax.set_xticks(x)
    ax.set_xticklabels(labels, rotation=15, ha="right", fontsize=10)
    ax.set_ylabel("ATP yield per glucose molecule", fontsize=13)
    ax.set_title("ATP Yield Comparison Across Catabolic Pathways", fontsize=14)
    ax.legend(fontsize=10, frameon=False)
    ax.tick_params(labelsize=10)
    fig.tight_layout()
    return _save_figure(fig, output_dir, "atp_yield_comparison.png", aspect="landscape")

