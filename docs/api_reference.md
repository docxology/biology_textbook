# API Reference — `src/biology/` Public Functions

**Covers:** nine domain subpackages (biochemistry, cell, genetics, evolution, ecology, physiology, microbiology, botany, neuroscience), curriculum/orchestration metadata (`chapter_metadata`, `curriculum`, `alignment`), manuscript utilities (`crossref_validator`), `src/mermaid/biology_diagrams`, and `src/visualization` (including `cvd.py`). Public entry points are exercised by the project test suite (`uv run pytest tests/ --cov=src` from the project directory for current counts and coverage floors).

**Maintenance:** This file lists the main public entry points used from manuscript and tests. It is not an exhaustive dump of every `def` in `src/biology/` (helpers and module-private functions are omitted). After adding a user-facing function, add a row here; for a quick audit run `rg '^\s*def ' src/biology` and reconcile new names.

## `biology.biochemistry`

| Function | Arguments | Returns | Description |
| -------- | --------- | ------- | ----------- |
| `michaelis_menten(substrate_conc, Vmax, Km)` | floats | `EnzymeKineticsResult` | Reaction rate v by MM equation |
| `competitive_inhibition(substrate_conc, Vmax, Km, inhibitor_conc, Ki)` | floats | `EnzymeKineticsResult` | Apparent-Km shift under competitive inhibition |
| `enzyme_rate_curve(Vmax, Km, n_points=50, max_conc=None)` | floats, int | `list[EnzymeKineticsResult]` | Michaelis-Menten curve samples |
| `reaction_free_energy(delta_G_standard_kJ, product_conc, reactant_conc, temperature_K=310.0)` | floats | float | Actual ΔG from ΔG° and reaction quotient |
| `atp_free_energy(atp_conc_mM=3.0, adp_conc_mM=1.0, pi_conc_mM=10.0, temperature_K=310.0)` | floats | float | Cellular ΔG of ATP hydrolysis |
| `glycolysis_summary()` | — | `GlycolysisResult` | ATP yield, NADH, pyruvate, and pathway steps |

## `biology.cell`

| Function | Arguments | Returns | Description |
| -------- | --------- | ------- | ----------- |
| `nernst_potential(ion)` | `IonConcentration` | float (mV) | Equilibrium potential |
| `goldman_equation(ions, permeabilities)` | lists | float (mV) | Resting membrane potential |
| `osmotic_pressure(concentration_mOsm)` | float | float (Pa) | van't Hoff osmotic pressure |
| `diffusion_flux(permeability, area, concentration_out, concentration_in)` | floats | `MembraneTransportResult` | Passive membrane flux and direction |
| `compute_all_nernst_potentials()` | — | dict[str, float] | Reference Nernst potentials for physiological ions |
| `receptor_occupancy(ligand_conc, Kd)` | floats | float | Fractional receptor occupancy |
| `hill_equation(ligand_conc, Kd, hill_coefficient)` | floats | float | Cooperative ligand response |
| `signal_amplification(initial_signal, amplification_factor, steps)` | floats, int | list[float] | Multiplicative signal cascade |
| `ORGANELLES` | — | dict | Organelle inventory with functions |

## `biology.genetics`

| Function | Arguments | Returns | Description |
| -------- | --------- | ------- | ----------- |
| `punnett_square(parent1, parent2)` | str, str | `PunnettSquareResult` | Genotype/phenotype distributions |
| `translate_mrna(mrna)` | str | list[str] | mRNA → amino-acid names until stop codon |
| `transcribe_dna_to_mrna(dna)` | str | str | DNA template → mRNA |
| `dna_complement(sequence)` | str | str | 5'→3' complement |
| `hardy_weinberg(p, q=None, dominant_homozygous_freq=None, recessive_homozygous_freq=None)` | floats | `HardyWeinbergResult` | Genotype frequencies at HW eq. |
| `chi_squared_test(observed, expected, alpha=0.05)` | lists, float | `ChiSquaredResult` | χ² statistic + approximate p-value |
| `recombination_frequency(recombinants, total)` | ints | float | Recombination fraction, 0–1 |
| `genetic_distance(recombinants, total)` | ints | float (cM) | Map distance in centimorgans |
| `infer_three_point_order(distances_cM)` | dict[tuple[str, str], float] | `LinkageMapResult` | Simple three-marker gene-order inference |
| `hamming_distance(seq1, seq2)` | strings | int | Count mismatched positions |
| `jukes_cantor_distance(observed_divergence)` | float | float | JC69 corrected distance |
| `cpg_methylation_remaining(initial_methylation, divisions, maintenance_efficiency)` | floats, int | float | Maintenance methylation across cell divisions |
| `histone_modification_state(mark)` | str | str | Interpret common histone marks |
| `GENETIC_CODE` | — | dict | Codon → amino acid mapping |

