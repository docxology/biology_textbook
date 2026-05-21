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
| [AGENTS.md](AGENTS.md) | This `docs/` hub: directory list and documentation principles |

**Composable development:** Use [composable_authoring.md](composable_authoring.md) when adding or renaming chapters, registering `plot_*` figures or `*_diagram()` factories, or wiring `\cref` / `@fig:` / `{#eq:...}` so the same invariants the CI runs stay green. [agent_instructions.md](agent_instructions.md) covers **editorial** style; [manuscript/AGENTS.md](../manuscript/AGENTS.md) + tests are the **mechanical** contract.

## About This Project

The biology textbook project integrates:

- Manuscript content organised in **`manuscript/config.yaml`** (Unit 0, Units I – X, **39 chapters**, **39 labs**, **39 question banks**)
- **Quantitative models** in `src/biology/*` (9 domain subpackages) plus two manuscript utilities — `src/biology/chapter_metadata.py` (per-chapter difficulty/time/prereq records) and `src/biology/crossref_validator.py` (enforces `\label`/`\cref` consistency)
- **Figures** (`src/visualization/plots.py`, 18 generators; **`src/visualization/cvd.py`** for colour-vision–friendly defaults tied to `config.yaml` → `accessibility.color_blindness_safe`) and **diagrams** (`src/mermaid/`, 24 diagrams, optional `mmdc`)
- **Tests:** run `uv run pytest tests/ --cov=src --cov-fail-under=90` from the project directory for current count and coverage; invariant-style modules include build invariants, bibliography closure, crossref validator, chapter metadata, **accessibility** (alt proximity, quality, labs/questions)
- **Access / pedagogy reference:** [accessibility.md](accessibility.md), [pedagogy_objectives_mapping.md](pedagogy_objectives_mapping.md)
- **Embedded enrichment workflow:** run `uv run python scripts/enrich_embedded_textbook.py --dry-run` to inspect whether chapter frontier boxes, unit evidence threads, lab evidence upgrades, answer keys, and [embedded_enrichment_audit_matrix.md](embedded_enrichment_audit_matrix.md) are current.

**Checkout path:** `projects_in_progress/biology_textbook/` in this workspace. `resolve_project_root` uses `projects/biology_textbook/` when project markers are present; otherwise the same name under `projects_in_progress/`. Pipeline entry points use `--project biology_textbook` from the template repository root.

**Current gates:** 31 Python files under `scripts/`, 27 `test_*.py` modules under `tests/`, 24 registered Mermaid diagrams, 18 registered matplotlib figures, and 192 inline Mermaid fences in `manuscript/`. Use `scripts/generate_diagrams.py --strict-png` for publication PNG checks, `scripts/audit_current_claims.py --check` for fast-moving claims, `scripts/sync_assessment_metadata.py --dry-run` to preview question/lab metadata drift, `scripts/sync_assessment_metadata.py --check` for the assessment gate, and `scripts/audit_visual_contracts.py --check` for the derived visual manifest.

See [../AGENTS.md](../AGENTS.md) for project layout, validation commands, AI protocol, and invariant conventions.
