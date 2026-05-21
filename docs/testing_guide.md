# Testing Guide

> [!NOTE]
> **See also:** [composable_authoring.md](composable_authoring.md) for the workflow context, [manuscript_guide.md](manuscript_guide.md) for the patterns these tests enforce, and [pipeline_guide.md](pipeline_guide.md) for where tests sit in the build.

---

## Table of contents

- [Zero-mock policy](#zero-mock-policy)
- [Running tests](#running-tests)
- [Coverage standards](#coverage-standards)
- [Test organisation](#test-organisation)
- [Authoring mistake → test → fix (consolidated)](#authoring-mistake--test--fix-consolidated)
- [Failure-to-fix table](#failure-to-fix-table)
- [Writing new tests](#writing-new-tests)
- [Common patterns for difficult tests](#common-patterns-for-difficult-tests)

---

## Zero-mock policy

> [!IMPORTANT]
> All tests use **real data and real computations**. The use of `unittest.mock`, `MagicMock`, `mocker.patch`, or any mocking framework is **absolutely prohibited**.

This policy ensures:

- Tests validate actual biological algorithms, not mocked returns.
- Code is exercised in realistic computational conditions.
- Integration between modules is genuinely tested.

When you need to substitute a heavy resource:

| Resource | Real substitute |
| -------- | --------------- |
| HTTP server | `pytest-httpserver` (real local TCP socket) |
| File system | `tmp_path` fixture (real ephemeral directory) |
| Random number stream | Fixed-seed `np.random.default_rng(seed)` |
| External CLI (e.g. `mmdc`) | Skip the test with `pytest.importorskip` / `pytest.skipif(shutil.which(...) is None)` |
| Subprocess | Real `subprocess.run` against a real CLI under test |

---

## Running tests

> [!IMPORTANT]
> Run from **`projects/biology_textbook/`** (or the path returned by `resolve_project_root` for `--project biology_textbook`) so this project's `pyproject.toml` applies (`coverage fail_under=90`, `pythonpath=src`). Running pytest from the repo root may pick up different config.

```bash
# Full suite, verbose
uv run pytest tests/ -v

# Full suite with coverage report (HTML)
uv run pytest tests/ --cov=src --cov-report=html
open htmlcov/index.html

# Coverage with terminal-missing breakdown
uv run pytest tests/ --cov=src --cov-report=term-missing

# Run a single test file
uv run pytest tests/test_cell_biology.py -v

# Run a single test function
uv run pytest tests/test_genetics.py::test_punnett_square_monohybrid -v

# Run all tests matching a name pattern
uv run pytest tests/ -k "punnett" -v

# Run a specific invariant
uv run pytest tests/test_build_invariants.py::test_every_chapter_has_section_label -v

# Stop at first failure (useful for triage)
uv run pytest tests/ -x

# Show local variables on failure
uv run pytest tests/ -l

# Pure-domain tests (skip slow/optional)
uv run pytest tests/ -m "not slow"
```

> [!TIP]
> When debugging a single invariant, copy the **command** from the [authoring-mistake → test → fix table](#authoring-mistake--test--fix-consolidated) — each row gives the exact `uv run pytest …::test_name -v` line.

---

## Coverage standards

| Scope | Minimum coverage | Live target |
| ----- | ---------------- | ----------- |
| `src/` overall (line + branch) | **90 %** | run `pytest --cov=src` for current |
| `src/biology/` | 90 % | ~92 % (see `pyproject.toml` `fail_under`) |
| `src/biology/chapter_metadata.py` | 90 % | **100 %** |
| `src/biology/crossref_validator.py` | 80 % | ~92 % |
| `src/mermaid/` | 80 % | ~93 % (renderer 80 %, diagrams 100 %) |
| `src/visualization/` | 80 % | ≥ 80 % (exercised by `test_mermaid_and_visualization.py`) |
| Manuscript invariants | all green | `pytest` from project dir |

Run `uv run pytest tests/ --cov=src --cov-report=term-missing` for the per-file breakdown.

---

## Test organisation

**Total: 27 test files** (domain + invariant/quality). The suite is partitioned into **domain tests** (exercising `src/biology/*` models) and **invariant/quality tests** (asserting manuscript, lab, question-bank, table-of-contents, render-log, glossary, current-claim, assessment-alignment, accessibility, and script-level gates).

### Domain tests (6 `test_*.py` files)

| Test file | What it covers |
| --------- | -------------- |
| `test_cell_biology.py` | Organelles, Nernst, Goldman, osmotic pressure, diffusion |
| `test_genetics.py` | DNA, translation, Punnett squares, HW equilibrium, χ², genetic distance |
| `test_ecology_evolution_physiology_biochemistry.py` | Lotka-Volterra, selection, drift, glycolysis, Michaelis-Menten, Poiseuille |
| `test_microbiology_botany_neuroscience.py` | Bacterial growth, MIC, water potential, Hodgkin-Huxley, synaptic transmission, LTP |
| `test_mermaid_and_visualization.py` | Mermaid renderer, `ALL_BIOLOGY_DIAGRAMS`, matplotlib `ALL_FIGURE_GENERATORS` |
| `test_coverage_gap.py` | Deliberately closes residual branches in existing modules |
| `test_current_claims_ledger.py` | Fast-moving claim ledger, source tier, anchor, and stale-phrase checks |
| `test_assessment_metadata.py` | Item-level LO, Bloom, difficulty, format, and minutes metadata across all question banks |
| `test_lab_pedagogy_alignment.py` | Lab outcome, LO-coverage, and rubric-dimension metadata checks |
| `conftest.py` | `MPLBACKEND=Agg` + `sys.path` bootstrap |

### Textbook quality audit

`test_textbook_quality_audit.py` imports `scripts/audit_textbook_quality.py`
and requires zero blocking findings. The audit now targets zero active
absolute-language advisories; any current advisory should be revised before
publication. `manuscript/quality_advisories.yaml` remains the triage ledger for
future review cases; new untriaged findings or unresolved `needs_qualifier` /
`copyedit_artifact` entries fail. Blocking
findings also include generic answer-key templates,
`Expected reasoning:` scaffolds from earlier generated answers, stale WHO
or AMR burden language, required wet-lab wording, hard-coded rendered
references, weak Mermaid metadata, dangling glossary links, and bibliography
closure failures. It also blocks copyediting artifacts from prior broad cleanup
passes, such as uppercase `MOST`, `Not most`, and awkward `primarily` quantifier
phrases. It also requires the embedded-enrichment audit matrix,
chapter frontier boxes, unit evidence threads, and paper-based lab evidence
upgrade sections introduced by `scripts/enrich_embedded_textbook.py`.

### Invariant and quality tests (18 files)

| Test file | What it guards |
| --------- | -------------- |
| `test_atomic_io.py` | Atomic write/replace helpers used by maintenance scripts |
| `test_audit_v3_and_crossref_gate.py` | Generic-answer v3 and malformed `\cref` detector regressions |
| `test_build_invariants.py` | Every chapter has `\label{sec:…}` and a metadata badge; every lab/question `\cref`-links to its parent chapter; every registered figure generator is referenced; Course Planning Grid populated |
| `test_bibliography_closure.py` | `{cited}` == `{defined}` in `references.bib` — no orphans, no dangling citations, no mid-word citation artefacts |
| `test_chapter_metadata.py` | Every `config.yaml` chapter has a `ChapterMeta` record; prerequisites resolve; difficulty ∈ {1, 2, 3}; chapter numbers contiguous 1..N |
| `test_curriculum_metadata.py` | Every `config.yaml` chapter has a curriculum record; lab/question companion paths exist and align |
| `test_toc_consistency.py` | Renderable H1s, front-matter navigation, reference appendix headings, and Course Planning Grid titles match `biology.toc`; lab/question config entries avoid duplicated titles |
| `test_accessibility.py` | Alt-text substance + proximity; unit chapters, labs, questions; Mermaid or italic caption after blocks |
| `test_crossref_validator.py` | Top-level invariant: no unresolved `@fig:`/`@eq:`/`@tbl:`/`@sec:` refs, no duplicate labels, `cleveref` loaded in preamble |
| `test_crossref_validator_internals.py` | Parser coverage: `$$…$$`, `\begin{figure}`, `\begin{equation}`, table captions, section labels, prose xrefs |
| `test_crossref_validator_edges.py` | Edge cases: markdown images with `{#fig:}` attrs, block equations with id on following line, duplicate labels across files |
| `test_lab_integrity.py` | Lab Part 2 computation sections are self-contained, avoid hidden notebooks/CSV dependencies, and execute `biology.*` snippets |
| `test_enrichment_substance_gate.py` | Embedded-enrichment boilerplate and duplicate-body detectors |
| `test_pdf_log_quality.py` | PDF-log checker reports undefined references and severe overfull boxes above the configured threshold |
| `test_pdf_opening_and_mermaid.py` | Book opening uses `book.*` metadata, cover asset exists, and inline Mermaid converts to PNG references |
| `test_question_answer_refinement.py` | Generated-answer heuristics classify quantitative questions, strip command prefixes, and preserve hand-written answers |
| `test_script_quality.py` | Scripts parse as Python, avoid hard-coded local checkout paths, and keep retired duplicate helpers removed |
| `test_textbook_quality_audit.py` | Umbrella textbook-quality audit: stale claims, copyedit artifacts, enrichment presence, and current-source locks |

---

## Authoring mistake → test → fix (consolidated)

Use this table when pytest fails. Each row gives the **specific authoring mistake**, the **specific test that catches it**, the **single-test command** for fast iteration, and the **fix** (often an idempotent script).

| # | Authoring mistake | Test name | Single-test command | How to fix |
| - | ----------------- | --------- | ------------------- | ---------- |
| 1 | Forgot `\label{sec:unit_X_<stem>}` after a chapter's H1 | `test_every_chapter_has_section_label` | `uv run pytest tests/test_build_invariants.py::test_every_chapter_has_section_label -v` | Run `scripts/insert_crossref_labels.py` (idempotent) |
| 2 | Forgot the `<!-- chapter-metadata-badge -->` block | `test_every_chapter_has_metadata_badge` | `uv run pytest tests/test_build_invariants.py::test_every_chapter_has_metadata_badge -v` | Run `scripts/insert_chapter_metadata.py` (requires matching `ChapterMeta`) |
| 3 | Lab file is missing `\cref{sec:...}` to its parent chapter | `test_every_lab_links_to_parent_chapter` | `uv run pytest tests/test_build_invariants.py::test_every_lab_links_to_parent_chapter -v` | Run `scripts/link_labs_to_chapters.py` |
| 4 | Question bank is missing `\cref{sec:...}` to its parent chapter | `test_every_question_links_to_parent_chapter` | `uv run pytest tests/test_build_invariants.py::test_every_question_links_to_parent_chapter -v` | Run `scripts/link_labs_to_chapters.py` |
| 5 | Registered `plot_*` never referenced from any chapter | `test_every_registered_figure_is_referenced` | `uv run pytest tests/test_build_invariants.py::test_every_registered_figure_is_referenced -v` | Add a `\begin{figure}...\end{figure}` block (use `scripts/insert_orphan_figures.py --dry-run` to scaffold) |
| 6 | Front-matter Course Planning Grid empty / stale | `test_course_planning_grid_populated` | `uv run pytest tests/test_build_invariants.py::test_course_planning_grid_populated -v` | Re-run `scripts/insert_chapter_metadata.py` |
| 6a | A chapter, unit intro, lab, question bank, reference appendix, or glossary H1 drifts from `config.yaml` | `test_renderable_h1s_match_canonical_toc` | `uv run pytest tests/test_toc_consistency.py::test_renderable_h1s_match_canonical_toc -v` | Run `scripts/sync_curriculum_materials.py` |
| 6b | Lab/question entries duplicate derived `title:` strings in `config.yaml` | `test_lab_and_question_config_entries_do_not_duplicate_titles` | `uv run pytest tests/test_toc_consistency.py::test_lab_and_question_config_entries_do_not_duplicate_titles -v` | Delete the duplicated `title:` keys; keep only `file:` |
| 7 | Citekey in chapter not present in `references.bib` | `test_no_dangling_citations` | `uv run pytest tests/test_bibliography_closure.py::test_no_dangling_citations -v` | Add the BibTeX entry to `references.bib` (`@article{...}`) |
| 8 | BibTeX entry never cited | `test_no_orphan_bib_entries` | `uv run pytest tests/test_bibliography_closure.py::test_no_orphan_bib_entries -v` | Cite it in the most relevant chapter, or run `scripts/integrate_orphan_citations.py` |
| 9 | `\cite{}` glued to a word (`...as\citep{x}shows...`) | `test_no_midword_citations` | `uv run pytest tests/test_bibliography_closure.py::test_no_midword_citations -v` | Add a space before/after the `\citep{}` |
| 10 | `ChapterMeta` missing for a chapter listed in `config.yaml` | `test_every_config_chapter_has_meta` | `uv run pytest tests/test_chapter_metadata.py::test_every_config_chapter_has_meta -v` | Add a `ChapterMeta(...)` record to `src/biology/chapter_metadata.py` |
| 11 | `ChapterMeta.prerequisites` references unknown `chapter_id` | `test_prerequisites_resolve` | `uv run pytest tests/test_chapter_metadata.py::test_prerequisites_resolve -v` | Fix typo, or add the missing `ChapterMeta` for the prereq |
| 12 | Difficulty out of {1, 2, 3} | `test_difficulty_in_range` | `uv run pytest tests/test_chapter_metadata.py::test_difficulty_in_range -v` | Set difficulty to 1, 2, or 3; rendered badges display Level 1/3 through Level 3/3 |
| 13 | Chapter numbers non-contiguous | `test_chapter_numbers_contiguous` | `uv run pytest tests/test_chapter_metadata.py::test_chapter_numbers_contiguous -v` | Renumber `ChapterMeta(..., number=N, ...)` to be contiguous 1..N |
| 14 | Figure has no `<!-- alt: ... -->` immediately after `\end{figure}` | `test_every_latex_figure_has_alt_nearby` | `uv run pytest tests/test_accessibility.py::test_every_latex_figure_has_alt_nearby -v` | Add `<!-- alt: ... -->` comment immediately after `\end{figure}` |
| 15 | Mermaid block has missing, duplicate, or stale metadata | `test_every_mermaid_block_has_exactly_one_alt_and_caption` | `uv run pytest tests/test_accessibility.py::test_every_mermaid_block_has_exactly_one_alt_and_caption -v` | Add one `<!-- alt: ... -->` comment and one italic caption, or run `scripts/add_mermaid_alt_text.py` |
| 16 | Alt text is too short / generic ("Figure 4", "graph") | `test_alt_text_substance` | `uv run pytest tests/test_accessibility.py::test_alt_text_substance -v` | Rewrite to describe axes, trend, and salient features (15–35 words) |
| 17 | `@fig:foo` referenced but no `{#fig:foo}` defined | `test_no_unresolved_refs` | `uv run pytest tests/test_crossref_validator.py::test_no_unresolved_refs -v` | Define the label, or fix the reference typo |
| 18 | Same `\label{fig:foo}` defined in two files | `test_no_duplicate_labels` | `uv run pytest tests/test_crossref_validator.py::test_no_duplicate_labels -v` | Make the label globally unique (use the `unit_X_<descriptor>` convention) |
| 19 | `cleveref` missing from preamble | `test_cleveref_loaded` | `uv run pytest tests/test_crossref_validator.py::test_cleveref_loaded -v` | Add `\usepackage{cleveref}` to `manuscript/preamble.md` after `hyperref` |
| 20 | `$$…$$` block mixing `\tag{}` and `\label{}` | `test_dollar_block_label_tag_mutex` | `uv run pytest tests/test_crossref_validator_internals.py::test_dollar_block_label_tag_mutex -v` | Promote to `\begin{equation}\tag{}\label{}\end{equation}` (see [manuscript_guide.md#equations](manuscript_guide.md#equations)) |
| 21 | Markdown image with `{#fig:...}` attribute parses incorrectly | `test_markdown_image_attrs` | `uv run pytest tests/test_crossref_validator_edges.py::test_markdown_image_attrs -v` | Check syntax: `![alt](path){#fig:label}` (no space before `{`) |
| 22 | Lab Part 2 references a hidden notebook, CSV, pandas import, or display-only `plt.show()` workflow | `test_labs_do_not_reference_missing_computational_artifacts` | `uv run pytest tests/test_lab_integrity.py::test_labs_do_not_reference_missing_computational_artifacts -v` | Run `scripts/normalize_lab_computational_workflows.py`; keep snippets self-contained |
| 23 | Optional lab snippet imports a module path that does not resolve | `test_lab_python_snippets_execute_against_project_modules` | `uv run pytest tests/test_lab_integrity.py::test_lab_python_snippets_execute_against_project_modules -v` | Fix the `from biology... import ...` line or add/export the missing API in `src/biology` |
| 24 | Generated answer refiner starts rewriting hand-written answers or stops recognizing current generated signatures | `test_current_generated_signatures_are_refinable` / `test_hand_written_answer_is_not_refinable` | `uv run pytest tests/test_question_answer_refinement.py -v` | Update `scripts/refine_generated_answers.py` signature predicates with paired tests |
| 25 | Script contains an absolute local checkout path or an obsolete duplicate helper returns | `test_scripts_do_not_embed_absolute_checkout_paths` / `test_obsolete_mermaid_alt_helpers_removed` | `uv run pytest tests/test_script_quality.py -v` | Replace hard-coded paths with project-relative `Path` logic; keep one canonical helper |
| 26 | A fast-moving biology claim loses its source, anchor, source tier, checked date, or refresh trigger | `test_current_claims_ledger_is_valid` | `uv run pytest tests/test_current_claims_ledger.py -v` | Update `manuscript/current_claims.yaml` and keep the cited claim text/source close to the manuscript claim |
| 27 | A question-bank item or lab loses LO/Bloom/rubric metadata | `test_all_question_bank_items_have_assessment_metadata` / `test_every_lab_maps_to_measurable_outcomes_and_chapter_los` | `uv run pytest tests/test_assessment_metadata.py tests/test_lab_pedagogy_alignment.py -v` | Run `scripts/sync_assessment_metadata.py --dry-run`, write with `scripts/sync_assessment_metadata.py`, then review any pedagogical mismatch manually |

> [!TIP]
> The single-test command form is `uv run pytest <file>::<test_name> -v`. You can run **multiple** tests at once with a `-k` filter — e.g. `uv run pytest tests/test_build_invariants.py -k "label or badge" -v`.

---

## Failure-to-fix table

When pytest fails on a **whole file** (multiple tests in one module), look up the symptom and apply the suggested fix:

| Symptom / failing area | Where to look | Fix |
| ---------------------- | ------------- | --- |
| Missing `\label{sec:...}` or metadata badge | `test_build_invariants.py` | Run `scripts/insert_crossref_labels.py` and `scripts/insert_chapter_metadata.py` |
| `ChapterMeta` missing or prerequisite `chapter_id` unknown | `test_chapter_metadata.py` | Align [src/biology/chapter_metadata.py](../src/biology/chapter_metadata.py) with [manuscript/config.yaml](../manuscript/config.yaml) |
| Cite key in chapter not in `references.bib` (or unused bib entry) | `test_bibliography_closure.py` | Add the entry to `references.bib`, or weave an orphan in via `scripts/integrate_orphan_citations.py` |
| Unresolved `@fig:` / `@eq:`, duplicate `\label`, missing `{#fig:...}` | `test_crossref_validator*.py` | Fix labels or references — see [src/biology/crossref_validator.py](../src/biology/crossref_validator.py) |
| Registered `plot_*` never mentioned in any chapter | `test_build_invariants.py` (figure reference invariant) | Add a figure block (or `scripts/insert_orphan_figures.py`) or remove dead registry entry |
| Lab/question missing parent `\cref` | `test_build_invariants.py` | Run `scripts/link_labs_to_chapters.py` |
| Lab computation depends on hidden notebooks, CSVs, pandas, or non-executable snippets | `test_lab_integrity.py` | Run `scripts/normalize_lab_computational_workflows.py`; use tested `biology.*` module imports |
| Generated answer refinement regresses or `Expected reasoning:` reappears | `test_question_answer_refinement.py` / `test_textbook_quality_audit.py` | Add/adjust heuristics in `scripts/refine_generated_answers.py`, run it, and keep hand-written answer guardrails |
| Script path or duplicate-helper hygiene regresses | `test_script_quality.py` | Remove absolute checkout paths; delete retired helper clones; ensure every `scripts/*.py` parses |
| Figure missing alt text, or Mermaid block without descriptive line | `test_accessibility.py` | Add `<!-- alt: ... -->` after `\end{figure}` or italic line after mermaid; consider `scripts/add_mermaid_alt_text.py` for bulk Mermaid fixes |
| Coverage < 90 % on `src/` | pytest-cov fails the gate | Add tests in `tests/test_*.py`; no mocks; use real numerical inputs |
| Mid-word citation (`...x\citep{a}y...`) | `test_bibliography_closure.py` | Add a space before/after the `\citep{}` |
| `MPLBACKEND` error in CI | conftest sets `Agg`, but test imports matplotlib differently | Move `matplotlib.use("Agg")` to before any `pyplot` import in the test module |

Workflow context: [composable_authoring.md](composable_authoring.md).

---

## Writing new tests

```python
import pytest
from biology.genetics import punnett_square


def test_punnett_monohybrid_3to1_phenotype():
    """HW cross Aa × Aa must give 3:1 dominant:recessive ratio."""
    result = punnett_square("Aa", "Aa")
    assert result.phenotype_ratios["dominant"] == pytest.approx(0.75)
    assert result.phenotype_ratios["recessive"] == pytest.approx(0.25)
    assert result.genotype_ratios == pytest.approx({"AA": 0.25, "Aa": 0.5, "aa": 0.25})
```

**Rules:**

1. One logical assertion per test function when feasible.
2. Use descriptive test names (snake_case): `test_<function>_<scenario>_<expectation>`.
3. **No mocks** — create real inputs (numerical arrays, biological data structures).
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
def test_plot_returns_figure(tmp_path):
    """Generator must produce a non-trivial PNG at the requested path."""
    from visualization import plot_michaelis_menten
    fig_path = plot_michaelis_menten(
        output_dir=tmp_path,
        Vmax=10.0, Km=2.0,
    )
    assert fig_path.exists()
    assert fig_path.stat().st_size > 1000  # non-trivial file
```

### Testing numerical models

```python
def test_hodgkin_huxley_fires_at_threshold():
    """A 10 nA stimulus must depolarise the membrane above 0 mV."""
    from biology.neuroscience import action_potential_hh
    result = action_potential_hh(stimulus_current_µA=10.0, t_end_ms=50.0)
    assert max(result.voltage_mV) > 0.0  # must depolarise above 0 mV
    assert result.fired
```

### Testing manuscript invariants

```python
from pathlib import Path
import re

def test_every_chapter_starts_with_section_label():
    """Every chapter file must have \\label{sec:unit_X_<stem>} after the H1."""
    pattern = re.compile(r"^# .*\n+\\label\{sec:unit_[0IVX]+_\w+\}", re.MULTILINE)
    chapters = Path("manuscript").rglob("unit_*/[!._]*.md")
    failures = [c for c in chapters if not pattern.search(c.read_text())]
    assert failures == [], f"Chapters missing section label: {failures}"
```

### Testing CLI / subprocess

```python
import subprocess, sys

def test_generate_figures_cli_runs(tmp_path):
    """Smoke test: scripts/generate_figures.py must complete and emit PNGs."""
    result = subprocess.run(
        [sys.executable, "scripts/generate_figures.py", "--output-dir", str(tmp_path)],
        capture_output=True, text=True, check=True, timeout=60,
    )
    assert result.returncode == 0
    assert any(tmp_path.glob("*.png"))
```

---

## See also

- [composable_authoring.md](composable_authoring.md) — workflows and stable IDs
- [manuscript_guide.md](manuscript_guide.md) — the patterns these tests enforce
- [pipeline_guide.md](pipeline_guide.md) — where tests sit in the build (Stage 2)
- [accessibility.md](accessibility.md) — alt text rules enforced by `test_accessibility.py`
- [api_reference.md](api_reference.md) — public functions exercised by domain tests
- [../manuscript/AGENTS.md](../manuscript/AGENTS.md) — manuscript contract
