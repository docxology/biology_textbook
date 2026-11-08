# API reference: biological models, manuscript metadata, and rendering

**Covers:** biological domain packages including `foundations`, shared utilities, metadata/maintenance packages, YAML-backed Mermaid diagrams and domain matplotlib modules. This is a curated reference, not an exhaustive export list.

**Maintenance:** This file lists the main public entry points used from manuscript and tests. It is not an exhaustive dump of every `def` in `src/biology/` (helpers and module-private functions are omitted). After adding a user-facing function, add a row here; for a quick audit run `rg '^\s*def ' src/biology` and reconcile new names.

Software 2.0.0 is a breaking release candidate, not fresh runtime proof. Numerical inputs must meet finite-domain constraints. Synthetic examples are teaching models, not empirical measurements or clinical validation.

Existing explicit count/container guards now raise `TypeError` for invalid Python
types (including bool or float-as-count), while admissible numeric types outside
their domain raise `ValueError`. This applies to Euler/ODE steps, replication
origins, CpG divisions, chi-square ddof, network/connectance counts, MIC dilution,
SIR counts and the existing claim/catalog/config/diagram container checks. It is
not a claim that every API performs blanket type validation. NaN/inf abundance
remains a numeric-domain `ValueError`; no new abundance-container restriction was added.

`biology.citations.bib_keys(text)` returns the defined key set and raises
`ValueError` on duplicate identities; it never silently merges two source records.
Quality and orphan-insertion consumers report an invalid bibliography explicitly
while continuing independent diagnostics. Citation closure is not proof of the
scientific meaning or full text of a source.

## `biology.numerics`

| Function | Arguments | Returns | Description |
| -------- | --------- | ------- | ----------- |
| `euler_integrate_scalar(f, y0, t_end, steps)` | callable, float, float, int | `tuple[list[float], list[float]]` | Fixed-step explicit Euler; finite states and valid resolution required; no automatic accuracy guarantee |

## `biology.constants`

| Name | Description |
| ---- | ----------- |
| `FARADAY`, `FARADAY_CONSTANT` | Faraday constant (C/mol) — aliases |
| `GAS_CONSTANT` | Ideal gas constant (J/(mol·K)) |
| `AVOGADRO`, `BOLTZMANN` | Avogadro and Boltzmann constants |

## `biology.biochemistry`

| Function | Arguments | Returns | Description |
| -------- | --------- | ------- | ----------- |
| `michaelis_menten(substrate_conc, Vmax, Km)` | floats | `EnzymeKineticsResult` | Reaction rate v by MM equation |
| `competitive_inhibition(substrate_conc, Vmax, Km, inhibitor_conc, Ki)` | floats | `EnzymeKineticsResult` | Apparent-Km shift under competitive inhibition |
| `enzyme_rate_curve(Vmax, Km, n_points=50, max_conc=None)` | floats, int | `list[EnzymeKineticsResult]` | Michaelis-Menten curve samples |
| `reaction_free_energy(delta_G_standard_kJ, product_conc, reactant_conc, temperature_K=310.0)` | floats | float | Specified 1:1 ideal-dilute quotient; supply the standard energy for matching temperature/convention, not arbitrary stoichiometry or pH/Mg speciation |
| `atp_free_energy(atp_conc_mM=3.0, adp_conc_mM=1.0, pi_conc_mM=10.0, temperature_K=310.0)` | floats | float (kJ/mol) | Ideal-dilute 1-M standard-state model with fixed ΔG°′=-30.5 kJ/mol; not a pH/Mg-speciation model or an AMPK measurement |
| `glycolysis_summary()` | — | `GlycolysisResult` | Per-reaction standard energies with multiplicity; total about -73.97 kJ/mol glucose, not cellular ΔG |

## `biology.cell`

