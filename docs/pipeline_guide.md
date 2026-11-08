# Pipeline Guide

## Pipeline Entry Points

Run from the standalone project directory. Install with `uv sync --frozen --extra dev` and `npm ci` (Node >=22.13.0), then add `$PWD/node_modules/.bin` to PATH. Mermaid CLI is pinned to 12.2.0. Pandoc, XeLaTeX and a compatible browser are external render prerequisites.

Select a compatible template as a **read-only library** with `BIOLOGY_TEXTBOOK_TEMPLATE_ROOT=/path/to/template`, or use a genuine enclosing template. Invalid explicit selection fails; neighboring repositories never participate. Local src/scripts win imports. Do not run template-root recipes or WIP resolvers.

```bash
uv run --frozen --extra dev python scripts/audit_publication_readiness.py --check
uv run --frozen --extra dev python scripts/audit_publication_readiness.py --check --full
```

## Pipeline Stages

| Stage | Project-local entry | Contract |
| --- | --- | --- |
| Source audits | `audit_textbook_quality.py --check --max-advisories 0`, `audit_current_claims.py --check`, `sync_assessment_metadata.py --check`, `add_mermaid_alt_text.py --check` | Validate manuscript, claim and curated assessment surfaces |
| Graphics | `generate_figures.py`, `generate_diagrams.py --strict-png` | Produce real decoded PNGs; no `.mmd` publication substitute |
| Lint/types | `python -m ruff check src scripts tests --ignore E402`, `python -m mypy src scripts tests` | Project-local static checks |
| Full tests | `python -m pytest tests --cov=src --cov-fail-under=90 --cov-report=term-missing -q` | Full mode only; branch-enabled reported total with configured omissions, not independent line/branch floors |
| Analysis | `biology_analysis.py` | Full mode: collect configured manuscript, stage complete source and write analysis report |
| Render | `render_textbook.py` | Full mode: independently refresh staging from validated live config, strict inline PNGs, read-only template PDF library |
| Visual/source validation | `audit_visual_contracts.py --check` plus recursive markdown/prerender validation in aggregate gate | Default mode renders inline assets for review; full mode audits actual render assets |
| PDF log | `check_pdf_log.py output/pdf/_combined_manuscript.log --max-overfull-pt 50` | Full mode: both horizontal and vertical overflows above 50 pt fail, as do undefined references and missing glyphs; no missing-glyph allowance |

The dependency DAG blocks consumers of failed prerequisites but continues independent peers. Failure aggregation counts nonzero statuses, so negative signal codes cannot cancel positive failures. Full tests depend on source audits; analysis depends on tests and strict diagrams; render depends on analysis; PDF-log and full visual checks depend on render. Default review uses the supplied review artifact directory (the module fallback is output/publication_readiness); the CLI owns that selection. Full artifacts stay under this project's output tree, including output/manuscript, output/figures and output/pdf. No template output tree is used.

Every PDF render validates the selected configuration and atomically replaces the complete staged source set; deleted/disabled chapters cannot survive from a previous staging. Inline assets are rendered fresh and matched to canonical normalized source identities before replacement. Missing or corrupt PNGs fail. Do not edit generated staging as manuscript source.

Inline Mermaid print layout is project-owned. The audited square PNG stays byte-for-byte intact; LaTeX clips white/transparent padding around visible content, retaining a two-pixel safety margin. Diagrams print at 144 raster pixels per inch or denser, capped at 96% of the local line width and 8.5 inches high without stretching. The frozen emitter still escapes captions and alt metadata. Native box measurements and raster inspection are distinct from physical-print or PDF/UA certification.

Multipage tables start after pending figures have been placed. The preamble uses TeX's `placeins` package and a pre-longtable float barrier: longtable's page builder must not compete with a deferred large figure for the same page. This favors intact content/order over filling every page; the 9 pt/2 mm/1.28 layout is unchanged. The checker CLI and Python runner inherit the horizontal budget for vertical overflow unless a separate vertical budget is explicitly supplied; native publication uses 50 pt for both, not the former implicit 350-point vertical allowance.

Source admission covers the complete manuscript file graph, including configuration, bibliography, preamble and cover inputs; an escaping file or directory alias refuses before collection. Generated destinations must remain beneath the project's real `output/` tree, without symlink ancestors, including aliases that resolve back inside the project. These checks do not authorize arbitrary external renderer code.

Rendering assumes trusted repository sources and the admitted renderer. Path
containment and disabled shell escape do not constitute a hostile-TeX file-read
sandbox. A local source-bound receipt is not external certification of scientific
claims, print acceptance, or publication permission.

