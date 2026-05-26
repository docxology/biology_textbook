# `src/` — AGENTS.md

## Role

All scientific computation and manuscript-consumed metadata for the biology textbook lives here. The test suite runs against these modules; scripts in `../scripts/` import from here and only coordinate I/O and rendering — **no business logic belongs in scripts.**

## Layout

```text
src/
├── __init__.py
├── textbook_paths.py              # template-root discovery, ensure_project_paths()
├── textbook_io.py                 # atomic text writes (used by scripts/atomic_io.py)
├── textbook_logging.py            # infrastructure-aware logging fallback
├── biology/                      # nine domain subpackages + manuscript utilities
│   ├── __init__.py
│   ├── biochemistry/biochemistry.py
│   ├── botany/botany.py
│   ├── cell/cell_biology.py
│   ├── ecology/ecology.py
│   ├── evolution/evolution.py
│   ├── genetics/                      # eight topic modules + genetics.py shim
│   │   ├── sequence.py, mendelian.py, population.py, linkage.py
│   │   ├── distance.py, epigenetics.py, mutation.py, replication.py
│   │   └── genetics.py                # legacy re-export shim (manuscript bridge paths)
│   ├── microbiology/microbiology.py
│   ├── neuroscience/neuroscience.py
│   ├── physiology/physiology.py
│   ├── foundations/                   # Unit 0 + Unit I foundational tables (no I/O)
│   ├── chapter_metadata.py        # per-chapter difficulty / reading time / lecture time / prereqs
│   ├── toc.py                     # canonical units/chapters/labs/questions/reference appendices
│   ├── current_claims.py          # current-claim ledger loader and validator
│   ├── assessment.py              # question-bank and lab assessment metadata parser
│   ├── curriculum.py              # learning objectives and curriculum records
│   ├── alignment.py               # standards, skills, and instructor alignment
│   ├── visual_contracts.py        # derived visual manifest helpers
│   ├── crossref/                  # split validator package (shim: crossref_validator.py)
│   ├── quality/                   # manuscript quality audit engine
│   ├── enrichment/                # embedded frontier/companion enrichment
│   ├── answer_refinement/         # question-bank answer heuristics
│   ├── curriculum_sync/           # TOC-driven curriculum scaffold sync
│   └── crossref_validator.py      # re-export shim for biology.crossref
├── mermaid/                       # Mermaid source + renderer
│   ├── renderer.py
│   ├── diagrams.py
│   ├── diagram_spec_loader.py     # loads diagram_specs.yaml
│   ├── diagram_specs.yaml
│   └── biology_diagrams.py        # ALL_BIOLOGY_DIAGRAMS (24 diagrams)
└── visualization/
    ├── __init__.py                # ALL_FIGURE_GENERATORS registry
    ├── plots.py                   # aggregator + registry (42 generators)
    ├── plots_{cell,genetics,ecology,evolution,physiology,botany,microbiology,foundations}.py
    ├── _scaffold.py               # shared matplotlib scaffolding
    └── cvd.py                     # colour-vision–friendly palette defaults
```

## `biology/` — nine domain subpackages

Each subpackage exposes frozen result dataclasses (`EnzymeKineticsResult`, `PunnettSquareResult`, `ActionPotentialResult`, `SIRResult`, …) and pure functions. See [`../docs/api_reference.md`](../docs/api_reference.md) for the full function-by-function API and [`../docs/architecture.md`](../docs/architecture.md) for the test-file mapping.

