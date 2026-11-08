# Biology Textbook Source

This directory contains the project code that the manuscript and tests depend on.
Scripts in `../scripts/` are thin orchestrators; reusable logic belongs here.

## Layout

| Path | Purpose |
| ---- | ------- |
| `biology/` | Nine traditional domains, `foundations/`, and manuscript/maintenance packages; see the API reference rather than a fixed copied module inventory |
| `mermaid/` | Declarative biology diagrams and shared builders/rendering; strict PNG mode is required for publication |
| `visualization/` | Registered domain/foundations matplotlib generators and color/line/hatch conventions |

Run `uv run python -m pytest tests/ --cov=src --cov-fail-under=90` from the project root
after changing public functions, metadata APIs, diagram registries, or figure
generators.

See [AGENTS.md](AGENTS.md) for the detailed contributor contract and
[../docs/api_reference.md](../docs/api_reference.md) for manuscript-facing APIs.
