# Architecture Guide

## Two-Layer Architecture

Relative to the **template** repository: generic infrastructure lives in `infrastructure/` and `scripts/` (Layer 1). The biology textbook tree is **project Layer 2**: domain code in `src/`, content in `manuscript/`, and thin orchestrators in this project's `scripts/`.

```text
biology_textbook/
├── src/
│   ├── biology/                  # Nine domain subpackages + manuscript utilities and maintenance packages
│   │   ├── __init__.py
│   │   ├── biochemistry/, cell/, genetics/, evolution/, ecology/,
│   │   ├── physiology/, microbiology/, botany/, neuroscience/
│   │   ├── numerics.py, constants.py
│   │   ├── chapter_metadata.py, toc.py, curriculum.py, assessment.py
│   │   ├── current_claims.py, alignment.py, visual_contracts.py
│   │   ├── crossref/              # package; shim at crossref_validator.py
│   │   ├── quality/, enrichment/, answer_refinement/, curriculum_sync/
│   │   └── crossref_validator.py  # re-export shim
│   ├── textbook_paths.py         # template-root discovery, ensure_project_paths()
│   ├── textbook_io.py            # atomic text writes
│   ├── textbook_logging.py       # infrastructure-aware logging fallback
│   ├── mermaid/                  # diagram_specs.yaml + diagram_spec_loader (24 diagrams)
│   └── visualization/            # plots_*.py domain modules + plots.py registry + cvd.py
├── tests/                        # domain + invariant tests; zero mocks; ≥90 % coverage on src/ (see pytest)
├── scripts/                      # 36 Python files — see project [AGENTS.md](../AGENTS.md)
├── manuscript/                   # config.yaml + 11 units + labs + questions + glossary + references.bib
├── docs/                         # guides (this directory; see [README.md](README.md))
├── output/                       # Generated (disposable)
└── pyproject.toml
```

## Subpackage Summary

| Subpackage | Key exports | Tests |
| ---------- | ----------- | ----- |
| `biology.biochemistry` | `michaelis_menten`, `glycolysis_summary`, `atp_free_energy` | `test_ecology_evolution_physiology_biochemistry.py`, `test_coverage_gap.py` |
| `biology.cell` | `nernst_potential`, `goldman_equation`, `diffusion_flux`, `ORGANELLES` | `test_cell_biology.py`, `test_coverage_gap.py` |
| `biology.genetics` | `punnett_square`, `translate_mrna`, `hardy_weinberg`, `mutation_rate_spectrum`, `replication_fork_progression` | `test_genetics_{sequence,mendelian,population,linkage,distance,epigenetics,mutation,replication}.py`, `test_coverage_gap.py` |
| `biology.evolution` | `simulate_selection`, `simulate_drift`, `molecular_clock_divergence_time` | `test_ecology_evolution_physiology_biochemistry.py` |
| `biology.ecology` | `lotka_volterra`, `logistic_growth`, `allee_strong_growth`, `species_area_relationship`, `biodiversity_indices` | `test_ecology_evolution_physiology_biochemistry.py` |
| `biology.physiology` | `poiseuille_flow`, `oxygen_saturation`, `homeostasis_response` | `test_ecology_evolution_physiology_biochemistry.py` |
| `biology.microbiology` | `bacterial_growth_curve`, `mic_fold_dilution`, `basic_reproduction_number`, `sir_model` | `test_microbiology_botany_neuroscience.py` |
| `biology.botany` | `water_potential`, `transpiration_flux`, `photosynthesis_rate` | `test_microbiology_botany_neuroscience.py` |
| `biology.neuroscience` | `action_potential_hh`, `cable_voltage_attenuation`, `synaptic_current`, `hebbian_weight_update` | `test_microbiology_botany_neuroscience.py` |
| `biology.chapter_metadata` | `CHAPTERS` list of `ChapterMeta(difficulty, reading_time_min, lecture_time_min, prerequisites)` | `test_chapter_metadata.py` |
| `biology.toc` | `load_toc()` canonical units, chapters, companion-material titles, and reference appendices | `test_toc_consistency.py` |
| `biology.curriculum` | `CurriculumRecord`, learning objectives, curriculum scaffold | `test_curriculum_metadata.py` |
| `biology.assessment` | Question-bank and lab assessment metadata parsers | `test_assessment_metadata.py`, `test_lab_pedagogy_alignment.py` |
| `biology.current_claims` | `CurrentClaim` ledger loader and validator | `test_current_claims_ledger.py` |
| `biology.quality` | Umbrella manuscript quality audit engine | `test_textbook_quality_audit.py` |
| `biology.enrichment` | Embedded frontier/companion enrichment catalog | `test_enrichment_substance_gate.py`, `test_textbook_quality_audit.py` |
| `biology.crossref_validator` | `validate()`, `scan_file()`, `scan_directory()`, `CrossRefReport` | `test_crossref_validator{,_edges,_internals}.py` |