These are implemented contracts, not a declaration that a particular source has passed. Read the exact-source full receipt and separate print-review evidence; local export does not establish remote publication. Software 2.0.0/edition 1.1 remains unreleased; see [../CHANGELOG.md](../CHANGELOG.md).

## Source-bound native release assets

The full gate atomically writes `output/publication_readiness/receipt.json` with
its exact commands, outcomes, runtime, before/after Git state, renderer-manifest
identity and artifact hashes. A new attempt replaces old success with `running`
**before fallible configuration, toolchain or snapshot preflight**. Preflight
failure or interruption cannot revive an earlier passing receipt. The selected
renderer manifest must cover the exact on-disk runtime payload tree; its actual
file bytes are checked before and after the gate and again during export.

Git source checks explicitly select this project's worktree even if stored Git configuration points elsewhere; unrelated configuration, authentication and transport settings are retained. Print-review evidence must match the current clean source as well as the PDF hash. Dependency-install proofs disable ambient uv configuration and project/destination selectors, retaining only admitted repository-local cache paths; verify the installed consumer, not merely an install exit status.

A release export requires **clean main**, a passing full receipt for that exact
commit/tree, the same frozen renderer and unchanged PDF bytes. Use the licensed
`renderer/` snapshot supplied in a validated executable bundle, or an independently
verified committed Git-archive snapshot with its per-file `source_manifest.json`.
A mutable neighboring checkout is not that provenance input. Re-run full proof
with the selected snapshot before exporting:

```bash
export BIOLOGY_TEXTBOOK_TEMPLATE_ROOT="$RENDERER_SNAPSHOT"
export SOURCE_DATE_EPOCH="$(git show -s --format=%ct HEAD)"
uv run --locked --extra dev python scripts/audit_publication_readiness.py --check --full
uv run --locked --extra dev python scripts/build_release_assets.py \
  --renderer-root "$RENDERER_SNAPSHOT" --output-dir output/releases/v2.0.0
```

The new destination must not exist and must be disjoint from the frozen renderer:
it cannot equal the snapshot or be beneath it. It contains the instructor PDF, versioned
executable ZIP, independent main-only Git bundle, provenance and SHA256SUMS.
The ZIP supplies all project source, the licensed frozen rendering library and
`REPRODUCE.py`; no template-root wrapper or missing Docker entry point is used.
Extract into a fresh directory and run `python3 REPRODUCE.py`. It refuses an
occupied checkout, explicitly clones bundled `main` and verifies its commit.
Dependency bootstrap pins the restored project's own `.venv`, supplies an explicit
project directory and ignores inherited project/interpreter selectors and uv
configuration files; it must not synchronize an unrelated active environment.
Source-state capture and Git restoration also discard inherited repository, worktree,
common-store, index, object-store and namespace selectors. Explicit project paths
must not bind another repository. Git configuration, authentication and transport
policy remain inherited; no host or repository configuration is rewritten.
The runner installs locked Python/Node dependencies and executes the real full gate
into the restored project's output tree. Git, uv, Python 3.15.2, compatible Node/npm,
Pandoc, XeLaTeX and Chrome/Chromium are prerequisites; review `.puppeteer.json`
on other hosts. Standard offline/cache flags are honored. Preserve the same
`SOURCE_DATE_EPOCH` for same-input deterministic PDF comparisons; PDF
canonicalization uses the locked `pypdf` dependency.
No Docker run or byte-identical cross-platform PDF is asserted.

Exporting is not remote publication or Zenodo deposition. Follow the actual host's
identity/admission/review policy for commits, pushes, tags and releases; this CLI
has no remote-write permission or bypass. A release blocked by policy remains
unpublished even when its local assets are complete.

## Project-Specific Scripts

Run `uv run python scripts/audit_textbook_quality.py --check --max-advisories 0` before a render
when a pass changes chapters, labs, question banks, glossary entries, or recent
biological claims. It catches generic answer-key prose, `Expected reasoning:`,
`Key answer:`, and `Mechanistic answer:` scaffolds, stale current-science
claims, student-facing source boilerplate, required wet-lab drift, hard-coded
rendered references, glossary and citation closure, weak figure metadata,
ledger-backed absolute-language triage in `docs/manuscript/quality_advisories.yaml`,
and embedded-enrichment coverage.

Enrichment may inspect or update supported authored content, but cannot invent scientifically defensible answers. `refine_generated_answers.py --dry-run` validates authored keys; missing, generic or unsupported answers raise without writing in either mode. Repair each answer from its actual prompt and evidence. Preserve curated semantic objective mappings and lab rubrics; positional regeneration is not supported.

