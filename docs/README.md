# Biology Textbook Documentation

## Quick Navigation

| Document | What it covers |
| -------- | -------------- |
| [composable_authoring.md](composable_authoring.md) | **Stable IDs** (`sec:` / `fig:` / `eq:`), workflows (new chapter, figure, diagram, API), validation commands, test pointers |
| [architecture.md](architecture.md) | Standalone ownership, read-only renderer dependency, src/ layout and manuscript–code contract |
| [testing_guide.md](testing_guide.md) | Real-computation policy, isolation exceptions and coverage limits |
| [pipeline_guide.md](pipeline_guide.md) | Build pipeline stages, execution commands, maintenance script order |
| [manuscript_guide.md](manuscript_guide.md) | Writing conventions, auto-numbering, figures, equations, templates |
| [manuscript/AGENTS.md](manuscript/AGENTS.md) | Canonical H1s, stable IDs, authored assessments and paired PDF typography settings |
| [visualization_guide.md](visualization_guide.md) | Figure generation, Mermaid diagrams, matplotlib conventions, add-new-asset checklists |
| [api_reference.md](api_reference.md) | Public API of `src/biology/` subpackages and manuscript utilities |
| [agent_instructions.md](agent_instructions.md) | Editorial standards (voice, vignettes, clinical boxes); defers to composable + manuscript AGENTS for numbering |
| [publication_abstract.md](publication_abstract.md) | Two-paragraph Zenodo/GitHub/cover abstract (metadata only; not in PDF pipeline) |
| [accessibility.md](accessibility.md) | `config.yaml` keys: advisory vs test/code enforcement; optional reader PDF profile; HTML/PDF limits |
| [pedagogy_objectives_mapping.md](pedagogy_objectives_mapping.md) | Curated semantic LO/Bloom mappings and lab rubrics |
| [absolute_language_triage.md](absolute_language_triage.md) | Advisory absolute-language categories: valid scientific absolutes, needed qualifiers, copyedit artifacts |
| [embedded_enrichment_audit_matrix.md](embedded_enrichment_audit_matrix.md) | Generated structural navigation snapshot; not scientific/human-review evidence |
| [current_source_refresh_matrix.md](current_source_refresh_matrix.md) | Dated source-refresh reports and current maintenance rules, not live certification |
| [STUDENT_GUIDE.md](STUDENT_GUIDE.md) | Study strategies and selected equation/term review |
| [figure_gap_matrix.md](figure_gap_matrix.md) | Historical plot-coverage snapshot, not a current manifest |
| [figure_expansion_research_memo.md](figure_expansion_research_memo.md) | Historical prioritization rationale and superseded deferrals |
| [AGENTS.md](AGENTS.md) | This `docs/` hub: directory list and documentation principles |
| [../TODO.md](../TODO.md) | Native Markdown-checkbox backlog; dated completion summaries and ISA/REVIEW snapshots are historical, not live gate or release receipts |

**Composable development:** Use [composable_authoring.md](composable_authoring.md) when adding or renaming chapters, registering `plot_*` figures or `*_diagram()` factories, or wiring `\cref` / `@fig:` / `{#eq:...}` so the same invariants the CI runs stay green. [agent_instructions.md](agent_instructions.md) covers **editorial** style; [docs/manuscript/AGENTS.md](../docs/manuscript/AGENTS.md) + tests are the **mechanical** contract.

## About This Project

The biology textbook project integrates:

- Manuscript content organized in **`docs/manuscript/config.yaml`** (Unit 0, Units I – X, **44 chapters**, **44 labs**, **44 question banks**)
- **Quantitative models** in `src/biology/`, including `foundations/`, plus metadata/maintenance packages: `chapter_metadata.py`, `toc.py`, `curriculum/`, `assessment.py`, `current_claims.py`, `alignment.py`, `crossref/`, `quality/`, `enrichment/`, `answer_refinement/` and `curriculum_sync/`. Bootstrap and atomic I/O live in `textbook_paths.py` and `textbook_io.py`.
- **Visuals:** registered matplotlib/diagram generators and manuscript Mermaid fences; publication requires pinned mmdc and decoded PNGs, not fixed inventory proof here.
- **Tests:** run `uv run python -m pytest tests/ --cov=src --cov-fail-under=90` from the project directory for current count and coverage; invariant-style modules include build invariants, bibliography closure, crossref validator, chapter metadata, **accessibility** (alt proximity, quality, labs/questions)
- **Access / pedagogy reference:** [accessibility.md](accessibility.md), [pedagogy_objectives_mapping.md](pedagogy_objectives_mapping.md)
- **Assessments:** preserve authored prompt-specific solutions, semantic mappings and finite printed lab packets. Unsupported answer generation refuses without writing.

**Standalone execution:** project-local scripts use locked dependencies and a read-only template selected explicitly or genuinely enclosing the project, never ambient neighbors or template-root recipes. See [pipeline_guide.md](pipeline_guide.md).

Software 2.0.0/edition 1.1 remains unreleased. Current proof is the exact-source full receipt plus separate inspection of its PDF, not historical ISA/REVIEW reports; local validation is distinct from remote publication. The existing DOI identifies prior release 1.0.0 only. See [../CHANGELOG.md](../CHANGELOG.md).

**Current gate contracts:** scripts/audit_publication_readiness.py --check performs source, visual, lint/type and recursive markdown/prerender review. Add --full for tests with configured coverage, analysis, fresh project-local render and strict PDF-log checks. Current passing counts and artifact inventories require execution, not this guide. Assessment synchronization validates curated records; unsupported answer generation refuses without writing.

See [../AGENTS.md](../AGENTS.md) for project layout, validation commands, AI protocol, and invariant conventions.