| Function | Arguments | Returns | Description |
| -------- | --------- | ------- | ----------- |
| `nernst_potential(ion)` | `IonConcentration` | float (mV) | Equilibrium potential |
| `goldman_equation(ions, permeabilities)` | lists | float (mV) | GHK for monovalent ions only; divalent ions rejected |
| `osmotic_pressure(concentration_mOsm)` | float | float (Pa) | van't Hoff osmotic pressure |
| `diffusion_flux(permeability, area, concentration_out, concentration_in)` | floats | `MembraneTransportResult` | Passive membrane flux and direction |
| `compute_all_nernst_potentials()` | — | dict[str, float] | Reference Nernst potentials for physiological ions |
| `receptor_occupancy(ligand_concentration, kd)` | floats | float | One-site binding occupancy; `kd` is the dissociation constant |
| `hill_equation(ligand_concentration, kd, hill_coefficient)` | floats | float | Phenomenological occupancy; `kd` supplies the half-response, not generally a microscopic affinity |
| `signal_amplification(initial_signal, amplification_factor, steps)` | floats, int | list[float] | Multiplicative signal cascade |
| `ORGANELLES` | — | dict | Organelle inventory with functions |

## `biology.genetics`

Package layout: `sequence`, `mendelian`, `population`, `linkage`, `distance`, `epigenetics`, `mutation`, `replication` (import via `biology.genetics` or legacy `biology.genetics.genetics` shim).

| Function | Arguments | Returns | Description |
| -------- | --------- | ------- | ----------- |
| `punnett_square(parent1, parent2)` | str, str | `PunnettSquareResult` | Genotype/phenotype distributions |
| `gametes(genotype)` | str | tuple[str, ...] | Gamete strings from a diploid genotype (alias of internal gamete helper) |
| `translate_mrna(mrna)` | str | list[str] | mRNA → amino-acid names until stop codon |
| `transcribe_dna_to_mrna(dna)` | str | str | DNA template → mRNA |
| `dna_complement(sequence)` | str | str | 5'→3' complement |
| `gc_content(sequence)` | str | float | GC fraction for a DNA/RNA sequence |
| `hardy_weinberg(p, q=None, dominant_homozygous_freq=None, recessive_homozygous_freq=None)` | floats | `HardyWeinbergResult` | Genotype frequencies at HW eq. |
| `chi_squared_test(observed, expected, alpha=0.05, *, ddof=0)` | lists, float, keyword-only int | `ChiSquaredResult` | Equal-total Pearson χ²; df = categories - 1 - ddof; decision honors alpha. Fitted biallelic HWE uses ddof=1; fixed Mendelian ratios use 0; not a small-sample exact test |
| `recombination_frequency(recombinants, total)` | ints | float | Recombination fraction, 0–1 |
| `genetic_distance(recombinants, total)` | ints | float (cM) | Map distance in centimorgans |
| `infer_three_point_order(distances_cM)` | dict[tuple[str, str], float] | `LinkageMapResult` | Simple three-marker gene-order inference |
| `hamming_distance(seq1, seq2)` | strings | int | Count mismatched positions |
| `jukes_cantor_distance(p_distance)` | float | float | JC69 corrected distance; p_distance must be in [0, 0.75) |
| `cpg_methylation_remaining(initial_methylation, divisions, maintenance_efficiency)` | floats, int | float | Semiconservative maintenance: f_next = f*(1+p)/2 |
| `histone_modification_state(mark)` | str | str | Interpret common histone marks |
| `synthetic_methylation_beta_matrix(...)` | ints/floats | ndarray | Deterministic CpG methylation β matrix for figures |
| `mutation_rate_spectrum()` | — | `tuple[MutationRateEvidence, ...]` | Unsorted source-scoped MUTATION_RATE_EVIDENCE catalog, not a burden ranking |
| `replication_fork_progression(...)` | floats, int | `ReplicationForkProfile` | Bidirectional fork progression profile |
| `GENETIC_CODE` | — | dict | Codon → amino acid mapping |

`MutationRateEvidence` fields: `mutation_class`, `rate_range` (interval or `None`), `target`, `time_basis`, `organism`, `source_url`, `source_label`, `ascertainment`. Compare only compatible targets, time bases and ascertainment. `None` means unquantified, not zero; no automatic cross-class ranking or unit conversion.

