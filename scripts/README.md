# Biology Textbook Scripts

## Project-local entry points

The tables below describe orchestrators and maintenance utilities; use current CLI help and the source registries rather than historical file counts. Details: [AGENTS.md](AGENTS.md).

### Stage-2 orchestrators (called by the pipeline)

| Script | Run command | Output |
| ------ | ----------- | ------ |
| `biology_analysis.py` | `uv run python scripts/biology_analysis.py` | Complete configured manuscript staging plus live configuration, bibliography, preamble and cover assets under `output/manuscript/` |
| `generate_diagrams.py` | `uv run python scripts/generate_diagrams.py --strict-png` | Registered decoded PNGs under `output/figures/mermaid/`; `.mmd` fallback is not publication output |
| `generate_figures.py` | `uv run python scripts/generate_figures.py` | Registered PNGs in `output/figures/`, following the per-figure aspect policy |

Use these project-local entry points in this standalone checkout. A template-hosted integration may consume the configured analysis allowlist, but template-root recipes are not this project's launch workflow and must not write another checkout.

### Manuscript maintenance and build-quality helpers

Markdown/YAML/BibTeX mutators are idempotent and support `--dry-run` unless
their CLI help says otherwise. Non-mutating quality gates such as
`check_pdf_log.py` do not need `--dry-run`.

| Script | Fixes | Target invariant |
| ------ | ----- | ---------------- |
| `insert_crossref_labels.py` | Inserts `\label{sec:unit_X_<stem>}` after every H1; rewrites legacy chapter-number prose to `\cref{}` when a canonical target exists | `test_build_invariants.test_every_chapter_has_section_label` |
| `insert_chapter_metadata.py` | Chapter-metadata badges + canonical-title Course Planning Grid | `test_build_invariants.test_every_chapter_has_metadata_badge` |
| `sync_curriculum_materials.py` | Canonical headings, navigation, chapter Study Blueprints and generated curriculum/instructor appendices; preserves authored lab/question bodies | `test_curriculum_metadata.py` / `test_toc_consistency.py` |
| `integrate_orphan_citations.py` | Weaves unused `references.bib` entries into chapter prose | `test_bibliography_closure.test_no_orphan_bibentries` |
| `link_glossary.py` | `{#gl:<slug>}` anchors + semantic `\cref{sec:…}` glossary/index back-references; `--check` fails on dangling glossary links, duplicate anchors, or legacy chapter-number back-references | `test_build_invariants.test_glossary_and_index_use_semantic_chapter_links` |
| `link_labs_to_chapters.py` | `\cref{sec:…}` opening in every lab & question bank | `test_build_invariants.test_every_{lab,question}_links_to_parent_chapter` |
| `normalize_lab_computational_workflows.py` | Replaces hidden-notebook/data-file instructions with self-contained `src/biology` snippets | `test_lab_integrity.py` |
| `insert_orphan_figures.py` | Adds `\begin{figure}…\end{figure}` for unused `ALL_FIGURE_GENERATORS` entries | `test_build_invariants.test_every_registered_figure_is_referenced` |
| `normalize_typography.py` | ASCII `-->` → `→` in prose (skips code, math, HTML comments, YAML front matter, `preamble.md`) | cosmetic |
| `fix_greek_math_prose.py` | `$\greek$` → Unicode in prose (avoids a pandoc quirk in pipe-table cells) | PDF-build safety |
| `generate_cover_art.py` | Regenerates the reusable, text-free `book.cover.image` montage asset | `test_pdf_opening_and_mermaid.py` |
| `check_pdf_log.py` | Fails on undefined LaTeX references and severe overfull boxes above the configured point threshold | `test_pdf_log_quality.py` |
| `audit_textbook_quality.py` | Reports generic answer keys, stale/current claims, student-facing authoring boilerplate, wet-lab drift, hard-coded references, glossary/citation closure, embedded-enrichment coverage, and ledger-backed absolute-language triage; `--check --max-advisories 0` is the blocking gate | `test_textbook_quality_audit.py` |
| `audit_current_claims.py` | Validates `docs/manuscript/current_claims.yaml` and stale fast-moving claim phrases | `test_current_claims_ledger.py` |
| `audit_publication_readiness.py` | Local source/static/visual gate; `--full` adds coverage, live analysis, fresh native rendering and strict PDF-log checks | `test_publication_gate.py` / `test_publication_receipt_custody.py` |
| `audit_visual_contracts.py` | Generates/checks a visual manifest and review matrix from raw figures, registered Mermaid, inline Mermaid fences, dimensions, alt text, captions, action taken, exceptions, and square-ish aspect policy; use `--figures-root output/review/figures --output output/review/visual_manifest.json --render-inline --check` for repository-local disposable review assets | publication-readiness gate |
| `annotate_table_captions.py` | Inserts `Table: … {#tbl:…}` captions before chapter and lab pipe tables missing them | `test_table_captions.py` |
| `polish_table_captions.py` | Polishes existing pandoc table captions across the manuscript (thin CLI for `biology.crossref.table_captions`) | `test_table_captions.py` |
| `normalize_american_english.py` | Rewrites British spellings to American English in manuscript and docs | `test_american_english.py` |
| `repair_split_chapter_shells.py` | Repairs pedagogy shells on chapters created by the Phase 5 mega-chapter split (thin CLI for `biology.maintenance.chapter_shells`) | `test_chapter_shells.py` |
| `sync_assessment_metadata.py` | Nonwriting validation of authored semantic question mappings and lab LO/rubric records; missing records require author review | `test_assessment_metadata.py` / `test_lab_pedagogy_alignment.py` |

