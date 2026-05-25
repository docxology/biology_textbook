# Biology Textbook Documentation

## Quick Navigation

| Document | What it covers |
| -------- | -------------- |
| [composable_authoring.md](composable_authoring.md) | **Stable IDs** (`sec:` / `fig:` / `eq:`), workflows (new chapter, figure, diagram, API), validation commands, test pointers |
| [architecture.md](architecture.md) | Two-layer architecture, module organisation, src/ layout, manuscript–code contract |
| [testing_guide.md](testing_guide.md) | Zero-mock policy, coverage standards, running tests, failure-to-fix |
| [pipeline_guide.md](pipeline_guide.md) | Build pipeline stages, execution commands, maintenance script order |
| [manuscript_guide.md](manuscript_guide.md) | Writing conventions, auto-numbering, figures, equations, templates |
| [../manuscript/AGENTS.md](../manuscript/AGENTS.md) | PDF density: keep `config.yaml` and `preamble.md` in sync; figure/diagram allowlists |
| [visualisation_guide.md](visualisation_guide.md) | Figure generation, Mermaid diagrams, matplotlib conventions, add-new-asset checklists |
| [api_reference.md](api_reference.md) | Public API of `src/biology/` subpackages and manuscript utilities |
| [agent_instructions.md](agent_instructions.md) | Editorial standards (voice, vignettes, clinical boxes); defers to composable + manuscript AGENTS for numbering |
| [accessibility.md](accessibility.md) | `config.yaml` keys: advisory vs test/code enforcement; optional reader PDF profile; HTML/PDF limits |
| [pedagogy_objectives_mapping.md](pedagogy_objectives_mapping.md) | Optional LO↔question-bank HTML comment convention |
| [absolute_language_triage.md](absolute_language_triage.md) | Advisory absolute-language categories: valid scientific absolutes, needed qualifiers, copyedit artifacts |
| [embedded_enrichment_audit_matrix.md](embedded_enrichment_audit_matrix.md) | Section-by-section audit matrix for embedded chapter, lab, question-bank, glossary, and appendix enrichment |
| [current_source_refresh_matrix.md](current_source_refresh_matrix.md) | Config-driven current-source refresh matrix for renderable manuscript sections and fast-moving claims |
| [AGENTS.md](AGENTS.md) | This `docs/` hub: directory list and documentation principles |

**Composable development:** Use [composable_authoring.md](composable_authoring.md) when adding or renaming chapters, registering `plot_*` figures or `*_diagram()` factories, or wiring `\cref` / `@fig:` / `{#eq:...}` so the same invariants the CI runs stay green. [agent_instructions.md](agent_instructions.md) covers **editorial** style; [manuscript/AGENTS.md](../manuscript/AGENTS.md) + tests are the **mechanical** contract.

## About This Project

The biology textbook project integrates:

- Manuscript content organised in **`manuscript/config.yaml`** (Unit 0, Units I – X, **44 chapters**, **44 labs**, **44 question banks**)
- **Quantitative models** in `src/biology/*` (9 domain subpackages) plus manuscript utilities and maintenance packages: `chapter_metadata.py`, `toc.py`, `curriculum.py`, `assessment.py`, `current_claims.py`, `alignment.py`, `crossref/` (shim at `crossref_validator.py`), and extracted `quality/`, `enrichment/`, `answer_refinement/`, `curriculum_sync/`; checkout bootstrap in `textbook_paths.py` and atomic I/O in `textbook_io.py`
- **Figures** (`src/visualization/plots.py`, 32 generators; **`src/visualization/cvd.py`** for colour-vision–friendly defaults tied to `config.yaml` → `accessibility.color_blindness_safe`) and **diagrams** (`src/mermaid/`, 24 registered diagrams plus 193 inline Mermaid fences, optional `mmdc`)
- **Tests:** run `uv run python -m pytest tests/ --cov=src --cov-fail-under=90` from the project directory for current count and coverage; invariant-style modules include build invariants, bibliography closure, crossref validator, chapter metadata, **accessibility** (alt proximity, quality, labs/questions)
- **Access / pedagogy reference:** [accessibility.md](accessibility.md), [pedagogy_objectives_mapping.md](pedagogy_objectives_mapping.md)
- **Embedded enrichment workflow:** run `uv run python scripts/enrich_embedded_textbook.py --dry-run` to inspect whether chapter frontier boxes, unit evidence threads, lab evidence upgrades, answer keys, and [embedded_enrichment_audit_matrix.md](embedded_enrichment_audit_matrix.md) are current.

**Checkout path:** this active tree can be used as a standalone project directory. Pipeline entry points still use `--project biology_textbook` from the template repository root when template infrastructure is available.

**Current gates:** 33 Python files under `scripts/`, 37 `test_*.py` modules under `tests/`, 32 registered matplotlib figures, 24 registered Mermaid diagrams, and 193 inline Mermaid fences in `manuscript/`. Use `scripts/generate_diagrams.py --strict-png` for publication PNG checks, `scripts/audit_current_claims.py --check` for fast-moving claims, `scripts/sync_assessment_metadata.py --dry-run` to preview question/lab metadata drift, `scripts/sync_assessment_metadata.py --check` for the assessment gate, `scripts/audit_visual_contracts.py --figures-root <tmp>/figures --output <tmp>/visual_manifest.json --render-inline --check` for the derived 249-record visual manifest and square-ish aspect policy, `tests/test_chapter_pedagogy_coverage.py` for REVIEW §7 pedagogy locks, and `scripts/audit_publication_readiness.py --check` (temporary visual artifacts; `--full` before release) for the aggregate gate.

See [../AGENTS.md](../AGENTS.md) for project layout, validation commands, AI protocol, and invariant conventions.
