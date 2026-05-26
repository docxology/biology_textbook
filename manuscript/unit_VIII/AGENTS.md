# Unit VIII — Botany: AGENTS.md

## Source Module

`src/biology/botany/botany.py`:
- `water_potential()` — ψ = ψs + ψp from solute concentration and turgor
- `transpiration_flux()` — Fick evaporation model
- `photosynthesis_rate()` — Michaelis-Menten CO₂ fixation model
- `light_response_curve()` — hyperbolic Pmax saturation
- `PHOTOSYNTHESIS_PATHWAYS` — C3/C4/CAM comparative data

## Chapters

1. `plant_structure_and_water.md` — Plant Structure and Water Relations
2. `plant_reproduction.md` — Plant Reproduction and Development
3. `plant_responses.md` — Plant Responses to the Environment

## Key Equations

- Water potential: ψ = ψs + ψp; ψs = −iCRT; ψp = turgor pressure
- Transpiration flux: E = g_s · Δw
- Cohesion-tension: negative xylem pressure (tension) up to −50 MPa before cavitation

## Figures and Diagrams

- `src/visualization/plots.py` — `plot_light_response_curve()`
- `src/mermaid/biology_diagrams.py` — `hormone_signaling_diagram()`, `photosynthesis_light_dark_diagram()`

## Chapter Metadata Convention

All chapter files in this unit carry (inserted automatically by the scripts):

- `\label{sec:unit_VIII_<stem>}` on the line after the H1 — cross-reference with `\cref{sec:unit_VIII_<stem>}`
- `<!-- chapter-metadata-badge -->` blockquote with difficulty (Level 1/3–3/3), reading time, lecture time, and prerequisites (data in `../../src/biology/chapter_metadata.py`)

See [../AGENTS.md](../AGENTS.md) and [../../docs/manuscript_guide.md](../../docs/manuscript_guide.md) for the full set of invariants.
