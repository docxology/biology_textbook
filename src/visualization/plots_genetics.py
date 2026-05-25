"""Domain matplotlib figure generators."""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

from visualization._scaffold import (
    BAR_POS,
    GRAY,
    PUNNETT_DOMINANT,
    PUNNETT_RECESSIVE,
    SERIES2,
    SERIES3,
    _save_figure,
)


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
    from biology.genetics import gametes, punnett_square

    result = punnett_square(parent1, parent2)
    g1 = gametes(parent1)
    g2 = gametes(parent2)
    n1, n2 = len(g1), len(g2)

    fig, ax = plt.subplots(figsize=(max(3, n2 + 1), max(3, n1 + 1)))
    ax.set_xlim(0, n2 + 1)
    ax.set_ylim(0, n1 + 1)

    offspring = result.offspring_genotypes
    for i, ga in enumerate(g1):
        for j, gb in enumerate(g2):
            geno = offspring[i * n2 + j]
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
    return _save_figure(fig, output_dir, "selection_simulation.png", aspect="landscape")


# ---------------------------------------------------------------------------
# Physiology — Oxygen-haemoglobin dissociation curve
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
    from biology.genetics import synthetic_methylation_beta_matrix

    beta = synthetic_methylation_beta_matrix()

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
    return _save_figure(fig, output_dir, "genetic_drift_trajectories.png", aspect="landscape")


def plot_hardy_weinberg(
    output_dir: Path,
) -> Path:
    """Plot Hardy-Weinberg genotype frequencies versus allele frequency p."""
    from biology.genetics import hardy_weinberg

    p_values = np.linspace(0.0, 1.0, 100)
    aa_freq, ab_freq, bb_freq = [], [], []
    for p in p_values:
        result = hardy_weinberg(p=p, q=1.0 - p)
        aa_freq.append(result.p_squared)
        ab_freq.append(result.two_pq)
        bb_freq.append(result.q_squared)

    fig, ax = plt.subplots(figsize=(9, 5))
    ax.plot(p_values, aa_freq, color=SERIES3[0], linewidth=2.2, linestyle="-", label="freq(AA) = p²")
    ax.plot(p_values, ab_freq, color=SERIES3[1], linewidth=2.2, linestyle="--", label="freq(Aa) = 2pq")
    ax.plot(p_values, bb_freq, color=SERIES3[2], linewidth=2.2, linestyle="-.", label="freq(aa) = q²")
    ax.set_xlabel("Allele A frequency (p)", fontsize=13)
    ax.set_ylabel("Genotype frequency", fontsize=13)
    ax.set_title("Hardy-Weinberg Equilibrium Genotype Curves", fontsize=15)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.legend(fontsize=10, frameon=False)
    ax.tick_params(labelsize=11)
    fig.tight_layout()
    return _save_figure(fig, output_dir, "hardy_weinberg.png", aspect="landscape")


def plot_translation_codons(
    output_dir: Path,
) -> Path:
    """Bar chart of amino-acid counts from a representative mRNA translation."""
    from biology.genetics import translate_mrna

    mrna = (
        "AUGUUUGGCCAUUGGCAUGGCCAUUGGCAUGGCCAUUGGCAUGGCCAUUGGCAUGGCCAUUGG"
        "UAA"
    )
    amino_acids = translate_mrna(mrna)
    counts: dict[str, int] = {}
    for aa in amino_acids:
        counts[aa] = counts.get(aa, 0) + 1
    labels = list(counts.keys())
    values = [counts[k] for k in labels]

    fig, ax = plt.subplots(figsize=(9, 4.5))
    ax.bar(labels, values, color=BAR_POS, edgecolor="black", linewidth=0.8)
    ax.set_xlabel("Amino acid", fontsize=13)
    ax.set_ylabel("Count in translated peptide", fontsize=13)
    ax.set_title("Translation Output — Codon-to-Amino-Acid Counts", fontsize=15)
    ax.tick_params(labelsize=10)
    fig.tight_layout()
    return _save_figure(fig, output_dir, "translation_codons.png")

