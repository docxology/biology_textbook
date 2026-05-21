"""Visualization subpackage — matplotlib scientific figure generators.

All visualizers:
- Return pathlib.Path to saved PNG
- Never open display windows
- Require MPLBACKEND=Agg (set in conftest.py)
- Use real biological data / computations from src/biology modules
"""

from __future__ import annotations

from collections.abc import Callable
import os

os.environ.setdefault("MPLBACKEND", "Agg")

from pathlib import Path
from typing import Optional

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

from infrastructure.core.logging.utils import get_logger

from .cvd import (
    BAR_NEG,
    BAR_POS,
    GRAY,
    ORANGE,
    PUNNETT_DOMINANT,
    PUNNETT_RECESSIVE,
    PURPLE,
    SERIES2,
    SERIES3,
    TEAL,
)

logger = get_logger(__name__)


def _save_figure(fig: "plt.Figure", output_dir: Path, filename: str) -> Path:
    """Save a matplotlib figure to disk and close it."""
    output_dir.mkdir(parents=True, exist_ok=True)
    path = output_dir / filename
    fig.savefig(path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    logger.info(f"Saved figure: {path}")
    return path


# ---------------------------------------------------------------------------
# Cell Biology — Nernst / membrane potential curves
# ---------------------------------------------------------------------------


def plot_nernst_potentials(
    output_dir: Path,
    ions: Optional[list] = None,
) -> Path:
    """Bar chart of Nernst equilibrium potentials for physiological ions.

    Args:
        output_dir: Directory to save PNG.
        ions: Optional list of IonConcentration objects. Defaults to PHYSIOLOGICAL_IONS.

    Returns:
        Path to saved PNG.
    """
    from biology.cell import PHYSIOLOGICAL_IONS, nernst_potential

    if ions is None:
        ions = [i for i in PHYSIOLOGICAL_IONS if i.charge != 0]

    labels = []
    potentials = []
    for ion in ions:
        if ion.inside_mM <= 0 or ion.outside_mM <= 0 or ion.charge == 0:
            logger.warning(f"Skipping invalid ion for Nernst plot: {ion.ion}")
            continue
        e = nernst_potential(ion)
        labels.append(ion.ion)
        potentials.append(e)

    fig, ax = plt.subplots(figsize=(7, 4))
    colors = [BAR_POS if v > 0 else BAR_NEG for v in potentials]
    ax.bar(labels, potentials, color=colors, edgecolor="black", linewidth=0.8)
    ax.axhline(0, color="black", linewidth=0.8, linestyle="--")
    ax.set_xlabel("Ion", fontsize=14)
    ax.set_ylabel("Nernst Potential (mV)", fontsize=14)
    ax.set_title("Nernst Equilibrium Potentials — Physiological Ions", fontsize=15)
    ax.tick_params(labelsize=12)
    fig.tight_layout()
    return _save_figure(fig, output_dir, "nernst_potentials.png")


# ---------------------------------------------------------------------------
# Genetics — Punnett square heatmap
# ---------------------------------------------------------------------------


def plot_punnett_square(
    parent1: str,
    parent2: str,
    output_dir: Path,
) -> Path:
    """Visualise a monohybrid Punnett square as a 2D grid.

    Args:
        parent1: Genotype of parent 1 (e.g. 'Aa').
        parent2: Genotype of parent 2 (e.g. 'Aa').
        output_dir: Directory to save PNG.

    Returns:
        Path to saved PNG.
    """
    from biology.genetics import punnett_square

    punnett_square(parent1, parent2)

    def gametes(geno: str) -> list[str]:
        """Generate the set of unique gametes from a diploid genotype string.

        Args:
            geno: Two-character genotype string (e.g. ``"Aa"``, ``"BB"``).

        Returns:
            List of unique allele characters. Homozygous genotypes return a
            single-element list; heterozygous genotypes return two elements.
        """
        a, b = geno[0], geno[1]
        return [a] if a == b else [a, b]

    g1 = gametes(parent1)
    g2 = gametes(parent2)
    n1, n2 = len(g1), len(g2)

    fig, ax = plt.subplots(figsize=(max(3, n2 + 1), max(3, n1 + 1)))
    ax.set_xlim(0, n2 + 1)
    ax.set_ylim(0, n1 + 1)

    for i, ga in enumerate(g1):
        for j, gb in enumerate(g2):
            geno = f"{ga}{gb}" if ga.isupper() or not gb.isupper() else f"{gb}{ga}"
            dom = bool(geno[0].isupper() or geno[1].isupper())
            color = PUNNETT_DOMINANT if dom else PUNNETT_RECESSIVE
            hatch = "///" if dom else "..."
            rect = mpatches.FancyBboxPatch(
                (j + 0.05, n1 - i - 1 + 0.05),
                0.9,
                0.9,
                boxstyle="round,pad=0.05",
                facecolor=color,
                edgecolor="#333333",
                linewidth=1.2,
                hatch=hatch,
            )
            ax.add_patch(rect)
            ax.text(j + 0.5, n1 - i - 0.5, geno, ha="center", va="center", fontsize=16, fontweight="bold")

    for j, gb in enumerate(g2):
        ax.text(j + 0.5, n1 + 0.5, gb, ha="center", va="center", fontsize=14, color=BAR_POS)
    for i, ga in enumerate(g1):
        ax.text(-0.3, n1 - i - 0.5, ga, ha="center", va="center", fontsize=14, color=BAR_POS)

    ax.axis("off")
    ax.set_title(f"Punnett Square: {parent1} × {parent2}", fontsize=15, pad=18)
    fig.tight_layout()
    return _save_figure(fig, output_dir, f"punnett_{parent1}x{parent2}.png")


# ---------------------------------------------------------------------------
# Genetics — metaphase chromosome schematic
# ---------------------------------------------------------------------------


def plot_chromosome_structure(output_dir: Path) -> Path:
    """Draw a labelled metaphase chromosome with core architectural features."""
    fig, ax = plt.subplots(figsize=(9, 5.4))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.axis("off")

    arm_color = PUNNETT_DOMINANT
    heterochromatin_color = PUNNETT_RECESSIVE
    telomere_color = ORANGE
    centromere_color = PURPLE

    # Sister chromatids, drawn as broad rounded traces.
    chromatid_segments = [
        ((3.0, 5.0), (4.7, 3.0)),
        ((3.0, 1.0), (4.7, 3.0)),
        ((7.0, 5.0), (5.3, 3.0)),
        ((7.0, 1.0), (5.3, 3.0)),
    ]
    for (x0, y0), (x1, y1) in chromatid_segments:
        ax.plot(
            [x0, x1],
            [y0, y1],
            color=arm_color,
            linewidth=22,
            solid_capstyle="round",
            alpha=0.92,
        )

    # Pericentromeric heterochromatin bands.
    heterochromatin_segments = [
        ((3.95, 3.9), (4.7, 3.0)),
        ((3.95, 2.1), (4.7, 3.0)),
        ((6.05, 3.9), (5.3, 3.0)),
        ((6.05, 2.1), (5.3, 3.0)),
    ]
    for (x0, y0), (x1, y1) in heterochromatin_segments:
        ax.plot(
            [x0, x1],
            [y0, y1],
            color=heterochromatin_color,
            linewidth=24,
            solid_capstyle="round",
            alpha=0.85,
        )

    # Telomere caps at chromosome ends.
    for x, y in [(3.0, 5.0), (7.0, 5.0), (3.0, 1.0), (7.0, 1.0)]:
        cap = mpatches.Circle((x, y), radius=0.25, facecolor=telomere_color, edgecolor="black", linewidth=0.8)
        ax.add_patch(cap)

    # Centromere and kinetochore disks.
    ax.add_patch(mpatches.Ellipse((5.0, 3.0), 1.35, 0.85, facecolor=centromere_color, edgecolor="black", lw=1.0))
    ax.add_patch(mpatches.Circle((4.62, 3.0), radius=0.14, facecolor="white", edgecolor="black", linewidth=0.7))
    ax.add_patch(mpatches.Circle((5.38, 3.0), radius=0.14, facecolor="white", edgecolor="black", linewidth=0.7))

    labels = [
        ("Telomeres\nTTAGGG repeats", (1.4, 5.25), (2.75, 5.05)),
        ("Sister chromatids", (1.25, 0.65), (3.1, 1.05)),
        ("Centromere\nCENP-A chromatin", (7.1, 3.2), (5.55, 3.0)),
        ("Kinetochore\nmicrotubule interface", (7.1, 2.15), (5.38, 3.0)),
        ("Pericentromeric\nheterochromatin", (1.2, 3.25), (4.0, 3.55)),
        ("Euchromatic arms\ngene-rich regions", (7.05, 4.75), (6.1, 4.0)),
    ]
    for text, xytext, xy in labels:
        ax.annotate(
            text,
            xy=xy,
            xytext=xytext,
            fontsize=10.5,
            ha="center",
            va="center",
            arrowprops={"arrowstyle": "->", "color": GRAY, "lw": 1.1},
            bbox={"boxstyle": "round,pad=0.3", "facecolor": "white", "edgecolor": "#cccccc", "alpha": 0.92},
        )

    legend_handles = [
        mpatches.Patch(facecolor=arm_color, edgecolor="black", label="Euchromatin"),
        mpatches.Patch(facecolor=heterochromatin_color, edgecolor="black", label="Heterochromatin"),
        mpatches.Patch(facecolor=telomere_color, edgecolor="black", label="Telomere caps"),
        mpatches.Patch(facecolor=centromere_color, edgecolor="black", label="Centromere"),
    ]
    ax.legend(handles=legend_handles, loc="lower center", ncol=4, frameon=False, fontsize=9.5)
    ax.set_title("Metaphase Chromosome Architecture", fontsize=16, fontweight="bold", pad=8)
    fig.tight_layout()
    return _save_figure(fig, output_dir, "chromosome_structure.png")


# ---------------------------------------------------------------------------
# Ecology — Lotka-Volterra phase plane
# ---------------------------------------------------------------------------


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

    result = lotka_volterra(prey0, predator0, alpha, beta, delta, gamma, t_end)

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
    ax2.set_title("Phase Plane (Prey vs Predator)", fontsize=15)
    ax2.legend(fontsize=12)
    ax2.tick_params(labelsize=12)

    fig.suptitle("Predator-Prey Dynamics — Lotka-Volterra", fontsize=16, fontweight="bold")
    fig.tight_layout()
    return _save_figure(fig, output_dir, "lotka_volterra.png")


# ---------------------------------------------------------------------------
# Evolution — Allele frequency under selection
# ---------------------------------------------------------------------------


def plot_selection_simulation(
    output_dir: Path,
    fitness_AA: float = 1.0,
    fitness_Aa: float = 0.9,
    fitness_aa: float = 0.5,
    p0: float = 0.1,
    generations: int = 50,
) -> Path:
    """Plot allele frequency change under multiple selection regimes.

    Args:
        output_dir: Directory to save PNG.

    Returns:
        Path to saved PNG.
    """
    from biology.evolution import Population, simulate_selection

    regimes = [
        (
            "Directional selection",
            [
                (
                    Population(
                        "Directional",
                        p=p0,
                        q=1.0 - p0,
                        fitness_AA=fitness_AA,
                        fitness_Aa=fitness_Aa,
                        fitness_aa=fitness_aa,
                    ),
                    "favoured A",
                    SERIES2[0],
                    "-",
                ),
            ],
            "wAA > wAa > waa",
        ),
        (
            "Stabilising / balancing",
            [
                (
                    Population("Balancing", p=0.2, q=0.8, fitness_AA=0.75, fitness_Aa=1.0, fitness_aa=0.75),
                    "from p0 = 0.2",
                    SERIES2[0],
                    "-",
                ),
                (
                    Population("Balancing", p=0.8, q=0.2, fitness_AA=0.75, fitness_Aa=1.0, fitness_aa=0.75),
                    "from p0 = 0.8",
                    SERIES2[1],
                    "--",
                ),
            ],
            "heterozygote advantage",
        ),
        (
            "Disruptive / underdominance",
            [
                (
                    Population("Underdominance", p=0.35, q=0.65, fitness_AA=1.0, fitness_Aa=0.55, fitness_aa=1.0),
                    "below threshold",
                    SERIES2[0],
                    "-",
                ),
                (
                    Population("Underdominance", p=0.65, q=0.35, fitness_AA=1.0, fitness_Aa=0.55, fitness_aa=1.0),
                    "above threshold",
                    SERIES2[1],
                    "--",
                ),
            ],
            "heterozygote disadvantage",
        ),
    ]

    fig, axes = plt.subplots(1, 3, figsize=(11, 4.8), sharex=True, sharey=True)
    for ax, (title, populations, subtitle) in zip(axes, regimes):
        for pop, label, color, linestyle in populations:
            results = simulate_selection(pop, generations)
            gen_num = [0, *[r.generation for r in results]]
            p_vals = [pop.p, *[r.p for r in results]]
            ax.plot(gen_num, p_vals, color=color, linewidth=2.2, linestyle=linestyle, label=label)
        ax.axhline(0.5, color=GRAY, linestyle=":", linewidth=1, alpha=0.75)
        ax.set_title(f"{title}\n{subtitle}", fontsize=11.5)
        ax.set_xlabel("Generation", fontsize=11)
        ax.set_ylim(0, 1)
        ax.tick_params(labelsize=10)
        ax.legend(fontsize=9, frameon=False, loc="best")
    axes[0].set_ylabel("Allele A frequency (p)", fontsize=11)
    fig.suptitle("Allele-Frequency Trajectories Under Three Selection Modes", fontsize=14, fontweight="bold")
    fig.tight_layout()
    return _save_figure(fig, output_dir, "selection_simulation.png")


# ---------------------------------------------------------------------------
# Physiology — Oxygen-haemoglobin dissociation curve
# ---------------------------------------------------------------------------


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


# ---------------------------------------------------------------------------
# Botany — Photosynthesis light response
# ---------------------------------------------------------------------------


def plot_light_response_curve(
    output_dir: Path,
) -> Path:
    """Plot photosynthesis light-response curves for C3, C4, and CAM plants.

    Args:
        output_dir: Directory to save PNG.

    Returns:
        Path to saved PNG.
    """
    from biology.botany import light_response_curve

    fig, ax = plt.subplots(figsize=(9, 5))

    pathways: list[tuple[str, float, float, float, str, str]] = [
        ("C3", 20.0, 500.0, 1.5, SERIES3[0], "-"),
        ("C4", 35.0, 1500.0, 2.0, SERIES3[1], "--"),
        ("CAM", 15.0, 800.0, 1.0, SERIES3[2], "-."),
    ]
    for label, amax, light_sat, rd, color, ls in pathways:
        curve = light_response_curve(amax, light_sat, rd, n_points=80, max_par=2100.0)
        pars = [x for x, _ in curve]
        rates = [y for _, y in curve]
        ax.plot(pars, rates, color=color, linewidth=2.5, linestyle=ls, label=label)

    ax.axhline(0, color="black", linewidth=0.8, linestyle="--")
    ax.set_xlabel("Photon Flux Density, PAR (µmol m⁻² s⁻¹)", fontsize=14)
    ax.set_ylabel("Net Photosynthesis A_net (µmol CO₂ m⁻² s⁻¹)", fontsize=14)
    ax.set_title("Photosynthesis Light-Response Curves: C3, C4, CAM", fontsize=15)
    ax.legend(fontsize=12)
    ax.tick_params(labelsize=12)
    fig.tight_layout()
    return _save_figure(fig, output_dir, "light_response_curves.png")


# ---------------------------------------------------------------------------
# Microbiology — Bacterial growth curve
# ---------------------------------------------------------------------------


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


# ---------------------------------------------------------------------------
# Epigenetics — CpG methylation heatmap (synthetic deterministic pattern)
# ---------------------------------------------------------------------------


def plot_methylation_heatmap(
    output_dir: Path,
) -> Path:
    """Heatmap of synthetic CpG methylation (β values) across loci and samples.

    Uses a fixed RNG seed for reproducible pedagogy; not patient data.

    Args:
        output_dir: Directory to save PNG.

    Returns:
        Path to saved PNG.
    """
    rng = np.random.default_rng(42)
    n_loci, n_samples = 24, 8
    base = rng.uniform(0.15, 0.85, size=(n_loci, n_samples))
    # Simulate partially methylated promoter region (rows 8–14)
    base[8:15, :] *= 0.4
    beta = np.clip(base, 0.0, 1.0)

    fig, ax = plt.subplots(figsize=(8, 6))
    im = ax.imshow(beta, aspect="auto", cmap="viridis", vmin=0.0, vmax=1.0)
    ax.set_xlabel("Sample index", fontsize=12)
    ax.set_ylabel("CpG locus index", fontsize=12)
    ax.set_title("Synthetic CpG Methylation (β) — Illustrative Heatmap", fontsize=13)
    cbar = fig.colorbar(im, ax=ax, fraction=0.046, pad=0.04)
    cbar.set_label("β (methylation fraction)", fontsize=11)
    ax.tick_params(labelsize=10)
    fig.tight_layout()
    return _save_figure(fig, output_dir, "methylation_heatmap.png")


# ---------------------------------------------------------------------------
# Cell Biology — GHK permeability sensitivity
# ---------------------------------------------------------------------------


def plot_ghk_permeability(
    output_dir: Path,
) -> Path:
    """Plot Goldman-Hodgkin-Katz voltage sensitivity to Na+ permeability."""
    from biology.cell import IonConcentration, goldman_equation

    ions = [
        IonConcentration(ion="K+", charge=1, inside_mM=140.0, outside_mM=5.0),
        IonConcentration(ion="Na+", charge=1, inside_mM=15.0, outside_mM=145.0),
        IonConcentration(ion="Cl-", charge=-1, inside_mM=10.0, outside_mM=110.0),
    ]
    p_na_ratios = np.logspace(-2.0, 0.2, 120)
    p_cl_values = [0.15, 0.45, 0.90]

    fig, ax = plt.subplots(figsize=(9, 5))
    styles = [("-", SERIES3[0]), ("--", SERIES3[1]), ("-.", SERIES3[2])]
    for p_cl, (linestyle, color) in zip(p_cl_values, styles):
        potentials = [
            goldman_equation(ions, [1.0, float(p_na), p_cl])
            for p_na in p_na_ratios
        ]
        ax.plot(
            p_na_ratios,
            potentials,
            color=color,
            linestyle=linestyle,
            linewidth=2.2,
            label=f"PCl/PK = {p_cl:g}",
        )

    ax.axhline(-70, color=GRAY, linestyle=":", linewidth=1.1, alpha=0.85, label="typical resting Vm")
    ax.axvline(0.04, color=ORANGE, linestyle=":", linewidth=1.1, alpha=0.85, label="resting PNa/PK")
    ax.set_xscale("log")
    ax.set_xlabel("Relative sodium permeability, PNa / PK", fontsize=13)
    ax.set_ylabel("GHK membrane potential Vm (mV)", fontsize=13)
    ax.set_title("Goldman-Hodgkin-Katz Permeability Sensitivity", fontsize=15)
    ax.legend(fontsize=10, frameon=False)
    ax.tick_params(labelsize=11)
    fig.tight_layout()
    return _save_figure(fig, output_dir, "ghk_permeability.png")


# ---------------------------------------------------------------------------
# Botany — water potential and transpiration
# ---------------------------------------------------------------------------


def plot_water_potential_transpiration(
    output_dir: Path,
) -> Path:
    """Plot plant water potential components and transpiration flux."""
    from biology.botany import transpiration_flux, water_potential

    solutes = np.linspace(0.05, 0.60, 90)
    psi_s = []
    psi_total = []
    for concentration in solutes:
        result = water_potential(float(concentration), turgor_pressure_MPa=0.5)
        psi_s.append(result.osmotic_potential_MPa)
        psi_total.append(result.water_potential_MPa)

    external_vapor = np.linspace(0.30, 0.50, 90)
    conductances = [0.10, 0.20, 0.35]

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11.5, 5))
    ax1.plot(solutes, psi_s, color=SERIES2[0], linewidth=2.2, label="solute potential psi_s")
    ax1.plot(solutes, psi_total, color=SERIES2[1], linestyle="--", linewidth=2.2, label="total psi at psi_p=0.5 MPa")
    ax1.axhline(0, color=GRAY, linewidth=0.9, linestyle=":")
    ax1.set_xlabel("Solute concentration (mol L^-1)", fontsize=12)
    ax1.set_ylabel("Water potential (MPa)", fontsize=12)
    ax1.set_title("Water Potential Components", fontsize=13)
    ax1.legend(fontsize=9, frameon=False)

    for conductance, color, linestyle in zip(conductances, SERIES3, ("-", "--", "-.")):
        flux = [
            transpiration_flux(
                stomatal_conductance_mol_m2_s=conductance,
                internal_vapor_conc_mol_m3=0.52,
                external_vapor_conc_mol_m3=float(external),
            ).flux_mmol_m2_s
            for external in external_vapor
        ]
        ax2.plot(external_vapor, flux, color=color, linestyle=linestyle, linewidth=2.2, label=f"g = {conductance:g}")
    ax2.set_xlabel("External water vapor concentration (mol m^-3)", fontsize=12)
    ax2.set_ylabel("Transpiration flux (mmol m^-2 s^-1)", fontsize=12)
    ax2.set_title("Fick-Law Transpiration Gradient", fontsize=13)
    ax2.legend(title="Conductance", fontsize=9, title_fontsize=9, frameon=False)

    for ax in (ax1, ax2):
        ax.tick_params(labelsize=10)
    fig.suptitle("Plant Water Potential and Transpiration", fontsize=15, fontweight="bold")
    fig.tight_layout()
    return _save_figure(fig, output_dir, "water_potential_transpiration.png")


