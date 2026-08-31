# AGENTS — biology_textbook/src/biology/quality/audits

Status: REAL (doc fleet, 2026-08-30)

Audit modules for the textbook quality engine (invoked via `biology.quality.cli`).

## Layout
- `content.py`, `references.py`, `enrichment.py`, `advisories.py`, `surfaces.py` — individual audit lanes (content, references, enrichment, advisories, surfaces).
- `helpers.py` — shared audit helpers.
- `__init__.py` — exports.

## Gotchas
- The audit engine/CLI live in the parent `quality/` package (`engine.py`, `cli.py`); this subpackage holds the lane implementations only.
