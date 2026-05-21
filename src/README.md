# Biology Textbook Source

This directory contains the project code that the manuscript and tests depend on.
Scripts in `../scripts/` are thin orchestrators; reusable logic belongs here.

## Layout

| Path | Purpose |
| ---- | ------- |
| `biology/` | Nine domain subpackages plus manuscript utilities (`chapter_metadata.py`, `toc.py`, `crossref_validator.py`, `current_claims.py`, `assessment.py`) |
| `mermaid/` | Mermaid renderer, generic builders, and the 24 registered biology diagram factories; use strict PNG mode for publication builds |
| `visualization/` | Eighteen matplotlib figure generators plus the colour-vision-friendly palette helpers |

Run `uv run pytest tests/ --cov=src --cov-fail-under=90` from the project root
after changing public functions, metadata APIs, diagram registries, or figure
generators.

See [AGENTS.md](AGENTS.md) for the detailed contributor contract and
[../docs/api_reference.md](../docs/api_reference.md) for manuscript-facing APIs.
