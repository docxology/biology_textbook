# Biology Textbook Documentation — AGENTS.md

## Overview

This `docs/` directory documents **`projects_in_progress/biology_textbook/`** in this checkout. The same tree may be promoted to `projects/biology_textbook/`; `resolve_project_root` prefers `projects/` when markers are present and otherwise resolves the WIP path.

## Directory Contents

| File | Purpose |
| ---- | ------- |
| `AGENTS.md` | This file — documentation hub overview and conventions |
| `README.md` | Quick navigation index for docs/ |
| `composable_authoring.md` | Stable `\label` / `\cref` schema, end-to-end workflows (chapter, figure, diagram, API), validation commands, test pointers |
| `architecture.md` | System architecture: src/, tests/ (27 `test_*.py` modules), scripts/, manuscript/ relationships |
| `accessibility.md` | Which `config.yaml` flags are advisory vs test/code; reader PDF profile; CVD / alt-text policy |
| `pedagogy_objectives_mapping.md` | Optional learning-objective → question-bank comment mapping |
| `agent_instructions.md` | Editorial standards for agents (voice, structure); not the mechanical numbering contract |
| `testing_guide.md` | Zero-mock testing policy, coverage standards, running tests |
| `pipeline_guide.md` | Build pipeline stages, execution, and pipeline configuration |
| `manuscript_guide.md` | Chapter writing conventions, auto-numbering, figures, citations |
| `visualisation_guide.md` | Figure generation, Mermaid diagrams, matplotlib conventions |
| `api_reference.md` | Key public functions from all `src/biology/` subpackages (manually curated; refresh when you add or rename public APIs—see spot-check note in [api_reference.md](api_reference.md)) |

## Documentation Principles

- **Composable reference rules** (IDs, registries, script order, which test fails when) live in `composable_authoring.md`; pair it with `../manuscript/AGENTS.md` for allowlists and paths.
- `agent_instructions.md` is **editorial** (quantitative writing, vignettes, clinical boxes); it defers to `manuscript/AGENTS.md` + tests for mechanical cross-refs and figure numbering.
- `api_reference.md` is a **curated** list of manuscript-facing and test-exercised entry points (not an auto-generated dump); after substantive module changes, run `rg '^\s*def ' src/biology` and add or update rows for any new public API you expect authors to call
- Current-claim workflow docs must point to `manuscript/current_claims.yaml`, `src/biology/current_claims.py`, `scripts/audit_current_claims.py --check`, and `tests/test_current_claims_ledger.py`.
- Assessment workflow docs must point to `src/biology/assessment.py`, `scripts/sync_assessment_metadata.py --check`, `tests/test_assessment_metadata.py`, and `tests/test_lab_pedagogy_alignment.py`.
- Visual workflow docs must distinguish registered Mermaid PNGs (`scripts/generate_diagrams.py --strict-png` for publication), 192 inline Mermaid fences rendered strictly during PDF preprocessing, matplotlib figures registered in `ALL_FIGURE_GENERATORS`, and the derived `output/figures/visual_manifest.json` checked by `scripts/audit_visual_contracts.py --check`.
- Every pipeline stage must be documented in `pipeline_guide.md`
- All testing patterns (and any exceptions to the zero-mock policy) must appear in `testing_guide.md`
- Manuscript conventions (naming, numbering, figures, equations) are defined in `manuscript_guide.md` and `composable_authoring.md` (workflows)

## Conventions

- Documentation files use Markdown (`.md`) with GitHub-style alerts
- Internal links use relative paths
- External links include retrieval date
- All code examples are real (not pseudocode), runnable, and tested
