"""Domain matplotlib figure generators."""

from __future__ import annotations

from pathlib import Path
from typing import Optional

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

from visualization._scaffold import (
    BAR_NEG,
    BAR_POS,
    GRAY,
    ORANGE,
    PUNNETT_DOMINANT,
    PUNNETT_RECESSIVE,
    PURPLE,
    SERIES3,
    _save_figure,
    logger,
)


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


def plot_hill_equation(
    output_dir: Path,
) -> Path:
    """Plot Hill-equation receptor occupancy for several cooperativity values."""
    from biology.cell import hill_equation

    ligand = np.logspace(-1, 2, 120)
    kd = 10.0
    fig, ax = plt.subplots(figsize=(9, 5))
    for n, color, linestyle in zip((1, 2, 4), SERIES3, ("-", "--", "-.")):
        occupancy = [hill_equation(float(conc), kd, float(n)) for conc in ligand]
        label = "Michaelis-Menten (n=1)" if n == 1 else f"Hill n = {n}"
        ax.plot(ligand, occupancy, color=color, linewidth=2.2, linestyle=linestyle, label=label)
    ax.axhline(0.5, color=GRAY, linestyle=":", linewidth=1.0, alpha=0.75)
    ax.axvline(kd, color=ORANGE, linestyle=":", linewidth=1.0, alpha=0.75, label=f"Kd = {kd:g}")
    ax.set_xscale("log")
    ax.set_xlabel("Ligand concentration (arbitrary units)", fontsize=13)
    ax.set_ylabel("Fractional receptor occupancy", fontsize=13)
    ax.set_title("Hill Equation — Cooperative Binding", fontsize=15)
    ax.set_ylim(0, 1.05)
    ax.legend(fontsize=10, frameon=False)
    ax.tick_params(labelsize=11)
    fig.tight_layout()
    return _save_figure(fig, output_dir, "hill_equation.png")


def plot_osmotic_pressure(
    output_dir: Path,
) -> Path:
    """Plot van 't Hoff osmotic pressure versus solute concentration."""
    from biology.cell import osmotic_pressure

    concentrations = np.linspace(0.01, 1.0, 80)
    pressures_kpa = [osmotic_pressure(float(c), temperature_K=310.0, solute_count=1) / 1000.0 for c in concentrations]
    nacl_pressures = [
        osmotic_pressure(float(c), temperature_K=310.0, solute_count=2) / 1000.0 for c in concentrations
    ]

    fig, ax = plt.subplots(figsize=(9, 5))
    ax.plot(concentrations, pressures_kpa, color=SERIES3[0], linewidth=2.2, linestyle="-", label="Non-electrolyte (i=1)")
    ax.plot(concentrations, nacl_pressures, color=SERIES3[1], linewidth=2.2, linestyle="--", label="NaCl (i=2)")
    ax.set_xlabel("Solute concentration (mol L⁻¹)", fontsize=13)
    ax.set_ylabel("Osmotic pressure (kPa)", fontsize=13)
    ax.set_title("van 't Hoff Osmotic Pressure at 37 °C", fontsize=15)
    ax.legend(fontsize=10, frameon=False)
    ax.tick_params(labelsize=11)
    fig.tight_layout()
    return _save_figure(fig, output_dir, "osmotic_pressure.png")


def plot_organelle_size_scale(output_dir: Path) -> Path:
    """Log-scale horizontal bars for canonical organelle and cell sizes.

    The plot uses a logarithmic diameter axis so a ribosome (25 nm) and a
    plant cell (50 um) coexist in the same panel. Categories share colors:
    macromolecular complexes, organelles, prokaryotic cells, eukaryotic
    cells.

    Args:
        output_dir: Directory to save PNG.

    Returns:
        Path to the saved PNG.
    """
    from biology.cell import organelle_size_table

    rows = list(organelle_size_table())
    names = [row.name for row in rows]
    diameters = np.array([row.diameter_um for row in rows])

    palette = {
        "macromolecular": SERIES3[0],
        "organelle": SERIES3[1],
        "prokaryotic cell": SERIES3[2],
        "eukaryotic cell": PURPLE,
    }
    colors = [palette[row.category] for row in rows]

    fig, ax = plt.subplots(figsize=(10, 6))
    y_positions = np.arange(len(rows))
    ax.barh(y_positions, diameters, color=colors, edgecolor="black", linewidth=0.6)
    ax.set_yticks(y_positions)
    ax.set_yticklabels(names, fontsize=10)
    ax.set_xscale("log")
    ax.set_xlabel("Diameter (micrometres, log scale)", fontsize=13)
    ax.set_title("Cellular Structures on a Logarithmic Size Scale", fontsize=14)
    ax.tick_params(labelsize=10)
    ax.grid(True, which="both", axis="x", color="#dddddd", linewidth=0.6, alpha=0.7)

    legend_handles = [
        plt.Rectangle((0, 0), 1, 1, color=color, ec="black", linewidth=0.6)
        for color in palette.values()
    ]
    ax.legend(
        legend_handles,
        list(palette.keys()),
        loc="lower right",
        fontsize=9,
        frameon=False,
        title="Category",
    )
    fig.tight_layout()
    return _save_figure(fig, output_dir, "organelle_size_scale.png", aspect="landscape")

