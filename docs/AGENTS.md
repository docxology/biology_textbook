# Biology Textbook Documentation — AGENTS.md

## Documentation Contract

This `docs/` directory documents the active standalone `biology_textbook` checkout. Template-hosted runs may still resolve the same project through `--project biology_textbook` when the template infrastructure is available.

## Directory Contents

| File | Purpose |
| ---- | ------- |
| `AGENTS.md` | This file — documentation hub overview and conventions |
| `README.md` | Quick navigation index for docs/ |
| `composable_authoring.md` | Stable `\label` / `\cref` schema, end-to-end workflows (chapter, figure, diagram, API), validation commands, test pointers |
| `architecture.md` | System architecture: src/, tests/ (70 `test_*.py` modules), scripts/, docs/manuscript/ relationships |
| `accessibility.md` | Which `config.yaml` flags are advisory vs test/code; reader PDF profile; CVD / alt-text policy |
| `absolute_language_triage.md` | Advisory absolute-language categories: valid scientific absolutes, needed qualifiers, copyedit artifacts |
| `embedded_enrichment_audit_matrix.md` | Section-by-section audit matrix for embedded chapter, lab, question-bank, glossary, and appendix enrichment |
| `current_source_refresh_matrix.md` | Config-driven current-source refresh matrix for renderable manuscript sections and fast-moving claims |
| `pedagogy_objectives_mapping.md` | Optional learning-objective → question-bank comment mapping |
| `agent_instructions.md` | Editorial standards for agents (voice, structure); not the mechanical numbering contract |
| `testing_guide.md` | Zero-mock testing policy, coverage standards, running tests |
| `pipeline_guide.md` | Build pipeline stages, execution, and pipeline configuration |
| `manuscript_guide.md` | Chapter writing conventions, auto-numbering, figures, citations |
| `visualization_guide.md` | Figure generation, Mermaid diagrams, matplotlib conventions |
| `api_reference.md` | Key public functions from all `src/biology/` subpackages (manually curated; refresh when you add or rename public APIs—see spot-check note in [api_reference.md](api_reference.md)) |

## Documentation Principles

- **Composable reference rules** (IDs, registries, script order, which test fails when) live in `composable_authoring.md`; pair it with `../manuscript/AGENTS.md` for allowlists and paths.
- `agent_instructions.md` is **editorial** (quantitative writing, vignettes, clinical boxes); it defers to `docs/manuscript/AGENTS.md` + tests for mechanical cross-refs and figure numbering.
- `api_reference.md` is a **curated** list of manuscript-facing and test-exercised entry points (not an auto-generated dump); after substantive module changes, run `rg '^\s*def ' src/biology` and add or update rows for any new public API you expect authors to call
- Current-claim workflow docs must point to `docs/manuscript/current_claims.yaml`, `src/biology/current_claims.py`, `scripts/audit_current_claims.py --check`, and `tests/test_current_claims_ledger.py`.
- Assessment workflow docs must point to `src/biology/assessment.py`, `scripts/sync_assessment_metadata.py --check`, `tests/test_assessment_metadata.py`, `tests/test_lab_pedagogy_alignment.py`, and `tests/test_chapter_pedagogy_coverage.py`.
- Visual workflow docs must distinguish registered Mermaid PNGs (`scripts/generate_diagrams.py --strict-png` for publication), 197 inline Mermaid fences rendered strictly during PDF preprocessing or `audit_visual_contracts.py --render-inline`, 42 matplotlib figures registered in `ALL_FIGURE_GENERATORS`, and the derived visual manifest/review matrix checked by `scripts/audit_visual_contracts.py --figures-root <tmp>/figures --output <tmp>/visual_manifest.json --render-inline --check`.
- Every pipeline stage must be documented in `pipeline_guide.md`
- All testing patterns (and any exceptions to the zero-mock policy) must appear in `testing_guide.md`
- Manuscript conventions (naming, numbering, figures, equations) are defined in `manuscript_guide.md` and `composable_authoring.md` (workflows)

## Conventions

- Documentation files use Markdown (`.md`) with GitHub-style alerts
- Internal links use relative paths
- External links include retrieval date
- All code examples are real (not pseudocode), runnable, and tested
