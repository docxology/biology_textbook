# Biology Textbook Scripts — AGENTS.md

## Script Roles

This directory contains **36** Python files. **Three** are Stage-2 **orchestrators** called by the root pipeline; **seventeen** are idempotent **structural / build-quality** utilities (labels, metadata, curriculum, bib, labs, figures, typography, lab computation, cover art, PDF-log checks, manuscript-quality audits, current-claim audits, assessment metadata, visual-contract audit, publication-readiness audit) that keep invariants in `tests/test_build_invariants.py` and related tests satisfied; **nine** are **optional pedagogy / content** helpers (glossary linking, embedded enrichment, question-bank answers, labs, further reading, Mermaid alt text, glossary-card export) used during content iteration. `_bootstrap.py` centralizes `sys.path` setup; `atomic_io.py` re-exports `src/textbook_io.write_text_atomic`; `__init__.py` marks the package.

All scientific computation resides in `../src/`; orchestrators only coordinate I/O, path resolution, and module invocation. Utilities parse and rewrite markdown/bib/yaml source. The root Stage 02 runner reads `analysis.scripts` in `../manuscript/config.yaml` and runs only the three build-producing scripts below; maintenance utilities stay manual.

## Scripts — Stage-2 orchestrators

| Script | Purpose |
| ------ | ------- |
| `biology_analysis.py` | Reads `manuscript/config.yaml`, runs all biology src modules, collects the full ordered textbook into `output/manuscript/` (front matter, unit intros, chapters, labs, question banks, reference appendices), marks injected files to skip per-section Beamer slide derivation, and copies live `config.yaml`, `references.bib`, `preamble.md`, and cover assets alongside so the PDF renderer can find book metadata and images |
| `generate_diagrams.py` | Renders 24 diagrams in `ALL_BIOLOGY_DIAGRAMS` to PNG via `mmdc` when available; fallback `.mmd` → `output/figures/mermaid/` |
| `generate_figures.py` | Generates 42 square-padded matplotlib figures via `src/visualization/ALL_FIGURE_GENERATORS` (`cvd.py` palette when `config.yaml` has `color_blindness_safe: true`); logs policy; output → `output/figures/` |

## Scripts — Manuscript maintenance and build-quality utilities

Markdown/YAML/BibTeX mutators support `--dry-run` unless their CLI help says otherwise.
They are idempotent — running any of them twice leaves the manuscript unchanged.
Non-mutating quality gates such as `check_pdf_log.py` do not need `--dry-run`.
Each exists because a specific invariant is asserted by the test suite; running
the matching script is the canonical fix.

