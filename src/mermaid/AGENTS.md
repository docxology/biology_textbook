# `src/mermaid/` — AGENTS.md

Treat `ALL_BIOLOGY_DIAGRAMS` as the registered Mermaid visual manifest. New reusable diagrams must return a `MermaidDiagram`, be added to the registry, be documented in `../../docs/api_reference.md`, and be referenced from manuscript prose before they count as part of the textbook.

Inline manuscript Mermaid is separate: the manuscript currently has 192 inline fences, each requiring one alt comment and one italic caption. PDF preprocessing renders those fences strictly to PNG under `output/figures/mermaid_inline/`.

Use `../../scripts/generate_diagrams.py --strict-png` for publication checks and `../../tests/test_mermaid_and_visualization.py` for registry/renderer coverage.
