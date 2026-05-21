# Biology Textbook Scripts

## Quick Reference — 31 `*.py` files

**31** Python files: **3** Stage-2 orchestrators, **17** structural / build-quality utilities (labels, metadata, curriculum, citations, figures, labs, typography, lab computation, cover art, PDF-log checks, quality audit, current-claim audit, assessment metadata, visual-contract audit, publication-readiness audit), **9** optional pedagogy/content helpers, `atomic_io.py`, and `__init__.py`. Details: [AGENTS.md](AGENTS.md).

### Stage-2 orchestrators (called by the pipeline)

| Script | Run command | Output |
| ------ | ----------- | ------ |
| `biology_analysis.py` | `uv run python scripts/biology_analysis.py` | `output/manuscript/*.md` (134 files: front matter + preface + unit intros + chapters + labs + question banks + reference appendices; per-section Beamer skipped), plus live `config.yaml`, `references.bib`, `preamble.md`, and cover assets for the PDF renderer |
| `generate_diagrams.py` | `uv run python scripts/generate_diagrams.py` | 24 PNGs (via `mmdc`) or 24 `.mmd` fallbacks in `output/figures/mermaid/`; add `--strict-png` for publication gates so non-PNG output fails |
| `generate_figures.py` | `uv run python scripts/generate_figures.py` | 18 PNGs in `output/figures/` |

These three scripts are called automatically by `../../scripts/02_run_analysis.py --project biology_textbook` via the `analysis.scripts` allowlist in `manuscript/config.yaml`; maintenance utilities stay manual and never run as part of Stage 02.

### Manuscript maintenance and build-quality helpers

Markdown/YAML/BibTeX mutators are idempotent and support `--dry-run` unless
their CLI help says otherwise. Non-mutating quality gates such as
`check_pdf_log.py` do not need `--dry-run`.

| Script | Fixes | Target invariant |
| ------ | ----- | ---------------- |
| `insert_crossref_labels.py` | Inserts `\label{sec:unit_X_<stem>}` after every H1; rewrites legacy chapter-number prose to `\cref{}` when a canonical target exists | `test_build_invariants.test_every_chapter_has_section_label` |
| `insert_chapter_metadata.py` | Chapter-metadata badges + canonical-title Course Planning Grid | `test_build_invariants.test_every_chapter_has_metadata_badge` |
| `sync_curriculum_materials.py` | Canonical H1s/front-matter navigation, Study Blueprint blocks in chapters, evidence checklists in labs, instructor coverage notes in question banks, Appendix A curriculum map, and Appendix B instructor orchestration guide | `test_curriculum_metadata.py` / `test_toc_consistency.py` |
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
| `audit_current_claims.py` | Validates `manuscript/current_claims.yaml` and stale fast-moving claim phrases | `test_current_claims_ledger.py` |
| `audit_publication_readiness.py` | Umbrella publication gate; `--check` runs project-local audits and `--full` adds root setup/test/render/validation plus coverage | `test_script_quality.py` |
| `audit_visual_contracts.py` | Generates/checks `output/figures/visual_manifest.json` from raw figures, registered Mermaid, and inline Mermaid fences | publication-readiness gate |
| `sync_assessment_metadata.py` | Inserts/verifies item-level question metadata and lab LO/rubric alignment blocks; `--dry-run` previews drift without writing | `test_assessment_metadata.py` / `test_lab_pedagogy_alignment.py` |

### Pedagogy and content (optional; mostly idempotent)

| Script | Role |
| ------ | ---- |
| `add_mermaid_alt_text.py` | Audits Mermaid alt/caption metadata; `--check` fails on missing, duplicate, generic, or stale text |
| `bold_glossary_first_use.py` | Bold+link first glossary use per chapter to `#gl:` anchors |
| `extract_glossary_cards.py` | Exports glossary terms as study-card / review data |
| `insert_further_reading.py` | Injects `## Further Reading` from chapter cites + `references.bib` |
| `pad_short_labs.py` | Appends debrief to short lab files |
| `fill_answer_scaffolds.py` | Fills instructor scaffolds in question banks |
| `insert_answer_keys.py` | Inserts solution HTML comments for instructor PDF path |
| `refine_generated_answers.py` | Rewrites legacy/generated question answers, including `Expected reasoning:`, `Key answer:`, `Mechanistic answer:`, and stale source-boilerplate scaffolds; `--dry-run` should report `refined=0` after a clean pass |
| `enrich_embedded_textbook.py` | Adds embedded chapter frontier boxes, unit evidence threads, lab evidence upgrades, answer-key refinement, and `docs/embedded_enrichment_audit_matrix.md` |

