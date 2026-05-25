# Embedded enrichment

Frontier boxes, unit evidence threads, lab evidence upgrades, and audit-matrix generation for embedded manuscript content. `scripts/enrich_embedded_textbook.py` is the CLI entrypoint.

```bash
uv run python scripts/enrich_embedded_textbook.py --dry-run
```

Tests: `tests/test_enrichment_substance_gate.py`, `tests/test_textbook_quality_audit.py`. See [AGENTS.md](AGENTS.md).
