# Unit III — Energy and Metabolism: AGENTS.md

## Unit Overview

This unit covers cellular bioenergetics (thermodynamics, glycolysis, TCA cycle, oxidative phosphorylation), photosynthesis (light reactions, Calvin cycle, C3/C4/CAM), and metabolic integration and regulation.

## Source Module

`src/biology/biochemistry/biochemistry.py`:
- `glycolysis_summary()` — 10-step pathway; net ATP, NADH, total ΔG
- `atp_free_energy()` — fixed-standard ideal-dilute ATP-hydrolysis teaching model, not a pH/Mg-resolved cellular measurement
- `michaelis_menten()` — for enzyme regulation discussions
- `reaction_free_energy()` — specified 1:1 ideal-dilute product/reactant quotient; arbitrary stoichiometric quotients must be constructed separately

`src/biology/botany/botany.py`:
- `photosynthesis_rate()` — Michaelis-Menten O₂ evolution
- `light_response_curve()` — hyperbolic light saturation
- `PHOTOSYNTHESIS_PATHWAYS` — C3/C4/CAM data

## Chapters

1. `bioenergetics_and_respiration.md` — Bioenergetics and Cellular Respiration
2. `photosynthesis.md` — Photosynthesis
3. `metabolic_integration.md` — Metabolic Integration and Regulation

## Key Equations

- Gibbs free energy: ΔG = ΔH − TΔS
- Actual ΔG: ΔG = ΔG°' + RT ln Q
- ATP hydrolysis: −30.5 kJ/mol is a conventional standard transformed reference; cellular ΔG depends on the normalized quotient and matching thermodynamic conditions
- Idealized linear electron transfer uses one PSII and one PSI excitation per electron (four photons per NADPH); a stipulated 680-nm photon carries about 1.82 eV. Additional cyclic flow and losses require separate assumptions.
- Calvin cycle: 18 ATP + 12 NADPH → fix 6 CO₂ (1 net hexose)

## Figures and Diagrams

- `src/mermaid/biology_diagrams.py` — `glycolysis_pathway_diagram()`, `atp_synthesis_diagram()`, `photosynthesis_light_dark_diagram()`
- `src/visualization/plots.py` — `plot_light_response_curve()`

## Chapter Metadata Convention

All chapter files in this unit carry (inserted automatically by the scripts):

- `\label{sec:unit_III_<stem>}` on the line after the H1 — cross-reference with `\cref{sec:unit_III_<stem>}`
- `<!-- chapter-metadata-badge -->` blockquote with difficulty (Level 1/3–3/3), reading time, lecture time, and prerequisites (data in `../../../src/biology/chapter_metadata.py`)

See [../AGENTS.md](../AGENTS.md) and [../../manuscript_guide.md](../../manuscript_guide.md) for the full set of invariants.
