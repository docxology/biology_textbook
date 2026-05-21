# Unit VI — Evolution: AGENTS.md

## Source Module

`src/biology/evolution/evolution.py`:
- `simulate_selection()` — allele frequency change over generations
- `simulate_drift()` — stochastic drift with configurable N_e and seed
- `fitness_landscape()` — two-locus epistatic fitness surface
- `molecular_clock_divergence_time()` — t = d_JC / (2μ)
- `jukes_cantor_distance()` — corrected sequence divergence
- `isolation_index()` — reproductive isolation metric (0–1)

## Chapters

1. `evolution_and_selection.md` — Theory, Natural Selection, and Adaptation
2. `genetic_drift_and_speciation.md` — Genetic Drift, Gene Flow, and Speciation
3. `phylogenetics.md` — Phylogenetics and the Tree of Life

## Key Equations

- Selection: Δq = −spq² / W̄
- Drift variance: σ²(Δp) = pq / (2N_e)
- Gene flow: p₁' = (1 − m)p₁ + mp₂
- Jukes-Cantor: d_JC = −(3/4) ln(1 − 4d/3)
- Molecular clock: t = d_JC / (2μ)

## Figures and Diagrams

- `src/visualization/plots.py` — `plot_selection_simulation()`
- `src/mermaid/biology_diagrams.py` — `natural_selection_diagram()`, `phylogenetic_tree_diagram()`

## Chapter Metadata Convention

All chapter files in this unit carry (inserted automatically by the scripts):

- `\label{sec:unit_VI_<stem>}` on the line after the H1 — cross-reference with `\cref{sec:unit_VI_<stem>}`
- `<!-- chapter-metadata-badge -->` blockquote with difficulty (Level 1/3–3/3), reading time, lecture time, and prerequisites (data in `../../src/biology/chapter_metadata.py`)

See [../AGENTS.md](../AGENTS.md) and [../../docs/manuscript_guide.md](../../docs/manuscript_guide.md) for the full set of invariants.
