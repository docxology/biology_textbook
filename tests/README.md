# Biology Textbook — Tests

**Domain, visualization, and manuscript-invariant suites · zero mocks.** Run `pytest` from this project directory (`projects_in_progress/biology_textbook/` in this checkout, or `projects/biology_textbook/` after promotion) for the current test count and line coverage; `pyproject.toml` enforces a **90 %** gate on `src/`.

## Running

From this project directory:

```bash
uv run pytest tests/ -v
uv run pytest tests/ --cov=src --cov-report=html --cov-fail-under=90
```

`conftest.py` sets `MPLBACKEND=Agg` and adds `src/` plus the template root to `sys.path` so `infrastructure.*` imports resolve.

## Config vs tests

- **`manuscript/config.yaml`**: drives layout, ordering, front matter, appendices, and **declares** policies (e.g. `accessibility.*`, `content_notes`, `export`). Not every key is consumed by a script. **Authoritative table:** [docs/accessibility.md](../docs/accessibility.md).
- **Invariant tests** (this directory) are the main **mechanical** enforcement for alt text, labels, metadata, closure, and cross-refs. Do not assume the PDF build fails on YAML alone for alt text; see `test_accessibility.py`.

## Layout

**27** `test_*.py` files: **6** domain modules (exercising `src/biology/*`, mermaid, visualization) + **21** invariant / render-quality / script-quality modules (`test_accessibility.py` includes alt-text quality, unit chapters, labs, and questions). Plus `conftest.py` (fixtures and `sys.path`, not a test module). Run `uv run pytest tests/ -q` for the current collected count.

### Domain tests (6 `test_*.py` + `conftest.py`)

| File | Focus |
| ---- | ----- |
| `test_cell_biology.py` | Organelles, Nernst/Goldman, transport, signalling |
| `test_genetics.py` | DNA/RNA, Punnett, Hardy–Weinberg, related |
| `test_ecology_evolution_physiology_biochemistry.py` | Cross-domain quantitative models |
| `test_microbiology_botany_neuroscience.py` | Growth, plants, neural models |
| `test_mermaid_and_visualization.py` | Renderer and figure generators |
| `test_coverage_gap.py` | Branches, edge cases, and error paths |
| `conftest.py` | `MPLBACKEND=Agg`, `sys.path` bootstrap |

### Invariant and quality tests (21 files)

| File | Focus |
| ---- | ----- |
| `test_atomic_io.py` | Atomic write/replace helpers used by maintenance scripts |
| `test_audit_v3_and_crossref_gate.py` | Generic-answer v3 and malformed `\cref` detector regressions |
| `test_build_invariants.py` | Chapter labels, metadata badges, lab/question back-links, figure-generator usage, Course Planning Grid |
| `test_bibliography_closure.py` | `{cited} == {defined}` in `references.bib`; no mid-word citation artefacts |
| `test_chapter_metadata.py` | `ChapterMeta` completeness and consistency vs `config.yaml` |
| `test_curriculum_metadata.py` | `CurriculumRecord` completeness and chapter/lab/question path closure |
| `test_current_claims_ledger.py` | Fast-moving current-claim ledger coverage, sources, anchors, and stale-phrase locks |
| `test_assessment_metadata.py` | Item-level LO, Bloom, difficulty, format, and minutes metadata across all question banks |
| `test_lab_pedagogy_alignment.py` | Lab outcome, LO-coverage, and rubric-dimension metadata checks |
| `test_toc_consistency.py` | Canonical H1s, front-matter navigation, reference appendices, and no duplicated lab/question titles |
| `test_accessibility.py` | Alt `<!-- ... -->` quality; LaTeX figure proximity; inline Mermaid exact-one alt/comment caption contract |
| `test_crossref_validator.py` | Top-level: 0 unresolved / 0 duplicates; cleveref loaded |
| `test_crossref_validator_internals.py` | Parser coverage for `$$…$$`, `\begin{figure}`, `\begin{equation}`, tables, sections, refs |
| `test_crossref_validator_edges.py` | Edge cases (markdown `{#fig:}`, multi-line equations, duplicates across files) |
| `test_lab_integrity.py` | Lab computation sections are self-contained and execute against `biology.*` snippets |
| `test_enrichment_substance_gate.py` | Embedded-enrichment boilerplate and duplicate-body detectors |
| `test_pdf_log_quality.py` | PDF-log checker catches undefined references and severe overfull boxes |
| `test_pdf_opening_and_mermaid.py` | Book opening metadata, cover asset, and inline Mermaid rendering |
| `test_question_answer_refinement.py` | Generated-answer heuristics classify quantitative questions and preserve hand-written answers |
| `test_script_quality.py` | Scripts parse cleanly and avoid hard-coded checkout paths or obsolete helpers |
| `test_textbook_quality_audit.py` | Umbrella textbook-quality audit: stale claims, copyedit artifacts, enrichment presence, and current-source locks |

No mocks for scientific behaviour — real numeric data and file output only.

See [docs/testing_guide.md](../docs/testing_guide.md) for policy detail.
