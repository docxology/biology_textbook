# Biology Textbook — *Introduction to Biology: A Generative Approach*

Manuscript-driven introductory biology (44 chapters across Units 0-X, 44 paper-based labs, 44 question banks of 30 questions each) with tested Python models (kinetics, population genetics, neural signaling, ecology, and related topics). Registered diagrams use Mermaid through `src/mermaid/`; publication builds use PNG output. Figures use matplotlib from `src/visualization/plots.py`.

## Source and citation

| | |
| --- | --- |
| **Repository** | [biology textbook source repository](https://github.com/docxology/biology_textbook) |
| **DOI (Zenodo)** | [10.5281/zenodo.20286478](https://doi.org/10.5281/zenodo.20286478) |
| **Text license** | CC BY 4.0 (`manuscript/config.yaml` → `book.license`) |
| **Code license** | Apache-2.0 (`book.code_license`) |

**Build health:** run `uv run python -m pytest tests/ --cov=src --cov-fail-under=90` from this directory for test count and coverage; the current filesystem has 36 Python files under `scripts/` and 41 `test_*.py` modules under `tests/`. `references.bib`, `glossary.md`, lab computation snippets, question-bank answers, current-claim ledger entries, quality-advisory triage, assessment metadata, visual-contract manifest findings, textbook-quality audit findings, chapter pedagogy regression locks (`test_chapter_pedagogy_coverage.py`), and script hygiene are kept closed by tests. Aggregate publication gate: `uv run python scripts/audit_publication_readiness.py --check` (uses temporary visual artifacts; add `--full` before release). The question-bank gate rejects generated-style solution scaffolds such as `Expected reasoning:`, `Key answer:`, and `Mechanistic answer:`. The visual manifest covers 252 records: 32 `plot_*` figure generators, 24 registered Mermaid diagrams in `src/`, and 196 inline Mermaid fences in the manuscript. Regenerate the combined PDF to refresh file size and layout.

## Location

This tree is currently maintained as an active standalone checkout. Run project-local commands from this directory; when using the template pipeline, invoke entry points from the template repository root with `--project biology_textbook` so the resolver can locate the active project tree.

## Quick start

```bash
cd /path/to/biology_textbook

uv sync
uv run python -m pytest tests/ --cov=src --cov-fail-under=90 -v     # run from this directory for the 90% gate

uv run python scripts/generate_diagrams.py                # 24 mermaid diagrams
uv run python scripts/generate_diagrams.py --strict-png   # publication gate: reject .mmd fallbacks
uv run python scripts/generate_figures.py                 # 32 square-padded matplotlib figures
uv run python scripts/biology_analysis.py                 # injects full textbook + copies live config, references, preamble, and cover assets
uv run python scripts/enrich_embedded_textbook.py --dry-run # audit embedded enrichment coverage without editing
uv run python scripts/refine_generated_answers.py --dry-run # verify answer keys need no generated-scaffold rewrite
uv run python scripts/audit_textbook_quality.py --check --max-advisories 0 # manuscript/lab/question/current-claim quality gate
uv run python scripts/audit_current_claims.py --check     # fast-moving claim ledger
uv run python scripts/sync_assessment_metadata.py --dry-run # preview question/lab metadata drift
uv run python scripts/sync_assessment_metadata.py --check   # question-item and lab-alignment metadata gate
uv run python scripts/audit_visual_contracts.py --check   # visual manifest, alt/caption, and aspect contract
```

Validate Markdown (from a template repository root with infrastructure available):

```bash
uv run python -m infrastructure.validation.cli markdown /path/to/biology_textbook/manuscript/
```

Render the combined PDF (from repository root, works with the in-progress path as well):

```bash
uv run python scripts/03_render_pdf.py --project biology_textbook
```

## Manuscript structure

Authoritative ordering: **`manuscript/config.yaml`**. It defines Unit 0 (systems / complexity prelude), Units I – X (**44** core chapter files across unit directories), front matter, and optional appendices (`labs/`, `questions/`). Chapter numbers are assigned at render time; filenames are descriptive slugs.

Supporting files in `manuscript/`: `preamble.md` (LaTeX geometry, body size, and `cleveref` — keep in sync with `config.yaml` layout/typography), `references.bib` (358 entries, fully closed), `glossary.md` (226 terms with `{#gl:…}` anchors), `front_matter.md` (includes auto-generated Course Planning Grid), `preface.md`.

### Manuscript-wide conventions

- Every chapter H1 is followed by `\label{sec:unit_X_<stem>}` — refer via `\cref{sec:unit_X_<stem>}`
- Every chapter carries a metadata badge (Level 1/3–3/3 difficulty · reading time · lecture time · prerequisites)
- Every lab and question bank `\cref`-links back to its parent chapter
- Every BibTeX entry is cited at least once; every citation resolves (enforced by `tests/test_bibliography_closure.py`)
- Current or fast-moving claims are tracked in `manuscript/current_claims.yaml` and checked by `scripts/audit_current_claims.py --check` plus `tests/test_current_claims_ledger.py`
- Absolute-language advisories are triaged in `manuscript/quality_advisories.yaml`; `scripts/audit_textbook_quality.py --check --max-advisories 0` is the current zero-advisory gate and fails on new untriaged advisories or unresolved `needs_qualifier` / `copyedit_artifact` entries.
- Question-bank item metadata and lab learning-objective/rubric alignment are synchronized by `scripts/sync_assessment_metadata.py`; use `--dry-run` to preview drift, `--check` for the gate, and `tests/test_assessment_metadata.py` plus `tests/test_lab_pedagogy_alignment.py` for invariant coverage.
- Structural locks are asserted in `tests/test_build_invariants.py`

### Compact PDF defaults

The built textbook PDF uses **9 pt** body text, **2 mm** margins, and **1.28** line spacing for dense letter-size output. To change print density, edit **`manuscript/config.yaml`** and the matching **`manuscript/preamble.md`** blocks together (see [AGENTS.md](AGENTS.md) table).

### Optional reader (large-type) profile

For more legible print or on-screen reading, use a second build with larger margins and body size: edit **`manuscript/config.yaml`** (`layout.margin_*_mm`, `typography.base_font_size_pt`, `layout.line_height`) and the same values in **`manuscript/preamble.md`** (`geometry`, `\normalsize`, `\setstretch`) in one pass. Suggested starting values: **10.5–11 pt** body, **10–12 mm** margins, **1.35–1.4** line height. See [docs/accessibility.md](docs/accessibility.md#reader--large-type-profile-optional).

## Project layout

```text
├── src/biology/       # 9 domain subpackages + chapter_metadata.py + crossref_validator.py
├── src/mermaid/       # diagram definitions + renderer
├── src/visualization/ # __init__.py (ALL_FIGURE_GENERATORS, 32 plots) + cvd.py (palette)
├── scripts/           # 36 Python files — see [AGENTS.md](AGENTS.md) (core build + content maintenance)
├── tests/             # 41 test modules, ≥90% line+branch on `src/`, no mocks
├── manuscript/        # config.yaml drives unit/chapter/lab/question order
└── docs/              # composable authoring, architecture, pipeline, testing, API, guides
```

## Documentation

- [docs/composable_authoring.md](docs/composable_authoring.md) — **start here** for new chapters, figures, and `\cref` / label workflows (invariant tests, script order)
- [AGENTS.md](AGENTS.md) — layout, tests, validation, invariants, AI protocol
- [manuscript/AGENTS.md](manuscript/AGENTS.md) — figure/diagram allowlists, chapter/lab/question conventions
- [manuscript/README.md](manuscript/README.md) — author quick reference and course pathways
- [docs/README.md](docs/README.md) — full doc index
- [docs/agent_instructions.md](docs/agent_instructions.md) — editorial style and structure targets
- [docs/pipeline_guide.md](docs/pipeline_guide.md) — pipeline stages and maintenance scripts
- [docs/testing_guide.md](docs/testing_guide.md) — zero-mock policy, failure-to-fix table
- [docs/architecture.md](docs/architecture.md) — `src/`, tests, manuscript–code contract
- [docs/api_reference.md](docs/api_reference.md) — public `biology.*` and manuscript utilities
- [docs/accessibility.md](docs/accessibility.md) — config vs tests, alt text, CVD figures, reader PDF profile
- [docs/pedagogy_objectives_mapping.md](docs/pedagogy_objectives_mapping.md) — optional LO ↔ question-bank mapping
