# `src/biology/curriculum_sync/` — curriculum synchronization

The project-local `scripts/sync_curriculum_materials.py` delegates to `biology.curriculum_sync.cli.main`. Run it from the repository root; it supports preview with `--dry-run` and apply without that flag, not `--check`.

The engine uses `biology.toc` and the `biology.curriculum` package to maintain canonical H1s/identifiers, chapter blueprints, generated curriculum/reference appendices and navigation. Authored lab procedures, question prompts/keys, rubrics and coverage notes are outside its write ownership. Former assessment-body writers and ownership markers are retired; do not restore them.

Preserve authored assessments and validate their curated semantic mappings using the separately owned assessment metadata gate. Repeated-run preservation requires actual content/mtime/inode evidence, not a reported success counter.

Use the repository-root [pipeline guide](../../../docs/pipeline_guide.md), [composable authoring](../../../docs/composable_authoring.md), [manuscript contract](../../../docs/manuscript/AGENTS.md) and [testing guide](../../../docs/testing_guide.md) rather than copied inventories or template-root recipes.