# ---------------------------------------------------------------------------
# Ecology — logistic growth, species–area, biome NPP
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
    return _save_figure(fig, output_dir, "logistic_growth.png")


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
    return _save_figure(fig, output_dir, "species_area_relationship.png")


def plot_biome_distribution(
    output_dir: Path,
) -> Path:
    """Whittaker-style temperature-precipitation biome space from ``BIOMES``."""
    from biology.ecology import BIOMES

    names = list(BIOMES.keys())
    temps = [float(BIOMES[b]["mean_annual_temp_C"]) for b in names]
    precip = [float(BIOMES[b]["annual_precipitation_mm"]) for b in names]
    npp = np.array([float(BIOMES[b]["NPP_g_m2_yr"]) for b in names])
    sizes = 80 + (npp / npp.max()) * 520

    fig, ax = plt.subplots(figsize=(9, 5.5))
    colors = [SERIES3[i % len(SERIES3)] for i in range(len(names))]
    ax.scatter(precip, temps, s=sizes, c=colors, edgecolor="black", linewidth=0.8, alpha=0.86)
    for name, x_val, y_val in zip(names, precip, temps):
        ax.annotate(
            name,
            (x_val, y_val),
            xytext=(6, 5),
            textcoords="offset points",
            fontsize=8.5,
            bbox={"boxstyle": "round,pad=0.18", "facecolor": "white", "edgecolor": "#dddddd", "alpha": 0.78},
        )
    ax.set_xlabel("Mean annual precipitation (mm yr^-1)", fontsize=13)
    ax.set_ylabel("Mean annual temperature (deg C)", fontsize=13)
    ax.set_title("Representative Biomes in Temperature-Precipitation Space", fontsize=14)
    ax.grid(True, color="#dddddd", linewidth=0.6, alpha=0.7)
    ax.tick_params(labelsize=11)
    fig.tight_layout()
    return _save_figure(fig, output_dir, "biome_distribution.png")


