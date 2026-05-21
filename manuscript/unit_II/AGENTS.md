# Unit II — The Cell: AGENTS.md

## Unit Overview

Unit II covers cell theory, prokaryotic and eukaryotic cell structure, membrane transport including the Nernst and Goldman equations, and cell signalling cascades and the cell cycle.

## Source Module

`src/biology/cell/cell_biology.py`:
- `ORGANELLES` — organelle inventory (12 entries)
- `get_organelles_by_cell_type()` — filter by cell type
- `nernst_potential()` — equilibrium potential per ion
- `goldman_equation()` — multi-ion membrane potential
- `osmotic_pressure()` — van 't Hoff calculation
- `diffusion_flux()` — Fick's First Law

## Chapters

1. `cell_theory.md` — Cell Theory and Cell Types
2. `cell_structure.md` — Cell Structure and Organelles
3. `membrane_transport.md` — Membrane Structure and Transport
4. `cell_signaling.md` — Cell Signalling and Communication

## Key Equations

- Nernst: E_i = (RT/zF) ln([C]_out / [C]_in)
- Goldman-Hodgkin-Katz: V_m = (RT/F) ln[(P_K[K+]_o + P_Na[Na+]_o + P_Cl[Cl-]_i) / (denominator)]
- Osmotic pressure: π = iCRT
- Fick: J = −D(dC/dx)

## Figures and Diagrams

- `src/visualization/plots.py` — `plot_nernst_potentials()`
- `src/mermaid/biology_diagrams.py` — `organelle_function_diagram()`, `membrane_transport_diagram()`, `cell_cycle_diagram()`

## Chapter Metadata Convention

All chapter files in this unit carry (inserted automatically by the scripts):

- `\label{sec:unit_II_<stem>}` on the line after the H1 — cross-reference with `\cref{sec:unit_II_<stem>}`
- `<!-- chapter-metadata-badge -->` blockquote with difficulty (Level 1/3–3/3), reading time, lecture time, and prerequisites (data in `../../src/biology/chapter_metadata.py`)

See [../AGENTS.md](../AGENTS.md) and [../../docs/manuscript_guide.md](../../docs/manuscript_guide.md) for the full set of invariants.