### Pedagogy and content (optional; mostly idempotent)

| Script | Role |
| ------ | ---- |
| `add_mermaid_alt_text.py` | Audits canonical Mermaid alt/caption structure and generic metadata; preserves meaningful authored alt text and does not truncate caption-derived fallback descriptions. `--check` does not establish semantic freshness. |
| `bold_glossary_first_use.py` | Bold+link first prose use to `#gl:` anchors; mixed-case alphabetic symbols match exact case (`pH` is not `Ph`), while ordinary words retain case-insensitive plural matching |
| `extract_glossary_cards.py` | Exports glossary terms as study-card / review data |
| `insert_further_reading.py` | Injects `## Further Reading and Source Notes: <Chapter Title>` from configured chapter cites + `references.bib` |
| `pad_short_labs.py` | Appends debrief to short lab files |
| `fill_answer_scaffolds.py` | Unsupported automatic answer filling refuses without writing; author evidence-bound answers directly |
| `insert_answer_keys.py` | Unsupported automatic key insertion refuses without writing; retain the canonical SOLUTION protocol |
| `refine_generated_answers.py` | Validates and preserves authored answers; `--dry-run` reports required author actions without manufacturing keys |
| `enrich_embedded_textbook.py` | Maintains supported frontier/companion material while preserving authored content; inspect proposed changes, not just counts |

## Prerequisites

```bash
# From this project directory, with inherited project/environment overrides cleared:
UV_PROJECT_ENVIRONMENT="$PWD/.venv" uv sync --frozen --extra dev
npm --prefix "$PWD" ci --ignore-scripts
export PATH="$PWD/node_modules/.bin:$PATH"
mmdc --version  # locked project CLI, not a global install
```

## Custom Output Paths

```bash
uv run python scripts/generate_diagrams.py --strict-png --output-dir output/review/diagrams
uv run python scripts/generate_figures.py --output-dir output/review/figures
```

## Extending

- **Add registered Mermaid diagram:** `src/mermaid/biology_diagrams.py` → `ALL_BIOLOGY_DIAGRAMS`
- **Add inline Mermaid diagram:** write a fenced `mermaid` block followed by one descriptive alt comment and one italic caption. Rendering requires a fresh PNG under this project's output tree; run `uv run python scripts/add_mermaid_alt_text.py --check` after edits.
- **Add matplotlib figure:** `src/visualization/plots.py` → `ALL_FIGURE_GENERATORS`, then run `scripts/insert_orphan_figures.py` or reference it manually in a chapter
- **Update current claims:** edit `docs/manuscript/current_claims.yaml`, then run `uv run python scripts/audit_current_claims.py --check` and `uv run python -m pytest tests/test_current_claims_ledger.py -v`.
- **Update assessment metadata:** review the actual prompt/answer/outcome and edit its semantic record directly; use `sync_assessment_metadata.py --dry-run` and `--check` to validate, not generate, that content.
- **Update visual manifest:** use `uv run python scripts/audit_visual_contracts.py --figures-root output/review/figures --output output/review/visual_manifest.json --render-inline --check`; re-derive the manifest and matrix rather than hand-authoring them.
- **Add/reorder chapters:** update `docs/manuscript/config.yaml`, `src/biology/chapter_metadata.py`, the `src/biology/curriculum/` records and `src/biology/alignment.py`; list companion filenames without duplicate titles. [Composable authoring](../docs/composable_authoring.md) owns the complete sequence.
- **Add a citation:** author a matched `\citep{key}` against `docs/manuscript/references.bib`; curated orphan insertions belong to `src/biology/pipeline/orphan_citations.yaml`, not a duplicated script constant.
- **Run an embedded enrichment pass:** `uv run python scripts/enrich_embedded_textbook.py --dry-run`, inspect the reported counts, then run without `--dry-run` if it only touches expected chapter/lab/question surfaces.

## See Also

- [`AGENTS.md`](AGENTS.md) — detailed architecture, stage documentation, invariants
- [`../docs/manuscript/config.yaml`](../docs/manuscript/config.yaml) — book configuration
- [`../src/biology/chapter_metadata.py`](../src/biology/chapter_metadata.py) — per-chapter difficulty / time / prereqs
- [`../src/biology/toc.py`](../src/biology/toc.py) — canonical ToC and derived lab/question/reference titles
- [`../src/biology/curriculum/`](../src/biology/curriculum/) — per-chapter pedagogy, model/data skill, lab/question alignment (`CurriculumRecord` in `models.py`)
- [`../src/biology/alignment.py`](../src/biology/alignment.py) — standards, skills, and instructor orchestration alignment
- [`../src/biology/crossref_validator.py`](../src/biology/crossref_validator.py) — label/crossref scanner
- [`../src/mermaid/`](../src/mermaid/) — diagram source definitions
- [`../src/visualization/`](../src/visualization/) — figure generator modules
