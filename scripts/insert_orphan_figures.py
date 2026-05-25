#!/usr/bin/env python3
# ruff: noqa: E501
"""Insert references to orphan figure generators into their natural
home chapters. Every figure generator in ``src/visualization/`` should have
at least one corresponding ``\\begin{figure}…\\end{figure}`` block in the
manuscript so the PDF includes the generated PNG.

Idempotent: if the ``\\includegraphics{../figures/<name>.png}`` directive
is already present in the target file, that file is skipped.
"""

from __future__ import annotations

import sys
from dataclasses import dataclass
from pathlib import Path

from _bootstrap import ensure_project_paths

ensure_project_paths(include_scripts=True)

try:
    from scripts.atomic_io import write_text_atomic
except ModuleNotFoundError:  # pragma: no cover - direct script execution path
    from atomic_io import write_text_atomic  # type: ignore[import-not-found,no-redef]


MANUSCRIPT = Path(__file__).resolve().parent.parent / "manuscript"


@dataclass
class FigureInsertion:
    png: str            # figure file stem (also generator name)
    target: Path        # chapter file
    anchor: str         # literal substring marking the insertion point
    caption: str
    label: str          # crossref label, e.g. "fig:unit_V_punnett_square"
    alt: str            # alt text (accessibility)


INSERTIONS: list[FigureInsertion] = [
    FigureInsertion(
        png="punnett_AaxAa",
        target=MANUSCRIPT / "unit_V/mendelian_principles.md",
        anchor="Punnett Square",
        caption="Punnett square for a monohybrid cross Aa × Aa. Each cell shows the zygote genotype; the 3:1 phenotype ratio follows directly from the 1:2:1 genotype ratio.",
        label="fig:unit_V_punnett_square",
        alt="Two-by-two Punnett square labelled with Aa times Aa showing four offspring: one AA homozygous dominant, two Aa heterozygous, one aa homozygous recessive.",
    ),
    FigureInsertion(
        png="light_response_curves",
        target=MANUSCRIPT / "unit_III/photosynthesis.md",
        anchor="saturating light response",
        caption="Light-response curves for C3 and C4 plants. Net CO2 assimilation versus photosynthetic photon flux density, showing light compensation point, light saturation, and maximum assimilation rate.",
        label="fig:unit_III_light_response",
        alt="Hyperbolic curves relating net photosynthesis to light intensity for C3 and C4 plants, with the C4 curve saturating at higher irradiance.",
    ),
    FigureInsertion(
        png="methylation_heatmap",
        target=MANUSCRIPT / "unit_IV/chromatin_and_epigenetic_mechanisms.md",
        anchor="methylation",
        caption="DNA methylation heatmap across a panel of promoters and enhancers (rows) and cell lines (columns). Darker cells denote higher CpG methylation; cell-type-specific hypermethylation corresponds to silenced loci.",
        label="fig:unit_IV_methylation_heatmap",
        alt="Heatmap with regulatory elements on rows and cell types on columns; methylation level colour-coded from low (yellow) to high (red).",
    ),
    FigureInsertion(
        png="logistic_growth",
        target=MANUSCRIPT / "unit_X/population_ecology.md",
        anchor="logistic",
        caption="Logistic growth of a population with carrying capacity K. Population size follows dN/dt = rN(1 - N/K); the S-shaped curve asymptotes at K after an inflection at N = K/2.",
        label="fig:unit_X_logistic_growth",
        alt="Sigmoid population growth curve rising from a small initial size to a plateau at the carrying capacity K.",
    ),
    FigureInsertion(
        png="species_area_relationship",
        target=MANUSCRIPT / "unit_X/biomes_and_conservation.md",
        anchor="species-area",
        caption="Species–area relationship on log–log axes. The slope z of the linear fit (S = cA^z) ranges from ~0.15 for contiguous continental biomes to ~0.35 for isolated oceanic islands, implying doubled habitat area roughly adds 10 percent species (mainland) or 25 percent (islands).",
        label="fig:unit_X_species_area",
        alt="Log-log plot of species richness against area, with two distinct slopes for islands versus mainlands.",
    ),
    FigureInsertion(
        png="biome_distribution",
        target=MANUSCRIPT / "unit_X/biomes_and_conservation.md",
        anchor="terrestrial biome",
        caption="Whittaker biome classification in temperature-precipitation space. Tropical rainforest, savanna, desert, temperate forest, tundra, and ten other biomes occupy characteristic climate envelopes; the diagonals define the major biome boundaries.",
        label="fig:unit_X_biome_distribution",
        alt="Two-axis plot of mean annual temperature against precipitation with coloured polygons denoting biome classes.",
    ),
    FigureInsertion(
        png="hardy_weinberg",
        target=MANUSCRIPT / "unit_V/population_genetics.md",
        anchor="Hardy-Weinberg equilibrium",
        caption="Hardy-Weinberg genotype-frequency curves. As allele frequency $p$ varies, $p^2$, $2pq$, and $q^2$ trace the expected AA, Aa, and aa proportions under random mating.",
        label="fig:unit_V_hardy_weinberg",
        alt="Three curves showing genotype frequencies versus allele frequency p for AA, Aa, and aa under Hardy-Weinberg equilibrium.",
    ),
    FigureInsertion(
        png="hill_equation",
        target=MANUSCRIPT / "unit_II/cell_signaling.md",
        anchor="Hill coefficient",
        caption="Hill-equation receptor occupancy for cooperative binding. Higher Hill coefficients steepen the dose-response curve around the dissociation constant $K_d$.",
        label="fig:unit_II_hill_equation",
        alt="Sigmoid occupancy curves for Hill coefficients n equals 1, 2, and 4 on a log-scaled ligand axis.",
    ),
    FigureInsertion(
        png="sir_model",
        target=MANUSCRIPT / "unit_VII/host_immunity_and_vaccines.md",
        anchor="SIR trajectory",
        caption="SIR compartment trajectories for a closed population. Susceptible individuals decline as the infected compartment peaks, then recoveries accumulate; $R_0$ sets outbreak scale.",
        label="fig:unit_VII_sir_model",
        alt="Time series of susceptible, infected, and recovered populations during an SIR epidemic.",
    ),
    FigureInsertion(
        png="glycolysis_summary",
        target=MANUSCRIPT / "unit_III/bioenergetics_and_respiration.md",
        anchor="glycolysis",
        caption="Glycolysis energetics by pathway step. Net ATP and NADH yields per reaction summarise the investment and payoff phases of the ten-step pathway.",
        label="fig:unit_III_glycolysis_summary",
        alt="Grouped bar chart of ATP and NADH yield for each glycolysis step.",
    ),
    FigureInsertion(
        png="poiseuille_flow",
        target=MANUSCRIPT / "unit_IX/circulation_respiration_homeostasis.md",
        anchor="Poiseuille",
        caption="Hagen-Poiseuille flow versus vessel radius. Volumetric flow scales with $r^4$, so small radius reductions sharply reduce perfusion at fixed pressure gradient.",
        label="fig:unit_IX_poiseuille_flow",
        alt="Curve showing blood flow increasing steeply with vessel radius under Poiseuille law.",
    ),
    FigureInsertion(
        png="fitness_landscape",
        target=MANUSCRIPT / "unit_VI/genetic_drift_and_speciation.md",
        anchor="Genetic drift",
        caption="One-locus mean fitness landscapes under directional selection, heterozygote advantage, and underdominance. The shape of $\\bar W(p)$ predicts whether allele frequency moves toward fixation, an interior equilibrium, or disruptive thresholds.",
        label="fig:unit_VI_fitness_landscape",
        alt="Three mean-fitness curves over allele frequency p illustrating different selection modes.",
    ),
    FigureInsertion(
        png="molecular_clock",
        target=MANUSCRIPT / "unit_VI/phylogenetics.md",
        anchor="molecular clock",
        caption="Molecular-clock divergence estimates from substitution rate and sequence divergence ($t = d / 2\\mu$). Faster-evolving lineages and larger divergences yield shorter inferred times when rates are held constant.",
        label="fig:unit_VI_molecular_clock",
        alt="Horizontal bar chart of estimated divergence times in million years for four example taxon pairs.",
    ),
    FigureInsertion(
        png="biodiversity_indices",
        target=MANUSCRIPT / "unit_X/biodiversity_and_food_webs.md",
        anchor="Shannon",
        caption="Shannon and Simpson diversity indices compared for an even meadow assemblage and a dominant-species grassland. Evenness raises Shannon $H'$ and Simpson $1-D$ relative to skewed abundance distributions.",
        label="fig:unit_X_biodiversity_indices",
        alt="Bar chart comparing Shannon and Simpson indices for two communities with different evenness.",
    ),
    FigureInsertion(
        png="photosynthesis_rate",
        target=MANUSCRIPT / "unit_VIII/plant_responses.md",
        anchor="photosynthesis",
        caption="Net photosynthesis light-response curves for C3-like and C4-like parameter sets. Higher light-saturation points and lower dark respiration shift the compensation and saturation regions.",
        label="fig:unit_VIII_photosynthesis_rate",
        alt="Two hyperbolic net-photosynthesis curves versus photosynthetically active radiation.",
    ),
    FigureInsertion(
        png="osmotic_pressure",
        target=MANUSCRIPT / "unit_I/water_and_life.md",
        anchor="osmotic",
        caption="van 't Hoff osmotic pressure versus solute concentration at 37 °C. Electrolytes with van 't Hoff factor $i>1$ generate proportionally higher osmotic pressure than non-electrolytes at equal molarity.",
        label="fig:unit_I_osmotic_pressure",
        alt="Linear rise of osmotic pressure with concentration for i equals 1 and i equals 2 solutes.",
    ),
    FigureInsertion(
        png="translation_codons",
        target=MANUSCRIPT / "unit_IV/gene_expression.md",
        anchor="translation",
        caption="Translation output for a representative mRNA. Codon parsing yields an amino-acid count profile summarising peptide composition from the genetic code.",
        label="fig:unit_IV_translation_codons",
        alt="Bar chart of amino-acid counts produced from translating a sample mRNA sequence.",
    ),
    FigureInsertion(
        png="mic_dilution_series",
        target=MANUSCRIPT / "unit_VII/microbial_ecology.md",
        anchor="MIC",
        caption="Serial two-fold broth dilution series for minimum inhibitory concentration (MIC) testing. Antibiotic concentration halves in each successive tube from the starting stock.",
        label="fig:unit_VII_mic_dilution_series",
        alt="Log-scaled bar chart of antibiotic concentration across eight serial dilution tubes.",
    ),
    FigureInsertion(
        png="homeostasis_feedback",
        target=MANUSCRIPT / "unit_IX/endocrine_signaling.md",
        anchor="homeostasis",
        caption="Proportional negative-feedback correction of a temperature deviation toward a set point. Each iteration applies a corrective response proportional to the measured error.",
        label="fig:unit_IX_homeostasis_feedback",
        alt="Line plot of measured temperature converging toward set point with overlaid corrective responses.",
    ),
    FigureInsertion(
        png="food_web_trophic_levels",
        target=MANUSCRIPT / "unit_X/ecosystem_ecology.md",
        anchor="trophic",
        caption="Trophic levels inferred by breadth-first search from producer species in a simple aquatic food web. Each consumer is one level above its prey.",
        label="fig:unit_X_food_web_trophic_levels",
        alt="Horizontal bar chart assigning trophic levels from phytoplankton through apex predator.",
    ),
]