## `biology.evolution`

| Function | Arguments | Returns | Description |
| -------- | --------- | ------- | ----------- |
| `selection_one_generation(pop)` | `Population` | `Population` | One viability-selection update |
| `simulate_selection(initial_pop, generations)` | `Population`, int | `list[SelectionResult]` | Allele-frequency trajectory under selection |
| `wright_fisher_drift(p, N, rng_seed=42)` | float, int | float | One Wright-Fisher drift generation |
| `simulate_drift(p, N, generations, rng_seed=42)` | float, int | list[float] | Stochastic drift trajectory |
| `fitness_landscape_1d(allele_freqs, fitness_AA, fitness_Aa, fitness_aa)` | list[float], floats | list[float] | Mean fitness across allele frequencies |
| `molecular_clock_divergence_time(substitution_rate_per_site_per_year, sequence_divergence)` | floats | float | Divergence time in years |
| `isolation_index(gene_flow_rate, mutation_rate)` | floats | float | mu/(mu+m), an unvalidated teaching heuristic, not an empirical reproductive-isolation estimator |

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
| `BIOMES`, `BIOME_DATA` | — | dict | Illustrative climate/NPP metadata, not calibrated biome boundaries; marine `annual_precipitation_mm` is `None` (not zero) and excluded from terrestrial precipitation plots |

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
| `bacterial_growth_curve(N0, doubling_time_hr, t_end_hr, steps=200, lag_phase_hr=1.0, stationary_phase_start_hr=None, carrying_capacity=None)` | nums | `GrowthCurveResult` | Lag/exponential/stationary teaching trajectory with continuous stationary transition |
| `doubling_time(N0, Nt, elapsed_time_hr)` | floats | float | Doubling time from population counts |
| `mic_fold_dilution(starting_concentration_ug_mL, dilution_factor, n_tubes)` | floats, ints | list[float] | Antibiotic concentrations across serial dilution |
| `basic_reproduction_number(beta_per_day, gamma_per_day)` | floats | float | SIR R0 = β/γ |
| `sir_model(population, initial_infected, beta_per_day, gamma_per_day, days, steps_per_day=4)` | ints/floats | `SIRResult` | Conservative closed-population SIR; inadequate explicit-Euler resolution rejected |
| `REFERENCE_ORGANISMS` | — | list | Reference bacteria/archaea metadata |

## `biology.botany`

| Function | Arguments | Returns | Description |
| -------- | --------- | ------- | ----------- |
| `water_potential(solute_concentration_M, turgor_pressure_MPa, temperature_K=298.0)` | floats | `WaterPotentialResult` | ψ = ψs + ψp |
| `transpiration_flux(stomatal_conductance_mol_m2_s, internal_vapor_mole_fraction, external_vapor_mole_fraction)` | floats | `TranspirationResult` | E = g_s Δx; x in mol/mol, g_s in mol m^-2 s^-1; fields conductance_mol_m2_s, delta_mole_fraction, flux_mol_m2_s, flux_mmol_m2_s |
| `photosynthesis_rate(photon_flux_µmol_m2_s, max_rate_µmol_CO2_m2_s=20.0, light_saturation_point=800.0, dark_respiration_µmol_CO2_m2_s=1.5)` | floats | float | Net photosynthesis light-response rate |
| `light_response_curve(max_rate=20.0, light_saturation_point=800.0, dark_respiration=1.5, n_points=50, max_par=2000.0)` | floats, int | `list[tuple[float, float]]` | PAR vs net photosynthesis curve |
| `plant_biomass_growth(initial_biomass_g, relative_growth_rate, carrying_capacity_g, duration_days, steps=100)` | floats, int | `PlantGrowthResult` | Logistic biomass accumulation |
| `PHOTOSYNTHESIS_PATHWAYS` | — | list | C3/C4/CAM comparative data |

## `biology.neuroscience`