## `biology.evolution`

| Function | Arguments | Returns | Description |
| -------- | --------- | ------- | ----------- |
| `selection_one_generation(pop)` | `Population` | `Population` | One viability-selection update |
| `simulate_selection(initial_pop, generations)` | `Population`, int | `list[SelectionResult]` | Allele-frequency trajectory under selection |
| `wright_fisher_drift(p, N, rng_seed=42)` | float, int | float | One Wright-Fisher drift generation |
| `simulate_drift(p, N, generations, rng_seed=42)` | float, int | list[float] | Stochastic drift trajectory |
| `fitness_landscape_1d(allele_freqs, fitness_AA, fitness_Aa, fitness_aa)` | list[float], floats | list[float] | Mean fitness across allele frequencies |
| `molecular_clock_divergence_time(substitution_rate_per_site_per_year, sequence_divergence)` | floats | float | Divergence time in years |
| `isolation_index(gene_flow_rate, mutation_rate)` | floats | float | Isolation proxy from gene flow and mutation |

## `biology.ecology`

| Function | Arguments | Returns | Description |
| -------- | --------- | ------- | ----------- |
| `logistic_growth(N0, r, K, t_end, steps=200)` | nums | `PopulationGrowthResult` | Euler integration of $dN/dt = rN(1-N/K)$ |
| `allee_strong_growth(N0, r, A, K, t_end, steps=500)` | nums | `PopulationGrowthResult` | Strong Allee: $dN/dt = rN(N/A-1)(1-N/K)$ |
| `exponential_growth(N0, r, t_end, steps=100)` | nums | `PopulationGrowthResult` | $dN/dt = rN$ |
| `lotka_volterra(prey0, predator0, alpha, beta, delta, gamma, t_end, steps=1000)` | nums | `LotkaVolterraResult` | Coupled predator–prey ODEs |
| `biodiversity_indices(species_counts)` | list[int] | `BiodiversityResult` | Shannon, Simpson, richness, evenness |
| `species_area_relationship(A, c, z)` | floats | float | $S = c A^z$ |
| `food_web_trophic_levels(adjacency)` | dict[str, list[str]] | dict[str, int] | BFS trophic levels from producers |
| `connectance(num_species, num_links)` | ints | float | $L/S^2$ |
| `BIOME_DATA` | — | dict | Biome NPP metadata for figures |

## `biology.physiology`

| Function | Arguments | Returns | Description |
| -------- | --------- | ------- | ----------- |
| `poiseuille_flow(pressure_difference_Pa, radius_m, length_m, viscosity_Pa_s=3e-3)` | floats | `BloodFlowResult` | Volume flow rate (m³/s), mL/min, Reynolds number |
| `oxygen_saturation(pO2_mmHg, p50_mmHg=26.0, hill_coefficient=2.7)` | floats | `RespiratoryResult` | O₂-Hb saturation (0–1) |
| `oxygen_dissociation_curve(p50_mmHg=26.0, n_points=100, max_pO2=150.0)` | floats, int | `list[RespiratoryResult]` | Full dissociation curve |
| `homeostasis_response(set_point, measured_value, gain=1.0, tolerance=0.05)` | nums | `HomeostasisResult` | Proportional negative-feedback response |
| `ORGAN_SYSTEMS` | — | dict | Organ system inventory |

