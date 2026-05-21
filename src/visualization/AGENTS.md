# `src/visualization/` — AGENTS.md

Treat `ALL_FIGURE_GENERATORS` as the matplotlib visual manifest. New reusable figures must be implemented in `plots.py`, registered, referenced from the manuscript, documented in `../../docs/api_reference.md`, and covered by `../../tests/test_mermaid_and_visualization.py`.

Use `cvd.py` palette constants instead of hard-coded red/green pairs. Plot functions must save files through the provided output directory and return the generated `Path`; do not call `plt.show()`.
