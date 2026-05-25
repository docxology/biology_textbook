# Biology Textbook — Tests

**Domain, visualization, and manuscript-invariant suites · zero mocks.** Run `pytest` from this active project directory for the current test count and line coverage; the tree currently ships **51** `test_*.py` files + `conftest.py` — run `uv run python -m pytest tests/ -q` for the current collected count; `pyproject.toml` enforces a **90 %** gate on `src/`.

## Running

From this project directory:

```bash
uv run python -m pytest tests/ -v
uv run python -m pytest tests/ --cov=src --cov-report=html --cov-fail-under=90
```

`conftest.py` sets `MPLBACKEND=Agg` and calls `textbook_paths.ensure_project_paths(include_scripts=True)` so `src/`, `scripts/`, and the template root resolve on `sys.path`.

## Config vs tests

- **`manuscript/config.yaml`**: drives layout, ordering, front matter, appendices, and **declares** policies (e.g. `accessibility.*`, `content_notes`, `export`). Not every key is consumed by a script. **Authoritative table:** [docs/accessibility.md](../docs/accessibility.md).
- **Invariant tests** (this directory) are the main **mechanical** enforcement for alt text, labels, metadata, closure, and cross-refs. Do not assume the PDF build fails on YAML alone for alt text; see `test_accessibility.py`.

## Layout

**51** `test_*.py` files: **7** domain modules (exercising `src/biology/*`, mermaid, visualization) + **44** invariant / render-quality / script-quality / bootstrap modules. Plus `conftest.py` (fixtures and path bootstrap, not a test module). Run `uv run python -m pytest tests/ -q` for the current collected count.

### Domain tests (6 `test_*.py` + `conftest.py`)

| File | Focus |
| ---- | ----- |
| `test_cell_biology.py` | Organelles, Nernst/Goldman, transport, signaling |
| `test_genetics.py` | DNA/RNA, Punnett, Hardy–Weinberg, related |
| `test_ecology_evolution_physiology_biochemistry.py` | Cross-domain quantitative models |
| `test_microbiology_botany_neuroscience.py` | Growth, plants, neural models |
| `test_mermaid_and_visualization.py` | Renderer and figure generators |
| `test_coverage_gap.py` | Branches, edge cases, and error paths |
| `conftest.py` | `MPLBACKEND=Agg`, `ensure_project_paths()` bootstrap |

### Invariant and quality tests (31 modules)

| File | Focus |
| ---- | ----- |
| `test_atomic_io.py` | Atomic write/replace helpers used by maintenance scripts |
| `test_audit_v3_and_crossref_gate.py` | Generic-answer v3 and malformed `\cref` detector regressions |
| `test_build_invariants.py` | Chapter labels, metadata badges, lab/question back-links, figure-generator usage, Course Planning Grid |
| `test_bibliography_closure.py` | `{cited} == {defined}` in `references.bib`; no mid-word citation artifacts |
| `test_chapter_metadata.py` | `ChapterMeta` completeness and consistency vs `config.yaml` |
| `test_chapter_pedagogy_coverage.py` | REVIEW §7 pedagogy locks: worked examples, Concept Checks, Bloom diversity, LO floor |
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
| `test_logging_compat.py` | Logging helper compatibility across checkout layouts |
| `test_maintenance_engine_smoke.py` | Smoke imports for extracted maintenance engines under `src/biology/` |
| `test_pdf_log_quality.py` | PDF-log checker catches undefined references and severe overfull boxes |
| `test_pdf_opening_and_mermaid.py` | Book opening metadata, cover asset, and inline Mermaid rendering |
| `test_question_answer_refinement.py` | Generated-answer heuristics classify quantitative questions and preserve hand-written answers |
| `test_script_quality.py` | Scripts parse cleanly and avoid hard-coded checkout paths or obsolete helpers |
| `test_textbook_paths.py` | Checkout path discovery and `ensure_project_paths()` bootstrap |
| `test_textbook_quality_audit.py` | Umbrella textbook-quality audit: stale claims, copyedit artifacts, enrichment presence, and current-source locks |

No mocks for scientific behavior — real numeric data and file output only.

See [docs/testing_guide.md](../docs/testing_guide.md) for policy detail.
