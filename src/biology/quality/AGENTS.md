# `src/biology/quality/` — textbook quality audit engine

Logic extracted from `scripts/audit_textbook_quality.py` (formerly 1161 lines). The script is now a thin argparse wrapper (~110 lines).

## Modules

| File | Role |
| --- | --- |
| `paths.py` | `PROJECT`, `MANUSCRIPT`, `QUALITY_ADVISORIES` (monkeypatchable in tests) |
| `models.py` | `Finding`, `ManuscriptSurface` |
| `patterns.py` | Copyedit regex catalogs, generic-answer patterns, advisory classifications |
| `engine.py` | `collect_findings()` and per-surface auditors |
| `cli.py` | `main(argv)` — `--check`, `--max-advisories`, ledger integration |

## CLI

```bash
uv run python scripts/audit_textbook_quality.py --check --max-advisories 0
```

Exit **0** when no errors and advisory count ≤ `--max-advisories`. The script re-exports `Finding`, `ManuscriptSurface`, and pattern constants for legacy `importlib` tests.
