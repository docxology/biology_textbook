# Biology Textbook — Manuscript

## Manuscript Source Map

All Markdown sources for the book. PDF/HTML output is produced by the template rendering pipeline (Pandoc/LaTeX) after analysis injects ordered files into `output/manuscript/`. **Chapter order and numbering** come only from **`config.yaml`** — filenames are descriptive slugs, not chapter indices.

Rendering through the template pipeline uses `infrastructure.project.discovery.resolve_project_root` with `--project biology_textbook` when template infrastructure is available. Project-local authoring, tests, and maintenance scripts should run from this active checkout.

## Quick reference

| Action | Where / command |
| ------ | ----------------- |
| Source repository | [biology textbook source repository](https://github.com/docxology/biology_textbook) |
| Archival DOI | [Zenodo archival DOI record](https://doi.org/10.5281/zenodo.20286478) |
| End-to-end add chapter / figure / labels | [../docs/composable_authoring.md](../docs/composable_authoring.md) (checklists + tests) |
| View chapter order | `config.yaml` → `units[]` and `appendices` |
| Add a chapter | Create `unit_<id>/<slug>.md`; add `chapters[]` entry; add `ChapterMeta(…)` in `../src/biology/chapter_metadata.py` |
| Toggle labs / questions | `config.yaml` → `appendices.include_labs`, `include_questions` |
| Reference appendices | `appendices/` plus root `glossary.md`; rendered when `config.yaml` → `appendices.include_reference` is true, with titles and order from `appendices.reference[]` |
| Author / ORCID | `config.yaml` → `book`, `authors[]` |
| Cover image | `config.yaml` → `book.cover.image`; regenerate with `uv run python scripts/generate_cover_art.py` |
| Margins / body size | `config.yaml` → `layout.margin_*_mm`, `typography.base_font_size_pt`, `layout.line_height` **and** the matching `geometry`, `\normalsize`, `\setstretch` block in `preamble.md` |
| Link colour | `config.yaml` → `typography.link_color` |
| Toggle front matter | `config.yaml` → `front_matter.include_front_matter` |
| Navigation / scope blocks | `front_matter.md` and `preface.md` generated markers — edit `config.yaml`, then rerun `uv run python scripts/sync_curriculum_materials.py` |
| Course Planning Grid | Auto-generated in `front_matter.md` between `<!-- course-planning-grid-start -->` and `<!-- course-planning-grid-end -->` markers — edit `config.yaml` titles/order and `../src/biology/chapter_metadata.py`, then rerun `../scripts/insert_chapter_metadata.py` |
| Glossary | `glossary.md` — each term is a bracketed span `` [**Term**]{#gl:<slug>} `` (PDF ``\label{gl:…}``); link on first use with `` `[**term**](#gl:<slug>)` `` |
| Generate figures | From project root: `uv run python scripts/generate_figures.py` (32 square-padded matplotlib; uses `src/visualization/cvd.py` for CVD-friendly colours) |
| Accessibility, config vs tests | [../docs/accessibility.md](../docs/accessibility.md) |
| Generate registered Mermaid PNGs | `uv run python scripts/generate_diagrams.py --strict-png` for publication checks (24 registry diagrams); the 193 inline Mermaid fences render during PDF preprocessing |
| Check current claims | `uv run python scripts/audit_current_claims.py --check`; source data lives in `current_claims.yaml` |
| Check assessment metadata | `uv run python scripts/sync_assessment_metadata.py --dry-run` to preview drift; `uv run python scripts/sync_assessment_metadata.py --check` gates question items and lab alignment |
| Render PDF | From repo root: `uv run python scripts/03_render_pdf.py --project biology_textbook` |

After large bibliography or glossary edits, refresh any documented counts with `rg -c '^@' manuscript/references.bib` (BibTeX entry count) and `rg '{#gl:' manuscript/glossary.md | wc -l` (glossary lines with bracketed-span anchors).

## Manuscript-wide conventions

- Every chapter H1 is followed by `\label{sec:unit_X_<stem>}` — reference with `\cref{sec:unit_X_<stem>}`
- Every unit intro H1 is followed by a stable `\label{sec:unit_X_unit_intro}` — reference visible unit names with `\nameref{sec:unit_X_unit_intro}`
- Renderable H1s for chapters, unit intros, labs, question banks, reference appendices, and the glossary are normalized from `config.yaml` by `../src/biology/toc.py` and `../scripts/sync_curriculum_materials.py`
- Student-facing navigation, scope tables, reading paths, and concept maps must be generated from `BookToc` marker blocks or written with semantic `\cref{...}` / `\nameref{...}` references; do not hand-author visible "Unit I", "Appendix C", "Chapter 7", or "Figure FM-1" prose
- Do not hand-number Markdown headings (`## 1 ...`, `### 1.1 ...`); `../scripts/sync_curriculum_materials.py` strips manual prefixes and applies unnumbered attributes to non-chapter materials for a clean detailed ToC
- Inline Mermaid fences must include one descriptive `<!-- alt: ... -->` comment and one italic caption; PDF rendering converts them to PNGs under `output/figures/mermaid_inline/`
- Every chapter carries a `<!-- chapter-metadata-badge -->` blockquote
- Every lab and question bank `\cref`-links back to its parent chapter
- Lab and question-bank entries in `config.yaml` store only `file:` names; do not add duplicated `title:` strings there
- Every `\citep{…}` / `\citet{…}` resolves to an entry in `references.bib`; no entry is orphaned
- All invariants are asserted by `../tests/test_toc_consistency.py`, `../tests/test_build_invariants.py`, `../tests/test_bibliography_closure.py`, `../tests/test_chapter_metadata.py`, `../tests/test_curriculum_metadata.py`, `../tests/test_accessibility.py`, `../tests/test_crossref_validator*.py`, `../tests/test_lab_integrity.py`, `../tests/test_question_answer_refinement.py`, `../tests/test_chapter_pedagogy_coverage.py`, and `../tests/test_script_quality.py`

## Course pathways

- **One semester (survey)**: Unit 0 (select sections) + Units I–III + Units IV–V + chosen Unit X chapters.
- **Two semesters**: Semester 1: Units I–V; Semester 2: Units VI–X (plus Unit 0 as orientation if desired).
- **Pre-health / majors**: Add Units VII–IX and use appendix labs for quantitative drills; see `front_matter.md` → “Suggested reading paths”.
- **Default PDF layout**: 2 mm margins, 9 pt body, 1.28 line spacing (compact print); adjust in `config.yaml` + `preamble.md` together.
- **Reader / large-type build** (optional): larger margins and body size in the same paired edit; start from [../docs/accessibility.md](../docs/accessibility.md#reader--large-type-profile-optional).

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
| 0 | Systems Science and the Biology of Complexity | 4 |
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
