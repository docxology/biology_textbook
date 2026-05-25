"""Matplotlib generators for Unit 0 and Unit I foundations chapters.

Each generator calls a tabulated helper in ``biology.foundations`` so the
figure and the prose share one source of truth.
"""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from visualization._scaffold import (
    GRAY,
    ORANGE,
    PURPLE,
    SERIES2,
    SERIES4,
    _save_figure,
)


def plot_network_degree_distribution(
    output_dir: Path,
    *,
    mean_degree: float = 4.0,
    gamma: float = 2.5,
    k_min: int = 1,
    k_max: int = 200,
) -> Path:
    """Plot a scale-free (power-law) and a random (Poisson) degree distribution.

    The figure uses log-log axes so the heavy power-law tail and the Poisson
    cut-off are both legible. Hubs in the scale-free network sit at high
    degrees where the Poisson curve has already vanished.

    Args:
        output_dir: Directory to save PNG.
        mean_degree: Poisson mean.
        gamma: Power-law exponent.
        k_min: Smallest degree shown (inclusive).
        k_max: Largest degree shown (inclusive).

    Returns:
        Path to the saved PNG.
    """
    from biology.foundations import scale_free_vs_random

    poisson, powerlaw = scale_free_vs_random(
        mean_degree=mean_degree, gamma=gamma, k_min=k_min, k_max=k_max
    )

    fig, ax = plt.subplots(figsize=(9, 5))
    ax.loglog(
        poisson.degrees,
        poisson.probabilities,
        color=SERIES2[0],
        linewidth=2.2,
        linestyle="-",
        marker="o",
        markersize=4,
        label=f"Random (Poisson, mean k = {mean_degree:g})",
    )
    ax.loglog(
        powerlaw.degrees,
        powerlaw.probabilities,
        color=SERIES2[1],
        linewidth=2.2,
        linestyle="--",
        marker="s",
        markersize=4,
        label=f"Scale-free (power law, gamma = {gamma:g})",
    )
    ax.set_xlabel("Degree k (log scale)", fontsize=13)
    ax.set_ylabel("P(k) (log scale)", fontsize=13)
    ax.set_title(
        "Scale-Free vs Random Network Degree Distribution",
        fontsize=14,
    )
    ax.grid(True, which="both", color="#dddddd", linewidth=0.6, alpha=0.7)
    ax.legend(fontsize=10, frameon=False)
    ax.tick_params(labelsize=11)
    fig.tight_layout()
    return _save_figure(fig, output_dir, "network_degree_distribution.png", aspect="landscape")


def plot_prediction_error_precision(
    output_dir: Path,
    *,
    prior_mean: float = 0.0,
    prior_precision: float = 1.0,
    observation: float = 1.0,
) -> Path:
    """Plot posterior mean and weight against sensory precision.

    The active-inference figure shows two curves on a shared log-precision
    axis: the posterior mean shifts from the prior toward the observation as
    sensory precision rises, and the sensory weight pi_s / (pi_p + pi_s)
    saturates near 1.

    Args:
        output_dir: Directory to save PNG.
        prior_mean: Prior expectation mu_p.
        prior_precision: Prior precision pi_p.
        observation: Sensory observation y.

    Returns:
        Path to the saved PNG.
    """
    from biology.foundations import prediction_error_precision_curve

    profile = prediction_error_precision_curve(
        prior_mean=prior_mean,
        prior_precision=prior_precision,
        observation=observation,
    )
    precisions = np.array([p.sensory_precision for p in profile.points])
    posterior = np.array([p.posterior_mean for p in profile.points])
    sensory_weight = precisions / (precisions + prior_precision)

    fig, ax_left = plt.subplots(figsize=(9, 5))
    ax_left.semilogx(
        precisions,
        posterior,
        color=SERIES2[0],
        linewidth=2.2,
        marker="o",
        markersize=4,
        label="Posterior mean shift",
    )
    ax_left.axhline(prior_mean, color=GRAY, linestyle=":", linewidth=1.2, label="Prior")
    ax_left.axhline(observation, color=ORANGE, linestyle="--", linewidth=1.2, label="Observation")
    ax_left.set_xlabel("Sensory precision pi_s (log scale)", fontsize=13)
    ax_left.set_ylabel("Posterior mean", fontsize=13, color=SERIES2[0])
    ax_left.tick_params(labelsize=11, axis="y", labelcolor=SERIES2[0])
    ax_left.tick_params(labelsize=11, axis="x")

    ax_right = ax_left.twinx()
    ax_right.semilogx(
        precisions,
        sensory_weight,
        color=PURPLE,
        linewidth=2.0,
        linestyle="-.",
        marker="s",
        markersize=4,
        label="Sensory weight",
    )
    ax_right.set_ylabel("Sensory weight pi_s / (pi_s + pi_p)", fontsize=13, color=PURPLE)
    ax_right.tick_params(labelsize=11, axis="y", labelcolor=PURPLE)
    ax_right.set_ylim(0.0, 1.05)

    handles_left, labels_left = ax_left.get_legend_handles_labels()
    handles_right, labels_right = ax_right.get_legend_handles_labels()
    ax_left.legend(
        handles_left + handles_right,
        labels_left + labels_right,
        loc="center left",
        fontsize=10,
        frameon=False,
    )
    ax_left.set_title(
        "Active Inference: Prediction Error vs Sensory Precision", fontsize=14
    )
    fig.tight_layout()
    return _save_figure(fig, output_dir, "prediction_error_precision.png", aspect="landscape")


