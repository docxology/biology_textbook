"""Domain matplotlib figure generators."""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from visualization._scaffold import (
    BAR_POS,
    GRAY,
    ORANGE,
    PURPLE,
    SERIES2,
    SERIES3,
    TEAL,
    _save_figure,
)


def plot_lotka_volterra(
    output_dir: Path,
    prey0: float = 40.0,
    predator0: float = 9.0,
    alpha: float = 0.5,
    beta: float = 0.02,
    delta: float = 0.01,
    gamma: float = 0.2,
    t_end: float = 100.0,
) -> Path:
    """Plot Lotka-Volterra predator-prey dynamics.

    Args:
        output_dir: Directory to save PNG.
        All other args: LV parameters.

    Returns:
        Path to saved PNG.
    """
    from biology.ecology import lotka_volterra

    # Fine fixed Euler grid reduces, but does not eliminate, invariant drift.
    # The ODE's closed orbit is not an exact property of this discretization.
    result = lotka_volterra(prey0, predator0, alpha, beta, delta, gamma, t_end, steps=100000)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5))

    # Time series (hue + line style for CVD)
    ax1.plot(result.times, result.prey, color=SERIES2[0], linewidth=2, linestyle="-", label="Prey")
    ax1.plot(result.times, result.predator, color=SERIES2[1], linewidth=2, linestyle="--", label="Predator")
    ax1.set_xlabel("Time", fontsize=14)
    ax1.set_ylabel("Population", fontsize=14)
    ax1.set_title("Lotka-Volterra Dynamics", fontsize=15)
    ax1.legend(fontsize=12)
    ax1.tick_params(labelsize=12)

    # Phase plane
    ax2.plot(result.prey, result.predator, color=PURPLE, linewidth=1.5, alpha=0.85)
    ax2.scatter([result.prey[0]], [result.predator[0]], color=ORANGE, zorder=5, s=80, label="Start")
    ax2.set_xlabel("Prey Population", fontsize=14)
    ax2.set_ylabel("Predator Population", fontsize=14)
    ax2.set_title("Phase Plane (Euler approximation)", fontsize=15)
    ax2.legend(fontsize=12)
    ax2.tick_params(labelsize=12)

    fig.suptitle("Predator-Prey Dynamics — Lotka-Volterra", fontsize=16, fontweight="bold")
    fig.tight_layout()
    return _save_figure(fig, output_dir, "lotka_volterra.png", aspect="landscape")


# ---------------------------------------------------------------------------
# Evolution — Allele frequency under selection
# ---------------------------------------------------------------------------


def plot_logistic_growth(
    output_dir: Path,
    N0: float = 50.0,
    r: float = 0.15,
    K: float = 1000.0,
    t_end: float = 80.0,
) -> Path:
    """Plot logistic population growth from ``biology.ecology.logistic_growth``."""
    from biology.ecology import logistic_growth

    result = logistic_growth(N0=N0, r=r, K=K, t_end=t_end, steps=400)

    fig, ax = plt.subplots(figsize=(9, 5))
    ax.plot(result.times, result.populations, color=BAR_POS, linewidth=2.2, label="N(t)")
    ax.axhline(K, color=ORANGE, linestyle="--", linewidth=1.2, alpha=0.85, label=f"K = {K:g}")
    ax.set_xlabel("Time (arbitrary units)", fontsize=14)
    ax.set_ylabel("Population size N", fontsize=14)
    ax.set_title("Logistic Growth — dN/dt = rN(1 − N/K)", fontsize=15)
    ax.legend(fontsize=12)
    ax.tick_params(labelsize=12)
    fig.tight_layout()
    return _save_figure(fig, output_dir, "logistic_growth.png", aspect="landscape")


def plot_species_area_relationship(
    output_dir: Path,
    c: float = 2.5,
    z: float = 0.25,
) -> Path:
    """Log-log plot of mainland and island species-area scaling."""
    from biology.ecology import species_area_relationship

    areas = np.logspace(0.0, 4.0, 80)
    scenarios = [
        ("Mainland fragments (z = 0.15)", 7.0, 0.15, SERIES2[0], "-"),
        ("Oceanic islands (z = 0.35)", 7.0, 0.35, SERIES2[1], "--"),
    ]

    fig, ax = plt.subplots(figsize=(8, 5))
    for label, c_value, z_value, color, linestyle in scenarios:
        richness = [species_area_relationship(float(a), c_value, z_value) for a in areas]
        ax.loglog(areas, richness, color=color, linewidth=2.2, linestyle=linestyle, label=label)
    reference = [species_area_relationship(float(a), c, z) for a in areas]
    ax.loglog(areas, reference, color=TEAL, linewidth=1.3, linestyle=":", label=f"Reference z = {z:g}")
    ax.set_xlabel("Habitat area A (km^2, log scale)", fontsize=14)
    ax.set_ylabel("Species richness S", fontsize=14)
    ax.set_title("Species-Area Relationship: Mainland vs Island Slopes", fontsize=15)
    ax.legend(fontsize=10, frameon=False)
    ax.tick_params(labelsize=12)
    fig.tight_layout()
    return _save_figure(fig, output_dir, "species_area_relationship.png", aspect="landscape")


