# Unit VII — Microbiology: AGENTS.md

## Source Module

`src/biology/microbiology/microbiology.py`:
- `REFERENCE_ORGANISMS` — list of reference bacteria/archaea with traits
- `bacterial_growth_curve()` — logistic growth with lag/stationary phases
- `doubling_time()` — g = ln2/µ
- `mic_broth_dilution()` — minimum inhibitory concentration
- `VIRAL_CYCLE_DATA` — lytic/lysogenic parameters for model phages
- `antibiotic_resistance_rate()` — probabilistic resistance simulation

## Chapters

1. `bacteria_archaea_viruses.md` — Bacteria, Archaea, and Viruses
2. `microbial_ecology.md` — Microbial Ecology and the Microbiome
3. `infectious_disease.md` — Infectious Disease and Immunity

## Key Equations

- Exponential growth: N(t) = N₀·2^(t/g) = N₀·e^(µt)
- Logistic growth: dN/dt = rN(1 − N/K)
- MIC broth dilution: serial 2-fold dilutions

## Figures and Diagrams

- `src/visualization/plots.py` — `plot_bacterial_growth()`
- `src/mermaid/biology_diagrams.py` — `viral_replication_cycle_diagram()`, `immune_response_diagram()`

## Chapter Metadata Convention

All chapter files in this unit carry (inserted automatically by the scripts):

- `\label{sec:unit_VII_<stem>}` on the line after the H1 — cross-reference with `\cref{sec:unit_VII_<stem>}`
- `<!-- chapter-metadata-badge -->` blockquote with difficulty (Level 1/3–3/3), reading time, lecture time, and prerequisites (data in `../../src/biology/chapter_metadata.py`)

See [../AGENTS.md](../AGENTS.md) and [../../docs/manuscript_guide.md](../../docs/manuscript_guide.md) for the full set of invariants.