def plot_biology_milestones(output_dir: Path) -> Path:
    """Render the curated history-of-biology milestone timeline.

    A horizontal bar chart with one bar per milestone, ordered chronologically
    and colored by era. The label sits to the right of each bar so dense
    nineteenth- and twentieth-century clusters remain readable.

    Args:
        output_dir: Directory to save PNG.

    Returns:
        Path to the saved PNG.
    """
    from biology.foundations import BIOLOGY_MILESTONES, milestones_by_era

    eras = list(milestones_by_era().keys())
    era_to_color = {era: SERIES4[idx % len(SERIES4)] for idx, era in enumerate(eras)}

    years = [m.year for m in BIOLOGY_MILESTONES]
    labels = [f"{m.year}: {m.event} ({m.figure})" for m in BIOLOGY_MILESTONES]
    colors = [era_to_color[m.era] for m in BIOLOGY_MILESTONES]

    fig, ax = plt.subplots(figsize=(11, 6))
    y_positions = np.arange(len(BIOLOGY_MILESTONES))
    ax.barh(
        y_positions,
        years,
        color=colors,
        edgecolor="black",
        linewidth=0.6,
        height=0.7,
    )
    ax.set_yticks(y_positions)
    ax.set_yticklabels(labels, fontsize=9)
    ax.set_xlim(min(years) - 30, max(years) + 30)
    ax.set_xlabel("Year of milestone", fontsize=13)
    ax.set_title("History of Biology: Milestone Timeline", fontsize=14)
    ax.invert_yaxis()
    ax.tick_params(labelsize=10)

    legend_handles = [
        plt.Rectangle((0, 0), 1, 1, color=color, ec="black", linewidth=0.6)
        for color in era_to_color.values()
    ]
    ax.legend(
        legend_handles,
        list(era_to_color.keys()),
        loc="lower right",
        fontsize=9,
        frameon=False,
        title="Era",
    )
    fig.tight_layout()
    return _save_figure(fig, output_dir, "biology_milestones.png", aspect="landscape")