def plot_biome_distribution(
    output_dir: Path,
) -> Path:
    """Illustrative terrestrial climate coordinates; exclude inapplicable rainfall."""
    from biology.ecology import BIOMES

    names = [name for name, data in BIOMES.items() if data["annual_precipitation_mm"] is not None]
    temps = [float(BIOMES[b]["mean_annual_temp_C"]) for b in names]
    precip = [float(BIOMES[b]["annual_precipitation_mm"]) for b in names]

    fig, ax = plt.subplots(figsize=(9, 5.5))
    ax.scatter(precip, temps, s=110, color=BAR_POS, edgecolor="black", linewidth=0.8, alpha=0.86)
    rightmost_precipitation = max(precip)
    for name, x_val, y_val in zip(names, precip, temps):
        ax.annotate(
            name,
            (x_val, y_val),
            xytext=(-8 if x_val == rightmost_precipitation else 8, 8),
            textcoords="offset points",
            ha="right" if x_val == rightmost_precipitation else "left",
            fontsize=10,
            bbox={"boxstyle": "round,pad=0.18", "facecolor": "white", "edgecolor": "#dddddd", "alpha": 0.78},
        )
    ax.set_xlabel("Mean annual precipitation (mm/year)", fontsize=13)
    ax.set_ylabel("Mean annual temperature (°C)", fontsize=13)
    ax.set_title("Illustrative Terrestrial Biome Climate Coordinates", fontsize=14)
    ax.grid(True, color="#dddddd", linewidth=0.6, alpha=0.7)
    ax.tick_params(labelsize=11)
    ax.text(0.02, 0.02, "Illustrative coordinates; equal marker sizes", transform=ax.transAxes, fontsize=10)
    fig.tight_layout()
    return _save_figure(fig, output_dir, "biome_distribution.png")


def plot_allee_threshold_dynamics(
    output_dir: Path,
) -> Path:
    """Plot strong-Allee threshold trajectories below and above A."""
    from biology.ecology import allee_strong_growth

    A = 100.0
    K = 800.0
    starts = [
        (40.0, "N0 below A: extinction basin", SERIES3[0], "-"),
        (100.0, "N0 at A: unstable threshold", SERIES3[1], "--"),
        (180.0, "N0 above A: recovery", SERIES3[2], "-."),
    ]

    fig, ax = plt.subplots(figsize=(9, 5.2))
    for N0, label, color, linestyle in starts:
        result = allee_strong_growth(N0=N0, r=0.035, A=A, K=K, t_end=160.0, steps=600)
        ax.plot(result.times, result.populations, color=color, linestyle=linestyle, linewidth=2.2, label=label)
    ax.axhline(A, color=ORANGE, linestyle=":", linewidth=1.4, label=f"Allee threshold A = {A:g}")
    ax.axhline(K, color=GRAY, linestyle="--", linewidth=1.0, alpha=0.8, label=f"Carrying capacity K = {K:g}")
    ax.set_xlabel("Time", fontsize=13)
    ax.set_ylabel("Population size N", fontsize=13)
    ax.set_title("Strong Allee-Effect Threshold Dynamics", fontsize=15)
    ax.set_ylim(0, K * 1.08)
    ax.legend(fontsize=10, frameon=False)
    ax.tick_params(labelsize=11)
    fig.tight_layout()
    return _save_figure(fig, output_dir, "allee_threshold_dynamics.png")


def plot_biodiversity_indices(
    output_dir: Path,
) -> Path:
    """Compare Shannon and Simpson indices for two hand-entered teaching scenarios."""
    from biology.ecology import biodiversity_indices

    communities = {
        "Even meadow": [50, 48, 52, 49, 51],
        "Dominant grassland": [200, 15, 8, 5, 3],
    }
    labels = list(communities.keys())
    shannon = [biodiversity_indices(counts).shannon_index for counts in communities.values()]
    simpson = [biodiversity_indices(counts).simpson_index for counts in communities.values()]

    fig, axes = plt.subplots(1, 2, figsize=(10, 5))
    for ax, values, title, units in zip(
        axes, (shannon, simpson), ("Shannon entropy H′", "Simpson diversity 1 − D"), ("nats", "dimensionless"),
    ):
        bars = ax.bar(labels, values, color=SERIES2, edgecolor="black", linewidth=0.8)
        for bar, hatch, value in zip(bars, ("///", "..."), values):
            bar.set_hatch(hatch)
            ax.annotate(f"{value:.2f}", (bar.get_x() + bar.get_width() / 2, bar.get_height()),
                        xytext=(0, 5), textcoords="offset points", ha="center", fontsize=11)
        ax.set_title(title, fontsize=13)
        ax.set_ylabel(units, fontsize=12)
        ax.tick_params(labelsize=10)
        ax.margins(y=0.18)
    fig.suptitle("Illustrative Five-Species Communities: Equal Richness, Different Evenness", fontsize=13)
    fig.tight_layout()
    return _save_figure(fig, output_dir, "biodiversity_indices.png", aspect="landscape")


def plot_food_web_trophic_levels(
    output_dir: Path,
) -> Path:
    """Horizontal bar chart of trophic levels from a simple food-web adjacency list."""
    from biology.ecology import food_web_trophic_levels

    adjacency = {
        "Phytoplankton": [],
        "Zooplankton": ["Phytoplankton"],
        "Small fish": ["Zooplankton"],
        "Large fish": ["Small fish"],
        "Apex predator": ["Large fish"],
    }
    levels = food_web_trophic_levels(adjacency)
    species = list(levels.keys())
    trophic = [levels[sp] for sp in species]
    colors = [SERIES3[min(lv - 1, 2)] for lv in trophic]

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.barh(species, trophic, color=colors, edgecolor="black", linewidth=0.6)
    ax.set_xlabel("Trophic level", fontsize=13)
    ax.set_title("Food-Web Trophic Levels (BFS from Producers)", fontsize=14)
    ax.tick_params(labelsize=11)
    fig.tight_layout()
    return _save_figure(fig, output_dir, "food_web_trophic_levels.png", aspect="landscape")
