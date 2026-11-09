# Testing Guide

> [!NOTE]
> **See also:** [composable_authoring.md](composable_authoring.md) for the workflow context, [manuscript_guide.md](manuscript_guide.md) for the patterns these tests enforce, and [pipeline_guide.md](pipeline_guide.md) for where tests sit in the build.

---

## Table of contents

- [Zero-mock policy](#zero-mock-policy)
- [Running tests](#running-tests)
- [Coverage standards](#coverage-standards)
- [Test organization](#test-organization)
- [Authoring mistake → test → fix (consolidated)](#authoring-mistake--test--fix-consolidated)
- [Failure-to-fix table](#failure-to-fix-table)
- [Writing new tests](#writing-new-tests)
- [Common patterns for difficult tests](#common-patterns-for-difficult-tests)

---

## Zero-mock policy

> [!IMPORTANT]
> Test scientific computations with real algorithms and explicit inputs, not mocked biological answers. Synthetic fixtures and seeded simulations are not empirical data.

“Zero-mock” is a policy goal, not a literal inventory assertion. Existing pytest monkeypatch use isolates temporary paths, environment/imports and targeted I/O failures, including atomic replacement failures. Such tests prove isolation/failure handling, not native-tool success. Native Mermaid/PDF tests exercise real tools and may skip when unavailable; skips are verification gaps, not publication passes. Use real temporary files and fixed RNG seeds. Publication requires actual PNG decoding and PDF rendering; see [pipeline_guide.md](pipeline_guide.md).

Shared Euler regressions include rounded subnormal grids that would otherwise repeat a timestamp or integrate a different horizon, alongside representable subnormal and ordinary constant-rate controls. These validate fixed-step geometry, not general accuracy or adaptive-step behavior. Plot and native PDF regressions use real files to check source-alias preservation, prior-artifact retention and failed-workspace evidence. A deliberately failing compiler fixture tests failure custody, not successful book compilation; the integrated full gate remains separate.

---

## Running tests

> [!IMPORTANT]
> Run from this checkout after uv sync --frozen --extra dev. Use project-local commands; the selected template is a read-only library. Full release proof is scripts/audit_publication_readiness.py --check --full.

```bash
# Full suite, verbose
uv run python -m pytest tests/ -v

# Full suite with coverage report (HTML)
uv run python -m pytest tests/ --cov=src --cov-report=html
open htmlcov/index.html

# Coverage with terminal-missing breakdown
uv run python -m pytest tests/ --cov=src --cov-report=term-missing

# Run a single test file
uv run python -m pytest tests/test_cell_biology.py -v

# Run a single test function
uv run python -m pytest tests/test_genetics_mendelian.py::TestPunnettSquare::test_monohybrid_Aa_x_Aa_genotype_ratios -v

# Run all tests matching a name pattern
uv run python -m pytest tests/ -k "punnett" -v

# Run a specific invariant
uv run python -m pytest tests/test_build_invariants.py::test_every_chapter_has_section_label -v

# Stop at first failure (useful for triage)
uv run python -m pytest tests/ -x

# Show local variables on failure
uv run python -m pytest tests/ -l

# Exclude tests explicitly marked slow (this is not a pure-domain selector)
uv run python -m pytest tests/ -m "not slow"
```

> [!TIP]
> When debugging a single invariant, copy the **command** from the [authoring-mistake → test → fix table](#authoring-mistake--test--fix-consolidated) — each row gives the exact `uv run python -m pytest …::test_name -v` line.

---

## Coverage standards

`pyproject.toml` enables branch measurement and sets `fail_under = 90` on the reported overall total, not independent line/branch floors or package minima. Its omit list excludes initializers, catalog/maintenance engines and selected helpers; inspect it when interpreting reports. Passing counts and coverage require fresh execution.

```bash
uv run --frozen --extra dev python -m pytest tests --cov=src --cov-fail-under=90 --cov-report=term-missing -q
uv run --frozen --extra dev python scripts/audit_publication_readiness.py --check --full
```

Default review audits its supplied artifact directory; the CLI owns selection and the module fallback is output/publication_readiness. Full mode includes tests, analysis, fresh render and PDF-log checks under project output. Missing glyphs fail; overfull threshold is 50 pt. A current exact-source full receipt and separate PDF inspection, not this guide, establish the exercised proof.

`tests/test_manuscript_transactions.py` parses actual hydrated Markdown with Pandoc to verify that answer code remains inside its answer while ordinary code and mathematical expressions retain their content. Cases cover code-only, leading, middle and trailing answer code. Native PDF tests separately exercise question-list boundaries and TeX grid width. A passing log threshold alone is not table readability proof: inspect the PDF and distinguish physical page bounds from within-page cell overlap.

Actual PDF navigation must resolve named destinations and link annotations to the intended physical body pages, especially across the Unit 0 section-counter reset. Matching a semantic label to a heading alias in the same `.aux` file can agree on the wrong destination. The native `test_real_pdf_chapter_links_survive_unit_zero_counter_reset` fixture exercises chapters and descendants through collection, injection, numbering, the manuscript preamble and rendering; temporary path redirection is not a mocked renderer. Display numbers, semantic IDs and PDF-internal destination names are distinct contracts.

Question-list AST checks establish source structure only. Reader coverage additionally needs each configured bank's actual PDF extent, numbered prompt and corresponding printed answer in order. Record the matched pages and any missing/ambiguous items; do not call source existence or 1–30 source numbering a printed-flow result. Even complete text/link coverage does not certify every formula, answer's scientific validity, screen-reader order, physical print or PDF/UA conformance.

---

## Test organization

These domain and invariant/quality tables are navigation aids, not a current count or passing-status inventory.

### Domain tests

| Test file | What it covers |
| --------- | -------------- |
| `test_cell_biology.py` | Organelles, Nernst, Goldman, osmotic pressure, diffusion |
| `test_genetics_sequence.py` | Genetic code, transcription, translation, GC content |
| `test_genetics_mendelian.py` | Punnett squares, gametes, diploid genotypes |
| `test_genetics_population.py` | Hardy–Weinberg, χ² goodness-of-fit |
| `test_genetics_linkage.py` | Recombination frequency, map distance, three-point order |
| `test_genetics_distance.py` | Hamming and Jukes–Cantor distances |
| `test_genetics_epigenetics.py` | CpG methylation decay, histone marks, synthetic β matrices |
| `test_genetics_mutation.py` | Mutation-rate spectrum reference data |
| `test_genetics_replication.py` | Replication-fork progression profiles |
| `test_ecology_evolution_physiology_biochemistry.py` | Lotka-Volterra, selection, drift, glycolysis, Michaelis-Menten, Poiseuille |
| `test_microbiology_botany_neuroscience.py` | Bacterial growth, MIC, water potential, Hodgkin-Huxley, synaptic transmission, LTP |
| `test_mermaid_and_visualization.py` | Mermaid renderer, `ALL_BIOLOGY_DIAGRAMS`, matplotlib `ALL_FIGURE_GENERATORS` |
| `test_coverage_gap.py` | Deliberately closes residual branches in existing modules |
| `conftest.py` | `MPLBACKEND=Agg`, `ensure_project_paths()` bootstrap, `COVERAGE_RCFILE` + early cov-config hook for direct pytest |

### Invariant and quality tests

| Test file | What it guards |
| --------- | -------------- |
| `test_atomic_io.py` | Atomic write/replace helpers used by maintenance scripts |
| `test_audit_v3_and_crossref_gate.py` | Generic-answer v3 and malformed `\cref` detector regressions |
| `test_build_invariants.py` | Every chapter has `\label{sec:…}` and a metadata badge; every lab/question `\cref`-links to its parent chapter; every registered figure generator is referenced; every `\label{fig:…}` has prose `\cref`; Course Planning Grid populated |
| `test_bibliography_closure.py` | `{cited}` == `{defined}` plus usable source metadata; duplicate source identities are rejected by the shared parser and consumer diagnostics |
| `test_chapter_metadata.py` | Every `config.yaml` chapter has a `ChapterMeta` record; prerequisites resolve; difficulty ∈ {1, 2, 3}; chapter numbers contiguous 1..N |
| `test_chapter_pedagogy_coverage.py` | REVIEW §7 pedagogy locks: ≥2 worked examples on 12 quantitative chapters, ≥3 Concept Checks on Unit IX + four named chapters, Bloom diversity on three chapters, ≥7 LOs on all core chapters |
| `test_curriculum_metadata.py` | Config/curriculum alignment and real twice-run CLI preservation of authored lab/question bytes, mtimes and inodes |
| `test_current_claims_ledger.py` | Fast-moving claim ledger, source tier, anchor, and stale-phrase checks |
| `test_assessment_metadata.py` | Item-level LO, Bloom, difficulty, format, and minutes metadata across all question banks |
| `test_lab_pedagogy_alignment.py` | Lab outcome, LO-coverage, and rubric-dimension metadata checks |
| `test_toc_consistency.py` | Renderable H1s, front-matter navigation, reference appendix headings, and Course Planning Grid titles match `biology.toc`; lab/question config entries avoid duplicated titles |
| `test_accessibility.py` | Alt-text substance/proximity and exactly one substantive alt comment plus caption per inline Mermaid block; these heuristics do not certify accessible output |
| `test_crossref_validator.py` | Top-level invariant: no unresolved `@fig:`/`@eq:`/`@tbl:`/`@sec:` refs, no duplicate labels, `cleveref` loaded in preamble |
| `test_crossref_validator_internals.py` | Parser coverage: `$$…$$`, `\begin{figure}`, `\begin{equation}`, table captions, section labels, prose xrefs |
| `test_crossref_validator_edges.py` | Edge cases: markdown images with `{#fig:}` attrs, block equations with id on following line, duplicate labels across files |
| `test_lab_integrity.py` | Hidden notebook/data-file rejection, module-link resolution and optional Python snippet execution under the test's selected scope |
| `test_enrichment_substance_gate.py` | Embedded-enrichment boilerplate and duplicate-body detectors |
| `test_logging_compat.py` | Logging helper compatibility across checkout layouts |
| `test_maintenance_engine_smoke.py` | Smoke imports for extracted maintenance engines under `src/biology/` |
| `test_pdf_log_quality.py` | PDF-log checker reports undefined references and severe overfull boxes above the configured threshold |
| `test_pdf_opening_and_mermaid.py` | Real native PDFs for cover/opening, rich inline captions and Mermaid; actual chapter/descendant destination routing across Unit 0, Pandoc question/answer hierarchy and TeX course-grid width |
| `test_question_answer_refinement.py` | Preserve authored answers; reject unsupported automatic repair without writes |
| `test_script_quality.py` | Mermaid metadata normalization and assessment dry-run nonwriting behavior |
| `test_textbook_paths.py` | Checkout path discovery, `ensure_project_paths()`, and template-root resolution |
| `test_textbook_quality_audit.py` | Umbrella textbook-quality audit: stale claims, copyedit artifacts, enrichment presence, and current-source locks |
| `test_publication_gate.py` | Publication gate step graph, dependency ordering, and parallel worker invariants |
| `test_release_asset_boundaries.py` | Real independent fixture export, exact frozen-renderer membership, source/artifact binding, output aliases/overlap and occupied-destination preservation; fixtures are not full-render evidence |
| `test_american_english.py` | American English spelling gate for manuscript and docs |
| `test_answer_refinement_modules.py` | Answer classification and unsupported-generation refusal |
| `test_answer_scaffolds.py` | Nonwriting refusal for missing authored answers |
| `test_assessment_sync.py` | Preserve curated semantic mappings; reject authoring gaps |
| `test_chapter_badges.py` | Badge and course-grid idempotence; dry-run and applied regeneration preserve unrelated authored bytes, mtimes/inodes and single page breaks |
| `test_chapter_shells.py` | `biology.maintenance.chapter_shells` chapter-shell repair |
| `test_citations.py` | Shared natbib citation parsing helpers |
| `test_cover_art.py` | Cover art generation |
| `test_crossref_label_insertion.py` | `biology.crossref.label_insertion` section-label insertion |
| `test_diagram_spec_loader.py` | Declarative Mermaid diagram specs (`diagram_specs.yaml`) |
| `test_enrichment_catalog_loader.py` | Enrichment catalog YAML loader |
| `test_foundations.py` | `biology.foundations` and related domain helpers |
| `test_further_reading.py` | `biology.maintenance.further_reading` maintenance |
| `test_glossary_cards.py` | Glossary card parsing |
| `test_glossary_first_use.py` | First-use glossary linking |
| `test_lab_padding.py` | Short-lab debrief padding |
| `test_lab_workflows.py` | Lab computational workflow normalization |
| `test_manuscript_spans.py` | Protected-span scanning |
| `test_numerics.py` | Shared numerical integration helpers |
| `test_orphan_citations.py` | Orphan citation YAML loader |
| `test_orphan_figures.py` | `biology.pipeline.orphan_figures` |
| `test_parent_chapter_links.py` | Parent-chapter cross-reference insertion |
| `test_pipeline.py` | `biology.pipeline` manuscript injection and numbering |
| `test_solution_scaffolds.py` | `biology.answer_refinement.solution_scaffolds` |
| `test_table_captions.py` | Table caption annotation helpers |
| `test_text_normalize.py` | Shared Mermaid metadata normalization |
| `test_textbook_io.py` | Shared `textbook_io` helpers |
| `test_textbook_visuals.py` | Shared figure post-processing helpers |
| `test_typography.py` | Manuscript typography normalization |
| `test_visual_contracts_audit.py` | Visual contract audit helpers and `check_records` branches |

### Textbook quality audit

`test_textbook_quality_audit.py` requires zero blocking findings and zero outstanding advisories. Source-bound, individually justified scientific absolutes may remain reviewed. Untriaged, unresolved, mismatched or stale entries fail; see [the triage contract](absolute_language_triage.md). Blocking findings also include generic answer-key templates,
`Expected reasoning:` scaffolds from earlier generated answers, stale WHO
or AMR burden language, required wet-lab wording, hard-coded rendered
references, weak Mermaid metadata, dangling glossary links, and bibliography
closure failures. It also blocks copyediting artifacts from prior broad cleanup
passes, such as uppercase `MOST`, `Not most`, and awkward `primarily` quantifier
phrases. It also requires the embedded-enrichment audit matrix,
chapter frontier boxes, unit evidence threads, and paper-based lab evidence
upgrade sections introduced by `scripts/enrich_embedded_textbook.py`.

---

## Authoring mistake → test → fix (consolidated)

Use this table when pytest fails. Each row gives the **specific authoring mistake**, the **specific test that catches it**, the **single-test command** for fast iteration, and the **fix** (often an idempotent script).

| # | Authoring mistake | Test name | Single-test command | How to fix |
| - | ----------------- | --------- | ------------------- | ---------- |
| 1 | Forgot `\label{sec:unit_X_<stem>}` after a chapter's H1 | `test_every_chapter_has_section_label` | `uv run python -m pytest tests/test_build_invariants.py::test_every_chapter_has_section_label -v` | Run `scripts/insert_crossref_labels.py` (idempotent) |
| 2 | Missing or stale canonical metadata badge | `test_chapter_badges_match_canonical_format` | `uv run python -m pytest tests/test_toc_consistency.py::test_chapter_badges_match_canonical_format -v` | Run `scripts/insert_chapter_metadata.py` (requires matching `ChapterMeta`) |
| 3 | Lab file is missing `\cref{sec:...}` to its parent chapter | `test_every_lab_links_to_parent_chapter` | `uv run python -m pytest tests/test_build_invariants.py::test_every_lab_links_to_parent_chapter -v` | Run `scripts/link_labs_to_chapters.py` |
| 4 | Question bank is missing `\cref{sec:...}` to its parent chapter | `test_every_question_links_to_parent_chapter` | `uv run python -m pytest tests/test_build_invariants.py::test_every_question_links_to_parent_chapter -v` | Run `scripts/link_labs_to_chapters.py` |
| 5 | Registered `plot_*` never referenced from any chapter | `test_every_registered_figure_is_referenced` | `uv run python -m pytest tests/test_build_invariants.py::test_every_registered_figure_is_referenced -v` | Add a `\begin{figure}...\end{figure}` block (use `scripts/insert_orphan_figures.py --dry-run` to scaffold) |
| 5b | Figure `\label{fig:…}` without prose `\cref{fig:…}` | `test_every_figure_label_has_prose_cref` | `uv run python -m pytest tests/test_build_invariants.py::test_every_figure_label_has_prose_cref -v` | Weave `\cref{fig:…}` into teaching prose in the same chapter (REVIEW §8 standard) |
| 6 | Front-matter Course Planning Grid empty / stale | `test_course_planning_grid_populated` | `uv run python -m pytest tests/test_build_invariants.py::test_course_planning_grid_populated -v` | Re-run `scripts/insert_chapter_metadata.py` |
| 6a | A chapter, unit intro, lab, question bank, reference appendix, or glossary H1 drifts from `config.yaml` | `test_renderable_h1s_match_canonical_toc` | `uv run python -m pytest tests/test_toc_consistency.py::test_renderable_h1s_match_canonical_toc -v` | Run `scripts/sync_curriculum_materials.py` |
| 6b | Lab/question entries duplicate derived `title:` strings in `config.yaml` | `test_lab_and_question_config_entries_do_not_duplicate_titles` | `uv run python -m pytest tests/test_toc_consistency.py::test_lab_and_question_config_entries_do_not_duplicate_titles -v` | Delete the duplicated `title:` keys; keep only `file:` |
| 7 | Citekey in chapter not present in `references.bib` | `test_no_dangling_citations` | `uv run python -m pytest tests/test_bibliography_closure.py::test_no_dangling_citations -v` | Add the BibTeX entry to `references.bib` (`@article{...}`) |
| 8 | BibTeX entry never cited | `test_no_orphan_bibentries` | `uv run python -m pytest tests/test_bibliography_closure.py::test_no_orphan_bibentries -v` | Cite it in the most relevant chapter, or run `scripts/integrate_orphan_citations.py` |
| 9 | `\cite{}` glued to a word (`...as\citep{x}shows...`) | `test_no_midword_citation_artifacts` | `uv run python -m pytest tests/test_bibliography_closure.py::test_no_midword_citation_artifacts -v` | Add a space before/after the `\citep{}` |
| 10 | `ChapterMeta` missing for a chapter listed in `config.yaml` | `test_every_config_chapter_has_metadata` | `uv run python -m pytest tests/test_chapter_metadata.py::test_every_config_chapter_has_metadata -v` | Add a `ChapterMeta(...)` record to `src/biology/chapter_metadata.py` |
| 11 | `ChapterMeta.prerequisites` references unknown `chapter_id` | `test_prerequisites_refer_to_defined_chapters` | `uv run python -m pytest tests/test_chapter_metadata.py::test_prerequisites_refer_to_defined_chapters -v` | Fix typo or supply missing metadata; resolution does not prove acyclicity |
| 12 | Difficulty out of {1, 2, 3} | `test_difficulty_in_range` | `uv run python -m pytest tests/test_chapter_metadata.py::test_difficulty_in_range -v` | Set difficulty to 1, 2, or 3; rendered badges display Level 1/3 through Level 3/3 |
| 13 | Chapter numbers non-contiguous | `test_chapter_numbers_contiguous` | `uv run python -m pytest tests/test_chapter_metadata.py::test_chapter_numbers_contiguous -v` | Renumber `ChapterMeta(..., number=N, ...)` to be contiguous 1..N |
| 14 | Figure has no `<!-- alt: ... -->` immediately after `\end{figure}` | `test_every_latex_figure_has_alt_nearby` | `uv run python -m pytest tests/test_accessibility.py::test_every_latex_figure_has_alt_nearby -v` | Add `<!-- alt: ... -->` comment immediately after `\end{figure}` |
| 15 | Mermaid block has missing, duplicate, or stale metadata | `test_every_mermaid_block_has_exactly_one_alt_and_caption` | `uv run python -m pytest tests/test_accessibility.py::test_every_mermaid_block_has_exactly_one_alt_and_caption -v` | Add one `<!-- alt: ... -->` comment and one italic caption, or run `scripts/add_mermaid_alt_text.py` |
| 16 | Alt text is too short / generic ("Figure 4", "graph") | `test_alt_text_body_is_substantive` | `uv run python -m pytest tests/test_accessibility.py::test_alt_text_body_is_substantive -v` | Rewrite to describe actual axes, trend and salient features |
| 17 | `@fig:foo` referenced but no `{#fig:foo}` defined | `test_no_unresolved_crossrefs` | `uv run python -m pytest tests/test_crossref_validator.py::test_no_unresolved_crossrefs -v` | Define the label or fix the reference typo |
| 18 | Same `\label{fig:foo}` defined in two files | `test_no_duplicate_labels` | `uv run python -m pytest tests/test_crossref_validator.py::test_no_duplicate_labels -v` | Make the label globally unique (use the `unit_X_<descriptor>` convention) |
| 19 | `cleveref` missing from preamble | `test_cleveref_loaded_in_preamble` | `uv run python -m pytest tests/test_crossref_validator.py::test_cleveref_loaded_in_preamble -v` | Add `\usepackage{cleveref}` to `docs/manuscript/preamble.md` after `hyperref` |
| 20 | Manual equation numbering in renderable manuscript prose | `test_latex_equation_environment_with_tag_is_flagged` | `uv run python -m pytest tests/test_crossref_validator_internals.py::test_latex_equation_environment_with_tag_is_flagged -v` | Use a labeled `equation` or `align` environment; let LaTeX assign the rendered number (see [manuscript_guide.md#equations](manuscript_guide.md#equations)) |
| 21 | Markdown image with `{#fig:...}` attribute parses incorrectly | `test_markdown_image_attrs` | `uv run python -m pytest tests/test_crossref_validator_edges.py::test_markdown_image_attrs -v` | Check syntax: `![alt](<path>){#fig:label}` (no space before `{`; `<path>` is a placeholder, not a link) |
| 22 | Lab references a hidden notebook or data file | `test_labs_do_not_reference_hidden_notebooks_or_data_files` | `uv run python -m pytest tests/test_lab_integrity.py::test_labs_do_not_reference_hidden_notebooks_or_data_files -v` | Keep optional snippets self-contained; use the workflow normalizer only within its ownership |
| 23 | Optional lab Python snippet fails under the test's selected execution scope | `test_optional_lab_python_snippets_execute` | `uv run python -m pytest tests/test_lab_integrity.py::test_optional_lab_python_snippets_execute -v` | Inspect the actual failing snippet and source signature; module links have a separate resolution test |
| 24 | Missing/generic answer or unintended authored-answer rewrite | `test_question_answer_refinement.py` | `uv run python -m pytest tests/test_question_answer_refinement.py -v` | Author prompt-specific solutions; preserve nonwriting refusal, not generic generation heuristics |
| 26 | Quantitative chapter drops below two worked examples, Concept-Check floor, Bloom diversity, or seven LOs | `test_chapter_pedagogy_coverage.py` (parametrized) | `uv run python -m pytest tests/test_chapter_pedagogy_coverage.py -v` | Add a second worked example, Concept Check, higher-order LO verb, or sync assessment metadata after LO edits |
| 27 | A fast-moving biology claim loses its source, anchor, source tier, checked date, or refresh trigger | `test_current_claims_ledger_is_valid` | `uv run python -m pytest tests/test_current_claims_ledger.py -v` | Update `docs/manuscript/current_claims.yaml` and keep the cited claim text/source close to the manuscript claim |
| 28 | Missing LO/Bloom/rubric metadata | `test_assessment_metadata.py`, `test_lab_pedagogy_alignment.py` | `uv run python -m pytest tests/test_assessment_metadata.py tests/test_lab_pedagogy_alignment.py -v` | Author semantic mappings/rubrics, then sync_assessment_metadata.py --check; never regenerate positionally |

> [!TIP]
> The single-test command form is `uv run python -m pytest <file>::<test_name> -v`. You can run **multiple** tests at once with a `-k` filter — e.g. `uv run python -m pytest tests/test_build_invariants.py -k "label or badge" -v`.

---

## Failure-to-fix table

When pytest fails on a **whole file** (multiple tests in one module), look up the symptom and apply the suggested fix:

| Symptom / failing area | Where to look | Fix |
| ---------------------- | ------------- | --- |
| Missing `\label{sec:...}` or metadata badge | `test_build_invariants.py` | Run `scripts/insert_crossref_labels.py` and `scripts/insert_chapter_metadata.py` |
| `ChapterMeta` missing or prerequisite `chapter_id` unknown | `test_chapter_metadata.py` | Align [src/biology/chapter_metadata.py](../src/biology/chapter_metadata.py) with [docs/manuscript/config.yaml](../docs/manuscript/config.yaml) |
| Cite key in chapter not in `references.bib` (or unused bib entry) | `test_bibliography_closure.py` | Add the entry to `references.bib`, or weave an orphan in via `scripts/integrate_orphan_citations.py` |
| Unresolved `@fig:` / `@eq:`, duplicate `\label`, missing `{#fig:...}` | `test_crossref_validator*.py` | Fix labels or references — see [src/biology/crossref_validator.py](../src/biology/crossref_validator.py) |
| Registered `plot_*` never mentioned in any chapter | `test_build_invariants.py` (figure reference invariant) | Add a figure block (or `scripts/insert_orphan_figures.py`) or remove dead registry entry |
| Lab/question missing parent `\cref` | `test_build_invariants.py` | Run `scripts/link_labs_to_chapters.py` |
| Lab computation depends on hidden notebooks, CSVs, pandas, or non-executable snippets | `test_lab_integrity.py` | Run `scripts/normalize_lab_computational_workflows.py`; use tested `biology.*` module imports |
| Missing/generic solution | `test_question_answer_refinement.py` / `test_textbook_quality_audit.py` | Author and review a prompt-specific solution; unsupported repairs refuse without writes |
| Figure missing alt text, or Mermaid block without descriptive line | `test_accessibility.py` | Add `<!-- alt: ... -->` after `\end{figure}` or italic line after mermaid; consider `scripts/add_mermaid_alt_text.py` for bulk Mermaid fixes |
| Reported coverage below 90% | pytest-cov gate | Add meaningful real-computation tests; keep exclusions and isolation substitutions explicit |
| Mid-word citation (`...x\citep{a}y...`) | `test_bibliography_closure.py` | Add a space before/after the `\citep{}` |
| `MPLBACKEND` error in CI | conftest sets `Agg`, but test imports matplotlib differently | Move `matplotlib.use("Agg")` to before any `pyplot` import in the test module |

Workflow context: [composable_authoring.md](composable_authoring.md).

Script hygiene remains an engineering requirement: avoid absolute checkout paths and retired duplicate helpers, but do not attribute that requirement to absent `test_script_quality.py` nodes.

---

## Writing new tests

```python
import pytest
from biology.genetics import punnett_square


def test_punnett_monohybrid_3to1_phenotype():
    """Aa × Aa gives the stipulated complete-dominance monohybrid ratios."""
    result = punnett_square("Aa", "Aa")
    assert result.phenotype_ratios["dominant"] == pytest.approx(0.75)
    assert result.phenotype_ratios["recessive"] == pytest.approx(0.25)
    assert result.genotype_ratios == pytest.approx({"AA": 0.25, "Aa": 0.5, "aa": 0.25})
```

**Rules:**

1. One logical assertion per test function when feasible.
2. Use descriptive test names (snake_case): `test_<function>_<scenario>_<expectation>`.
3. Exercise real computation; keep path/environment/failure injection distinct from native-integration proof.
4. Use `pytest.approx()` for floating-point comparisons with `abs=1e-4` or `rel=1e-3`.
5. Use `tmp_path` fixture for file I/O tests.
6. Set explicit RNG seeds for any stochastic test (`np.random.default_rng(42)`).
7. Prefer **table-driven** tests (`pytest.mark.parametrize`) when checking the same property over many inputs.

### Parametrised example

```python
import pytest
from biology.genetics import punnett_square


@pytest.mark.parametrize("p1,p2,expected_ratio", [
    ("AA", "aa", (1, 0)),       # All dominant phenotype
    ("Aa", "Aa", (3, 1)),       # Classic 3:1
    ("Aa", "aa", (1, 1)),       # 1:1 testcross
    ("aa", "aa", (0, 1)),       # All recessive
])
def test_punnett_phenotype_ratios(p1, p2, expected_ratio):
    """Phenotype ratios across the four canonical monohybrid crosses."""
    result = punnett_square(p1, p2)
    dominant, recessive = expected_ratio
    total = dominant + recessive
    assert result.phenotype_ratios["dominant"] == pytest.approx(dominant / total)
    assert result.phenotype_ratios["recessive"] == pytest.approx(recessive / total)
```

---

## conftest.py

`tests/conftest.py` configures:

- `MPLBACKEND=Agg` for headless matplotlib rendering.
- `sys.path` includes `src/` so modules are importable without installation.
- (No fixtures with side effects — keep `conftest.py` minimal and idempotent.)

---

## Common patterns for difficult tests

### Testing figures (no mocks, no display)

```python
def test_plot_returns_png(tmp_path):
    from PIL import Image
    from visualization import plot_michaelis_menten
    path = plot_michaelis_menten(output_dir=tmp_path, Vmax=10.0, Km=2.0)
    with Image.open(path) as image:
        assert image.format == "PNG"
        image.verify()
```

### Testing numerical models

```python
def test_hodgkin_huxley_fires_at_threshold():
    """A 10 microampere/cm² model current depolarizes above 0 mV."""
    from biology.neuroscience import action_potential_hh
    result = action_potential_hh(stimulus_current_µA=10.0, t_end_ms=30.0, steps=3000)
    assert max(result.voltage_mV) > 0.0  # must depolarise above 0 mV
    assert result.fired
```

### Testing manuscript invariants

```python
from biology.toc import load_toc

def test_every_configured_chapter_has_its_label():
    chapters = load_toc().chapters
    assert chapters, "No configured chapters were inspected"
    for chapter in chapters:
        text = chapter.path.read_text(encoding="utf-8")
        assert "\\label{sec:" + chapter.chapter_id + "}" in text
```

### Exercising CLI boundaries and actual artifacts

Use the [project-output visual review recipe](visualization_guide.md#visual-assets-review-outputs-and-publication-requirements) for a real graphics CLI smoke. A temporary directory must be beneath this project's real `output/`; the project CLIs intentionally reject arbitrary OS temporary destinations and default-directory aliases before generation. Low-level plotting tests can use their own admitted temporary directories.

`tests/test_manuscript_source_custody.py` exercises actual graphics entrypoints and native PDF failure/publication paths. `tests/test_mermaid_and_visualization.py` checks real plot output custody, and `tests/test_pdf_opening_and_mermaid.py` compiles rich captions with normalized mathematical symbols. Tool-dependent skips remain gaps. A subprocess exit or a nonempty file list is not evidence of scientific correctness, readable printing or complete figure provenance.

---

## See also

- [composable_authoring.md](composable_authoring.md) — workflows and stable IDs
- [manuscript_guide.md](manuscript_guide.md) — the patterns these tests enforce
- [pipeline_guide.md](pipeline_guide.md) — publication-gate dependency and artifact contracts
- [accessibility.md](accessibility.md) — alt text rules enforced by `test_accessibility.py`
- [api_reference.md](api_reference.md) — public functions exercised by domain tests
- [docs/manuscript/AGENTS.md](../docs/manuscript/AGENTS.md) — manuscript contract
