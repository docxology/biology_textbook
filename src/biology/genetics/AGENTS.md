# `src/biology/genetics/` — AGENTS.md

Genetics logic is split by topic; the package facade is `biology.genetics` and the compatibility shim is `genetics.py`.

## Modules

| Module | Topic | Key APIs |
| ------ | ----- | -------- |
| `sequence.py` | Central dogma, GC content | `GENETIC_CODE`, `dna_complement`, `translate_mrna` |
| `mendelian.py` | Monohybrid crosses | `punnett_square`, `gametes`, `DiploidGenotype` |
| `population.py` | HW equilibrium, goodness-of-fit | `hardy_weinberg`, `chi_squared_test` |
| `linkage.py` | Recombination maps | `genetic_distance`, `infer_three_point_order` |
| `distance.py` | Sequence divergence | `hamming_distance`, `jukes_cantor_distance` |
| `epigenetics.py` | Chromatin teaching helpers | `cpg_methylation_remaining`, `synthetic_methylation_beta_matrix` |
| `mutation.py` | Mutation-rate spectrum | `mutation_rate_spectrum`, `MUTATION_RATE_SPECTRUM` |
| `replication.py` | Fork kinematics | `replication_fork_progression` |
| `genetics.py` | Shim re-exporting all public symbols for legacy `biology.genetics.genetics.*` paths | — |

## Tests

| Test file | Module |
| --------- | ------ |
| `tests/test_genetics_sequence.py` | `sequence` |
| `tests/test_genetics_mendelian.py` | `mendelian` |
| `tests/test_genetics_population.py` | `population` |
| `tests/test_genetics_linkage.py` | `linkage` |
| `tests/test_genetics_distance.py` | `distance` |
| `tests/test_genetics_epigenetics.py` | `epigenetics` |
| `tests/test_genetics_mutation.py` | `mutation` |
| `tests/test_genetics_replication.py` | `replication` |

When changing public APIs, update `../../../docs/api_reference.md`, the matching `manuscript/unit_IV/AGENTS.md` or `manuscript/unit_V/AGENTS.md`, and the tests above.
