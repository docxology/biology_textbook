# Chapter Figure Gap Matrix (2026-05-23)

Chapters without `\includegraphics` before this pass, scored against callable
`src/biology/*` APIs and inline Mermaid density.

| Chapter | Tier | Candidate plot | API module | Deferral |
| --- | --- | --- | --- | --- |
| `unit_I/water_and_life.md` | 1 | Osmotic pressure vs concentration | `biology.cell.osmotic_pressure` | — |
| `unit_II/cell_signaling.md` | 1 | Hill cooperativity curves | `biology.cell.hill_equation` | — |
| `unit_III/bioenergetics_and_respiration.md` | 1 | Glycolysis ATP/NADH bar summary | `biology.biochemistry.glycolysis_summary` | — |
| `unit_IV/gene_expression.md` | 2 | Translation codon throughput | `biology.genetics.translate_mrna` | — |
| `unit_VI/genetic_drift_and_speciation.md` | 1 | Mean fitness landscape | `biology.evolution.fitness_landscape_1d` | — |
| `unit_VI/phylogenetics.md` | 1 | Molecular clock divergence | `biology.evolution.molecular_clock_divergence_time` | — |
| `unit_VII/infectious_disease.md` | 1 | SIR compartment curves | `biology.microbiology.sir_model` | — |
| `unit_VII/microbial_ecology.md` | 2 | MIC serial dilution | `biology.microbiology.mic_fold_dilution` | — |
| `unit_VIII/plant_responses.md` | 1 | Net photosynthesis vs PAR | `biology.botany.photosynthesis_rate` | — |
| `unit_IX/circulation_respiration_homeostasis.md` | 1 | Poiseuille flow vs radius | `biology.physiology.poiseuille_flow` | second plot |
| `unit_IX/endocrine_and_immune.md` | 2 | Homeostasis error correction | `biology.physiology.homeostasis_response` | — |
| `unit_X/community_ecology.md` | 1 | Shannon/Simpson comparison | `biology.ecology.biodiversity_indices` | — |
| `unit_X/ecosystem_ecology.md` | 2 | Food-web trophic levels | `biology.ecology.food_web_trophic_levels` | — |
| `unit_V/population_genetics.md` | 1 | Hardy–Weinberg curves | `biology.genetics.hardy_weinberg` | companion to drift |
| `unit_II/cell_theory.md` | — | — | — | prose; inline Mermaid sufficient |
| `unit_II/cell_structure.md` | — | — | Nernst in `membrane_transport` | defer |
| `unit_I/atoms_molecules.md` | — | — | — | defer |
| `unit_I/macromolecules.md` | — | — | — | defer |
| `unit_III/metabolic_integration.md` | — | — | glycolysis in bioenergetics | defer |
| `unit_IV/dna_replication.md` | — | — | — | defer |
| `unit_IV/mutations_and_genomics.md` | — | — | methylation in epigenetics | defer |
| `unit_VIII/plant_reproduction.md` | — | — | — | defer |
| Unit 0 (4 chapters) | — | — | — | skip per memo |

**Tier 1:** 10 plots. **Tier 2:** 4 plots. **Fixed regressions:** 4 prose `\cref` additions.