| Subpackage | Topic | Representative functions |
| ---------- | ----- | ------------------------ |
| `biochemistry` | Enzyme kinetics, bioenergetics | `michaelis_menten`, `glycolysis_summary`, `atp_free_energy` |
| `cell` | Membrane biophysics, organelles | `nernst_potential`, `goldman_equation`, `osmotic_pressure`, `ORGANELLES` |
| `genetics` | DNA/RNA, crosses, population genetics | `punnett_square`, `translate_mrna`, `hardy_weinberg`, `mutation_rate_spectrum`, `replication_fork_progression` — package: `biology.genetics.{sequence,mendelian,population,…}` |
| `evolution` | Selection, drift, speciation | `simulate_selection`, `simulate_drift`, `molecular_clock_divergence_time` |
| `ecology` | Growth models, diversity | `logistic_growth`, `lotka_volterra`, `biodiversity_indices`, `BIOME_DATA` |
| `physiology` | Circulation, gas exchange | `poiseuille_flow`, `oxygen_saturation`, `homeostasis_response` |
| `microbiology` | Growth curves, MIC, transmission | `bacterial_growth_curve`, `mic_fold_dilution`, `sir_model` |
| `botany` | Water relations, photosynthesis | `water_potential`, `transpiration_flux`, `photosynthesis_rate` |
| `neuroscience` | Action potentials, passive cables, synapses | `action_potential_hh`, `cable_voltage_attenuation`, `synaptic_current` |
| `foundations` | Unit 0 CAS/active inference; Unit I atoms/macromolecules | `BIOLOGY_MILESTONES`, `poisson_degree_distribution`, `electronegativity_difference`, `polymer_hierarchy_levels` |

## `biology/chapter_metadata.py`

Frozen `ChapterMeta` dataclasses declare, for every chapter in `manuscript/config.yaml`:

- sequential chapter number (1..N for Units I–X; 0 for Unit 0 orientation chapters)
- unit (Roman numeral or "0")
- difficulty 1 / 2 / 3 → `difficulty_label` for rendered badges; `star_badge` remains a legacy compatibility property
- estimated reading time (minutes)
- suggested lecture allotment (minutes)
- prerequisite chapter_ids

The list `CHAPTERS` is combined with the canonical table of contents from
`biology/toc.py` by `../scripts/insert_chapter_metadata.py` to render
per-chapter badges and the Course Planning Grid in `manuscript/front_matter.md`.
Invariant tests in `../tests/test_chapter_metadata.py` assert completeness
(every config chapter has a record), that prerequisites resolve, and that
chapter numbers are contiguous.

## `biology/toc.py`

Canonical book-structure API. `load_toc(project_root=None)` reads
`manuscript/config.yaml` plus `ChapterMeta` records and returns units, chapters,
labs, question banks, and reference appendices with derived display titles.
`../scripts/sync_curriculum_materials.py` uses it to normalize renderable H1s
and front-matter navigation; `../scripts/insert_chapter_metadata.py` uses it for
Course Planning Grid chapter titles. `../tests/test_toc_consistency.py` locks
those surfaces to the canonical structure.

## `biology/crossref_validator.py`

Dependency-free markdown / LaTeX scanner that parses:

- `\begin{figure}…\label{fig:…}…\end{figure}` blocks (raw LaTeX)
- `\begin{equation}…\label{eq:…}…\end{equation}` environments
- Inline `$$…$$` display equations, with manual equation-number tags rejected
- Markdown images with `{#fig:…}` pandoc-crossref attributes
- Table captions `Table: … {#tbl:…}`
- Section labels `## Heading {#sec:…}`
- Cross-reference usages `@fig:`, `@eq:`, `@tbl:`, `@sec:`
- Hand-typed rendered-number prose references such as `Chapter N`, `Figure N`, `Equation N`, `Section N`, and `§N`

Exports `CrossRefIssue`, `CrossRefReport`, `scan_file`, `scan_directory`, `validate`, `suggest_id`. Covered by three test files (`test_crossref_validator.py`, `test_crossref_validator_internals.py`, `test_crossref_validator_edges.py`).

## Current-claims, assessment, and maintenance packages

