# Unit V — Classical Genetics and Heredity: AGENTS.md

## Source Module

`src/biology/genetics/genetics.py`:
- `punnett_square()` — monohybrid crosses; genotype and phenotype ratios
- `chi_squared_test()` — observed vs. expected ratios
- `hardy_weinberg()` — HW genotype frequencies from $p$ or from recessive homozygote frequency
- `hamming_distance()`, `jukes_cantor_distance()` — sequence divergence helpers

`src/biology/evolution/evolution.py`:
- `simulate_selection()`, `simulate_drift()` — allele frequency trajectories

## Chapters

1. `mendelian_genetics.md` — Mendelian Genetics and Heredity
2. `chromosomal_inheritance.md` — Chromosomal Inheritance and Linkage
3. `population_genetics.md` — Population Genetics and Hardy-Weinberg Equilibrium

## Key Equations

- χ² = Σ (O − E)² / E
- Hardy-Weinberg: p² + 2pq + q² = 1; p + q = 1  
- Map distance (Morgan): d = (recombinant gametes / total gametes) × 100 cM

## Figures and Diagrams

- `plot_punnett_square()` — Punnett grid figure
- `plot_selection_simulation()` — selection trajectory figure
- `mendelian_cross_diagram()`, `cell_cycle_diagram()` — Mermaid factories

## Chapter Metadata Convention

All chapter files in this unit carry (inserted automatically by the scripts):

- `\label{sec:unit_V_<stem>}` on the line after the H1 — cross-reference with `\cref{sec:unit_V_<stem>}`
- `<!-- chapter-metadata-badge -->` blockquote with difficulty (Level 1/3–3/3), reading time, lecture time, and prerequisites (data in `../../src/biology/chapter_metadata.py`)

See [../AGENTS.md](../AGENTS.md) and [../../docs/manuscript_guide.md](../../docs/manuscript_guide.md) for the full set of invariants.
