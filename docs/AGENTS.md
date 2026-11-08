# Biology Textbook Documentation — AGENTS.md

## Documentation Contract

This directory documents the standalone checkout. Run project-local entry points; an admitted template is a read-only library, never an external working directory or output recipe. [pipeline_guide.md](pipeline_guide.md) owns execution prerequisites and commands.

## Guide ownership

[README.md](README.md) is the complete navigation index. Keep one authoritative home per contract:

- [manuscript/AGENTS.md](manuscript/AGENTS.md): canonical H1s, stable IDs, reference types and source ownership.
- [composable_authoring.md](composable_authoring.md): ordered cross-file authoring workflows.
- [manuscript_guide.md](manuscript_guide.md): copyable Markdown/LaTeX examples; [agent_instructions.md](agent_instructions.md): editorial evidence rules.
- [visualization_guide.md](visualization_guide.md): implementation/registry/facade, strict PNGs and project-output review recipe; [accessibility.md](accessibility.md): alt/caption semantics, redundant encodings and review limits.
- [pipeline_guide.md](pipeline_guide.md): custody, prerequisites and publication gates; [testing_guide.md](testing_guide.md): real test nodes, coverage and isolation limits.
- [api_reference.md](api_reference.md): curated current signatures; [pedagogy_objectives_mapping.md](pedagogy_objectives_mapping.md): required reviewed item mappings and lab rubrics.
- [absolute_language_triage.md](absolute_language_triage.md): source-bound advisory decisions.

## Documentation Principles

- Link to the contract owners above rather than copying mutable inventories, CLI recipes or symbol allowlists.
- API examples must match current exports/signatures; distinguish domain functions from registry wrappers.
- Current claims belong in `docs/manuscript/current_claims.yaml` and are checked by `scripts/audit_current_claims.py --check`.
- Assessment metadata validates authored semantic mappings; it must not regenerate question keys, procedures, rubrics or coverage notes.
- Visual documentation must distinguish registered diagrams, inline Mermaid and matplotlib output. Inline review rendering must remain under the project's real `output/`; use the owned visualization-guide recipe.
- Every pipeline stage must be documented in `pipeline_guide.md`
- All testing patterns (and any exceptions to the zero-mock policy) must appear in `testing_guide.md`
- Manuscript conventions (naming, numbering, figures, equations) are defined in `manuscript_guide.md` and `composable_authoring.md` (workflows)

## Conventions

- Documentation files use Markdown (`.md`) with GitHub-style alerts
- Internal links use relative paths
- External links include retrieval date
- Runnable examples must match current exports/signatures; record exercised checks separately. Label authoring templates and illustrative output explicitly, rather than claiming every example has passed.