## `biology.microbiology`

| Function | Arguments | Returns | Description |
| -------- | --------- | ------- | ----------- |
| `bacterial_growth_curve(N0, doubling_time_hr, t_end_hr, steps=200, lag_phase_hr=1.0, stationary_phase_start_hr=None, carrying_capacity=None)` | nums | `GrowthCurveResult` | Exponential bacterial growth with lag/stationary phases |
| `doubling_time(N0, Nt, elapsed_time_hr)` | floats | float | Doubling time from population counts |
| `mic_fold_dilution(starting_concentration_ug_mL, dilution_factor, n_tubes)` | floats, ints | list[float] | Antibiotic concentrations across serial dilution |
| `basic_reproduction_number(beta_per_day, gamma_per_day)` | floats | float | SIR R0 = β/γ |
| `sir_model(population, initial_infected, beta_per_day, gamma_per_day, days, steps_per_day=4)` | ints/floats | `SIRResult` | Closed-population SIR outbreak trajectory |
| `REFERENCE_ORGANISMS` | — | list | Reference bacteria/archaea metadata |

## `biology.botany`

| Function | Arguments | Returns | Description |
| -------- | --------- | ------- | ----------- |
| `water_potential(solute_concentration_M, turgor_pressure_MPa, temperature_K=298.0)` | floats | `WaterPotentialResult` | ψ = ψs + ψp |
| `transpiration_flux(stomatal_conductance_mol_m2_s, internal_vapor_conc_mol_m3, external_vapor_conc_mol_m3)` | floats | `TranspirationResult` | E = g_s · ΔC |
| `photosynthesis_rate(photon_flux_µmol_m2_s, max_rate_µmol_CO2_m2_s=20.0, light_saturation_point=800.0, dark_respiration_µmol_CO2_m2_s=1.5)` | floats | float | Net photosynthesis light-response rate |
| `light_response_curve(max_rate=20.0, light_saturation_point=800.0, dark_respiration=1.5, n_points=50, max_par=2000.0)` | floats, int | `list[tuple[float, float]]` | PAR vs net photosynthesis curve |
| `plant_biomass_growth(initial_biomass_g, relative_growth_rate, carrying_capacity_g, duration_days, steps=100)` | floats, int | `PlantGrowthResult` | Logistic biomass accumulation |
| `PHOTOSYNTHESIS_PATHWAYS` | — | list | C3/C4/CAM comparative data |

## `biology.neuroscience`

| Function | Arguments | Returns | Description |
| -------- | --------- | ------- | ----------- |
| `action_potential_hh(stimulus_current_µA=10.0, t_end_ms=30.0, steps=3000, ...)` | floats, int | `ActionPotentialResult` | Simplified Hodgkin-Huxley voltage trace |
| `cable_voltage_attenuation(V0_mV, axial_resistance_Ohm_cm=100.0, membrane_resistance_kOhm_cm2=50.0, axon_radius_cm=5e-4, ...)` | floats | `CableResult` | Passive voltage decay along a dendrite/axon cable |
| `synaptic_current(reversal_potential_mV, membrane_potential_mV, peak_conductance_nS, synapse_type="excitatory")` | floats, str | `SynapticResult` | Driving force and peak synaptic current |
| `hebbian_weight_update(current_weight, pre_activity, post_activity, learning_rate=0.01, weight_max=1.0, weight_min=0.0)` | floats | float | Clipped Hebbian synaptic-weight update |
| `BRAIN_REGIONS` | — | dict | Brain-region inventory and functions |

## `biology.toc`

Canonical table-of-contents API consumed by maintenance scripts. It reads
`manuscript/config.yaml` and `biology.chapter_metadata` to derive renderable
display titles for units, chapters, labs, question banks, reference appendices,
front-matter navigation, and the Course Planning Grid.

