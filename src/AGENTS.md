# `src/` — AGENTS.md

## Role

Scientific computation, manuscript metadata, maintenance engines and rendering adapters live here. Project-local scripts coordinate I/O and call these modules; do not move scientific/business logic into orchestrators.

## Module ownership

- `biology/`: domain models including `foundations/`, metadata and maintenance packages. `biology/curriculum/` and `biology/visual_contracts/` are packages, not flat `.py` modules.
- `visualization/plots_<domain>.py`: domain figure implementations; `plots.py`: registry and wrappers; `__init__.py`: public import facade. The facade exports functions as well as the registry; do not infer missing exports from implementation placement.
- `mermaid/`: registered specifications, factories and rendering. Non-strict `.mmd` fallback is authoring output, not publication evidence.
- `textbook_paths.py`, `textbook_io.py`, `textbook_logging.py`: project path, atomic-write and logging support. Standalone project sources take precedence; admitted template code is a read-only library.

## Contracts and changes

Use [architecture](../docs/architecture.md) for boundaries and [API reference](../docs/api_reference.md) for curated signatures; neither is a fabricated exhaustive symbol inventory. Re-read actual source exports/signatures when changing callers. Preserve frozen result objects where appropriate, typed public interfaces and explicit reproducible RNG inputs. Do not assume every simulation names its seed argument identically.

[Composable authoring](../docs/composable_authoring.md) owns cross-file updates; [manuscript instructions](../docs/manuscript/AGENTS.md) own H1s, labels and authored assessments. Curriculum/enrichment must preserve authored lab procedures, question prompts/keys, rubrics and coverage notes. Unsupported answer repair must refuse without writing.

[Visualization](../docs/visualization_guide.md) owns output and review conventions; [pipeline](../docs/pipeline_guide.md) owns launch recipes and receipts; [testing](../docs/testing_guide.md) owns real test nodes, coverage and permitted isolation. Numerical tests, structural counts and source gates do not establish scientific completeness, accessible final print layout or remote publication.