- `biology/current_claims.py` loads `manuscript/current_claims.yaml` as `CurrentClaim` records and validates source tier, source URL, checked date, refresh trigger, anchor text, and stale-phrase coverage. The script gate is `../scripts/audit_current_claims.py --check`; the test gate is `../tests/test_current_claims_ledger.py`.
- `biology/assessment.py` parses question-bank item metadata comments and lab alignment blocks as `QuestionBankAssessment`, `QuestionAssessment`, and `LabAlignment`. Keep it in sync with `../scripts/sync_assessment_metadata.py`; tests are `../tests/test_assessment_metadata.py` and `../tests/test_lab_pedagogy_alignment.py`.
- `biology/quality/` — umbrella audit engine and `publication_gate.py` aggregate orchestrator; see `biology/quality/AGENTS.md`.
- `biology/enrichment/` — embedded frontier/companion catalog and apply engine; see `biology/enrichment/AGENTS.md`.
- `biology/answer_refinement/` — heuristic question-bank answer upgrades; see `biology/answer_refinement/AGENTS.md`.
- `biology/curriculum_sync/` — Study Blueprint and appendix curriculum sync; see `biology/curriculum_sync/AGENTS.md`.

## `mermaid/`

Three files plus spec loader:

- `renderer.py` — `MermaidRenderer` class; invokes `mmdc` (Mermaid CLI) with optional `.puppeteer.json` for system Chrome; writes `.mmd` fallback when `mmdc` is missing unless `strict_png=True`.
- `diagrams.py` — generic builders (flowchart, sequence, graph).
- `diagram_spec_loader.py` + `diagram_specs.yaml` — declarative diagram metadata.
- `biology_diagrams.py` — domain-specific factories and the `ALL_BIOLOGY_DIAGRAMS` registry (24 diagrams used throughout the manuscript).

## `visualization/`

`__init__.py` hosts all matplotlib generators. Each has the signature `fn(output_dir: Path) -> Path` and saves a PNG at 150 dpi with `bbox_inches="tight"`. The registry `ALL_FIGURE_GENERATORS` maps a short name to the callable:

```python
ALL_FIGURE_GENERATORS = [
    ("nernst_potentials", plot_nernst_potentials),
    ("punnett_square", lambda output_dir: plot_punnett_square("Aa", "Aa", output_dir)),
    # … 12 more
]
```

Every entry **must** be referenced from a chapter (`test_every_registered_figure_is_referenced`) and every `\label{fig:…}` **must** have prose `\cref{fig:…}` (`test_every_figure_label_has_prose_cref`). Use `../scripts/insert_orphan_figures.py` to insert a reference if you add a generator.

Treat `ALL_FIGURE_GENERATORS` and `ALL_BIOLOGY_DIAGRAMS` as the visual manifests. Do not add unregistered visuals for reusable assets; register them, generate them, reference them from manuscript prose, and keep alt/caption text close to the image or inline Mermaid fence.

## Imports

Tests and scripts put both `src/` and the template root on `sys.path` (see `../tests/conftest.py`). Typical imports:

```python
from biology.biochemistry import michaelis_menten
from biology.genetics import punnett_square, hardy_weinberg
from biology.crossref_validator import validate
from biology.chapter_metadata import CHAPTERS, by_id
from mermaid.biology_diagrams import ALL_BIOLOGY_DIAGRAMS
from visualization import ALL_FIGURE_GENERATORS
```

> [!NOTE]
> `biology/__init__.py` imports every subpackage at package-import time. Subpackages use `textbook_logging.get_logger`, which delegates to template infrastructure logging when available and otherwise falls back to stdlib logging for standalone checkouts.

## Conventions

- Zero mocks — all tests use real numerical inputs (see `../docs/testing_guide.md`).
- Type hints on all public functions.
- Result objects are `@dataclass(frozen=True)` where immutability is natural.
- Deterministic RNG — simulations accept a `seed` argument; plots use fixed seeds.
- No inline `plt.show()`; always save to disk (`MPLBACKEND=Agg` is set by `conftest.py`).

## See also

- [`../AGENTS.md`](../AGENTS.md) — project-level reference and invariants
- [`../docs/architecture.md`](../docs/architecture.md) — subpackage table with tests
- [`../docs/api_reference.md`](../docs/api_reference.md) — full function API
- [`../docs/testing_guide.md`](../docs/testing_guide.md) — zero-mock policy