def plot_genetic_drift_trajectories(
    output_dir: Path,
) -> Path:
    """Plot deterministic-seed Wright-Fisher drift trajectories."""
    from biology.evolution import simulate_drift

    fig, ax = plt.subplots(figsize=(9.5, 5.3))
    generations = 80
    configs = [
        (25, SERIES3[0], "-"),
        (100, SERIES3[1], "--"),
        (1000, SERIES3[2], "-."),
    ]
    seeds = [11, 17, 23, 31, 43]
    for N, color, linestyle in configs:
        for idx, seed in enumerate(seeds):
            trajectory = simulate_drift(p=0.5, N=N, generations=generations, rng_seed=seed)
            label = f"N = {N}" if idx == 0 else None
            ax.plot(
                range(generations + 1),
                trajectory,
                color=color,
                linestyle=linestyle,
                linewidth=1.4,
                alpha=0.35 if idx else 0.9,
                label=label,
            )
    ax.axhline(0.5, color=GRAY, linestyle=":", linewidth=1.0)
    ax.set_xlabel("Generation", fontsize=13)
    ax.set_ylabel("Allele frequency p", fontsize=13)
    ax.set_title("Wright-Fisher Genetic Drift Trajectories", fontsize=15)
    ax.set_ylim(0, 1)
    ax.legend(fontsize=10, frameon=False)
    ax.tick_params(labelsize=11)
    fig.tight_layout()
    return _save_figure(fig, output_dir, "genetic_drift_trajectories.png")


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


