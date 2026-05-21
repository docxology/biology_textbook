# `src/biology/` — AGENTS.md

Keep scientific logic here, not in `../../scripts/`. Public functions should be deterministic, typed, and tested with real numerical inputs. Prefer frozen dataclasses for result objects.

Utilities in this directory are part of the manuscript contract:

- `chapter_metadata.py`, `curriculum.py`, `alignment.py`, and `toc.py` drive generated badges, front matter, labs, question banks, and reference appendices.
- `current_claims.py` validates `../../manuscript/current_claims.yaml`; use `../../scripts/audit_current_claims.py --check`.
- `assessment.py` parses question-bank and lab assessment metadata; use `../../scripts/sync_assessment_metadata.py --check`.
- `crossref_validator.py` scans labels, `\cref{}` references, and hard-coded rendered-number prose.

When changing exports, update `../../docs/api_reference.md` and run targeted tests under `../../tests/`.