| Symbol | Kind | Description |
| ------ | ---- | ----------- |
| `load_toc(project_root=None)` | function | Return a `BookToc` for the project |
| `BookToc` | frozen dataclass | Units, chapters, companion sections, reference appendices |
| `UnitTocItem` | frozen dataclass | Unit title, intro title, and chapter list |
| `ChapterTocItem` | frozen dataclass | Chapter title, path, `ChapterMeta`, and companion-title helpers |
| `CompanionTocItem` | frozen dataclass | Lab or question-bank path/title derived from its parent chapter |
| `ReferenceTocItem` | frozen dataclass | Reference appendix file/title/path from config |

Tests: `tests/test_toc_consistency.py` asserts renderable H1s, front-matter
navigation, appendices, and Course Planning Grid rows match canonical ToC data.

## `biology.chapter_metadata`

Per-chapter pedagogical metadata used by `scripts/insert_chapter_metadata.py`
to generate chapter badges. The Course Planning Grid combines this metadata
with canonical chapter titles from `biology.toc`.

| Symbol | Kind | Description |
| ------ | ---- | ----------- |
| `ChapterMeta(chapter_id, number, unit, difficulty, reading_time_min, lecture_time_min, prerequisites)` | frozen dataclass | One record per chapter |
| `ChapterMeta.difficulty_label` | property | PDF-safe string such as `Level 2/3` for rendered badges |
| `ChapterMeta.star_badge` | property | Legacy 3-char star string kept for compatibility tests only |
| `CHAPTERS` | `list[ChapterMeta]` | All 38 configured chapters, ordered as in `config.yaml` |
| `by_id(chapter_id)` | `ChapterMeta \| None` | Look up a single chapter record |
| `by_unit(unit)` | `list[ChapterMeta]` | All chapters in a given unit ("0", "I", …, "X") |

**`chapter_id` and `sec:` labels:** `chapter_id` is `unit_<X>_<stem>` (e.g. `unit_I_water_and_life`). The manuscript section label is `\label{sec:<chapter_id>}` — the same string with the `sec:` prefix. **Prerequisites** in `ChapterMeta` are a tuple of other **`chapter_id` strings** (not `\cref` text); insert scripts turn them into prerequisite links using `\cref{sec:...}` in the metadata badge. See [composable_authoring.md](composable_authoring.md).

Tests: `tests/test_chapter_metadata.py` asserts every `config.yaml` chapter has a record, prerequisites resolve, difficulty ∈ {1, 2, 3}, and chapter numbers are contiguous.

## `biology.curriculum`

Per-chapter curriculum spine consumed by `scripts/sync_curriculum_materials.py`.
Each record connects a chapter to its lab, question bank, model/data skill,
misconception probe, transfer task, and bridge API.

| Symbol | Kind | Description |
| ------ | ---- | ----------- |
| `CurriculumRecord(...)` | frozen dataclass | One instructional record per chapter |
| `CurriculumRecord.lab_label` | property | Companion lab `sec:` label |
| `CurriculumRecord.question_label` | property | Companion question-bank `sec:` label |
| `CURRICULUM` | `tuple[CurriculumRecord, ...]` | All 38 chapter records in `config.yaml` order |
| `CURRICULUM_BY_ID` | mapping | Fast lookup by `chapter_id` |
| `by_id(chapter_id)` | `CurriculumRecord \| None` | Optional lookup |
| `require(chapter_id)` | `CurriculumRecord` | Strict lookup with a clear error |

Tests: `tests/test_curriculum_metadata.py` checks ID coverage, companion files,
bridge API resolution, generated blocks, and the curriculum appendix.

## `biology.alignment`

Framework and instructor-orchestration metadata layered above
`biology.curriculum`. It maps each chapter to Vision & Change concepts and
competencies, AP Biology big ideas and science practices, NGSS-style
high-school life-science topics, and BioSkills categories.

