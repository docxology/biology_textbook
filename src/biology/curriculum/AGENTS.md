# AGENTS — biology_textbook/src/biology/curriculum

Status: REAL (doc fleet, 2026-08-30)

Curriculum metadata records for the textbook units (the canonical unit roster).

## Layout
- `models.py` — frozen dataclass `CurriculumRecord`.
- `_factory.py` — `_r(...)` record factory helper.
- `unit_0.py`, `unit_i.py` … `unit_x.py` — per-unit `RECORDS` tuples; authored config IDs remain `unit_I` … `unit_X`.
- `__init__.py` — aggregates all unit RECORDS into the package-level registry.

## Invariants
- Adding a unit means adding a `unit_*.py` module AND registering it in `__init__.py`; downstream quality/audits read this registry.
