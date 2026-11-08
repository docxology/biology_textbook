# Biology Textbook — Manuscript

## Manuscript Source Map

Markdown sources are ordered by config.yaml; filenames are semantic slugs, not indices. Project-local scripts/render_textbook.py validates the selected config, atomically replaces complete staging under output/manuscript and freshly renders strict canonical source-matched inline PNGs before invoking Pandoc/LaTeX through a read-only template library.

Run from this project root after uv sync --frozen --extra dev and npm ci; expose node_modules/.bin on PATH (Mermaid CLI pinned 12.2.0, Node >=22.13.0). Set BIOLOGY_TEXTBOOK_TEMPLATE_ROOT to an existing compatible template or use a genuine enclosing template. Invalid explicit selection fails; ambient neighbors and template-root entry points are not supported. See ../pipeline_guide.md.

Paths explicitly prefixed `src/`, `scripts/`, `tests/` or `output/` are repository-root paths. Manuscript-local `config.yaml`, `preamble.md`, unit slugs and appendix paths are relative to this directory; Markdown links are relative to this document.

## Quick reference

| Action | Where / command |
| ------ | ----------------- |
| Source repository | [biology textbook source repository](https://github.com/docxology/biology_textbook) |
| Prior release 1.0.0 DOI only | [10.5281/zenodo.20286478](https://doi.org/10.5281/zenodo.20286478); edition 1.1 DOI remains unassigned, with no new deposition claimed |
| End-to-end add chapter / figure / labels | [../docs/composable_authoring.md](../composable_authoring.md) (checklists + tests) |
| View chapter order | `config.yaml` → `units[]` and `appendices` |
| Add a chapter | Create `unit_<id>/<slug>.md`; register it in `config.yaml`; add metadata in `src/biology/chapter_metadata.py` |
| Toggle labs / questions | `config.yaml` → `appendices.include_labs`, `include_questions` |
| Reference appendices | `appendices/` plus root `glossary.md`; rendered when `config.yaml` → `appendices.include_reference` is true, with titles and order from `appendices.reference[]` |
| Author / ORCID | `config.yaml` → `book`, `authors[]` |
| Cover image | `config.yaml` → `book.cover.image`; regenerate with `uv run python scripts/generate_cover_art.py` |
| Margins / body size | `config.yaml` → `layout.margin_*_mm`, `typography.base_font_size_pt`, `layout.line_height` **and** the matching `geometry`, `\normalsize`, `\setstretch` block in `preamble.md` |
| Link color | `config.yaml` → `typography.link_color` |
| Toggle front matter | `config.yaml` → `front_matter.include_front_matter` |
| Navigation / scope blocks | `front_matter.md` and `preface.md` generated markers — edit `config.yaml`, then rerun `uv run python scripts/sync_curriculum_materials.py` |
| Course Planning Grid | Edit config titles/order and `src/biology/chapter_metadata.py`; run `scripts/insert_chapter_metadata.py` to refresh the owned marker block |
| Glossary | `glossary.md` — each term is a bracketed span `` [**Term**]{#gl:<slug>} `` (PDF ``\label{gl:…}``); link on first use with `` `[**term**](#gl:<slug>)` `` |
| Generate figures | Project-root `scripts/generate_figures.py`; domain implementations in `src/visualization/plots_*.py`, palette in `cvd.py`; inspect final-size output |
| Accessibility, config vs tests | [../docs/accessibility.md](../accessibility.md) |
| Registered Mermaid PNGs | From project root: uv run --frozen --extra dev python scripts/generate_diagrams.py --strict-png --size 1200; no source-only publication fallback |
| Check current claims | `uv run python scripts/audit_current_claims.py --check`; source data lives in `current_claims.yaml` |
| Assessment metadata | Author semantic item mappings and lab rubrics; scripts/sync_assessment_metadata.py --check validates/preserves them without ordinal regeneration |
| Render PDF | From project root: uv run --frozen --extra dev python scripts/render_textbook.py |
| Full publication proof | uv run --frozen --extra dev python scripts/audit_publication_readiness.py --check --full; includes tests, analysis, fresh render and strict PDF log |

Software 2.0.0/edition 1.1 is unreleased. Exact-source full-gate and separate PDF-review receipts establish local proof, not remote publication; historical reports are not current validation. Citation closure and metadata lookup do not establish full-text verification. See ../../CHANGELOG.md.

## Manuscript-wide conventions

- Every chapter H1 is followed by `\label{sec:unit_X_<stem>}` — reference with `\cref{sec:unit_X_<stem>}`
- Unnumbered unit intros use their stable sec identifier on the H1 as a Pandoc attribute, not a standalone label; reference visible unit names with nameref.
- Renderable H1s and stable surface identifiers are maintained from `config.yaml` via `src/biology/toc.py` and `scripts/sync_curriculum_materials.py`.
- Student-facing navigation, scope tables, reading paths, and concept maps must be generated from `BookToc` marker blocks or written with semantic `\cref{...}` / `\nameref{...}` references; do not hand-author visible "Unit I", "Appendix C", "Chapter 7", or "Figure FM-1" prose
- Use informative source titles without manual numeric prefixes. Synchronization is not a substitute for content-specific editorial titles; preserve literal headings inside protected examples/comments.
- Inline Mermaid fences must include one descriptive `<!-- alt: ... -->` comment and one italic caption; PDF rendering converts them to PNGs under `output/figures/mermaid_inline/`
- Every chapter carries a `<!-- chapter-metadata-badge -->` blockquote
- Every lab and question bank `\cref`-links back to its parent chapter
- Lab and question-bank entries in `config.yaml` store only `file:` names; do not add duplicated `title:` strings there
- Every documented natbib cite command resolves to an entry in `references.bib`; no entry is orphaned
- Required labs supply finite printed datasets/tasks with explicit criteria and provenance. Solutions are prompt-specific authored content; unsupported answer generation refuses without writing. Preserve semantic LO/Bloom mappings and rubrics.
- [The testing guide](../testing_guide.md) owns named invariant tests and their limits; structural passes do not establish empirical accuracy or accessibility.

## Course pathways

- **One semester (survey)**: Unit 0 (select sections) + Units I–III + Units IV–V + chosen Unit X chapters.
- **Two semesters**: Semester 1: Units I–V; Semester 2: Units VI–X (plus Unit 0 as orientation if desired).
- **Pre-health / majors**: Add Units VII–IX and use appendix labs for quantitative drills; see `front_matter.md` → “Suggested reading paths”.
- **Current source typography**: 2 mm margins, 9 pt body and 1.28 line spacing; not a readable-print finding. Inspect actual output and change config.yaml plus preamble.md together.
- **Reader / large-type build** (optional): larger margins and body size in the same paired edit; start from [../docs/accessibility.md](../accessibility.md#reader--large-type-profile-optional).

## Front matter

| File | Role |
| ---- | ---- |
| `front_matter.md` | Dedication, acknowledgements, generated navigation, generated reading paths, generated concept map, and textbook-use notes after the ToC |
| `preface.md` | Preface plus generated scope table |

The PDF opening itself is generated from `config.yaml`: page 1 cover, page 2
publishing information, page 3 Contents. Files listed under
`config.yaml` → `front_matter.files[]` render after the ToC.

## Unit map (core chapters only)

Counts are **body chapters** per `config.yaml` (excluding labs/questions appendices).

| Unit | Title | Chapters |
| ---- | ----- | -------- |
| 0 | Systems Science for Biology | 4 |
| I | Chemistry of Life | 4 |
| II | The Cell | 4 |
| III | Energy and Metabolism | 3 |
| IV | Molecular Genetics | 5 |
| V | Classical Genetics and Heredity | 4 |
| VI | Evolution | 3 |
| VII | Microbiology | 4 |
| VIII | Botany — Plant Biology | 3 |
| IX | Zoology and Systems Physiology | 5 |
| X | Ecology | 5 |
| **Total** | | **44** |

See `AGENTS.md` for naming conventions, figure rules, and contribution notes.
