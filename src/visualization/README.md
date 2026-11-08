# Visualization Package

Registered matplotlib figures, shared save/print geometry, and color/line/hatch conventions live here.

| File | Role |
| ---- | ---- |
| `plots.py` | `ALL_FIGURE_GENERATORS` and per-figure aspect policy; implementations live in `plots_*.py` |
| `_scaffold.py`, `cvd.py` | Shared rendering, palette, and distinguishability conventions |
| `__init__.py` | Re-exports public plot functions and the registry |

Project-local figure commands, provenance limits, manifests, and actual print/grayscale review are owned by [the visualization guide](../../docs/visualization_guide.md).
