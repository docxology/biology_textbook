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
| `publication_gate.py` | Aggregate publication readiness orchestrator (`run_publication_gate`) |

## `publication_gate.py`

`run_publication_gate(..., max_workers=1)` runs command and in-process Python checks with optional parallelism:

- Each step may declare `depends_on: frozenset[str]`; a step runs only after all dependencies succeed.
- **Sequential chains:** `figures-strict` → `diagrams-strict` → `visual-contracts` → `artifact-counts`; root `setup` → `render` → `validate` → `pdf-log` (always sequential under `--full`).
- **Parallel waves:** when `max_workers > 1`, independent steps (ruff, mypy, claims sync, recursive markdown/prerender, hygiene) run concurrently via thread pools; subprocess steps use isolated temp artifact dirs.
- Default `max_workers=1` preserves the original strictly sequential behavior.

CLI: `scripts/audit_publication_readiness.py --check [--full] [--workers N]`.

Tests: `tests/test_publication_gate.py` (dependency ordering, ready-step invariants, `max_workers=1` equivalence).

## CLI

```bash
uv run python scripts/audit_textbook_quality.py --check --max-advisories 0
```

Exit **0** when no errors and advisory count ≤ `--max-advisories`. The script re-exports `Finding`, `ManuscriptSurface`, and pattern constants for legacy `importlib` tests.
