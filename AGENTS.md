# Biology Textbook — Agent Documentation

## Location and pipeline status

This is an active standalone checkout. Run project-local commands so its `pyproject.toml` and output custody apply. Rendering uses `scripts/render_textbook.py` with an explicitly selected read-only template library; do not run template-root stage wrappers. **Publication:** `docs/manuscript/config.yaml` separates the current edition from the prior-release archive DOI.

Use thin orchestrators in `scripts/`, computation in `src/`, manuscript in `docs/manuscript/`, and tests in `tests/`. The configured coverage gate is 90% of the branch-enabled reported total with explicit omissions, not separate line/branch floors. Scientific behavior uses real algorithms; filesystem/environment/failure isolation is documented in [docs/testing_guide.md](docs/testing_guide.md).

**Composable authoring (stable `sec:` / `fig:` / `eq:` IDs, script order, which tests fail when):** [docs/composable_authoring.md](docs/composable_authoring.md). **Editorial** style for agents: [docs/agent_instructions.md](docs/agent_instructions.md). **Accessibility / config enforcement vs advisory:** [docs/accessibility.md](docs/accessibility.md). **Doc index:** [docs/README.md](docs/README.md).

## Manuscript Source Contract

Introductory biology textbook content is driven by **`docs/manuscript/config.yaml`**: unit ordering, chapter files, front matter, appendices (labs and question banks), and render metadata. Domain subpackages under `src/biology/` include `foundations/` alongside the nine traditional biology domains. Mermaid diagrams are declared in **`src/mermaid/diagram_specs.yaml`** and built via `src/mermaid/diagram_spec_loader.py`; matplotlib figures live in **`src/visualization/plots_*.py`** modules and register through `plots.py` → `ALL_FIGURE_GENERATORS`.

Canonical ordering and filenames live in `config.yaml`: Unit 0 plus Units I–X, **44 core chapters**, 44 paper-based labs and 44 thirty-item banks. Source H1s, stable identifiers, reference types, authored assessments and generated-block ownership are defined in [the manuscript contract](docs/manuscript/AGENTS.md), not duplicated here.

For current claims use `docs/manuscript/current_claims.yaml` and `scripts/audit_current_claims.py --check`. For reviewed item mappings and lab rubrics use `scripts/sync_assessment_metadata.py --check`; see [the pedagogy contract](docs/pedagogy_objectives_mapping.md).

---

## PDF typography and page layout

Student PDFs are built **compact** by default:

| Setting | `docs/manuscript/config.yaml` | `docs/manuscript/preamble.md` (LaTeX) |
| ------- | ------------------------ | -------------------------------- |
| Margins | `layout.margin_*_mm` → **2** | `geometry` → **2 mm** all sides, `headheight=12pt` |
| Body size | `typography.base_font_size_pt` → **9** | `\renewcommand{\normalsize}{...9}{10.8}...` |
| Line spacing | `layout.line_height` → **1.28** | `\setstretch{1.28}` |
| Headings / captions | (metadata only) | `titlesec` sizes; `caption` → `footnotesize`; header/footer → `footnotesize` |

**Rule:** Changing density requires editing **both** files so YAML comments and the rendered PDF stay aligned. Full authoring rules (figure/diagram allowlists, footers) are in [docs/manuscript/AGENTS.md](docs/manuscript/AGENTS.md).

---

## Domain modules (`src/biology/`)

| Subpackage | Typical manuscript topics |
| ---------- | ------------------------- |
| `foundations/` | Systems/complexity teaching models, biology milestone dates and chemical/macromolecular reference tables |
| `biochemistry/` | Enzyme kinetics, ΔG, pathways |
| `cell/` | Organelles, Nernst/Goldman, transport, signaling |
| `genetics/` | DNA/RNA, Punnett, Hardy–Weinberg, genomics |
| `evolution/` | Selection, drift, clock, speciation |
| `ecology/` | Growth models, Lotka–Volterra, diversity |
| `physiology/` | Circulation, gas transport, homeostasis |
| `microbiology/` | Growth curves, MIC, viral parameters |
| `botany/` | Water relations, photosynthesis pathways |
| `neuroscience/` | Hodgkin–Huxley, passive cable, synaptic transmission, Hebbian plasticity |

Shared utilities: `numerics.py` (Euler integration), `constants.py` (physical constants), `assessment.py`, `chapter_metadata.py`, `current_claims.py`, `toc.py`.

Maintenance packages (logic in `src/`, thin CLIs in `scripts/`):

| Package | Script | Role |
| --- | --- | --- |
| `crossref/` | — | Manuscript `\label`/`\cref` scanner (re-exported as `crossref_validator.py`) |
| `quality/` | `audit_textbook_quality.py` | Umbrella quality audit + advisory ledger |
| `enrichment/` | `enrich_embedded_textbook.py` | Frontier boxes, companion modules, audit matrix |
| `answer_refinement/` | `refine_generated_answers.py` | Preserve authored keys; unsupported answer repair refuses without writing |
| `curriculum_sync/` | `sync_curriculum_materials.py` | Canonical H1s/identifiers, blueprints, navigation and generated appendices; preserves authored assessment bodies |
| `visual_contracts/` | `audit_visual_contracts.py` | Figure/diagram manifest gate |

