# Unit X — Ecology: AGENTS.md

## Source Module

`src/biology/ecology/ecology.py`:
- `lotka_volterra()` — predator–prey ODE integration
- `logistic_growth()` — N(t) with carrying capacity K
- `biodiversity_indices()` — Shannon, Simpson, species richness
- `species_area_relationship()` — S = cA^z
- `BIOME_DATA` / `BIOMES` — biome NPP and climate fields

## Chapters

1. `population_ecology.md` — Population Ecology and Growth Models
2. `community_ecology.md` — Community Ecology and Species Interactions
3. `ecosystem_ecology.md` — Ecosystem Ecology and Biogeochemical Cycles
4. `biomes_and_conservation.md` — Biomes and Conservation Biology

## Key Equations

- Exponential growth: dN/dt = rN
- Logistic growth: dN/dt = rN(1 − N/K)
- Lotka-Volterra (prey): dN/dt = αN − βNP
- Lotka-Volterra (pred): dP/dt = δNP − γP
- Shannon diversity: H' = −Σ pᵢ ln pᵢ
- Species-area: S = cA^z (z ≈ 0.25 continents; 0.3 islands)

## Figures and Diagrams

- `src/visualization/plots.py` — `plot_lotka_volterra()`, `plot_logistic_growth()`, `plot_species_area_relationship()`, `plot_biome_distribution()`
- `src/mermaid/biology_diagrams.py` — `food_web_diagram()`, `nutrient_cycle_diagram()`, `population_growth_stages_diagram()`

## Chapter Metadata Convention

All chapter files in this unit carry (inserted automatically by the scripts):

- `\label{sec:unit_X_<stem>}` on the line after the H1 — cross-reference with `\cref{sec:unit_X_<stem>}`
- `<!-- chapter-metadata-badge -->` blockquote with difficulty (Level 1/3–3/3), reading time, lecture time, and prerequisites (data in `../../src/biology/chapter_metadata.py`)

See [../AGENTS.md](../AGENTS.md) and [../../docs/manuscript_guide.md](../../docs/manuscript_guide.md) for the full set of invariants.
