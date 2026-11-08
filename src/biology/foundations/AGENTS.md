# `src/biology/foundations/` — AGENTS.md

Deterministic content tables and helpers for **Unit 0** (systems science, complex adaptive systems, active inference, history of biology) and foundational **Unit I** chapters that do not belong in the nine domain subpackages (atomic bonding data, polymer hierarchy descriptors, network topology).

## Modules

| Module | Manuscript surfaces | Exports |
| ------ | ------------------- | ------- |
| `active_inference.py` | `unit_0/active_inference.md` | `prediction_error_precision_curve`, `active_inference_profile`, `ActiveInferenceProfile` |
| `atoms_molecules.py` | `unit_I/atoms_molecules.md` | `ATOM_ELECTRONEGATIVITIES`, `BIOLOGICAL_BOND_ENERGIES`, `electronegativity_difference`, `bond_polarity_class` |
| `history_of_biology.py` | `docs/manuscript/unit_0/history_philosophy_biology.md` | `BIOLOGY_MILESTONES`, `milestones_by_era` |
| `macromolecules_hierarchy.py` | `unit_I/macromolecules.md` | `MACROMOLECULE_TIERS`, `polymer_hierarchy_levels` |
| `network_topology.py` | `unit_0/complex_adaptive_systems.md`, `unit_0/systems_science.md` | `poisson_degree_distribution`, `powerlaw_degree_distribution`, `scale_free_vs_random` |

Plot helpers live in `src/visualization/plots_foundations.py` and register through `ALL_FIGURE_GENERATORS` (`network_degree_distribution`, `prediction_error_precision`, `biology_milestones`, `electronegativity_bond_energy`, `polymer_hierarchy`).

## Conventions

- Frozen dataclasses and immutable tuples only; no RNG, no filesystem I/O in this package.
- When changing a table consumed by prose or plots, update `docs/api_reference.md`, the matching `docs/manuscript/unit_*/` consumers and `tests/test_foundations.py` or domain figure tests. These paths are repository-root paths. Historical entries identify selected events, not measured durations or a complete discovery inventory.
