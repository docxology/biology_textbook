# Unit VII — Microbiology: AGENTS.md

## Source Module

`src/biology/microbiology/microbiology.py`:
- `REFERENCE_ORGANISMS` — list of reference bacteria/archaea with traits
- `bacterial_growth_curve()` — continuous piecewise lag/exponential/stationary growth with optional cap, not logistic growth
- `doubling_time(N0, Nt, elapsed_time_hr)` — doubling time from increasing population counts under an exponential-growth assumption
- `mic_fold_dilution(starting_concentration_ug_mL, dilution_factor, n_tubes)` — supplied serial antibiotic concentrations; not an MIC measurement or breakpoint classification
- `VIRAL_REPLICATION_CYCLES` — reference model-virus parameters, not a calibrated prediction for an arbitrary infection

## Chapters

[README.md](README.md) lists chapter filenames/titles; [config.yaml](../config.yaml) owns order.

## Key Equations

- Exponential growth: N(t) = N₀·2^(t/g) = N₀·e^(µt)
- Logistic growth: dN/dt = rN(1 − N/K)
- MIC broth dilution: serial 2-fold dilutions

## Figures and Diagrams

- Repository-root `src/visualization/plots_microbiology.py` implements `plot_bacterial_growth()`; `plots.py` owns registration.
- `src/mermaid/biology_diagrams.py` — `viral_replication_cycle_diagram()`, `immune_response_diagram()`

## Shared source contract

Follow [manuscript instructions](../AGENTS.md) for H1s, stable IDs, metadata badges, references and authored assessments; see [writing examples](../../manuscript_guide.md). Implementation paths above are repository-root paths.
