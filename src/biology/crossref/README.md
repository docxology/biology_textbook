# Cross-reference validator

Markdown and LaTeX label graph for `\label{}`, `@fig:`, `@eq:`, and cleveref consistency. Public API re-exported from `biology.crossref_validator`.

```bash
uv run python -m pytest tests/test_crossref_validator.py -q
```

Tests: `tests/test_crossref_validator.py`, `test_crossref_validator_internals.py`, `test_crossref_validator_edges.py`. See [AGENTS.md](AGENTS.md).
