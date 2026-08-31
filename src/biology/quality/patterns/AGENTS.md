# AGENTS — biology_textbook/src/biology/quality/patterns

Status: REAL (doc fleet, 2026-08-30)

Pattern-based quality checks.

## Layout
- `assessment.py` — pattern assessment primitives.
- `audit_manuscript.py` — runs pattern audits over the manuscript tree.

## Gotchas
- Part of the `biology.quality` engine; invoked via the quality CLI, not standalone (unverified whether a direct entry point exists).
