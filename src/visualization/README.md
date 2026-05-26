# Visualization Package

Matplotlib figure generation and colour-vision-friendly plotting defaults live here.

| File | Role |
| ---- | ---- |
| `plots.py` | 42 `plot_*` functions plus `ALL_FIGURE_GENERATORS` |
| `cvd.py` | Colour-vision-friendly palette constants and line/hatch conventions |
| `__init__.py` | Re-exports public plot functions and the registry |

Run `uv run python scripts/generate_figures.py` from the project root to regenerate `output/figures/`.
