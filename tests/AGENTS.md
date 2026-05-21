# Tests — AGENTS.md

## Role

`pytest` suite for both `src/` computation and manuscript-level invariants. Enforces the **no-mocks** policy for scientific code (real numerics, real files, optional real `mmdc` when present) and additionally asserts manuscript-quality gates (canonical ToC surfaces, labels, badges, lab/question back-links, figure coverage, bibliography closure) as first-class tests.

Coverage and test count change with the suite; run with `--cov=src` to see current line coverage on `src/`. The project enforces **90 %** minimum via `pyproject.toml`.

## Running

```bash
cd projects_in_progress/biology_textbook
uv run pytest tests/ --cov=src --cov-fail-under=90
```

## Files

**27** `test_*.py` files + `conftest.py` — see [../docs/testing_guide.md](../docs/testing_guide.md#test-organisation) for the same split.

### Domain tests (6 modules + conftest)

| Module | Scope |
| ------ | ----- |
| `conftest.py` | `MPLBACKEND=Agg`; `sys.path` for `src/` and template root |
| `test_cell_biology.py` | Membrane biophysics, organelles, signalling helpers |
| `test_genetics.py` | DNA/RNA, crosses, population genetics |
| `test_ecology_evolution_physiology_biochemistry.py` | Multi-domain models |
| `test_microbiology_botany_neuroscience.py` | Growth, plants, neurons |
| `test_mermaid_and_visualization.py` | Diagram renderer and PNG outputs |
| `test_coverage_gap.py` | Error paths and low-coverage branches |

### Invariant and quality tests (21)

| Module | Scope |
| ------ | ----- |
| `test_atomic_io.py` | Atomic write/replace helpers used by maintenance scripts |
| `test_audit_v3_and_crossref_gate.py` | Generic-answer v3 and malformed `\cref` detector regressions |
| `test_build_invariants.py` | End-to-end structural locks: every chapter has `\label{sec:…}` and a metadata badge; every lab/question `\cref`-links to its parent; every registered figure generator is referenced; Course Planning Grid populated |
| `test_bibliography_closure.py` | `{cited} == {defined}` in `references.bib` — no orphans, no dangling, no mid-word citation artefacts |
| `test_chapter_metadata.py` | Every `config.yaml` chapter has a `ChapterMeta` record; prerequisites resolve; difficulty ∈ {1, 2, 3}; chapter numbers contiguous; `by_id` / `by_unit` lookups |
| `test_curriculum_metadata.py` | Every `config.yaml` chapter has a `CurriculumRecord`; lab/question paths exist and align to curriculum metadata |
| `test_current_claims_ledger.py` | `manuscript/current_claims.yaml` has source tiers, checked dates, refresh triggers, anchors, and stale-phrase coverage |
| `test_assessment_metadata.py` | Every question-bank item has LO/Bloom/difficulty/format/minutes metadata |
| `test_lab_pedagogy_alignment.py` | Every lab maps to measurable outcomes, chapter LOs, and rubric dimensions |
| `test_toc_consistency.py` | Renderable H1s, front-matter navigation, reference appendices, and Course Planning Grid titles match `biology.toc`; lab/question config entries do not duplicate derived titles |
| `test_accessibility.py` | LaTeX figures have nearby alt text; inline Mermaid has one alt comment and one italic caption per [../manuscript/AGENTS.md](../manuscript/AGENTS.md) |
| `test_crossref_validator.py` | Top-level: 0 unresolved refs, 0 duplicates, cleveref loaded in preamble, slug helper correct, config chapter count matches preface |
| `test_crossref_validator_internals.py` | Parser coverage: `$$…$$`, `\begin{figure}`, `\begin{equation}`, table captions, section labels, prose xref detection, @ref collection, duplicate detection across files |
| `test_crossref_validator_edges.py` | Edge cases: markdown images with `{#fig:}` attrs, block equations with id on following line, duplicate fig ids within a file, missing-file graceful handling |
| `test_lab_integrity.py` | Lab computation sections are self-contained and executable against `src/biology` |
| `test_enrichment_substance_gate.py` | Embedded-enrichment boilerplate and duplicate-body detectors |
| `test_pdf_log_quality.py` | PDF-log checker catches undefined references and severe overfull boxes |
| `test_pdf_opening_and_mermaid.py` | Book opening, cover asset, and inline Mermaid rendering contracts |
| `test_question_answer_refinement.py` | Generated answer refinement remains idempotent and preserves hand-written answers |
| `test_script_quality.py` | Scripts parse cleanly and avoid hard-coded local checkout paths or obsolete clones |
| `test_textbook_quality_audit.py` | Umbrella textbook-quality audit: stale claims, copyedit artifacts, enrichment presence, and current-source locks |

## Conventions

- Add tests next to the domain they exercise; use `test_coverage_gap.py` only for scattered edge cases.
- Do not import `unittest.mock` for behaviour verification.
- Dynamically loading modules outside the `biology` package (e.g. `crossref_validator`, `chapter_metadata` for tests): register in `sys.modules` before `spec.loader.exec_module(…)` so `@dataclass` can resolve its module context.

See [../docs/testing_guide.md](../docs/testing_guide.md) and [../docs/composable_authoring.md](../docs/composable_authoring.md) (when to run invariant tests after manuscript changes).