| Script | Guards | What it does |
| ------ | ------ | ------------ |
| `insert_crossref_labels.py` | `test_build_invariants.test_every_chapter_has_section_label` + `test_every_lab_and_question_has_section_label` | Inserts `\label{sec:unit_X_<stem>}` after every H1 and rewrites legacy chapter-number prose to `\cref{sec:…}` when a canonical chapter target exists |
| `insert_chapter_metadata.py` | `test_build_invariants.test_every_chapter_has_metadata_badge` + `test_course_planning_grid_populated` | Renders per-chapter difficulty / time / prereq badge from `src/biology/chapter_metadata.py` and refreshes the Course Planning Grid from `biology.toc` in `manuscript/front_matter.md` |
| `sync_curriculum_materials.py` | `test_curriculum_metadata.py` + `test_toc_consistency.py` | Renders canonical H1s/front-matter navigation, per-chapter Study Blueprint blocks, lab Evidence and Reproducibility checklists, question-bank Instructor Use notes, Appendix A's curriculum map, and Appendix B's instructor guide from `biology.toc`, `src/biology/curriculum.py`, and `src/biology/alignment.py` |
| `integrate_orphan_citations.py` | `test_bibliography_closure.test_no_orphan_bibentries` | Hand-curated map of BibTeX citekey → target chapter + anchor phrase; injects `\citep{key}` after the first safe occurrence (skips headings, code, LaTeX macro arguments) |
| `link_glossary.py` | `test_build_invariants.test_glossary_and_index_use_semantic_chapter_links` + `--check` | Maintains `{#gl:<slug>}` anchors, rewrites legacy glossary/index chapter back-references to canonical `\cref{sec:…}` labels, and fails on unresolved glossary links or duplicate anchors |
| `link_labs_to_chapters.py` | `test_build_invariants.test_every_{lab,question}_links_to_parent_chapter` | Inserts a one-line `\cref{sec:unit_X_<stem>}` opening into every lab and question bank file |
| `normalize_lab_computational_workflows.py` | `test_lab_integrity.py` | Replaces stale hidden-notebook/data-file instructions with self-contained optional Python snippets that import tested `biology.*` modules |
| `insert_orphan_figures.py` | `test_build_invariants.test_every_registered_figure_is_referenced` | Creates `\begin{figure}\includegraphics\caption\label\end{figure}` blocks for `ALL_FIGURE_GENERATORS` entries not yet used in any chapter |
| `normalize_typography.py` | (cosmetic; HTML-comment-aware) | Converts ASCII `-->` to `→` in prose; skips fenced code, `$…$` and `$$…$$` math, raw-LaTeX environments, HTML comments, YAML front matter, and `preamble.md` |
| `fix_greek_math_prose.py` | (works around pandoc quirk) | Replaces `$\greek$` in prose (outside code / math / LaTeX environments) with the Unicode code point — prevents pandoc emitting `\(\greek)` without a closing `\)` inside pipe-table cells |
| `generate_cover_art.py` | `test_pdf_opening_and_mermaid.py::test_configured_cover_asset_exists` | Regenerates the text-free cover montage asset referenced by `book.cover.image` in `manuscript/config.yaml` |
| `check_pdf_log.py` | `test_pdf_log_quality.py` | Fails on undefined LaTeX references and severe overfull boxes above the configured point threshold |
| `audit_textbook_quality.py` | `test_textbook_quality_audit.py` | Umbrella quality gate for generic answers, current-claim drift, wet-lab defaults, hard-coded rendered references, glossary/citation closure, embedded-enrichment coverage, and `manuscript/quality_advisories.yaml` triage |
| `audit_current_claims.py` | `test_current_claims_ledger.py` | Validates `manuscript/current_claims.yaml` source tiers, checked dates, refresh triggers, anchors, and stale-phrase locks |
| `audit_visual_contracts.py` | publication-readiness gate | Generates/checks a visual manifest and review matrix from raw figure blocks, registered Mermaid factories, inline Mermaid fences, asset dimensions, alt text, captions, generator names, action taken, exceptions, and square-ish aspect policy |
| `audit_publication_readiness.py` | aggregate gate | Runs quality, current-claim, assessment, Mermaid alt, strict figure/diagram, lint, mypy, WIP resolver, artifact-count, and tracked-artifact checks using temporary visual artifacts; `--full` adds root setup/test/render/validate; `--workers N` parallelizes independent gate steps (default `1`) |
| `sync_assessment_metadata.py` | `test_assessment_metadata.py` + `test_lab_pedagogy_alignment.py` | Inserts/verifies question-item metadata and lab outcome/LO/rubric alignment blocks from `biology.assessment` / `biology.toc` surfaces; `--dry-run` previews drift without writing |

## Pedagogy and content utilities (optional)

Idempotent unless noted. Support `--dry-run` where implemented in each script.

