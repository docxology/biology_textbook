"""Domain matplotlib figure generators."""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt

from visualization._scaffold import (
    BAR_POS,
    ORANGE,
    SERIES2,
    _save_figure,
)


def plot_bacterial_growth(
    output_dir: Path,
) -> Path:
    """Plot a complete bacterial growth curve with lag, log, and stationary phases.

    Args:
        output_dir: Directory to save PNG.

    Returns:
        Path to saved PNG.
    """
    from biology.microbiology import bacterial_growth_curve

    result = bacterial_growth_curve(
        N0=1e4,
        doubling_time_hr=0.5,
        t_end_hr=10.0,
        steps=300,
        lag_phase_hr=1.0,
        stationary_phase_start_hr=7.0,
        carrying_capacity=5e9,
    )

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    ax1.plot(result.times_hr, result.populations, color=SERIES2[0], linewidth=2.0)
    ax1.set_xlabel("Time (hours)", fontsize=14)
    ax1.set_ylabel("Population (cells)", fontsize=14)
    ax1.set_title("Bacterial Growth Curve (Linear)", fontsize=14)
    ax1.tick_params(labelsize=12)

    ax2.plot(result.times_hr, result.log_populations, color=SERIES2[1], linewidth=2.0, linestyle="--")
    ax2.set_xlabel("Time (hours)", fontsize=14)
    ax2.set_ylabel("log₁₀ (Population)", fontsize=14)
    ax2.set_title("Bacterial Growth Curve (Log Scale)", fontsize=14)
    ax2.tick_params(labelsize=12)

    fig.suptitle(f"Bacterial Growth: t_d = {result.doubling_time_hr} h", fontsize=15)
    fig.tight_layout()
    return _save_figure(fig, output_dir, "bacterial_growth.png")


def plot_sir_model(
    output_dir: Path,
) -> Path:
    """Plot SIR epidemic compartment trajectories."""
    from biology.microbiology import sir_model

    result = sir_model(
        population=10000,
        initial_infected=25,
        beta_per_day=0.45,
        gamma_per_day=0.12,
        days=180,
        steps_per_day=4,
    )

    fig, ax = plt.subplots(figsize=(9, 5))
    ax.plot(result.times_days, result.susceptible, color=SERIES2[0], linewidth=2.2, linestyle="-", label="Susceptible")
    ax.plot(result.times_days, result.infected, color=SERIES2[1], linewidth=2.2, linestyle="--", label="Infected")
    ax.plot(result.times_days, result.recovered, color=ORANGE, linewidth=2.2, linestyle="-.", label="Recovered")
    ax.set_xlabel("Time (days)", fontsize=13)
    ax.set_ylabel("Population (individuals)", fontsize=13)
    ax.set_title(f"SIR Epidemic Dynamics (R₀ ≈ {result.r0:.2f})", fontsize=15)
    ax.legend(fontsize=10, frameon=False)
    ax.tick_params(labelsize=11)
    fig.tight_layout()
    return _save_figure(fig, output_dir, "sir_model.png")


def plot_mic_dilution_series(
    output_dir: Path,
) -> Path:
    """Bar chart of serial broth-dilution antibiotic concentrations."""
    from biology.microbiology import mic_fold_dilution

    concentrations = mic_fold_dilution(starting_concentration_ug_mL=128.0, dilution_factor=2, n_tubes=8)
    labels = [f"Tube {i + 1}" for i in range(len(concentrations))]

    fig, ax = plt.subplots(figsize=(9, 4.5))
    ax.bar(labels, concentrations, color=BAR_POS, edgecolor="black", linewidth=0.8)
    ax.set_yscale("log")
    ax.set_ylabel("Antibiotic concentration (µg mL⁻¹)", fontsize=13)
    ax.set_xlabel("Serial dilution tube", fontsize=13)
    ax.set_title("MIC Broth Dilution Series (2-fold)", fontsize=15)
    ax.tick_params(labelsize=10)
    fig.tight_layout()
    return _save_figure(fig, output_dir, "mic_dilution_series.png")

