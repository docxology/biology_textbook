# Pipeline Guide

## Pipeline Entry Points

When **`biology_textbook`** is used as an active standalone checkout, run pytest and project-local scripts from this project directory so `pyproject.toml` applies. Template-hosted pipeline entry points such as `./run.sh --project biology_textbook` still resolve the project through the template infrastructure when available.

```bash
# From template root
./run.sh --project biology_textbook

# Or run individual stages:
uv run python scripts/00_setup_environment.py --project biology_textbook
uv run python scripts/01_run_tests.py --project biology_textbook
uv run python scripts/02_run_analysis.py --project biology_textbook
uv run python scripts/03_render_pdf.py --project biology_textbook
uv run python scripts/04_validate_output.py --project biology_textbook
uv run python scripts/05_copy_outputs.py --project biology_textbook
```

## Pipeline Stages

| # | Stage | Script | Description |
|---|-------|--------|-------------|
| 1 | Setup | `00_setup_environment.py` | Verify Python version, uv, mmdc (Mermaid CLI), LaTeX |
| 2 | Tests | `01_run_tests.py` | Project test suite (31 test files in-tree); fails if `src/` coverage < 90 % |
| 3 | Analysis | `02_run_analysis.py` | Runs `analysis.scripts` from `manuscript/config.yaml` (`generate_figures.py`, `generate_diagrams.py`, `biology_analysis.py`) → figures and the full ordered textbook are injected into `output/`, `output/analysis_report.json` written |
| 4 | PDF Render | `03_render_pdf.py` | Pandoc: Markdown → LaTeX → PDF; uses `manuscript/config.yaml`; loads `cleveref` via preamble; invokes `pandoc-crossref` if on PATH |
| 5 | Validate | `04_validate_output.py` | Checks PDF for `??` unresolved refs, word count, page count |
| 6 | Copy outputs | `05_copy_outputs.py` | Copies to root `output/biology_textbook/` |

## Project-Specific Scripts

Run `uv run python scripts/audit_textbook_quality.py --check --max-advisories 0` before a render
when a pass changes chapters, labs, question banks, glossary entries, or recent
biological claims. It catches generic answer-key prose, `Expected reasoning:`,
`Key answer:`, and `Mechanistic answer:` scaffolds, stale current-science
claims, student-facing source boilerplate, required wet-lab drift, hard-coded
rendered references, glossary and citation closure, weak figure metadata,
ledger-backed absolute-language triage in `manuscript/quality_advisories.yaml`,
and embedded-enrichment coverage.

Run `uv run python scripts/enrich_embedded_textbook.py --dry-run` before a
maximum-depth content pass. If the reported counts match the intended scope, run
without `--dry-run` to add embedded chapter frontier boxes, unit evidence
threads, lab evidence upgrades, non-generic answer-key refinements, and
`docs/embedded_enrichment_audit_matrix.md`.

Run `uv run python scripts/refine_generated_answers.py --dry-run` after any
question-bank edits. A clean manuscript reports `refined=0`; any nonzero count
means legacy/generated answer text should be rewritten before the audit gate.

From the active project root:

### Core generators (run before PDF render)

```bash
uv run python scripts/generate_figures.py        # 32 square-padded matplotlib PNGs into output/figures/
uv run python scripts/generate_diagrams.py       # 24 mermaid diagrams (PNG via mmdc or .mmd fallback)
uv run python scripts/biology_analysis.py        # inject chapters + references.bib + preamble.md into output/manuscript/
```

### Manuscript maintenance utilities

These scripts are **idempotent**; running any of them twice leaves the manuscript unchanged. They keep the invariants enforced by `tests/test_build_invariants.py` satisfied.