Instructor keys use the complete `<!-- SOLUTION` … `SOLUTION -->` authoring protocol. A bare `-->` is not an interchangeable key terminator. Validate the actual instructor-visible prose, not merely the presence of answer strings. Mermaid metadata normalization owns the adjacent alt comment and first italic caption, not subsequent worked examples or provenance paragraphs, which remain authored content.

Solution reveal preserves literal fenced examples of that protocol and fenced code inside real answers, including code-only, leading, middle and trailing positions. Delimiter whitespace must not consume position-masked code lines. Explicit block boundaries keep following numbered question stems outside the preceding answer's quote; inspect the actual reader and rendered hierarchy, not only extracted answer text. Course-grid widths include intercolumn padding, and metadata regeneration preserves authored front matter and existing page breaks.

Curriculum synchronization owns navigation, blueprints, canonical headings and
generated appendices—not authored lab procedures, question keys, rubrics or
coverage notes. Both former assessment-body regeneration paths are removed.
The native twice-run regression checks content and file-version stability rather
than accepting a generator's success counter as preservation evidence.

Bibliography keys identify distinct documents: approval announcements and product
labels have separate keys. Duplicate keys raise instead of silently collapsing;
an invalid bibliography cannot be interpreted as an empty, valid reference set.

From the active project root:

### Core generators (run before PDF render)

```bash
uv run --frozen --extra dev python scripts/generate_figures.py
uv run --frozen --extra dev python scripts/generate_diagrams.py --strict-png --size 1200
uv run --frozen --extra dev python scripts/render_textbook.py  # always freshly hydrates live sources
```

### Manuscript maintenance utilities

Apply only the helper whose ownership matches the edit, inspect its changes, and establish idempotence with the relevant behavioral tests. A general statement that all helpers are idempotent is not a fresh run result.

| Script | Purpose | Runs when |
|---|---|---|
| `insert_crossref_labels.py` | Inserts `\label{sec:unit_X_<stem>}` after every chapter H1; rewrites legacy chapter-number prose to `\cref{sec:…}` when a canonical target exists | After adding/renaming a chapter |
| `insert_chapter_metadata.py` | Renders chapter-metadata badges and the *Course Planning Grid* in `front_matter.md` from `biology.toc` + `src/biology/chapter_metadata.py` | After editing `config.yaml` titles/order or `chapter_metadata.py` |
| `sync_curriculum_materials.py` | Renders Study Blueprint/checklist blocks, generated curriculum appendices, unit-intro labels, front-matter navigation, reading paths, concept map, and preface scope table from `BookToc` | After editing `config.yaml`, curriculum/alignment records, or unit/chapter titles |
| `integrate_orphan_citations.py` | Weaves orphan BibTeX entries into chapter prose as `\citep{…}` | After adding entries to `references.bib` |
| `link_glossary.py` | Adds `{#gl:<slug>}` anchors to every glossary term; rewrites and checks glossary/index back-references as semantic `\cref{sec:…}` labels | After editing `glossary.md` |
| `link_labs_to_chapters.py` | Inserts `\cref{sec:unit_X_<stem>}` opening into every lab and question bank | After adding a lab or question file |
| `normalize_lab_computational_workflows.py` | Replaces stale notebook/CSV instructions with self-contained optional snippets backed by `src/biology` | After adding or bulk-editing lab Part 2 computation sections |
| `sync_assessment_metadata.py` | Validates and preserves curated question-item comments and lab LO/rubric blocks; --dry-run and --check do not manufacture missing semantic records | After author-reviewed assessment changes |
| `insert_orphan_figures.py` | Creates `\begin{figure}…\end{figure}` blocks for unreferenced `ALL_FIGURE_GENERATORS` entries | After registering a new figure generator |
| `normalize_typography.py` | Converts ASCII `-->` to `→` in prose (skips code, math, HTML comments, YAML front matter) | Bulk polish pass |
| `fix_greek_math_prose.py` | Replaces `$\alpha$`/`$\beta$`/… with Unicode in prose cells (works around a pandoc limitation) | Bulk polish pass |

Each helper supports `--dry-run`.

**Script ownership hub:** [../scripts/AGENTS.md](../scripts/AGENTS.md); use current CLI/source contracts rather than fixed inventory counts or copied launch recipes.

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

Then run the project-local default/full publication gates above; they include recursive markdown and prerender validation through the selected template library. Full workflow: [composable_authoring.md](composable_authoring.md).

## docs/manuscript/config.yaml — Rendering Configuration

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

