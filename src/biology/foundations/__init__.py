"""Foundations subpackage.

Domain primitives for Unit 0 (systems and complex adaptive systems, active
inference, history of biology) and the foundational Unit I chapters that lack
a natural home elsewhere (atomic-bond data, polymer-hierarchy descriptors).

All entries here are content tables or deterministic helpers; they have no
mocks, no random state, and no I/O outside what the calling plot helper does.
"""

from .active_inference import (
    ActiveInferenceProfile,
    PredictionPrecisionPoint,
    active_inference_profile,
    prediction_error_precision_curve,
)
from .atoms_molecules import (
    ATOM_ELECTRONEGATIVITIES,
    BIOLOGICAL_BOND_ENERGIES,
    AtomElectronegativity,
    BondEnergy,
    bond_polarity_class,
    electronegativity_difference,
)
from .history_of_biology import (
    BIOLOGY_MILESTONES,
    BiologyMilestone,
    milestones_by_era,
)
from .macromolecules_hierarchy import (
    MACROMOLECULE_TIERS,
    MacromoleculeTier,
    polymer_hierarchy_levels,
)
from .network_topology import (
    DegreeDistribution,
    poisson_degree_distribution,
    powerlaw_degree_distribution,
    scale_free_vs_random,
)

__all__ = [
    "ATOM_ELECTRONEGATIVITIES",
    "BIOLOGICAL_BOND_ENERGIES",
    "BIOLOGY_MILESTONES",
    "MACROMOLECULE_TIERS",
    "ActiveInferenceProfile",
    "AtomElectronegativity",
    "BiologyMilestone",
    "BondEnergy",
    "DegreeDistribution",
    "MacromoleculeTier",
    "PredictionPrecisionPoint",
    "active_inference_profile",
    "bond_polarity_class",
    "electronegativity_difference",
    "milestones_by_era",
    "poisson_degree_distribution",
    "polymer_hierarchy_levels",
    "powerlaw_degree_distribution",
    "prediction_error_precision_curve",
    "scale_free_vs_random",
]
