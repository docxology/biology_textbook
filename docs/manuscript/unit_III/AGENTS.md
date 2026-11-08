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
- `photosynthesis_rate()` — hyperbolic gross light response minus dark respiration, returning net CO₂ assimilation
- `light_response_curve()` — hyperbolic light saturation
- `PHOTOSYNTHESIS_PATHWAYS` — C3/C4/CAM data

## Chapters

[README.md](README.md) lists chapter filenames/titles; [config.yaml](../config.yaml) owns order.

## Key Equations

- Gibbs free energy: ΔG = ΔH − TΔS
- Actual ΔG: ΔG = ΔG°' + RT ln Q
- ATP hydrolysis: −30.5 kJ/mol is a conventional standard transformed reference; cellular ΔG depends on the normalized quotient and matching thermodynamic conditions
- Idealized linear electron transfer uses one PSII and one PSI excitation per electron (four photons per NADPH); a stipulated 680-nm photon carries about 1.82 eV. Additional cyclic flow and losses require separate assumptions.
- Calvin cycle: 18 ATP + 12 NADPH → fix 6 CO₂ (1 net hexose)

## Figures and Diagrams

- `src/mermaid/biology_diagrams.py` — `glycolysis_pathway_diagram()`, `atp_synthesis_diagram()`, `photosynthesis_light_dark_diagram()`
- Repository-root `src/visualization/plots_botany.py` implements `plot_light_response_curve()`; `plots.py` owns registration.

## Shared source contract

Follow [manuscript instructions](../AGENTS.md) for H1s, stable IDs, metadata badges, references and authored assessments; see [writing examples](../../manuscript_guide.md). Implementation paths above are repository-root paths.
