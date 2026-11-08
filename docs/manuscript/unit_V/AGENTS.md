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

[README.md](README.md) lists chapter filenames/titles; [config.yaml](../config.yaml) owns order.

## Key Equations

- χ² = Σ (O − E)² / E
- Hardy-Weinberg: p² + 2pq + q² = 1; p + q = 1  
- For short intervals, recombination fraction × 100 approximates map distance in cM; do not label that value as Morgans or assume a linear long-interval map.

## Figures and Diagrams

- `plot_punnett_square()` — Punnett grid figure
- `plot_selection_simulation()` — selection trajectory figure
- `mendelian_cross_diagram()`, `cell_cycle_diagram()` — Mermaid factories

## Shared source contract

Follow [manuscript instructions](../AGENTS.md) for H1s, stable IDs, metadata badges, references and authored assessments; see [writing examples](../../manuscript_guide.md). Implementation paths above are repository-root paths.