Overall **`src/`** line + branch coverage is enforced at **≥90 %** via `pyproject.toml` (`fail_under = 90`). Run `uv run python -m pytest tests/ --cov=src` from the project directory for the live report.

## Manuscript invariants as tests

The [`tests/`](../tests/) suite is **58** `test_*.py` files: domain modules plus manuscript, lab, question, render, current-claim, assessment-alignment, maintenance-engine smoke, table-caption, publication-gate, and script-quality invariant modules. Authoritative list and failure-to-fix table: [testing_guide.md](testing_guide.md#test-organization); the same invariant list appears under “Invariant tests (Stage 2 gate-keepers)” in [pipeline_guide.md](pipeline_guide.md).

Invariant modules:

- `test_build_invariants.py` — chapter labels, badge presence, lab/question back-links, figure-generator usage
- `test_bibliography_closure.py` — `{cited}` == `{defined}` in `references.bib`
- `test_chapter_metadata.py` — every `config.yaml` chapter has a `ChapterMeta` record
- `test_curriculum_metadata.py` — every `config.yaml` chapter has curriculum metadata and aligned companion paths
- `test_toc_consistency.py` — renderable H1s, front-matter navigation, reference appendices, and Course Planning Grid titles match `biology.toc`
- `test_accessibility.py` — alt-text quality and near-block rules for LaTeX figures and Mermaid in chapters, labs, and questions ([../manuscript/AGENTS.md](../manuscript/AGENTS.md), [accessibility.md](accessibility.md))
- `test_crossref_validator.py`, `test_crossref_validator_edges.py`, `test_crossref_validator_internals.py` — pandoc-crossref + cleveref + `\label` consistency
- `test_lab_integrity.py` — lab computation sections are self-contained and executable against `src/biology`
- `test_pdf_log_quality.py` — PDF log checker catches undefined references and severe overfull boxes
- `test_pdf_opening_and_mermaid.py` — book opening metadata, cover asset, and inline Mermaid rendering contract
- `test_question_answer_refinement.py` — generated answer refinement remains idempotent and preserves hand-written answers
- `test_script_quality.py` — scripts parse cleanly and avoid hard-coded local checkout paths or obsolete clones

## Thin Orchestrator Pattern

Scripts in `scripts/` are **thin orchestrators** — they import from `src/biology/`, call functions, format output, and write JSON/PNG/PDF. No business logic in scripts.

```python
# GOOD: thin orchestrator
from biology.biochemistry import michaelis_menten
result = michaelis_menten(substrate_conc=5.0, Vmax=10.0, Km=2.0)
print(json.dumps(result.__dict__))

# BAD: logic in script
def michaelis_menten_inline(S, Vmax, Km):  # don't do this in scripts
    return Vmax * S / (Km + S)
```

## Module Import Pattern

All `src/biology/` modules use explicit imports. The user-facing `biology` package is importable from the project root after `uv sync`:

```python
from biology.cell import nernst_potential, IonConcentration
from biology.genetics import punnett_square
from biology.ecology import lotka_volterra, logistic_growth
```

Tests and scripts both import this way — see `pyproject.toml` for `pythonpath = ["src"]`.

## Manuscript–code contract

Composable authoring depends on a few **bidirectional** links between content and code:

| Anchor | Manuscript / config | Code / tests |
| ------ | ------------------- | ------------ |
| Chapter order & titles | [manuscript/config.yaml](../manuscript/config.yaml) `units[].chapters[]` | [src/biology/chapter_metadata.py](../src/biology/chapter_metadata.py) `CHAPTERS` / `ChapterMeta` — must match; [tests/test_chapter_metadata.py](../tests/test_chapter_metadata.py) |
| Section cross-refs | `\label{sec:unit_X_<stem>}` / `\cref{sec:...}` | `chapter_id` in `ChapterMeta` equals `unit_X_<stem>`; prerequisites tuple lists other `chapter_id` values (resolved to `\cref` in badges) |
| Matplotlib figures | `\includegraphics{../figures/...}` + `\label{fig:...}` in chapters | [src/visualization/plots.py](../src/visualization/plots.py) + domain `plots_*.py` modules; [cvd.py](../src/visualization/cvd.py) palette |
| Mermaid diagrams | Inline fences and/or generated PNGs | [src/mermaid/biology_diagrams.py](../src/mermaid/biology_diagrams.py) `ALL_BIOLOGY_DIAGRAMS`; [tests/test_mermaid_and_visualization.py](../tests/test_mermaid_and_visualization.py) |
| Cross-reference graph | `@fig:` / `@eq:`, `{#fig:...}`, raw `\label{}` | [src/biology/crossref_validator.py](../src/biology/crossref_validator.py) `validate()`; [tests/test_crossref_validator\*.py](../tests/) |

See [composable_authoring.md](composable_authoring.md) for workflows and validation commands.