| Symbol | Kind | Description |
| ------ | ---- | ----------- |
| `UnitAlignment(...)` | frozen dataclass | Unit-level default alignment |
| `AlignmentRecord(...)` | frozen dataclass | Chapter-level framework and instructor metadata |
| `UNIT_ALIGNMENTS` | mapping | Defaults for Unit 0 and Units I-X |
| `ALIGNMENTS` | `tuple[AlignmentRecord, ...]` | One record per curriculum chapter |
| `ALIGNMENTS_BY_ID` | mapping | Fast lookup by `chapter_id` |
| `by_id(chapter_id)` | `AlignmentRecord \| None` | Optional lookup |
| `require(chapter_id)` | `AlignmentRecord` | Strict lookup with a clear error |
| `framework_counts(records=ALIGNMENTS)` | dict | Count framework labels across records |

Tests: `tests/test_curriculum_metadata.py` asserts alignment coverage, known
framework labels, instructional completeness, and generated Appendix B links.

## `biology.crossref_validator`

Manuscript-wide pandoc-crossref / LaTeX `\label{}` validator. Consumed by manuscript maintenance scripts and `tests/test_crossref_validator*.py`.

| Symbol | Kind | Description |
| ------ | ---- | ----------- |
| `CrossRefIssue(file, line, kind, problem, suggested_id, context)` | frozen dataclass | One finding (missing / unresolved / duplicate / prose_xref) |
| `CrossRefReport` | dataclass | Aggregate of `defined`, `references`, `issues`; exposes `missing`, `unresolved`, `duplicates`, `prose` |
| `scan_file(path)` | `(defined, references, issues)` | Parse one markdown file |
| `scan_directory(root, patterns)` | `CrossRefReport` | Walk a manuscript tree |
| `validate(manuscript_root)` | `CrossRefReport` | Top-level entry point |
| `suggest_id(kind, path, descriptor, ordinal)` | str | Canonical slug for a new `\label` / `{#fig:}` / etc. |

**When to use:** after bulk-editing chapters, adding `@fig:` / `@eq:` references, or changing `{#fig:...}` / `\label{...}` — run `validate(manuscript_root)` in a small script or rely on `pytest tests/test_crossref_validator*.py`. Same logical checks as infrastructure `prerender` for undefined citations, plus label graph integrity.

Detects raw-LaTeX figure environments (`\begin{figure}…\label{fig:…}…\end{figure}`), LaTeX equation environments, inline `$$…$$` display math (with `\tag{}` or `\label{}`), table captions (`Table: … {#tbl:…}`), markdown images (`![alt](…){#fig:…}`), section labels (`## Heading {#sec:…}`), and cross-references (`@fig:`, `@eq:`, `@tbl:`, `@sec:`). Details: [composable_authoring.md](composable_authoring.md).

## `visualization.cvd`

Constants for **colour-vision–friendly** matplotlib styling (blue/orange/teal, Punnett hatching, line styles for overlapping series). Consumed by `src/visualization/plots.py`. Aligns with `manuscript/config.yaml` → `accessibility.color_blindness_safe: true` — see [accessibility.md](accessibility.md) and [visualisation_guide.md](visualisation_guide.md).

| Symbol | Role |
| ------ | ---- |
| `BAR_POS`, `BAR_NEG` | Signed bar charts (e.g. Nernst) |
| `PUNNETT_DOMINANT`, `PUNNETT_RECESSIVE` | Punnett cells (with hatch patterns in the square plot) |
| `SERIES2`, `SERIES3` | Default multi-line series colours |

## `mermaid.biology_diagrams`

`ALL_BIOLOGY_DIAGRAMS` currently registers **24** `MermaidDiagram` objects. Keep this table in sync with the registry names (not just the factory names) in `src/mermaid/biology_diagrams.py`.