| Script | Role | Related tests / notes |
| ------ | ---- | --------------------- |
| `add_mermaid_alt_text.py` | Audits inline Mermaid `<!-- alt: … -->` comments and italic captions; `--check` fails on drift and the tool refuses to insert generic filler | Supports [../tests/test_accessibility.py](../tests/test_accessibility.py) / [../manuscript/AGENTS.md](../manuscript/AGENTS.md) |
| `bold_glossary_first_use.py` | Bold+link first glossary-term occurrence per chapter to `#gl:` anchors | Works with `link_glossary.py` |
| `extract_glossary_cards.py` | Exports glossary entries into card-style study/review data | Content utility; not a structural gate |
| `insert_further_reading.py` | Adds `## Further Reading and Source Notes: <Chapter Title>` from configured chapter `\cite` keys + `references.bib` | Content quality; not a structural gate |
| `pad_short_labs.py` | Appends debrief block to labs under 100 lines | Labs only |
| `fill_answer_scaffolds.py` | Fills `INSTRUCTOR SCAFFOLD` blocks in question banks with generated stubs | Questions/appendices |
| `insert_answer_keys.py` | Inserts HTML-comment solution blocks for instructor edition | Works with `biology_analysis.py` `export.include_solutions` |
| `refine_generated_answers.py` | Replaces v1 auto-answers in question banks with improved heuristics; leaves hand-written solutions untouched | Follow-up to `fill_answer_scaffolds.py` |
| `enrich_embedded_textbook.py` | Inserts embedded frontier/evidence sections, current-evidence Mermaid maps, paper-based lab evidence upgrades, refined answer keys, and `docs/embedded_enrichment_audit_matrix.md` | Run with `--dry-run` before applying; preserves the 44/44/44 structure |

## Architecture: Thin Orchestrator Pattern

**All business logic lives in `../src/`** — never in these script files.

```text
scripts/biology_analysis.py          ← orchestrator (config reading, file I/O)
    └── reads:  manuscript/config.yaml
    └── calls:  src/biology/*        (scientific modules)
    └── copies: chapter .md files → output/manuscript/

scripts/generate_diagrams.py         ← orchestrator (path setup, CLI args)
    └── calls:  src/mermaid/biology_diagrams.py  (ALL_BIOLOGY_DIAGRAMS, MermaidRenderer)
    └── writes: output/figures/mermaid/*.png

scripts/generate_figures.py          ← orchestrator (path setup, error capture)
    └── calls:  src/visualization/   (ALL_FIGURE_GENERATORS)
    └── writes: output/figures/*.png
```

## Mermaid Diagram Pipeline

Registered Mermaid diagrams are authored in `src/mermaid/biology_diagrams.py`.
Each registered diagram is a Python function returning a `MermaidDiagram(name, definition)` object.
`generate_diagrams.py` calls `MermaidRenderer.render_all(ALL_BIOLOGY_DIAGRAMS)` which:

1. Writes each `.mmd` source to a temp directory
2. Invokes `mmdc` (Mermaid CLI) with background `--backgroundColor white` and theme `default`
3. Outputs `.png` files to the configured output directory
4. Returns a list of output `Path` objects for presence-checking

Inline Mermaid fences may also appear directly in manuscript Markdown. They must
carry exactly one nearby `<!-- alt: ... -->` comment and one italic caption. During combined PDF preprocessing,
the infrastructure renderer writes deterministic `.mmd` + `.png` files under
`output/figures/mermaid_inline/` and replaces the fence with a Pandoc image
reference. PDF rendering fails clearly if `mmdc` is unavailable or a diagram
cannot render; inline diagrams are never silently stripped. The manuscript currently has 193 inline Mermaid fences.

**Adding a new registered diagram:**

1. Add a function to `src/mermaid/biology_diagrams.py` returning a `MermaidDiagram`
2. Add it to `ALL_BIOLOGY_DIAGRAMS` list at the bottom of that file
3. Re-run `uv run python scripts/generate_diagrams.py --strict-png` for publication checks — no changes to orchestrator needed

## Figure Pipeline

All matplotlib figures are authored in `src/visualization/` submodules.
Each generator function has the signature `fn(output_dir: Path) -> Path` and receives
the output directory from `generate_figures.py`.
`ALL_FIGURE_GENERATORS` (from `src/visualization/plots.py`) is the registry.
This registry, together with `ALL_BIOLOGY_DIAGRAMS`, is the visual manifest: registered entries must be generated, referenced in the manuscript, and covered by accessibility text. `audit_visual_contracts.py` re-derives the concrete `output/figures/visual_manifest.json`; do not hand-edit that generated manifest.