| Script | Purpose | Runs when |
|---|---|---|
| `insert_crossref_labels.py` | Inserts `\label{sec:unit_X_<stem>}` after every chapter H1; rewrites legacy chapter-number prose to `\cref{sec:…}` when a canonical target exists | After adding/renaming a chapter |
| `insert_chapter_metadata.py` | Renders chapter-metadata badges and the *Course Planning Grid* in `front_matter.md` from `biology.toc` + `src/biology/chapter_metadata.py` | After editing `config.yaml` titles/order or `chapter_metadata.py` |
| `sync_curriculum_materials.py` | Renders Study Blueprint/checklist blocks, generated curriculum appendices, unit-intro labels, front-matter navigation, reading paths, concept map, and preface scope table from `BookToc` | After editing `config.yaml`, curriculum/alignment records, or unit/chapter titles |
| `integrate_orphan_citations.py` | Weaves orphan BibTeX entries into chapter prose as `\citep{…}` | After adding entries to `references.bib` |
| `link_glossary.py` | Adds `{#gl:<slug>}` anchors to every glossary term; rewrites and checks glossary/index back-references as semantic `\cref{sec:…}` labels | After editing `glossary.md` |
| `link_labs_to_chapters.py` | Inserts `\cref{sec:unit_X_<stem>}` opening into every lab and question bank | After adding a lab or question file |
| `normalize_lab_computational_workflows.py` | Replaces stale notebook/CSV instructions with self-contained optional snippets backed by `src/biology` | After adding or bulk-editing lab Part 2 computation sections |
| `sync_assessment_metadata.py` | Synchronizes question-item `<!-- assess: ... -->` comments and lab LO/rubric blocks; `--dry-run` previews drift, `--check` gates | After editing learning objectives, labs, or question banks |
| `insert_orphan_figures.py` | Creates `\begin{figure}…\end{figure}` blocks for unreferenced `ALL_FIGURE_GENERATORS` entries | After registering a new figure generator |
| `normalize_typography.py` | Converts ASCII `-->` to `→` in prose (skips code, math, HTML comments, YAML front matter) | Bulk polish pass |
| `fix_greek_math_prose.py` | Replaces `$\alpha$`/`$\beta$`/… with Unicode in prose cells (works around a pandoc limitation) | Bulk polish pass |

Each helper supports `--dry-run`.

**Full script inventory** (32 `*.py` files: orchestrators, structural maintenance, build-quality helpers, and optional pedagogy utilities): [../scripts/AGENTS.md](../scripts/AGENTS.md).

### Suggested order when changing structure

After you add, rename, or reorder chapters; register new figure or diagram generators; or bulk-edit cross-references:

1. `insert_crossref_labels.py` — section `\label{sec:…}` and prose cleanup toward `\cref`.
2. `sync_curriculum_materials.py` — canonical H1s, unit-intro labels, generated appendices, front-matter navigation, suggested reading paths, concept map, and preface scope table.
3. `insert_chapter_metadata.py` — badges and Course Planning Grid (requires `ChapterMeta` and `biology.toc` in sync with `config.yaml`).
4. `link_labs_to_chapters.py` — parent `\cref` from labs and question banks.
5. `normalize_lab_computational_workflows.py` — when labs mention optional computation or were generated from older notebook templates.
6. `link_glossary.py` — glossary anchors and back-reference checks.
7. `integrate_orphan_citations.py` — only if you added unused `references.bib` keys intentionally.
8. `generate_figures.py` / `generate_diagrams.py` — when new assets are registered.
9. **Reconcile** [api_reference.md](api_reference.md) with `rg '^\s*def ' src/biology` after renaming or adding public `src/biology` entry points (see the header in that file).

Then run pytest and (from repo root) `infrastructure.validation.cli` `markdown` + `prerender` on the manuscript path. Full step-by-step: [composable_authoring.md](composable_authoring.md).

## manuscript/config.yaml — Rendering Configuration

Front matter and preface toggles live under **`front_matter`** (not `rendering`):

```yaml
front_matter:
  include_front_matter: true
  include_preface: true
  files:
    - file: front_matter.md
      title: "Front Matter"
    - file: preface.md
      title: "Preface"

rendering:
  auto_number_chapters: true
  auto_number_figures: true
  auto_number_equations: true
  auto_number_tables: true
```

The PDF renderer reads `manuscript/config.yaml` to discover chapter file paths and ordering. It then:
1. Concatenates chapters in order
2. Resolves cross-references (`\cref{sec:…}`, `\cref{fig:…}`, `\cref{eq:…}` via `cleveref`; natbib `\citep{…}` / `\citet{…}` via bibtex)
3. Inserts auto-generated chapter and figure numbers
4. Passes to pandoc/LaTeX as a single document

Lab and question-bank entries under `appendices.labs/questions` store only
`file:` names. Their display titles are derived from the parent chapter by
`biology.toc` and synchronized into the markdown H1s by
`scripts/sync_curriculum_materials.py`.

Book-style PDF opening metadata lives under `book` in
`manuscript/config.yaml`. The renderer uses `book.title`, `book.subtitle`,
`authors[]`, and `book.cover.image` to create page 1 as the cover, page 2 as
publishing information, and page 3 as the detailed table of contents. Keep
cover art text-free; title and author typography are injected by LaTeX.

## Adding Chapters Without Breaking Numbering

Full checklist (config → `ChapterMeta` → maintenance scripts → pytest / prerender): [composable_authoring.md](composable_authoring.md).

