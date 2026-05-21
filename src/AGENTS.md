# `src/` — AGENTS.md

## Role

All scientific computation and manuscript-consumed metadata for the biology textbook lives here. The test suite runs against these modules; scripts in `../scripts/` import from here and only coordinate I/O and rendering — **no business logic belongs in scripts.**

## Layout

```text
src/
├── __init__.py
├── biology/                      # nine domain subpackages + manuscript utilities
│   ├── __init__.py
│   ├── biochemistry/biochemistry.py
│   ├── botany/botany.py
│   ├── cell/cell_biology.py
│   ├── ecology/ecology.py
│   ├── evolution/evolution.py
│   ├── genetics/genetics.py
│   ├── microbiology/microbiology.py
│   ├── neuroscience/neuroscience.py
│   ├── physiology/physiology.py
│   ├── chapter_metadata.py        # per-chapter difficulty / reading time / lecture time / prereqs
│   ├── toc.py                     # canonical units/chapters/labs/questions/reference appendices
│   ├── current_claims.py          # current-claim ledger loader and validator
│   ├── assessment.py              # question-bank and lab assessment metadata parser
│   ├── curriculum.py              # learning objectives and curriculum records
│   ├── alignment.py               # standards, skills, and instructor alignment
│   └── crossref_validator.py      # \label / \cref / @ref scanner + hard-coded prose refs
├── mermaid/                       # Mermaid source + renderer
│   ├── renderer.py
│   ├── diagrams.py
│   └── biology_diagrams.py        # ALL_BIOLOGY_DIAGRAMS (24 diagrams)
└── visualization/
    └── __init__.py                # ALL_FIGURE_GENERATORS (18 matplotlib generators)
```

## `biology/` — nine domain subpackages

Each subpackage exposes frozen result dataclasses (`EnzymeKineticsResult`, `PunnettSquareResult`, `ActionPotentialResult`, `SIRResult`, …) and pure functions. See [`../docs/api_reference.md`](../docs/api_reference.md) for the full function-by-function API and [`../docs/architecture.md`](../docs/architecture.md) for the test-file mapping.

| Subpackage | Topic | Representative functions |
| ---------- | ----- | ------------------------ |
| `biochemistry` | Enzyme kinetics, bioenergetics | `michaelis_menten`, `glycolysis_summary`, `atp_free_energy` |
| `cell` | Membrane biophysics, organelles | `nernst_potential`, `goldman_equation`, `osmotic_pressure`, `ORGANELLES` |
| `genetics` | DNA/RNA, crosses, population genetics | `punnett_square`, `translate_mrna`, `hardy_weinberg`, `GENETIC_CODE` |
| `evolution` | Selection, drift, speciation | `simulate_selection`, `simulate_drift`, `molecular_clock_divergence_time` |
| `ecology` | Growth models, diversity | `logistic_growth`, `lotka_volterra`, `biodiversity_indices`, `BIOME_DATA` |
| `physiology` | Circulation, gas exchange | `poiseuille_flow`, `oxygen_saturation`, `homeostasis_response` |
| `microbiology` | Growth curves, MIC, transmission | `bacterial_growth_curve`, `mic_fold_dilution`, `sir_model` |
| `botany` | Water relations, photosynthesis | `water_potential`, `transpiration_flux`, `photosynthesis_rate` |
| `neuroscience` | Action potentials, passive cables, synapses | `action_potential_hh`, `cable_voltage_attenuation`, `synaptic_current` |

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
- Inline `$$…$$` display equations (with `\tag{}` or `\label{}`)
- Markdown images with `{#fig:…}` pandoc-crossref attributes
- Table captions `Table: … {#tbl:…}`
- Section labels `## Heading {#sec:…}`
- Cross-reference usages `@fig:`, `@eq:`, `@tbl:`, `@sec:`
- Hand-typed rendered-number prose references such as `Chapter N`, `Figure N`, `Equation N`, `Section N`, and `§N`

Exports `CrossRefIssue`, `CrossRefReport`, `scan_file`, `scan_directory`, `validate`, `suggest_id`. Covered by three test files (`test_crossref_validator.py`, `test_crossref_validator_internals.py`, `test_crossref_validator_edges.py`).

## Current-claims and assessment utilities

- `biology/current_claims.py` loads `manuscript/current_claims.yaml` as `CurrentClaim` records and validates source tier, source URL, checked date, refresh trigger, anchor text, and stale-phrase coverage. The script gate is `../scripts/audit_current_claims.py --check`; the test gate is `../tests/test_current_claims_ledger.py`.
- `biology/assessment.py` parses question-bank item metadata comments and lab alignment blocks as `QuestionBankAssessment`, `QuestionAssessment`, and `LabAlignment`. Keep it in sync with `../scripts/sync_assessment_metadata.py`; tests are `../tests/test_assessment_metadata.py` and `../tests/test_lab_pedagogy_alignment.py`.

## `mermaid/`

Three files:

- `renderer.py` — `MermaidRenderer` class; invokes `mmdc` (Mermaid CLI) with optional `.puppeteer.json` for system Chrome; writes `.mmd` fallback when `mmdc` is missing unless `strict_png=True`.
- `diagrams.py` — generic builders (flowchart, sequence, graph).
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

Every entry **must** be referenced from a chapter (invariant `test_build_invariants.py::test_every_registered_figure_is_referenced`). Use `../scripts/insert_orphan_figures.py` to insert a reference if you add a generator.

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
> `biology/__init__.py` imports every subpackage at package-import time. Some subpackages use `from infrastructure.core.logging.utils import get_logger`, so either run from the template root with `infrastructure/` on `sys.path`, or dynamically load `biology.chapter_metadata` / `biology.crossref_validator` via `importlib.util` (as tests do) to avoid triggering the chain.

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