**Adding a new figure:**

1. Add a generator in `src/visualization/plots.py` (or refactor into a submodule later)
2. Register `(name, callable)` in `ALL_FIGURE_GENERATORS`
3. Re-run `uv run python scripts/generate_figures.py`

## Config Integration

`biology_analysis.py` reads `manuscript/config.yaml` for:

- `front_matter.include_front_matter` + `front_matter.files` — prepends front-matter source after the generated book opening and table of contents (preface appears only when listed there and allowed by `front_matter.include_preface`)
- `units[].chapters[].file` — ordered chapter list (`enabled: false` skips an entry)
- `appendices` — labs, question banks, and reference appendices (lab/question display titles are derived by `biology.toc`; keep only `file:` entries there)

**Typography and layout keys** (`layout.*`, `typography.*`) are consumed by the PDF pipeline for this project.

## Running Individually

```bash
cd /path/to/biology_textbook

# Stage-2 orchestrators
uv run python scripts/generate_diagrams.py                    # 24 mermaid diagrams
uv run python scripts/generate_diagrams.py --output-dir /custom/path
uv run python scripts/generate_figures.py                     # 42 square-padded matplotlib figures
uv run python scripts/generate_figures.py --output-dir /custom/path
uv run python scripts/biology_analysis.py                     # collect chapters + live config/references/preamble/cover assets
uv run python scripts/generate_cover_art.py                    # refresh text-free cover montage asset
uv run python scripts/check_pdf_log.py output/pdf/_xelatex_stdout.log --max-overfull-pt 50
uv run python scripts/audit_textbook_quality.py --check --max-advisories 0 # manuscript quality umbrella gate
uv run python scripts/audit_current_claims.py --check          # current-claim ledger gate
uv run python scripts/sync_assessment_metadata.py --dry-run    # preview assessment metadata drift
uv run python scripts/sync_assessment_metadata.py --check      # assessment metadata gate
uv run python scripts/audit_visual_contracts.py --figures-root <tmp>/figures --output <tmp>/visual_manifest.json --render-inline --check # visual manifest gate
uv run python scripts/audit_publication_readiness.py --check --workers 4   # aggregate local gate; parallel waves when N>1

# Manuscript maintenance (each supports --dry-run)
uv run python scripts/insert_crossref_labels.py
uv run python scripts/insert_chapter_metadata.py
uv run python scripts/sync_curriculum_materials.py
uv run python scripts/integrate_orphan_citations.py
uv run python scripts/link_glossary.py
uv run python scripts/link_labs_to_chapters.py
uv run python scripts/normalize_lab_computational_workflows.py
uv run python scripts/insert_orphan_figures.py
uv run python scripts/normalize_typography.py
uv run python scripts/fix_greek_math_prose.py
uv run python scripts/enrich_embedded_textbook.py --dry-run
uv run python scripts/refine_generated_answers.py --dry-run
uv run python scripts/insert_answer_keys.py --dry-run
uv run python scripts/fill_answer_scaffolds.py --dry-run
uv run python scripts/bold_glossary_first_use.py --dry-run
uv run python scripts/extract_glossary_cards.py --dry-run
uv run python scripts/insert_further_reading.py --dry-run
uv run python scripts/pad_short_labs.py --dry-run
uv run python scripts/add_mermaid_alt_text.py --dry-run
```

## No-Mocks Policy

All scripts invoke real src modules. No mocking of any kind (no `unittest.mock`,
no `MagicMock`, no patched file I/O). Tests live in `../tests/`.

## See Also

- `../src/mermaid/biology_diagrams.py` — diagram definitions
- `../src/visualization/` — figure generators
- `../manuscript/config.yaml` — all layout, typography, and chapter configuration
- `../../scripts/02_run_analysis.py` — generic pipeline orchestrator that calls these scripts
- `../../scripts/03_render_pdf.py` — PDF renderer that reads layout/typography config
