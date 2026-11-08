# Unit X — Ecology: AGENTS.md

## Source Module

`src/biology/ecology/ecology.py`:
- `lotka_volterra()` — predator–prey ODE integration
- `logistic_growth()` — N(t) with carrying capacity K
- `biodiversity_indices()` — Shannon, Simpson, species richness
- `species_area_relationship()` — S = cA^z
- `BIOME_DATA` / `BIOMES` — biome NPP and climate fields

## Chapters

[README.md](README.md) lists chapter filenames/titles; [config.yaml](../config.yaml) owns order.

## Key Equations

- Exponential growth: dN/dt = rN
- Logistic growth: dN/dt = rN(1 − N/K)
- Lotka-Volterra (prey): dN/dt = αN − βNP
- Lotka-Volterra (pred): dP/dt = δNP − γP
- Shannon diversity: H' = −Σ pᵢ ln pᵢ
- Species–area: S = cA^z with supplied scale-dependent parameters; no universal continental/island exponent is implied.

## Figures and Diagrams

- `plot_lotka_volterra()`, `plot_logistic_growth()`, `plot_species_area_relationship()` and `plot_biome_distribution()` are registered in `plots.py`. Biome climate markers are equal-sized; marker area does not encode NPP. See [visual conventions](../../visualization_guide.md).
- `src/mermaid/biology_diagrams.py` — `food_web_diagram()`, `nutrient_cycle_diagram()`, `population_growth_stages_diagram()`

## Shared source contract

Follow [manuscript instructions](../AGENTS.md) for H1s, stable IDs, metadata badges, references and authored assessments; see [writing examples](../../manuscript_guide.md). Implementation paths above are repository-root paths.
