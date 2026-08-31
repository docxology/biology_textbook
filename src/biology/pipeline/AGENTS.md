# AGENTS — biology_textbook/src/biology/pipeline

Status: REAL (doc fleet, 2026-08-30)

Manuscript collection, injection, and analysis pipeline for the textbook.

## Layout (principals)
- `collection.py` — collect ordered manuscript paths from config + canonical ToC.
- `injection.py` — inject ordered sources into `output/manuscript` for rendering.
- `numbering.py`, `registries.py`, `paths.py` — numbering, registries, path constants.
- `orphan_citations.py` + `orphan_citations.yaml`, `orphan_figures.py` + `orphan_figures.yaml` — orphan detection with config-driven rules.
- `analysis_smoke.py` — domain smoke tests run at the analysis stage.
- `report.py` — pipeline reporting.

## Gotchas
- The YAML files beside the orphan checkers are configuration, not output — edit those to tune rules.