Because numbers are assigned at render time:
- Adding a new chapter anywhere in the list renumbers only the subsequent chapters
- All cross-references use semantic labels, not hardcoded numbers
- Visible unit, appendix, section, chapter, and figure references in student-facing manuscript prose use `\cref{...}` / `\nameref{...}` or generated marker blocks owned by `sync_curriculum_materials.py` / `insert_chapter_metadata.py`
- Use `\label{fig:unit_X_<descriptor>}` and `\cref{fig:...}` — never hand-typed "Figure 4.3" in prose
- When a new chapter is added, run `scripts/insert_crossref_labels.py` so the H1 gets a `\label{sec:unit_X_<stem>}`, then use `\cref{sec:...}` for all prose references
- Update `src/biology/chapter_metadata.py` with a `ChapterMeta(...)` record, then rerun `scripts/sync_curriculum_materials.py` and `scripts/insert_chapter_metadata.py` to refresh canonical H1s, front-matter navigation, badges, and the Course Planning Grid
- Do not add manual heading numbers inside Markdown headings; `scripts/sync_curriculum_materials.py` normalizes ToC-safe heading titles and marks front matter, unit intros, labs, question banks, and reference appendices as unnumbered.

## Invariant tests (Stage 2 gate-keepers)

Fourteen **invariant/quality** `test_*.py` modules (plus six **domain** `test_*.py` modules exercising `src/`) — see [testing_guide.md](testing_guide.md#test-organisation). They fail the pipeline if manuscript, lab, question, render, or script quality regresses:

- `test_build_invariants.py` — every chapter labelled, every lab/question `\cref`-linked, every figure generator referenced
- `test_bibliography_closure.py` — `{cited}` == `{defined}` in `references.bib`
- `test_chapter_metadata.py` — `ChapterMeta` records cover every `config.yaml` chapter with valid difficulty and prerequisites
- `test_toc_consistency.py` — renderable H1s, unit-intro labels, front-matter/preface generated blocks, appendices, and Course Planning Grid match `biology.toc`
- `test_accessibility.py` — LaTeX figures and inline Mermaid meet alt/caption rules ([manuscript/AGENTS.md](../manuscript/AGENTS.md))
- `test_crossref_validator.py`, `test_crossref_validator_edges.py`, `test_crossref_validator_internals.py` — pandoc-crossref / cleveref resolution
- `test_lab_integrity.py` — optional lab computation snippets resolve project modules and do not require hidden notebooks, CSVs, pandas, or display-only plotting
- `test_pdf_log_quality.py` — PDF-log checker rejects undefined references and severe overfull boxes
- `test_pdf_opening_and_mermaid.py` — cover/opening metadata and inline Mermaid rendering stay intact
- `test_question_answer_refinement.py` — answer-refinement heuristics are idempotent and preserve hand-written solutions
- `test_script_quality.py` — scripts parse as Python and avoid hard-coded local paths or retired helper clones

## Known gotchas

| Gotcha | Symptom | Fix |
| ------ | ------- | --- |
| `\bibliographystyle{plainnat}` declared in `preamble.md` | bibtex aborts: "Illegal, another `\bibstyle` command" | **Remove** the line. Pandoc auto-injects it; a double declaration is fatal. |
| `\includegraphics{output/figures/foo.png}` (absolute-style path) | xelatex: `! LaTeX Error: File '...' not found.` | Use `../figures/foo.png` — paths are relative to `output/manuscript/`, not the source `manuscript/` tree. |
| Bare `$\alpha$` / `$\beta$` etc. in pipe-table cells | Pandoc emits `\(\alpha)` without closing `\)`; xelatex aborts on the table | Run `scripts/fix_greek_math_prose.py` to replace with Unicode in prose contexts. |
| Manual equation numbering on a `$$…$$` line | xelatex errors or numbering drift | Use a labelled `equation` or `align` environment for numbered display equations; use plain `$$…$$` only for unnumbered display math. See [manuscript_guide.md#equations](manuscript_guide.md#equations). |
| Hand-typed "Figure 4.2" / "Chapter 11" / "Equation 5.7" in chapter prose | Number drifts when chapters are reordered | Use `\cref{fig:unit_X_<descriptor>}`, `\cref{sec:unit_X_<stem>}`, or `\cref{eq:unit_X_<descriptor>}`; `cleveref` injects the right number and the cross-reference validator rejects hard-coded rendered numbers. |
| `mmdc` missing on CI | PDF rendering fails before Pandoc when inline Mermaid fences are present | Install Mermaid CLI on the build host. Registry diagrams can still be regenerated with `scripts/generate_diagrams.py`; inline diagrams render strictly during PDF preprocessing. |
| Mermaid label with unquoted `(`, `)`, `:` | mmdc render fails with parse error | Wrap label: `A["Glucose (C6H12O6)"]`. |
| Lab Part 2 references a hidden notebook or CSV | `test_lab_integrity.py` fails on stale phrases such as `.ipynb`, `pd.read_csv`, or "provided Jupyter Notebook" | Run `scripts/normalize_lab_computational_workflows.py`; keep optional computation snippets self-contained and backed by `biology.*` imports. |