| Function | Arguments | Returns | Description |
| -------- | --------- | ------- | ----------- |
| `action_potential_hh(stimulus_current_µA=10.0, t_end_ms=30.0, steps=3000, ...)` | floats, int | `ActionPotentialResult` | Simplified Hodgkin–Huxley; voltage/gates advance from one simultaneous prior state |
| `cable_voltage_attenuation(V0_mV, axial_resistance_Ohm_cm=100.0, membrane_resistance_kOhm_cm2=50.0, axon_radius_cm=5e-4, ...)` | floats | `CableResult` | Passive voltage decay along a dendrite/axon cable |
| `synaptic_current(reversal_potential_mV, membrane_potential_mV, peak_conductance_nS, synapse_type="excitatory")` | floats, str | `SynapticResult` | Driving force and peak synaptic current |
| `hebbian_weight_update(current_weight, pre_activity, post_activity, learning_rate=0.01, weight_max=1.0, weight_min=0.0)` | floats | float | Clipped Hebbian rule, not BCM |
| `BRAIN_REGIONS` | — | dict | Brain-region inventory and functions |

## `biology.foundations`

Unit 0 and foundational Unit I tables (no random state, no package I/O). Re-exported from `biology.foundations`.

| Symbol | Kind | Description |
| ------ | ---- | ----------- |
| `BIOLOGY_MILESTONES` | tuple | Historical milestones with era, year, and significance |
| `milestones_by_era()` | function | Group milestones by era into a dictionary |
| `ATOM_ELECTRONEGATIVITIES`, `BIOLOGICAL_BOND_ENERGIES` | tuples | Reference electronegativity and bond-energy records |
| `electronegativity_difference(symbol_a, symbol_b, *, table=ATOM_ELECTRONEGATIVITIES)` | function | Absolute ΔEN between symbols |
| `bond_polarity_class(symbol_a, symbol_b, *, table=ATOM_ELECTRONEGATIVITIES)` | function | Classify bond between symbols |
| `MACROMOLECULE_TIERS` | tuple | MacromoleculeTier(family, building_blocks, molecule, assembly, example_function, is_polymer); lipids are not polymers |
| `polymer_hierarchy_levels()` | function | Building blocks, Molecule, Assembly, Function |
| `poisson_degree_distribution(mean_degree, k_min=1, k_max=30)` | function | Discrete Poisson degree distribution |
| `powerlaw_degree_distribution(gamma=2.5, k_min=1, k_max=200)` | function | Discrete power-law degree distribution |
| `scale_free_vs_random(mean_degree=4.0, gamma=2.5, k_min=1, k_max=200)` | function | Pair on common degree support |
| `prediction_error_precision_curve(prior_mean=0.0, prior_precision=1.0, observation=1.0, precisions=...)` | function | Gaussian precision sweep returning ActiveInferenceProfile; not empirical validation |

Tests: `tests/test_foundations.py` for helpers; `tests/test_mermaid_and_visualization.py` for registry/renderer behavior. These do not certify every figure's scientific interpretation.

## `biology.toc`

Canonical table-of-contents API consumed by maintenance scripts. It reads
`docs/manuscript/config.yaml` and `biology.chapter_metadata` to derive renderable
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
| `CHAPTERS` | `list[ChapterMeta]` | All 44 configured chapters, ordered as in `config.yaml` |
| `by_id(chapter_id)` | `ChapterMeta \| None` | Look up a single chapter record |
| `by_unit(unit)` | `list[ChapterMeta]` | All chapters in a given unit ("0", "I", …, "X") |

**`chapter_id` and `sec:` labels:** `chapter_id` is `unit_<X>_<stem>` (e.g. `unit_I_water_and_life`). The manuscript section label is `\label{sec:<chapter_id>}` — the same string with the `sec:` prefix. **Prerequisites** in `ChapterMeta` are a tuple of other **`chapter_id` strings** (not `\cref` text); insert scripts turn them into prerequisite links using `\cref{sec:...}` in the metadata badge. See [composable_authoring.md](composable_authoring.md).