_FIGURE_TEMPLATE = (
    "\n\\begin{{figure}}[htbp]\n"
    "\\centering\n"
    "\\includegraphics[width=0.85\\textwidth]{{../figures/{png}.png}}\n"
    "\\caption{{{caption}}}\n"
    "\\label{{{label}}}\n"
    "\\end{{figure}}\n"
    "\n<!-- alt: {alt} -->\n"
)


def inject(path: Path, ins: FigureInsertion, dry_run: bool = False) -> bool:
    if not path.exists():
        print(f"WARN: missing {path}", file=sys.stderr)
        return False
    text = path.read_text(encoding="utf-8")
    if f"{ins.png}.png" in text:
        return False  # already referenced
    # Insert after the first paragraph containing the anchor phrase.
    idx = text.lower().find(ins.anchor.lower())
    if idx < 0:
        print(f"WARN: anchor '{ins.anchor}' not found in {path.name}", file=sys.stderr)
        return False
    # Find the next blank line after the anchor — insert the figure there.
    blank = text.find("\n\n", idx)
    if blank < 0:
        blank = len(text)
    block = _FIGURE_TEMPLATE.format(
        png=ins.png, caption=ins.caption, label=ins.label, alt=ins.alt,
    )
    new_text = text[: blank + 1] + block + text[blank + 1:]
    if not dry_run:
        write_text_atomic(path, new_text)
    return True


def main(argv: list[str] | None = None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    dry_run = "--dry-run" in argv
    n = 0
    for ins in INSERTIONS:
        if inject(ins.target, ins, dry_run=dry_run):
            n += 1
    mode = "DRY RUN" if dry_run else "APPLIED"
    print(f"[{mode}] figures_inserted={n}/{len(INSERTIONS)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
