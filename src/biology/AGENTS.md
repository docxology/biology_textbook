# `src/biology/` — AGENTS.md

Keep scientific logic here, not in repository-root `scripts/`. Public functions should be typed and tested with real numerical inputs; stochastic functions expose explicit reproducible RNG controls. Prefer frozen result dataclasses where immutability is appropriate.

Domain packages include `foundations/` as well as the traditional biology domains. `curriculum/` and `visual_contracts/` are packages. Metadata, ToC, assessment and claim modules participate in the [manuscript source contract](../../docs/manuscript/AGENTS.md); paths explicitly prefixed `src/`, `scripts/` or `docs/` in this paragraph are repository-root paths.

`current_claims.py` validates repository-root `docs/manuscript/current_claims.yaml`. `assessment.py` parses authored item and lab alignment metadata. Curriculum/enrichment engines may maintain their designated generated blocks, not authored assessment bodies, keys, rubrics or coverage notes.

When changing interfaces, reconcile actual exports/callers and the curated [API reference](../../docs/api_reference.md). Use [architecture](../../docs/architecture.md) for boundaries, [composable authoring](../../docs/composable_authoring.md) for ordered workflows, [pipeline](../../docs/pipeline_guide.md) for commands and [testing](../../docs/testing_guide.md) for verification scope. These relative links resolve from this directory; do not duplicate mutable file/symbol inventories here.
