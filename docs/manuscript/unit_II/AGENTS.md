# Unit II — The Cell: AGENTS.md

## Unit Overview

Unit II covers cell theory, prokaryotic and eukaryotic cell structure, membrane transport including the Nernst and Goldman equations, and cell signaling cascades and the cell cycle.

## Source Module

`src/biology/cell/cell_biology.py`:
- `ORGANELLES` — organelle inventory (12 entries)
- `get_organelles_by_cell_type()` — filter by cell type
- `nernst_potential()` — equilibrium potential per ion
- `goldman_equation()` — multi-ion membrane potential
- `osmotic_pressure()` — van 't Hoff calculation
- `diffusion_flux()` — Fick's First Law

## Chapters

[README.md](README.md) lists chapter filenames/titles; [config.yaml](../config.yaml) owns order.

## Key Equations

- Nernst: E_i = (RT/zF) ln([C]_out / [C]_in)
- Goldman–Hodgkin–Katz: use the full expression and permeability/concentration assumptions in the chapter; reverse the chloride concentrations relative to cations.
- Osmotic pressure: π = iCRT
- Fick: J = −D(dC/dx)

## Figures and Diagrams

- Repository-root `src/visualization/plots_cell.py` implements `plot_nernst_potentials()`; `plots.py` owns registration.
- `src/mermaid/biology_diagrams.py` — `organelle_function_diagram()`, `membrane_transport_diagram()`, `cell_cycle_diagram()`

## Shared source contract

Follow [manuscript instructions](../AGENTS.md) for H1s, stable IDs, metadata badges, references and authored assessments; see [writing examples](../../manuscript_guide.md). Implementation paths above are repository-root paths.