The PDF renderer reads `docs/manuscript/config.yaml` to discover chapter file paths and ordering. It then:
1. Concatenates chapters in order
2. Resolves cross-references (`\cref{sec:…}`, `\cref{fig:…}`, `\cref{eq:…}` via `cleveref`; natbib `\citep{…}` / `\citet{…}` via bibtex)
3. Inserts auto-generated chapter and figure numbers
4. Passes to pandoc/LaTeX as a single document

Lab and question-bank entries under `appendices.labs/questions` store only
`file:` names. Their display titles are derived from the parent chapter by
`biology.toc` and synchronized into the markdown H1s by
`scripts/sync_curriculum_materials.py`.

Book-style PDF opening metadata lives under `book` in
`docs/manuscript/config.yaml`. The renderer uses `book.title`, `book.subtitle`,
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
- Use informative source titles without manual numeric prefixes. Heading normalization does not establish semantic title quality; author content-specific headings while preserving canonical H1s and protected literal examples.

## Invariant tests used by the publication gate

Domain and invariant/quality tests cover manuscript, lab, question, render and script contracts; current passing counts require a fresh run. See [testing_guide.md](testing_guide.md#test-organization).

- `test_build_invariants.py` — every chapter labeled, every lab/question `\cref`-linked, every figure generator referenced
- `test_bibliography_closure.py` — `{cited}` == `{defined}` in `references.bib`
- `test_chapter_metadata.py` — `ChapterMeta` records cover every `config.yaml` chapter with valid difficulty and prerequisites
- `test_toc_consistency.py` — renderable H1s, unit-intro labels, front-matter/preface generated blocks, appendices, and Course Planning Grid match `biology.toc`
- `test_accessibility.py` — LaTeX figures and inline Mermaid meet alt/caption rules ([docs/manuscript/AGENTS.md](../docs/manuscript/AGENTS.md))
- `test_crossref_validator.py`, `test_crossref_validator_edges.py`, `test_crossref_validator_internals.py` — pandoc-crossref / cleveref resolution
- `test_lab_integrity.py` — optional lab computation snippets resolve project modules and do not require hidden notebooks, CSVs, pandas, or display-only plotting
- `test_pdf_log_quality.py` — PDF-log checker rejects undefined references and severe overfull boxes
- `test_pdf_opening_and_mermaid.py` — cover/opening metadata and inline Mermaid rendering stay intact
- `test_question_answer_refinement.py` — preserve authored solutions and refuse unsupported automatic answer repair without writing
- `test_script_quality.py` — Mermaid metadata and assessment dry-run behavior, not absent script-hygiene nodes

## Known gotchas

| Gotcha | Symptom | Fix |
| ------ | ------- | --- |
| `\bibliographystyle{plainnat}` declared in `preamble.md` | bibtex aborts: "Illegal, another `\bibstyle` command" | **Remove** the line. Pandoc auto-injects it; a double declaration is fatal. |
| `\includegraphics{output/figures/foo.png}` (absolute-style path) | xelatex: `! LaTeX Error: File '...' not found.` | Use `../figures/foo.png` — paths are relative to `output/manuscript/`, not the source `docs/manuscript/` tree. |
| Bare `$\alpha$` / `$\beta$` etc. in pipe-table cells | Pandoc emits `\(\alpha)` without closing `\)`; xelatex aborts on the table | Run `scripts/fix_greek_math_prose.py` to replace with Unicode in prose contexts. |
| Manual equation numbering on a `$$…$$` line | xelatex errors or numbering drift | Use a labeled `equation` or `align` environment for numbered display equations; use plain `$$…$$` only for unnumbered display math. See [manuscript_guide.md#equations](manuscript_guide.md#equations). |
| Hand-typed "Figure 4.2" / "Chapter 11" / "Equation 5.7" in chapter prose | Number drifts when chapters are reordered | Use `\cref{fig:unit_X_<descriptor>}`, `\cref{sec:unit_X_<stem>}`, or `\cref{eq:unit_X_<descriptor>}`; `cleveref` injects the right number and the cross-reference validator rejects hard-coded rendered numbers. |
| mmdc unavailable | Strict graphics/PDF paths fail | Use npm ci and expose the project-local pinned CLI on PATH; verify browser compatibility separately. |
| Mermaid label with unquoted `(`, `)`, `:` | mmdc render fails with parse error | Wrap label: `A["Glucose (C6H12O6)"]`. |
| Lab Part 2 references a hidden notebook or CSV | `test_lab_integrity.py` fails on stale phrases such as `.ipynb`, `pd.read_csv`, or "provided Jupyter Notebook" | Run `scripts/normalize_lab_computational_workflows.py`; keep optional computation snippets self-contained and backed by `biology.*` imports. |