Tests: `tests/test_chapter_metadata.py` asserts every `config.yaml` chapter has a record, prerequisites resolve, difficulty ∈ {1, 2, 3}, and chapter numbers are contiguous.

## `biology.curriculum`

Per-chapter curriculum spine consumed by `scripts/sync_curriculum_materials.py`.
Each record connects a chapter to its lab, question bank, model/data skill,
misconception probe, transfer task, and bridge API.

Implementation modules are `unit_i` through `unit_x` (plus `unit_0`); uppercase
Roman Python module paths were removed. Authored unit/chapter IDs remain unchanged.
Build distributions from a clean source export after case-only cutovers: stale
generated `*.egg-info/SOURCES.txt` can otherwise retain old casing on macOS.

| Symbol | Kind | Description |
| ------ | ---- | ----------- |
| `CurriculumRecord(...)` | frozen dataclass | One instructional record per chapter |
| `CurriculumRecord.lab_label` | property | Companion lab `sec:` label |
| `CurriculumRecord.question_label` | property | Companion question-bank `sec:` label |
| `CURRICULUM` | `tuple[CurriculumRecord, ...]` | All 44 chapter records in `config.yaml` order |
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

## `biology.assessment`

Question-bank and lab assessment metadata parsers. Consumed by `scripts/sync_assessment_metadata.py` and pedagogy invariant tests.

Mappings and rubrics are curated from question/lab meaning. `sync_assessment_metadata.py` validates and preserves reviewed records, not ordinal assignments.

| Symbol | Kind | Description |
| ------ | ---- | ----------- |
| `QuestionAssessment` | frozen dataclass | One question-bank item's LO, Bloom, difficulty, format, minutes |
| `QuestionBankAssessment` | dataclass | Parsed bank with item list and summary counts |
| `LabAlignment` | dataclass | Lab measurable outcomes, LO coverage, rubric dimensions |
| `parse_question_bank(path)` | function | Parse HTML-comment assessment fields from a question bank |
| `parse_lab_alignment(path)` | function | Parse lab alignment block from a lab markdown file |
| `chapter_learning_objectives(path)` | function | Extract declared LO strings from a chapter file |

Tests: `tests/test_assessment_metadata.py`, `tests/test_lab_pedagogy_alignment.py`, `tests/test_chapter_pedagogy_coverage.py`.

## `biology.current_claims`

Fast-moving fact ledger for `docs/manuscript/current_claims.yaml`. Gate script: `scripts/audit_current_claims.py --check`.

| Symbol | Kind | Description |
| ------ | ---- | ----------- |
| `CurrentClaim` | frozen dataclass | One auditable claim with source tier, dates, anchor, refresh trigger |
| `ClaimIssue` | frozen dataclass | Validation finding (`code`, `message`) |
| `load_current_claims(path=None, project_root=None)` | function | Load ledger YAML as typed records |
| `validate_current_claims(claims, *, today=None, max_checked_age_days=180, references_path=None)` | function | Structural, source-link and freshness checks, with explicit bibliography resource; not live URL/full-text verification |

Tests: `tests/test_current_claims_ledger.py`.

## `biology.citations`

Natbib parsing helpers and the curated orphan-citation insertion map for `scripts/integrate_orphan_citations.py`.

| Symbol | Kind | Description |
| ------ | ---- | ----------- |
| `Citation` | frozen dataclass | One `\cite*` command with citekeys and span |
| `OrphanCitationInsertion` | frozen dataclass | Maps one BibTeX key to chapter path + anchor text |
| `iter_citations(text)` | function | Yield documented natbib commands |
| `citation_keys(text)` | function | Set of citekeys referenced in prose |
| `ordered_citation_keys(text)` | function | De-duplicated citekeys in first-seen order |
| `strip_citations(text, strip_incomplete_tail=False)` | function | Remove natbib commands from prose |
| `bib_keys(bib_text)` | function | Parse `@type{key,` keys from a `.bib` body |
| `orphan_citation_insertions(manuscript_root)` | function | **32** curated insertions for bibliography closure |
| `validate_orphan_citation_insertions(manuscript_root)` | function | Fail when targets or citekeys are invalid |

