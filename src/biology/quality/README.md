# Textbook quality audit

Umbrella manuscript quality engine (copyedit artifacts, stale claims, enrichment presence, advisory ledger). `scripts/audit_textbook_quality.py` wraps `collect_findings()`.

```bash
uv run python scripts/audit_textbook_quality.py --check --max-advisories 0
```

Tests: `tests/test_textbook_quality_audit.py`, `tests/test_audit_v3_and_crossref_gate.py`. See [AGENTS.md](AGENTS.md).