## Prerequisites

```bash
# From this project directory (or use root workspace uv sync)
uv sync

# Mermaid CLI (required for PDF builds with inline Mermaid fences)
npm install -g @mermaid-js/mermaid-cli
mmdc --version
```

## Custom Output Paths

```bash
python3 scripts/generate_diagrams.py --strict-png --output-dir /tmp/diagrams
python3 scripts/generate_figures.py  --output-dir /tmp/figures
```

## Extending

- **Add registered Mermaid diagram:** `src/mermaid/biology_diagrams.py` → `ALL_BIOLOGY_DIAGRAMS`
- **Add inline Mermaid diagram:** write a fenced `mermaid` block followed by one `<!-- alt: ... -->` comment and one italic caption; PDF rendering converts it strictly to `output/figures/mermaid_inline/*.png` and fails if `mmdc` cannot render it. The manuscript currently has 192 inline Mermaid fences. Run `uv run python scripts/add_mermaid_alt_text.py --check` after edits.
- **Add matplotlib figure:** `src/visualization/plots.py` → `ALL_FIGURE_GENERATORS`, then run `scripts/insert_orphan_figures.py` or reference it manually in a chapter
- **Update current claims:** edit `manuscript/current_claims.yaml`, then run `uv run python scripts/audit_current_claims.py --check` and `uv run pytest tests/test_current_claims_ledger.py -v`.
- **Update assessment metadata:** run `uv run python scripts/sync_assessment_metadata.py --dry-run` to preview drift, run without flags to write updates, then run `uv run python scripts/sync_assessment_metadata.py --check` and verify `tests/test_assessment_metadata.py tests/test_lab_pedagogy_alignment.py`.
- **Update visual manifest:** run `uv run python scripts/audit_visual_contracts.py --check`; the manifest is generated under `output/figures/` and should be re-derived rather than hand-authored.
- **Add/reorder chapters:** `manuscript/config.yaml` → `units[].chapters[]`, then add a matching `ChapterMeta(…)` in `src/biology/chapter_metadata.py`, a matching `CurriculumRecord` in `src/biology/curriculum.py`, confirm the unit alignment in `src/biology/alignment.py`, list companion lab/question files without `title:` fields, and run `scripts/insert_crossref_labels.py` + `scripts/sync_curriculum_materials.py` + `scripts/insert_chapter_metadata.py`
- **Add a citation:** new `@entry{}` in `manuscript/references.bib`, then either write `\citep{key}` in a chapter or add it to `scripts/integrate_orphan_citations.py` `INSERTIONS`
- **Run an embedded enrichment pass:** `uv run python scripts/enrich_embedded_textbook.py --dry-run`, inspect the reported counts, then run without `--dry-run` if it only touches expected chapter/lab/question surfaces.

## See Also

- [`AGENTS.md`](AGENTS.md) — detailed architecture, stage documentation, invariants
- [`../manuscript/config.yaml`](../manuscript/config.yaml) — book configuration
- [`../src/biology/chapter_metadata.py`](../src/biology/chapter_metadata.py) — per-chapter difficulty / time / prereqs
- [`../src/biology/toc.py`](../src/biology/toc.py) — canonical ToC and derived lab/question/reference titles
- [`../src/biology/curriculum.py`](../src/biology/curriculum.py) — per-chapter pedagogy, model/data skill, lab/question alignment
- [`../src/biology/alignment.py`](../src/biology/alignment.py) — standards, skills, and instructor orchestration alignment
- [`../src/biology/crossref_validator.py`](../src/biology/crossref_validator.py) — label/crossref scanner
- [`../src/mermaid/`](../src/mermaid/) — diagram source definitions
- [`../src/visualization/`](../src/visualization/) — figure generator modules
