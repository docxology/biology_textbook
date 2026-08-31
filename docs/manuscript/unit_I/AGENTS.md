# Unit I — Chemistry of Life: AGENTS.md

## Unit Overview

Unit I covers the chemical and physical foundations of biology: atomic structure, chemical bonding, the unique properties of water, the four classes of biological macromolecules, and the kinetics of enzyme catalysis.

## Source Module

`src/biology/biochemistry/biochemistry.py` provides the quantitative backbone for this unit:
- `michaelis_menten()` — Chapter: enzymes_and_kinetics
- `glycolysis_summary()` — Chapter: bioenergetics (Unit III)
- `atp_free_energy()` — Chapter: bioenergetics (Unit III)

## Chapters in This Unit

Chapters are auto-numbered via `docs/manuscript/config.yaml`. Current order:

1. `atoms_molecules.md` — Atoms, Molecules, and Chemical Bonds
2. `water_and_life.md` — Water — The Molecule of Life
3. `macromolecules.md` — Biological Macromolecules
4. `enzymes_and_kinetics.md` — Enzymes and the Kinetics of Catalysis

## Key Equations

- Henderson-Hasselbalch: pH = pKₐ + log([A⁻]/[HA])
- van 't Hoff osmotic pressure: π = iCRT
- Fick's First Law: J = −D(dC/dx)
- Michaelis-Menten: v = Vmax[S]/(Km + [S])
- Competitive inhibition: v = Vmax[S] / (Km·α + [S]) where α = 1 + [I]/Ki

## Figures and Diagrams

- `src/visualization/plots.py` — `plot_michaelis_menten()`
- `src/mermaid/biology_diagrams.py` — `macromolecule_classification_diagram()`, `enzyme_kinetics_diagram()`

## Chapter Metadata Convention

All chapter files in this unit carry (inserted automatically by the scripts):

- `\label{sec:unit_I_<stem>}` on the line after the H1 — cross-reference with `\cref{sec:unit_I_<stem>}`
- `<!-- chapter-metadata-badge -->` blockquote with difficulty (Level 1/3–3/3), reading time, lecture time, and prerequisites (data in `../../src/biology/chapter_metadata.py`)

See [../AGENTS.md](../AGENTS.md) and [../../docs/manuscript_guide.md](../../docs/manuscript_guide.md) for the full set of invariants.
