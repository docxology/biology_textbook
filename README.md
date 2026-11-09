# Biology Textbook — *Introduction to Biology: A Generative Approach*

## Abstract

*Introduction to Biology: A Generative Approach* is an open instructor-edition textbook covering introductory biology across forty-four chapters from systems science and chemical foundations through cells, metabolism, molecular and classical genetics, evolution, microbiology, plant and animal physiology, and ecology. Organized as Unit 0 plus Units I–X, the text presents biology as an evidence-bound discipline in which mechanisms, measurements, and simple models are developed together, so readers can move between narrative explanation and the quantitative constraints that shape biological claims. Five recurring themes—evolution, information, structure and function, systems and emergence, and the cell—provide orientation across scales and align with mainstream undergraduate biology competencies; Unit 0 adds an optional systems lens (feedback, emergence, and prediction) without replacing the core molecular-to-ecological sequence.

Quantitative teaching models live in domain Python packages, and figures/process diagrams are generated programmatically. Each configured chapter is paired with a finite paper-based lab packet and a thirty-item bank with authored solutions and semantic mappings. Synthetic output is not empirical validation, and citation metadata is not full-text source verification. Source is on [GitHub](https://github.com/docxology/biology_textbook). DOI [10.5281/zenodo.20286478](https://doi.org/10.5281/zenodo.20286478) identifies prior release 1.0.0 only; edition 1.1 has no new deposition claimed. Text is licensed CC BY 4.0; code Apache-2.0.

Canonical copy for Zenodo and other metadata fields: [docs/publication_abstract.md](docs/publication_abstract.md).

Manuscript-driven introductory biology (44 chapters across Units 0–X, 44 paper-based labs, 44 thirty-item banks) is paired with Python teaching models. Registered Mermaid diagrams require PNG output for publication. Matplotlib implementations live in `src/visualization/plots_*.py`, registered through `plots.py`.

## Status

Software **2.0.0** and manuscript edition **1.1** are release candidates, not a published release. Current proof requires an exact-source full-gate receipt and separate inspection of the resulting PDF; historical reports are not current proof. Publication, tagging and deposition are separate states. See [CHANGELOG.md](CHANGELOG.md).

For content edits, start at [docs/composable_authoring.md](docs/composable_authoring.md) and [docs/agent_instructions.md](docs/agent_instructions.md). Run the project-local publication gate before release; its default mode is not the full test/PDF proof.

## Source and citation

| | |
| --- | --- |
| **Repository** | [biology textbook source repository](https://github.com/docxology/biology_textbook) |
| **Prior-release DOI only (1.0.0)** | [10.5281/zenodo.20286478](https://doi.org/10.5281/zenodo.20286478); no new deposition is claimed for edition 1.1 |
| **Text license** | [CC BY 4.0](LICENSE-CONTENT) (`docs/manuscript/config.yaml` → `book.license`) |
| **Code license** | [Apache-2.0](LICENSE) (`book.code_license`) |

The configured coverage threshold is 90% of the reported, branch-enabled coverage total, with explicit exclusions in `pyproject.toml`; this is not separate 90% line and branch guarantees. Current counts and passing results must come from a fresh run.

Software distributions include both notices: executable code remains Apache-2.0,
embedded teaching text remains CC BY 4.0. Their aggregate package expression does
not relicense either component. Python's project pin is 3.15.2; the declared
minimum Python support is not itself proof of a tested multi-version matrix.

- **Full publication proof:** `uv run --frozen --extra dev python scripts/audit_publication_readiness.py --check --full`
- **Default publication gate:** `uv run --frozen --extra dev python scripts/audit_publication_readiness.py --check`
- **Source quality:** `uv run --frozen --extra dev python scripts/audit_textbook_quality.py --check --max-advisories 0`
- **Current-claim ledger:** `uv run --frozen --extra dev python scripts/audit_current_claims.py --check`
- **Curated assessment metadata:** `uv run --frozen --extra dev python scripts/sync_assessment_metadata.py --check`

Answer-generation commands cannot supply scientifically defensible keys: unsupported generated answers are refused without writing. Author and review question-specific answers and semantic mappings directly.

Curriculum synchronization updates navigation, blueprints and generated appendices;
it does not regenerate authored lab procedures, question keys, rubrics or coverage
notes. Approval announcements and prescribing labels are distinct source records.
Duplicate bibliography keys fail rather than merging different documents.

For source conventions use [the manuscript contract](docs/manuscript/AGENTS.md); for actual invariant-test coverage and limits use [the testing guide](docs/testing_guide.md).

## Standalone quick start

Run from this checkout. Install the locked development extra and locked Node dependencies (Node >=22.13.0); do not install an unpinned global Mermaid CLI.

The declared empty uv workspace fixes this standalone project's lock root; the explicit npm prefix below fixes its installation/cleanup root. A containing development workspace must not annex either operation. Template rendering remains an independent read-only-library contract.

```bash
uv sync --frozen --extra dev
npm --prefix "$PWD" ci --ignore-scripts
export PATH="$PWD/node_modules/.bin:$PATH"
# Select an existing compatible template checkout as a read-only library:
export BIOLOGY_TEXTBOOK_TEMPLATE_ROOT=/path/to/template
uv run --frozen --extra dev python scripts/generate_figures.py
uv run --frozen --extra dev python scripts/generate_diagrams.py --strict-png
uv run --frozen --extra dev python scripts/audit_publication_readiness.py --check
uv run --frozen --extra dev python scripts/render_textbook.py
# Release proof includes tests, analysis, fresh render and strict PDF-log checks:
uv run --frozen --extra dev python scripts/audit_publication_readiness.py --check --full
```

Rendering also requires Pandoc, XeLaTeX and a working browser for Mermaid CLI **12.2.0**. Review the project-local `.puppeteer.json` for host compatibility; no host configuration change is implied here. Template discovery accepts the explicit environment selection or a genuine enclosing template, never an ambient neighboring checkout. Invalid explicit selection fails. Local source/scripts take precedence; template-root scripts are not entry points for this project.

`scripts/render_textbook.py` validates and freshly stages the live configured manuscript for every render, binds inline Mermaid PNGs to canonical source identities, and writes only to this project's `output/`. Complete staging replaces the prior source tree atomically. Missing/corrupt PNGs fail; `.mmd` source is not a publication substitute. See [docs/pipeline_guide.md](docs/pipeline_guide.md) for validation and artifact paths.

## Manuscript structure

Authoritative ordering: **`docs/manuscript/config.yaml`**. It defines Unit 0 (systems / complexity prelude), Units I – X (**44** core chapter files across unit directories), front matter, and optional appendices (`labs/`, `questions/`). Chapter numbers are assigned at render time; filenames are descriptive slugs.

Supporting files in `docs/manuscript/`: `preamble.md` (keep layout/typography paired with `config.yaml`), `references.bib`, `glossary.md`, `front_matter.md`, and `preface.md`. Bibliography closure is a software invariant, not full-text verification of every cited claim.

### Manuscript-wide conventions

- Every chapter H1 is followed by `\label{sec:unit_X_<stem>}` — refer via `\cref{sec:unit_X_<stem>}`
- Every chapter carries a metadata badge (Level 1/3–3/3 difficulty · reading time · lecture time · prerequisites)
- Every lab and question bank `\cref`-links back to its parent chapter
- Every BibTeX entry is cited at least once; every citation resolves (enforced by `tests/test_bibliography_closure.py`)
- Current or fast-moving claims are tracked in `docs/manuscript/current_claims.yaml` and checked by `scripts/audit_current_claims.py --check` plus `tests/test_current_claims_ledger.py`
- Absolute-language candidates are source-bound reviews in `docs/manuscript/quality_advisories.yaml`. `--max-advisories 0` still permits no outstanding advisories: accepted definitions remain explicitly `reviewed`, while missing rationales, wrong path/line/excerpt, untriaged/unresolved and stale entries fail. See [the triage contract](docs/absolute_language_triage.md).
- Question-item objective mappings and lab rubrics are curated semantic records. `scripts/sync_assessment_metadata.py --dry-run` previews drift and `--check` validates it; preserve reviewed mappings rather than regenerate them from item position.
- Structural locks are asserted in `tests/test_build_invariants.py`

### Compact PDF defaults

Current source defaults are **9 pt** body, **2 mm** margins and **1.28** line spacing. These are configuration values, not a readability claim; release print inspection remains required. Change `config.yaml` and `preamble.md` together.

### Optional reader (large-type) profile

For more legible print or on-screen reading, use a second build with larger margins and body size: edit **`docs/manuscript/config.yaml`** (`layout.margin_*_mm`, `typography.base_font_size_pt`, `layout.line_height`) and the same values in **`docs/manuscript/preamble.md`** (`geometry`, `\normalsize`, `\setstretch`) in one pass. Suggested starting values: **10.5–11 pt** body, **10–12 mm** margins, **1.35–1.4** line height. See [docs/accessibility.md](docs/accessibility.md#reader--large-type-profile-optional).

## Project layout

```text
├── src/biology/       # 9 domain subpackages + chapter_metadata.py + crossref_validator.py
├── src/mermaid/       # diagram definitions + renderer
├── src/visualization/ # registered quantitative figures and CVD palette
├── scripts/           # project-local thin orchestrators
├── tests/             # numerical, source, maintenance and integration contracts
├── docs/manuscript/        # config.yaml drives unit/chapter/lab/question order
└── docs/              # composable authoring, architecture, pipeline, testing, API, guides
```

## Documentation

- [docs/composable_authoring.md](docs/composable_authoring.md) — **start here** for new chapters, figures, and `\cref` / label workflows (invariant tests, script order)
- [AGENTS.md](AGENTS.md) — layout, tests, validation, invariants, AI protocol
- [docs/manuscript/AGENTS.md](docs/manuscript/AGENTS.md) — canonical H1s, stable identifiers, references and authored assessments
- [docs/manuscript/README.md](docs/manuscript/README.md) — author quick reference and course pathways
- [docs/README.md](docs/README.md) — full doc index
- [docs/agent_instructions.md](docs/agent_instructions.md) — editorial style and structure targets
- [docs/pipeline_guide.md](docs/pipeline_guide.md) — pipeline stages and maintenance scripts
- [docs/testing_guide.md](docs/testing_guide.md) — real-computation policy, isolation exceptions and coverage limits
- [docs/architecture.md](docs/architecture.md) — `src/`, tests, manuscript–code contract
- [docs/api_reference.md](docs/api_reference.md) — public `biology.*` and manuscript utilities
- [docs/accessibility.md](docs/accessibility.md) — config versus enforcement, alt text, CVD figures and unvalidated reader-profile suggestions
- [docs/pedagogy_objectives_mapping.md](docs/pedagogy_objectives_mapping.md) — curated semantic LO/Bloom mappings and lab rubrics
