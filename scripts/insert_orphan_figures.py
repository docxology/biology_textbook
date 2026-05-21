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

try:
    from scripts.atomic_io import write_text_atomic
except ModuleNotFoundError:  # pragma: no cover - direct script execution path
    sys.path.insert(0, str(Path(__file__).resolve().parent))
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
        target=MANUSCRIPT / "unit_V/mendelian_genetics.md",
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
        target=MANUSCRIPT / "unit_IV/epigenetics_and_gene_regulation.md",
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