Tests: `tests/test_citations.py`.

## `biology.quality`

Manuscript quality audit engine behind `scripts/audit_textbook_quality.py`.

| Symbol | Kind | Description |
| ------ | ---- | ----------- |
| `Finding` | dataclass | One audit finding (file, line, code, message) |
| `ManuscriptSurface` | dataclass | Configured manuscript surface for advisory audits |
| `collect_findings()` | function | Run all auditors and return findings |
| `print_report(findings, max_advisories=0)` | function | Human-readable report; respects advisory cap |
| `main(argv)` | function | CLI entry (`--check`, `--max-advisories`) |

Pattern catalogs in `biology.quality.patterns` (`QUESTION_GENERIC_PATTERNS`, `ALLOWED_ADVISORY_CLASSIFICATIONS`, `EXPECTED_CONFIGURED_SURFACE_COUNTS`) are consumed by the engine and re-exported for regression tests — not for direct manuscript editing.

Tests: `tests/test_textbook_quality_audit.py`, `tests/test_audit_v3_and_crossref_gate.py`.

## `biology.enrichment`

Embedded frontier/companion enrichment catalog and apply engine.

| Symbol | Kind | Description |
| ------ | ---- | ----------- |
| `ChapterRecord` | dataclass | Chapter stem, paths, and enrichment context |
| `chapter_records()` | function | Build chapter records from canonical ToC |
| `enrich_chapters(records, dry_run)` | function | Insert or refresh frontier sections |
| `enrich_labs(records, dry_run)` | function | Lab evidence-upgrade blocks |
| `write_audit_matrix(records, dry_run)` | function | Regenerate embedded-enrichment audit matrix doc |
| `main(argv)` | function | CLI entry for `scripts/enrich_embedded_textbook.py` |

Tests: `tests/test_enrichment_substance_gate.py`, `tests/test_textbook_quality_audit.py`.

## `biology.answer_refinement`

Answer validation and explicit nonwriting refusal (CLI: `scripts/refine_generated_answers.py`).

| Symbol | Kind | Description |
| ------ | ---- | ----------- |
| `classify_question(text)` | function | Categorize a question stem for refinement |
| `is_v1_generated(body)` | function | Detect legacy generated-answer signatures |
| `generate_answer(...)` | function | Raises UnsupportedAnswerRepair; prompt-specific authored answers required |
| `process_bank(path, dry_run=False)` | function | Preserve authored solutions or raise without writing; both modes refuse unsupported repair |
| `main(argv)` | function | CLI entry |

Tests: `tests/test_question_answer_refinement.py`.

## `biology.curriculum_sync`

TOC-driven curriculum scaffold sync (CLI: `scripts/sync_curriculum_materials.py`).

| Symbol | Kind | Description |
| ------ | ---- | ----------- |
| `sync_h1(path, title, *, dry_run)` | function | Replace first H1 with canonical title |
| `sync_section_label(path, label, *, dry_run, unnumbered=True)` | function | Embed the sec ID on the H1 and remove its standalone label |
| `sync_chapter(path, record, alignment, *, dry_run)` | function | Refresh the chapter scaffold block, not authored assessments |
| `build_appendix(...)` / `build_instructor_appendix(...)` | functions | Curriculum and instructor appendix bodies |
| `sync_front_matter_navigation(book_toc, *, dry_run)` | function | Front-matter navigation block |
| `main(argv)` | function | CLI entry |

Tests: `tests/test_toc_consistency.py`, `tests/test_curriculum_metadata.py`.

There are no `sync_lab`/`sync_question` body writers. Procedures, prompts/keys, rubrics and coverage notes remain authored. The CLI supports `--dry-run` as a nonwriting preview, not a failing drift gate; it has no `--check`. Validate semantic assessment records with `scripts/sync_assessment_metadata.py --check`.

## `textbook_paths` / `textbook_io`

Checkout bootstrap and atomic I/O helpers at `src/` root (not under `biology/`).

