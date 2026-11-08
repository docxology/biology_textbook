# Unit I — Chemistry of Life: AGENTS.md

## Unit Overview

Unit I covers the chemical and physical foundations of biology: atomic structure, chemical bonding, the unique properties of water, the four classes of biological macromolecules, and the kinetics of enzyme catalysis.

## Source Module

`src/biology/biochemistry/biochemistry.py` provides the quantitative backbone for this unit:
- `michaelis_menten()` — Chapter: enzymes_and_kinetics
- `glycolysis_summary()` — Chapter: bioenergetics (Unit III)
- `atp_free_energy()` — Chapter: bioenergetics (Unit III)

## Chapters in This Unit

[README.md](README.md) lists chapter filenames/titles; [config.yaml](../config.yaml) owns order.

## Key Equations

- Henderson–Hasselbalch: pH = pKₐ + log([A⁻]/[HA]) under the stated ideal-dilute/apparent-pKₐ approximation; the activity form defines the thermodynamic relation.
- van 't Hoff osmotic pressure: π = iCRT
- Fick's First Law: J = −D(dC/dx)
- Michaelis-Menten: v = Vmax[S]/(Km + [S])
- Competitive inhibition: v = Vmax[S] / (Km·α + [S]) where α = 1 + [I]/Ki

## Figures and Diagrams

- Repository-root `src/visualization/plots_*.py` implements figures; `plots.py` registers `plot_michaelis_menten()`.
- `src/mermaid/biology_diagrams.py` — `macromolecule_classification_diagram()`, `enzyme_kinetics_diagram()`

## Shared source contract

Follow [manuscript instructions](../AGENTS.md) for H1s, stable IDs, metadata badges, references and authored assessments; see [writing examples](../../manuscript_guide.md). Implementation paths above are repository-root paths.
