# Textbook Quality and Source-Bound Publication Gates

The quality CLI is thin; reusable checks live here. `paths.py` defines project/manuscript/ledger paths; `models.py` defines findings and surfaces; `patterns/` contains catalogs; `engine.py` collects findings; `cli.py` applies the unchanged error/advisory budgets.

## Advisory evidence

`quality_advisories.yaml` binds each accepted occurrence to exact path, line, excerpt, digest, classification, and scientific rationale. Moving or changing prose requires re-review and rebinding, not automatic blanket approval. Reviewed occurrences remain visible separately from outstanding advisories. [The triage policy](../../../docs/absolute_language_triage.md) owns the schema and its limitations.

## Publication orchestration

`publication_gate.py` schedules dependency-aware checks and invalidates stale receipts before renderer selection. Exact-source, renderer, PDF, and export custody are part of the contract. `--full` adds the native coverage/analysis/render/PDF checks; use `--workers 1` for heavyweight integration on the shared machine.

Commands, output paths, graph dependencies, and failure interpretation belong to [the pipeline guide](../../../docs/pipeline_guide.md) and [testing guide](../../../docs/testing_guide.md), rather than a duplicated mutable DAG here. Native tests include `test_publication_gate.py` and `test_publication_receipt_custody.py`. Run project-local commands under inherited admission; source counts and an old passing receipt are not current publication proof.
