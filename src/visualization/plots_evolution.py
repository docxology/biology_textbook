"""Evolution-themed matplotlib figure generators."""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from visualization._scaffold import BAR_POS, GRAY, ORANGE, SERIES2, SERIES3, _save_figure


def plot_fitness_landscape(
    output_dir: Path,
) -> Path:
    """Plot mean population fitness as a function of allele frequency."""
    from biology.evolution import fitness_landscape_1d

    p_values = np.linspace(0.0, 1.0, 120)
    scenarios = [
        ("Directional selection", 1.0, 0.9, 0.5, SERIES3[0], "-"),
        ("Heterozygote advantage", 0.75, 1.0, 0.75, SERIES3[1], "--"),
        ("Underdominance", 1.0, 0.55, 1.0, SERIES3[2], "-."),
    ]

    fig, ax = plt.subplots(figsize=(9, 5))
    for title, w_aa, w_aba, w_aa_rec, color, linestyle in scenarios:
        fitness = fitness_landscape_1d(p_values.tolist(), w_aa, w_aba, w_aa_rec)
        ax.plot(p_values, fitness, color=color, linewidth=2.2, linestyle=linestyle, label=title)
    ax.axvline(0.5, color=GRAY, linestyle=":", linewidth=1.0, alpha=0.75)
    ax.set_xlabel("Allele A frequency (p)", fontsize=13)
    ax.set_ylabel("Mean fitness W̄", fontsize=13)
    ax.set_title("One-Locus Mean Fitness Landscapes", fontsize=15)
    ax.set_xlim(0, 1)
    ax.legend(fontsize=10, frameon=False)
    ax.tick_params(labelsize=11)
    fig.tight_layout()
    return _save_figure(fig, output_dir, "fitness_landscape.png")


def plot_molecular_clock(
    output_dir: Path,
) -> Path:
    """Bar chart of divergence times from substitution rates and sequence divergence."""
    from biology.evolution import molecular_clock_divergence_time

    cases = [
        ("Primates vs rodents", 1.0e-9, 0.12),
        ("Divergent bird lineages", 2.0e-9, 0.08),
        ("Plant sister genera", 6.0e-9, 0.05),
        ("Bacterial strains", 5.0e-8, 0.02),
    ]
    labels = [c[0] for c in cases]
    times_myr = [
        molecular_clock_divergence_time(rate, div) / 1.0e6 for _, rate, div in cases
    ]

    fig, ax = plt.subplots(figsize=(9, 5))
    colors = [BAR_POS, SERIES2[0], SERIES2[1], ORANGE]
    ax.barh(labels, times_myr, color=colors, edgecolor="black", linewidth=0.8)
    ax.set_xlabel("Estimated divergence time (million years)", fontsize=13)
    ax.set_title("Molecular Clock Divergence Estimates", fontsize=15)
    ax.tick_params(labelsize=11)
    fig.tight_layout()
    return _save_figure(fig, output_dir, "molecular_clock.png")