| Symbol | Kind | Description |
| ------ | ---- | ----------- |
| `ensure_project_paths(*, include_scripts=False, include_template=True)` | function | Local src/scripts first; optional read-only integration discovery. Publication startup uses local-only bootstrap until its previous receipt is invalidated |
| `discover_template_root(start)` | function | Explicit BIOLOGY_TEXTBOOK_TEMPLATE_ROOT or genuine enclosing template; invalid explicit root raises; no ambient neighbors |
| `template_root()` | function | Discover selected root or None |
| `write_text_atomic(path, text, encoding="utf-8")` | function | Atomic text write via temp file + replace |

Tests: `tests/test_textbook_paths.py`, `tests/test_atomic_io.py`. Used by `tests/conftest.py` and maintenance scripts.

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

Detects raw-LaTeX figure environments (`\begin{figure}…\label{fig:…}…\end{figure}`), LaTeX equation environments, inline `$$…$$` display math, table captions (`Table: … {#tbl:…}`), markdown images (`![alt](path){#fig:…}`), section labels (`## Heading {#sec:…}`), and cross-references (`@fig:`, `@eq:`, `@tbl:`, `@sec:`). Manual equation-number tags are rejected so rendered numbering stays LaTeX-assigned. Details: [composable_authoring.md](composable_authoring.md).

## `visualization.cvd`

Constants for **colorvision–friendly** matplotlib styling (blue/orange/teal, Punnett hatching, line styles for overlapping series). Consumed by `src/visualization/plots.py`. Aligns with `docs/manuscript/config.yaml` → `accessibility.color_blindness_safe: true` — see [accessibility.md](accessibility.md) and [visualization_guide.md](visualization_guide.md).

| Symbol | Role |
| ------ | ---- |
| `BAR_POS`, `BAR_NEG` | Signed bar charts (e.g. Nernst) |
| `PUNNETT_DOMINANT`, `PUNNETT_RECESSIVE` | Punnett cells (with hatch patterns in the square plot) |
| `SERIES2`, `SERIES3` | Default multi-line series colors |

## `mermaid.renderer`

`MermaidRenderer(output_dir, *, strict_png=False).render(name, source, size=1200, background_color="white", square=True)` and `MermaidDiagram.render(output_dir, size=1200, background_color="white", square=True)` use one positive integer size, not width/height arguments. Publication requires `strict_png=True` and real PNG decoding; non-strict `.mmd` output is authoring source only. Mermaid CLI is pinned to 12.2.0; use `scripts/generate_diagrams.py --size 1200 --strict-png`.

`MermaidDiagram.render(...)` constructs a non-strict renderer and cannot select publication strictness. Use `MermaidRenderer(..., strict_png=True).render(...)` or the strict project CLI for publication.

## `biology.pipeline.rendering`

`render_textbook() -> Path` (CLI `scripts/render_textbook.py`) freshly stages validated configured sources and strict inline PNGs, checks source/asset identity and calls the read-only template library. Outputs remain project-local. See [pipeline_guide.md](pipeline_guide.md).

## `biology.pipeline.release_assets`