# ---------------------------------------------------------------------------
# Registry of all visualization functions
# ---------------------------------------------------------------------------

FigureGenerator = Callable[[Path], Path]

ALL_FIGURE_GENERATORS: list[tuple[str, FigureGenerator]] = [
    ("nernst_potentials", plot_nernst_potentials),
    ("ghk_permeability", plot_ghk_permeability),
    ("punnett_square", lambda output_dir: plot_punnett_square("Aa", "Aa", output_dir)),
    ("chromosome_structure", plot_chromosome_structure),
    ("oxygen_dissociation", plot_oxygen_dissociation),
    ("michaelis_menten", plot_michaelis_menten),
    ("lotka_volterra", plot_lotka_volterra),
    ("selection_simulation", plot_selection_simulation),
    ("action_potential", plot_action_potential),
    ("light_response_curves", plot_light_response_curve),
    ("water_potential_transpiration", plot_water_potential_transpiration),
    ("bacterial_growth", plot_bacterial_growth),
    ("methylation_heatmap", plot_methylation_heatmap),
    ("logistic_growth", plot_logistic_growth),
    ("allee_threshold_dynamics", plot_allee_threshold_dynamics),
    ("species_area_relationship", plot_species_area_relationship),
    ("biome_distribution", plot_biome_distribution),
    ("genetic_drift_trajectories", plot_genetic_drift_trajectories),
]
