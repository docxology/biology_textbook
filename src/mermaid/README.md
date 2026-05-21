# Mermaid Package

Mermaid source builders and rendering live here.

| File | Role |
| ---- | ---- |
| `renderer.py` | `MermaidDiagram` and `MermaidRenderer`; writes PNG with `mmdc`, or `.mmd` fallback unless strict PNG mode is enabled |
| `diagrams.py` | Generic flowchart, sequence, class, state, and pie builders |
| `biology_diagrams.py` | Biology diagram factories and `ALL_BIOLOGY_DIAGRAMS` registry with 24 entries |

Run `uv run python scripts/generate_diagrams.py --strict-png` from the project root for publication checks.