Root I/O: `textbook_io.py` (`write_text_atomic`); `textbook_paths.py` for shared path helpers.

Curriculum synchronization must not generate lab procedures, question prompts or
keys, rubrics, or coverage notes. Former lab/question body sync functions and
ownership markers are retired. Preserve authored assessment content; validate
semantic mappings with `sync_assessment_metadata.py`, and use the native repeated
CLI regression for byte/mtime/inode stability rather than success counters.

---

## Source layout and ownership

- `src/biology/`: scientific models, metadata and maintenance packages; see [architecture](docs/architecture.md) and [API reference](docs/api_reference.md).
- `src/visualization/`: domain `plots_*.py` implementations, `plots.py` registry, public `__init__.py` facade and `cvd.py` palette.
- `src/mermaid/`: registered specifications/factories and renderer. `.mmd` fallback is authoring output, never publication proof.
- `scripts/`: project-local thin entry points; use the [pipeline guide](docs/pipeline_guide.md) for commands and output custody.
- `tests/`: numerical, source, maintenance and integration behavior; use the [testing guide](docs/testing_guide.md), not a copied mutable inventory.
- `docs/manuscript/`: config-owned order and authored content; `output/` is generated/disposable.

Optional project-root `.puppeteer.json` selects browser configuration for `mmdc`; inspect its host compatibility before rendering. Missing native tools do not establish a successful publication render.

---

## Validation and verification ownership

Run from the standalone project root after the locked setup in [README](README.md#standalone-quick-start):

```bash
uv run --frozen --extra dev python scripts/audit_publication_readiness.py --check
```

Add `--full` for tests with configured coverage, analysis, a fresh native render and strict PDF-log checks. A successful source gate alone is not PDF inspection or remote publication. [Pipeline](docs/pipeline_guide.md) owns prerequisites and artifacts; [testing](docs/testing_guide.md) owns named test nodes and isolation limits; [composable authoring](docs/composable_authoring.md) owns ordered edit workflows.

Preserve canonical H1s and all `sec:`/`fig:`/`eq:`/`tbl:` IDs. Numbered chapters/figures/equations/tables use `\cref`; unnumbered surfaces use `\nameref`. Every inline Mermaid fence needs one substantive alt comment and one matching caption; publication requires decoded PNGs. Derive visual inventories from configured sources and manifests, not copied counts. Bibliography closure, resolved prerequisites and structural tests do not prove scientific accuracy or causal/prerequisite completeness.

## Protocol for AI agents

1. For **new chapters, new `plot_*` / `*_diagram()` registrations, or cross-reference refactors**, read [docs/composable_authoring.md](docs/composable_authoring.md) first, then [docs/manuscript/AGENTS.md](docs/manuscript/AGENTS.md).
2. Read [docs/agent_instructions.md](docs/agent_instructions.md) for editorial voice and chapter structure targets.
3. Read [docs/testing_guide.md](docs/testing_guide.md) before changing tests.
4. Read [docs/architecture.md](docs/architecture.md) before changing `scripts/` vs `src/` boundaries.
5. New quantitative claims in prose should map to tested code in the appropriate `src/biology/` module when feasible.
6. Prefer `textbook_logging.get_logger(__name__)` in Python entrypoints; it uses template infrastructure logging when available and falls back to stdlib logging in standalone checkouts.
7. Treat `ALL_FIGURE_GENERATORS` and `ALL_BIOLOGY_DIAGRAMS` as visual manifests: add the generator/factory to the registry, reference it from manuscript prose, keep alt/caption text nearby, and verify the corresponding tests before relying on the visual.
8. After any manuscript edit that adds chapters, figures, diagrams, citations, current claims, labs, or question banks, re-run the relevant `scripts/insert_*` / `scripts/link_*` / `scripts/integrate_*` / audit helper and verify invariant tests still pass (see [docs/testing_guide.md](docs/testing_guide.md) failure-to-fix table).

## See also

- [docs/composable_authoring.md](docs/composable_authoring.md) — stable labels, workflows, validation commands
- [docs/accessibility.md](docs/accessibility.md) — `config.yaml` vs pytest enforcement; CVD; reader profile
- [docs/pedagogy_objectives_mapping.md](docs/pedagogy_objectives_mapping.md) — required reviewed per-item assess comments and lab alignment metadata
- [docs/README.md](docs/README.md) — documentation index
- [docs/manuscript/AGENTS.md](docs/manuscript/AGENTS.md) — source/identifier and assessment ownership contract
- [docs/manuscript/README.md](docs/manuscript/README.md) — author quick reference and course pathways
