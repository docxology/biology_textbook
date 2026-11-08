# `src/biology/enrichment/` — embedded enrichment engine

The project-local `scripts/enrich_embedded_textbook.py` delegates to `biology.enrichment.cli.main`; run from the repository root. Preview with `--dry-run` before applying supported generated-content changes.

The package maintains supported frontier/companion material and produces the structural enrichment matrix. Records derive from the current ToC. Change the matrix producer when its contract changes; do not hand-edit generated metrics. Character, heading, citation and solution-block counts are navigation/planning signals, not scientific correctness or human-review evidence.

Preserve authored chapter content and assessments, including procedures, prompts/keys, rubrics and coverage notes. Removed assessment-body generation and answer-key APIs must not be reinstated through compatibility exports. Missing or generic answers require prompt-specific authorship/evidence, not automated filler.

Use [pipeline guidance](../../../docs/pipeline_guide.md) for ordering and output custody, [composable authoring](../../../docs/composable_authoring.md) for shared ownership, [manuscript instructions](../../../docs/manuscript/AGENTS.md) for source contracts and [testing guidance](../../../docs/testing_guide.md) for actual behavioral checks. A preview count or unchanged source claim is not an exercised current pass.
