# Unit VIII — Botany: AGENTS.md

## Source Module

`src/biology/botany/botany.py`:
- `water_potential()` — ψ = ψs + ψp from solute concentration and turgor
- `transpiration_flux()` — Fick evaporation model
- `photosynthesis_rate()` — hyperbolic gross light response minus dark respiration, returning net CO₂ assimilation
- `light_response_curve()` — hyperbolic Pmax saturation
- `PHOTOSYNTHESIS_PATHWAYS` — C3/C4/CAM comparative data

## Chapters

[README.md](README.md) lists chapter filenames/titles; [config.yaml](../config.yaml) owns order.

## Key Equations

- Water potential: ψ = ψs + ψp; ψs = −iCRT; ψp = turgor pressure
- Transpiration flux: E = g_s · Δw
- Cohesion–tension: discuss negative xylem pressure and species/condition-dependent cavitation limits with chapter sources, not a universal numeric threshold.

## Figures and Diagrams

- Repository-root `src/visualization/plots_botany.py` implements `plot_light_response_curve()`; `plots.py` owns registration.
- `src/mermaid/biology_diagrams.py` — `hormone_signaling_diagram()`, `photosynthesis_light_dark_diagram()`

## Shared source contract

Follow [manuscript instructions](../AGENTS.md) for H1s, stable IDs, metadata badges, references and authored assessments; see [writing examples](../../manuscript_guide.md). Implementation paths above are repository-root paths.