| Factory | Registry name | Title / topic |
| ------- | ------------- | ------------- |
| `macromolecule_classification_diagram()` | `macromolecule_classification` | Macromolecule classes, components, and functions |
| `enzyme_kinetics_diagram()` | `enzyme_kinetics` | Enzyme catalysis cycle and transition-state stabilization |
| `organelle_function_diagram()` | `organelle_functions` | Eukaryotic organelle functions |
| `membrane_transport_diagram()` | `membrane_transport` | Membrane transport by energy source and cargo size |
| `glycolysis_pathway_diagram()` | `glycolysis_pathway` | Glycolysis investment, cleavage, and payoff |
| `atp_synthesis_diagram()` | `atp_synthesis` | Oxidative phosphorylation electron flow to ATP |
| `cell_cycle_diagram()` | `cell_cycle` | Eukaryotic cell cycle |
| `transcription_translation_diagram()` | `central_dogma` | Central dogma |
| `mendelian_cross_diagram()` | `mendelian_monohybrid` | Monohybrid cross |
| `natural_selection_diagram()` | `natural_selection` | Natural selection |
| `phylogenetic_tree_diagram()` | `phylogenetic_tree` | Tree of life and eukaryogenesis |
| `viral_replication_cycle_diagram()` | `viral_lytic_cycle` | Lytic viral replication |
| `photosynthesis_light_dark_diagram()` | `photosynthesis_reactions` | Light reactions and Calvin-Benson cycle |
| `nervous_system_reflex_diagram()` | `reflex_arc` | Spinal reflex arc |
| `immune_response_diagram()` | `immune_response` | Immune response overview |
| `food_web_diagram()` | `terrestrial_food_web` | Terrestrial food web and nutrient recycling |
| `population_growth_stages_diagram()` | `population_growth_phases` | Logistic growth phases |
| `speciation_diagram()` | `speciation_diagram` | Speciation mechanisms |
| `hormone_signaling_diagram()` | `hormone_signaling_diagram` | Hormone signalling pathways |
| `dna_replication_diagram()` | `dna_replication_diagram` | DNA replication fork |
| `nutrient_cycle_diagram()` | `nutrient_cycle_diagram` | Nitrogen cycle |
| `chromosome_inheritance_diagram()` | `chromosome_inheritance_diagram` | Sex-linked inheritance and X-inactivation |
| `mirna_biogenesis_diagram()` | `mirna_biogenesis_diagram` | miRNA biogenesis and RISC loading |
| `x_inactivation_diagram()` | `x_inactivation_diagram` | X-inactivation |

## `visualization` (matplotlib generators)

All plot entry points live in `src/visualization/plots.py`. Each `plot_*` function takes a required `output_dir: Path` and optional numeric parameters; each returns `Path` to a PNG. They are listed in registry order below (same as `ALL_FIGURE_GENERATORS`).

Colour defaults come from [`visualization.cvd`](#visualizationcvd) when multiple series or sign categories are shown. **Allowlist** names (what the manuscript may cite) are in [../manuscript/AGENTS.md](../manuscript/AGENTS.md).

| Registry key | `plot_*` / callable | Output filename (typical) |
| ------------ | -------------------- | --------------------------- |
| `nernst_potentials` | `plot_nernst_potentials` | `nernst_potentials.png` |
| `punnett_square` | `plot_punnett_square(parent1, parent2, …)` (registry uses demo genotypes) | `punnett_*.png` |
| `chromosome_structure` | `plot_chromosome_structure` | `chromosome_structure.png` |
| `oxygen_dissociation` | `plot_oxygen_dissociation` | `oxygen_dissociation_curve.png` |
| `michaelis_menten` | `plot_michaelis_menten` | `michaelis_menten.png` |
| `lotka_volterra` | `plot_lotka_volterra` | `lotka_volterra.png` |
| `selection_simulation` | `plot_selection_simulation` | `selection_simulation.png` |
| `action_potential` | `plot_action_potential` | `action_potential.png` |
| `light_response_curves` | `plot_light_response_curve` | `light_response_curves.png` |
| `bacterial_growth` | `plot_bacterial_growth` | `bacterial_growth.png` |
| `methylation_heatmap` | `plot_methylation_heatmap` | `methylation_heatmap.png` |
| `logistic_growth` | `plot_logistic_growth` | `logistic_growth.png` |
| `species_area_relationship` | `plot_species_area_relationship` | `species_area_relationship.png` |
| `biome_distribution` | `plot_biome_distribution` | `biome_distribution.png` |