`build_release_assets(project, destination, renderer_root, *, receipt=None)` exports
clean, validated main into a new project-local output directory. It requires the
same source/tree, frozen renderer manifest and PDF hashes as a completed passing
full gate; link escapes, changed input bytes and occupied outputs fail. The ZIP's
independent main-only Git bundle excludes unrelated private refs. The native CLI
is `scripts/build_release_assets.py`; see the [release workflow](pipeline_guide.md#source-bound-native-release-assets).

## `mermaid.biology_diagrams`

Diagram structure is declared in `src/mermaid/diagram_specs.yaml` and loaded by `diagram_spec_loader.py`. Factory functions are registered at import time; `ALL_BIOLOGY_DIAGRAMS` holds **24** built `MermaidDiagram` objects. Keep the table below in sync with registry `name` stems.

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
| `hormone_signaling_diagram()` | `hormone_signaling_diagram` | Hormone signaling pathways |
| `dna_replication_diagram()` | `dna_replication_diagram` | DNA replication fork |
| `nutrient_cycle_diagram()` | `nutrient_cycle_diagram` | Nitrogen cycle |
| `chromosome_inheritance_diagram()` | `chromosome_inheritance_diagram` | Sex-linked inheritance and X-inactivation |
| `mirna_biogenesis_diagram()` | `mirna_biogenesis_diagram` | miRNA biogenesis and RISC loading |
| `x_inactivation_diagram()` | `x_inactivation_diagram` | X-inactivation |

## `visualization` (matplotlib generators)

Implementations live in `src/visualization/plots_{cell,genetics,ecology,evolution,physiology,botany,microbiology,foundations}.py`. `plots.py` owns `ALL_FIGURE_GENERATORS`; `__init__.py` is the public facade. Each registry callable accepts `output_dir: Path` and returns a PNG `Path`; underlying domain functions may require additional inputs, such as Punnett parent genotypes.

Color defaults come from [`visualization.cvd`](#visualizationcvd). [The visualization guide](visualization_guide.md) owns exact palette values, canvas/print distinctions, project-output review recipe and quantitative illustration conventions; no palette certifies all-CVD safety.

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
| `ghk_permeability` | `plot_ghk_permeability` | `ghk_permeability.png` |
| `hill_equation` | `plot_hill_equation` | `hill_equation.png` |
| `osmotic_pressure` | `plot_osmotic_pressure` | `osmotic_pressure.png` |
| `hardy_weinberg` | `plot_hardy_weinberg` | `hardy_weinberg.png` |
| `translation_codons` | `plot_translation_codons` | `translation_codons.png` |
| `genetic_drift_trajectories` | `plot_genetic_drift_trajectories` | `genetic_drift_trajectories.png` |
| `poiseuille_flow` | `plot_poiseuille_flow` | `poiseuille_flow.png` |
| `glycolysis_summary` | `plot_glycolysis_summary` | `glycolysis_summary.png` |
| `homeostasis_feedback` | `plot_homeostasis_feedback` | `homeostasis_feedback.png` |
| `fitness_landscape` | `plot_fitness_landscape` | `fitness_landscape.png` |
| `molecular_clock` | `plot_molecular_clock` | `molecular_clock.png` |
| `photosynthesis_rate` | `plot_photosynthesis_rate` | `photosynthesis_rate.png` |
| `water_potential_transpiration` | `plot_water_potential_transpiration` | `water_potential_transpiration.png` |
| `sir_model` | `plot_sir_model` | `sir_model.png` |
| `mic_dilution_series` | `plot_mic_dilution_series` | `mic_dilution_series.png` |
| `allee_threshold_dynamics` | `plot_allee_threshold_dynamics` | `allee_threshold_dynamics.png` |
| `biodiversity_indices` | `plot_biodiversity_indices` | `biodiversity_indices.png` |
| `food_web_trophic_levels` | `plot_food_web_trophic_levels` | `food_web_trophic_levels.png` |
| `network_degree_distribution` | `plot_network_degree_distribution` | `network_degree_distribution.png` |
| `prediction_error_precision` | `plot_prediction_error_precision` | `prediction_error_precision.png` |
| `biology_milestones` | `plot_biology_milestones` | `biology_milestones.png` |
| `electronegativity_bond_energy` | `plot_electronegativity_bond_energy` | `electronegativity_bond_energy.png` |
| `polymer_hierarchy` | `plot_polymer_hierarchy` | `polymer_hierarchy.png` |
| `organelle_size_scale` | `plot_organelle_size_scale` | `organelle_size_scale.png` |
| `atp_yield_comparison` | `plot_atp_yield_comparison` | `atp_yield_comparison.png` |
| `replication_fork_progression` | `plot_replication_fork_progression` | `replication_fork_progression.png` |
| `mutation_rate_spectrum` | `plot_mutation_rate_spectrum` | `mutation_rate_spectrum.png` |
| `pollen_tube_growth` | `plot_pollen_tube_growth` | `pollen_tube_growth.png` |