def plot_electronegativity_bond_energy(output_dir: Path) -> Path:
    """Side-by-side bar chart of Pauling electronegativity and bond energies.

    Two stacked subplots share the figure: top bars show electronegativity for
    the biologically common atoms, bottom bars show bond dissociation
    energies split by covalent vs noncovalent class.

    Args:
        output_dir: Directory to save PNG.

    Returns:
        Path to the saved PNG.
    """
    from biology.foundations import ATOM_ELECTRONEGATIVITIES, BIOLOGICAL_BOND_ENERGIES

    atoms = list(ATOM_ELECTRONEGATIVITIES)
    bond_rows = list(BIOLOGICAL_BOND_ENERGIES)

    fig, (ax_top, ax_bottom) = plt.subplots(2, 1, figsize=(10, 8))

    atom_x = np.arange(len(atoms))
    atom_values = [atom.pauling for atom in atoms]
    atom_labels = [f"{atom.symbol}" for atom in atoms]
    ax_top.bar(
        atom_x,
        atom_values,
        color=SERIES2[0],
        edgecolor="black",
        linewidth=0.6,
    )
    ax_top.set_xticks(atom_x)
    ax_top.set_xticklabels(atom_labels, fontsize=11)
    ax_top.set_ylabel("Pauling electronegativity", fontsize=12)
    ax_top.set_title("Electronegativity of Biologically Common Atoms", fontsize=13)
    ax_top.tick_params(labelsize=10)

    bond_x = np.arange(len(bond_rows))
    bond_values = [row.energy_kJ_per_mol for row in bond_rows]
    bond_labels = [row.bond for row in bond_rows]
    bond_colors = [
        SERIES2[0] if row.bond_class == "covalent" else SERIES2[1] for row in bond_rows
    ]
    ax_bottom.bar(
        bond_x,
        bond_values,
        color=bond_colors,
        edgecolor="black",
        linewidth=0.6,
    )
    ax_bottom.set_xticks(bond_x)
    ax_bottom.set_xticklabels(bond_labels, rotation=35, ha="right", fontsize=9)
    ax_bottom.set_ylabel("Bond energy (kJ/mol, log scale)", fontsize=12)
    ax_bottom.set_yscale("log")
    ax_bottom.set_title("Bond Energies: Covalent vs Noncovalent", fontsize=13)
    ax_bottom.tick_params(labelsize=10)

    legend_handles = [
        plt.Rectangle((0, 0), 1, 1, color=SERIES2[0], ec="black", linewidth=0.6),
        plt.Rectangle((0, 0), 1, 1, color=SERIES2[1], ec="black", linewidth=0.6),
    ]
    ax_bottom.legend(
        legend_handles,
        ["Covalent", "Noncovalent"],
        loc="upper right",
        fontsize=9,
        frameon=False,
    )
    fig.tight_layout()
    return _save_figure(fig, output_dir, "electronegativity_bond_energy.png", aspect="landscape")


def plot_polymer_hierarchy(output_dir: Path) -> Path:
    """Draw the macromolecule hierarchy as a labelled grid of boxes.

    One row per polymer family (proteins, nucleic acids, carbohydrates,
    lipids) and four columns (monomer, polymer, assembly, function). Each
    cell is a coloured box with text inside, plus arrows showing the
    monomer-to-polymer-to-assembly flow.

    Args:
        output_dir: Directory to save PNG.

    Returns:
        Path to the saved PNG.
    """
    from biology.foundations import MACROMOLECULE_TIERS, polymer_hierarchy_levels

    tiers = list(MACROMOLECULE_TIERS)
    columns = polymer_hierarchy_levels()
    n_rows = len(tiers)
    n_cols = len(columns)

    fig, ax = plt.subplots(figsize=(12, 1.4 + 1.2 * n_rows))
    family_colors = [SERIES4[i % len(SERIES4)] for i in range(n_rows)]
    cell_width = 1.0
    cell_height = 1.0
    arrow_pad = 0.05

    # Column headers
    for col_idx, label in enumerate(columns):
        ax.text(
            col_idx + 0.5,
            n_rows + 0.4,
            label,
            ha="center",
            va="bottom",
            fontsize=12,
            fontweight="bold",
        )

    # Row family labels (left)
    for row_idx, tier in enumerate(tiers):
        ax.text(
            -0.15,
            n_rows - row_idx - 0.5,
            tier.family,
            ha="right",
            va="center",
            fontsize=11,
            fontweight="bold",
            color=family_colors[row_idx],
        )

    # Cells
    for row_idx, tier in enumerate(tiers):
        cells = (tier.monomer, tier.polymer, tier.assembly, tier.example_function)
        y = n_rows - row_idx - 1
        for col_idx, text in enumerate(cells):
            rect = plt.Rectangle(
                (col_idx + 0.04, y + 0.04),
                cell_width - 0.08,
                cell_height - 0.08,
                facecolor=family_colors[row_idx],
                alpha=0.22,
                edgecolor=family_colors[row_idx],
                linewidth=1.4,
            )
            ax.add_patch(rect)
            ax.text(
                col_idx + 0.5,
                y + 0.5,
                text,
                ha="center",
                va="center",
                fontsize=10,
                wrap=True,
            )
        # Arrows monomer -> polymer -> assembly
        for col_idx in range(n_cols - 2):
            ax.annotate(
                "",
                xy=(col_idx + 1 - arrow_pad, y + 0.5),
                xytext=(col_idx + arrow_pad, y + 0.5),
                arrowprops={"arrowstyle": "->", "color": GRAY, "linewidth": 1.4},
            )

    ax.set_xlim(-1.4, n_cols + 0.2)
    ax.set_ylim(-0.4, n_rows + 0.8)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title("Polymer Hierarchy of Biological Macromolecules", fontsize=14, pad=12)
    fig.tight_layout()
    return _save_figure(fig, output_dir, "polymer_hierarchy.png", aspect="landscape")
