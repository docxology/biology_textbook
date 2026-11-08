# Biology Textbook Scripts — AGENTS.md

## Role and launch location

Run thin project-local entry points from the standalone repository root. Scientific and maintenance logic belongs in `src/`; scripts coordinate arguments, paths and I/O. An admitted template is a read-only rendering library, never the launch directory or output destination.

## Authoritative contracts

- [Pipeline guide](../docs/pipeline_guide.md): locked prerequisites, entry points, maintenance ordering, output custody and source-bound publication receipts.
- [Composable authoring](../docs/composable_authoring.md): cross-file workflows and stable identifiers.
- [Visualization guide](../docs/visualization_guide.md): project-output review recipe, strict PNG requirements and accessibility review limits. Do not use arbitrary OS temporary directories for inline rendering.
- [Testing guide](../docs/testing_guide.md): actual test nodes, branch-enabled coverage and isolation limits.
- [Manuscript contract](../docs/manuscript/AGENTS.md): config-owned H1s, reference types and authored assessment ownership.

## Ownership boundaries

Figure implementations live in `src/visualization/plots_<domain>.py`; `plots.py` owns `ALL_FIGURE_GENERATORS` and `__init__.py` is the public facade. Registered Mermaid specifications/factories and inline fences are distinct inputs; publication requires decoded PNGs, not fallback `.mmd` files. Derive counts from current sources/manifests, not this instruction file.

Curriculum synchronization owns canonical headings, navigation, blueprints and generated appendices. It must not regenerate authored lab procedures, question prompts/keys, rubrics or coverage notes. Unsupported automatic answer repair refuses without writing. Assessment metadata validates curated semantic mappings, not positional replacements.

Use only CLI flags actually implemented by the selected entry point; `sync_curriculum_materials.py` supports `--dry-run`, not `--check`. Do not assume all helpers expose identical preview/check flags or that an idempotence claim is a fresh result. Preserve authored content and inspect the matching source ownership before applying a maintenance helper.

Source gates, native rendering, physical-size visual inspection and remote publication are separate evidence. Instructions and generated manifests do not establish a current pass.
