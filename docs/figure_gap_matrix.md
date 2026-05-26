# Chapter Figure Gap Matrix (2026-05-25)

Status of chapter figure coverage. All prior deferrals have been cleared by
the unit_0/unit_I/unit_II/unit_III/unit_IV/unit_VIII figure pass landed on
2026-05-25 (see `src/visualization/plots_foundations.py` plus extensions in
`plots_cell.py`, `plots_physiology.py`, `plots_genetics.py`, `plots_botany.py`).

| Chapter | Tier | Plot | API module | Status |
| --- | --- | --- | --- | --- |
| `unit_0/systems_science.md` | 1 | Logistic growth | `biology.ecology.logistic_growth` | wired (`fig:unit_0_logistic_growth`) |
| `unit_0/complex_adaptive_systems.md` | 1 | Scale-free vs random degree distribution | `biology.foundations.scale_free_vs_random` | wired (`fig:unit_0_network_degree_distribution`) |
| `unit_0/active_inference.md` | 2 | Prediction error vs precision | `biology.foundations.prediction_error_precision_curve` | wired (`fig:unit_0_prediction_error_precision`) |
| `unit_0/history_philosophy_biology.md` | 1 | Biology milestone timeline | `biology.foundations.BIOLOGY_MILESTONES` | wired (`fig:unit_0_biology_milestones`) |
| `unit_I/atoms_molecules.md` | 1 | Electronegativity + bond energy | `biology.foundations.ATOM_ELECTRONEGATIVITIES`, `BIOLOGICAL_BOND_ENERGIES` | wired (`fig:unit_I_electronegativity_bond_energy`) |
| `unit_I/macromolecules.md` | 1 | Polymer hierarchy schematic | `biology.foundations.MACROMOLECULE_TIERS` | wired (`fig:unit_I_polymer_hierarchy`) |
| `unit_I/water_and_life.md` | 1 | Osmotic pressure vs concentration | `biology.cell.osmotic_pressure` | wired |
| `unit_II/cell_theory.md` | — | — | — | prose; inline Mermaid sufficient |
| `unit_II/cell_structure.md` | 1 | Organelle / cell size scale (log) | `biology.cell.organelle_size_table` | wired (`fig:unit_II_organelle_size_scale`) |
| `unit_II/cell_signaling.md` | 1 | Hill cooperativity curves | `biology.cell.hill_equation` | wired |
| `unit_III/bioenergetics_and_respiration.md` | 1 | Glycolysis ATP/NADH bar summary | `biology.biochemistry.glycolysis_summary` | wired |
| `unit_III/metabolic_integration.md` | 1 | ATP yield comparison | `biology.biochemistry.atp_yield_by_pathway` | wired (`fig:unit_III_atp_yield_comparison`) |
| `unit_IV/dna_replication_and_cell_cycle.md` | 2 | Replication-fork progression | `biology.genetics.replication_fork_progression` | wired (`fig:unit_IV_replication_fork_progression`) |
| `unit_IV/gene_expression.md` | 2 | Translation codon throughput | `biology.genetics.translate_mrna` | wired |
| `unit_IV/mutations_and_genomics.md` | 1 | Mutation rate spectrum | `biology.genetics.mutation_rate_spectrum` | wired (`fig:unit_IV_mutation_rate_spectrum`) |
| `unit_V/population_genetics.md` | 1 | Hardy–Weinberg curves + drift | `biology.genetics.hardy_weinberg`, `biology.evolution.simulate_drift` | wired |
| `unit_VI/genetic_drift_and_speciation.md` | 1 | Mean fitness landscape | `biology.evolution.fitness_landscape_1d` | wired |
| `unit_VI/phylogenetics.md` | 1 | Molecular clock divergence | `biology.evolution.molecular_clock_divergence_time` | wired |
| `unit_VII/host_immunity_and_vaccines.md` | 1 | SIR compartment curves | `biology.microbiology.sir_model` | wired |
| `unit_VII/microbial_ecology.md` | 2 | MIC serial dilution | `biology.microbiology.mic_fold_dilution` | wired |
| `unit_VIII/plant_responses.md` | 1 | Net photosynthesis vs PAR | `biology.botany.photosynthesis_rate` | wired |
| `unit_VIII/plant_reproduction.md` | 2 | Pollen-tube growth curve | `biology.botany.pollen_tube_growth` | wired (`fig:unit_VIII_pollen_tube_growth`) |
| `unit_IX/circulation_respiration_homeostasis.md` | 1 | Poiseuille flow vs radius | `biology.physiology.poiseuille_flow` | wired |
| `unit_IX/endocrine_signaling.md` | 2 | Homeostasis error correction | `biology.physiology.homeostasis_response` | wired |
| `unit_X/community_ecology.md` | 1 | Shannon/Simpson comparison | `biology.ecology.biodiversity_indices` | wired |
| `unit_X/ecosystem_ecology.md` | 2 | Food-web trophic levels | `biology.ecology.food_web_trophic_levels` | wired |

**Coverage:** all listed chapters now embed at least one `\includegraphics`
figure block with alt text and `\cref` cross-reference. No outstanding tier-1
or tier-2 deferrals.
