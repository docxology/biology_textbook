"""Unit tests for biology.foundations and related domain helpers.

These tests cover the domain logic backing the figure pass that landed on
2026-05-25 (Unit 0, Unit I, Unit II, Unit III, Unit IV, Unit VIII chapters).
They exercise the data tables and small numerical helpers; figure rendering
is covered separately in :mod:`tests.test_mermaid_and_visualization`.
"""

from __future__ import annotations

import math

import pytest


# ---------------------------------------------------------------------------
# foundations.network_topology
# ---------------------------------------------------------------------------


class TestNetworkTopology:
    def test_poisson_distribution_sums_near_one_with_excluded_zero(self):
        from biology.foundations import poisson_degree_distribution

        # k_min defaults to 1; the missing P(k=0) = exp(-lambda) is small for
        # lambda=4 (~0.018), so the truncated mass stays just under 1.
        dist = poisson_degree_distribution(mean_degree=4.0, k_max=50)
        total = sum(dist.probabilities)
        assert 0.95 < total < 1.0

    def test_poisson_peak_near_mean(self):
        from biology.foundations import poisson_degree_distribution

        dist = poisson_degree_distribution(mean_degree=5.0, k_max=30)
        peak_k = dist.degrees[dist.probabilities.index(max(dist.probabilities))]
        assert 4 <= peak_k <= 6

    def test_powerlaw_distribution_decreasing(self):
        from biology.foundations import powerlaw_degree_distribution

        dist = powerlaw_degree_distribution(gamma=2.5, k_min=1, k_max=200)
        probs = dist.probabilities
        assert all(probs[i] >= probs[i + 1] - 1e-12 for i in range(len(probs) - 1))

    def test_powerlaw_log_slope_matches_gamma(self):
        from biology.foundations import powerlaw_degree_distribution

        gamma = 3.0
        dist = powerlaw_degree_distribution(gamma=gamma, k_min=1, k_max=200)
        slope = (
            math.log(dist.probabilities[50]) - math.log(dist.probabilities[10])
        ) / (math.log(dist.degrees[50]) - math.log(dist.degrees[10]))
        assert -gamma - 0.05 < slope < -gamma + 0.05

    def test_scale_free_vs_random_returns_pair(self):
        from biology.foundations import scale_free_vs_random

        poisson, powerlaw = scale_free_vs_random()
        assert poisson.degrees and powerlaw.degrees
        assert len(poisson.probabilities) == len(poisson.degrees)
        assert len(powerlaw.probabilities) == len(powerlaw.degrees)


# ---------------------------------------------------------------------------
# foundations.active_inference
# ---------------------------------------------------------------------------


class TestActiveInference:
    def test_low_precision_keeps_prior(self):
        from biology.foundations import prediction_error_precision_curve

        curve = prediction_error_precision_curve(
            prior_mean=0.0, prior_precision=1.0, observation=1.0
        )
        # First point uses the smallest precision; posterior should sit close
        # to the prior of 0 rather than the observation of 1.
        assert abs(curve.points[0].posterior_mean) < 0.2

    def test_high_precision_approaches_observation(self):
        from biology.foundations import prediction_error_precision_curve

        curve = prediction_error_precision_curve(
            prior_mean=0.0, prior_precision=1.0, observation=1.0
        )
        # Last point uses the largest precision; posterior should be near 1.
        assert curve.points[-1].posterior_mean > 0.9

    def test_active_inference_profile_has_consistent_lengths(self):
        from biology.foundations import active_inference_profile

        profile = active_inference_profile()
        # The dataclass holds a sequence of named precision/error pairs.
        assert profile.points, "profile must contain points"
        precisions = [p.sensory_precision for p in profile.points]
        assert all(p_a < p_b for p_a, p_b in zip(precisions, precisions[1:]))


# ---------------------------------------------------------------------------
# foundations.history_of_biology
# ---------------------------------------------------------------------------


class TestHistoryOfBiology:
    def test_milestones_chronological(self):
        from biology.foundations import BIOLOGY_MILESTONES

        years = [m.year for m in BIOLOGY_MILESTONES]
        assert years == sorted(years), "BIOLOGY_MILESTONES must be chronological"

    def test_milestones_have_required_fields(self):
        from biology.foundations import BIOLOGY_MILESTONES

        for milestone in BIOLOGY_MILESTONES:
            assert milestone.event
            assert milestone.figure
            assert milestone.era
            assert isinstance(milestone.year, int)

    def test_milestones_grouped_by_era(self):
        from biology.foundations import BIOLOGY_MILESTONES, milestones_by_era

        grouped = milestones_by_era()
        assert grouped, "milestones_by_era must return at least one era"
        flattened = [m for milestones in grouped.values() for m in milestones]
        assert len(flattened) == len(BIOLOGY_MILESTONES)


# ---------------------------------------------------------------------------
# foundations.atoms_molecules
# ---------------------------------------------------------------------------


class TestAtomsAndBonds:
    def test_electronegativity_table_contains_common_atoms(self):
        from biology.foundations import ATOM_ELECTRONEGATIVITIES

        symbols = {atom.symbol for atom in ATOM_ELECTRONEGATIVITIES}
        for atom in ("H", "C", "N", "O", "P", "S"):
            assert atom in symbols

    def test_oxygen_more_electronegative_than_carbon(self):
        from biology.foundations import ATOM_ELECTRONEGATIVITIES

        lookup = {a.symbol: a.pauling for a in ATOM_ELECTRONEGATIVITIES}
        assert lookup["O"] > lookup["C"] > lookup["H"]

    def test_bond_energy_table_orders_by_class(self):
        from biology.foundations import BIOLOGICAL_BOND_ENERGIES

        covalent = [b for b in BIOLOGICAL_BOND_ENERGIES if b.bond_class == "covalent"]
        noncovalent = [
            b for b in BIOLOGICAL_BOND_ENERGIES if b.bond_class == "noncovalent"
        ]
        assert covalent and noncovalent
        # Median covalent strictly above median noncovalent.
        cov_energies = sorted(b.energy_kJ_per_mol for b in covalent)
        non_energies = sorted(b.energy_kJ_per_mol for b in noncovalent)
        cov_median = cov_energies[len(cov_energies) // 2]
        non_median = non_energies[len(non_energies) // 2]
        assert cov_median > non_median * 5

    def test_electronegativity_difference_classification(self):
        from biology.foundations import bond_polarity_class, electronegativity_difference

        diff_oh = electronegativity_difference("O", "H")
        assert diff_oh > 0.5
        assert bond_polarity_class("O", "H") in {"polar covalent", "ionic"}
        diff_cc = electronegativity_difference("C", "C")
        assert diff_cc == pytest.approx(0.0, abs=1e-9)
        assert bond_polarity_class("C", "C") == "nonpolar covalent"


# ---------------------------------------------------------------------------
# foundations.macromolecules_hierarchy
# ---------------------------------------------------------------------------


class TestMacromoleculeHierarchy:
    def test_polymer_hierarchy_levels_are_canonical(self):
        from biology.foundations import polymer_hierarchy_levels

        levels = polymer_hierarchy_levels()
        assert tuple(level.lower() for level in levels) == (
            "monomer",
            "polymer",
            "assembly",
            "function",
        )

    def test_macromolecule_tiers_cover_main_families(self):
        from biology.foundations import MACROMOLECULE_TIERS

        families = {tier.family.lower() for tier in MACROMOLECULE_TIERS}
        for required in ("proteins", "nucleic acids", "carbohydrates", "lipids"):
            assert required in families


# ---------------------------------------------------------------------------
# cell.organelle_size_table
# ---------------------------------------------------------------------------


class TestOrganelleSizes:
    def test_organelle_sizes_are_strictly_positive(self):
        from biology.cell import organelle_size_table

        rows = organelle_size_table()
        assert rows
        for row in rows:
            assert row.diameter_um > 0
            assert row.name
            assert row.category

    def test_organelle_sizes_span_orders_of_magnitude(self):
        from biology.cell import organelle_size_table

        diameters = [row.diameter_um for row in organelle_size_table()]
        ratio = max(diameters) / min(diameters)
        assert ratio >= 1000.0  # log plot is meaningful only at scale


# ---------------------------------------------------------------------------
# biochemistry.atp_yield_by_pathway
# ---------------------------------------------------------------------------


class TestATPYields:
    def test_atp_yield_pathway_table_nonempty(self):
        from biology.biochemistry import atp_yield_by_pathway

        rows = list(atp_yield_by_pathway())
        assert rows
        for row in rows:
            assert row.pathway
            assert row.total_atp >= 0
            assert row.substrate_level_atp >= 0
            assert row.oxidative_atp >= 0

    def test_aerobic_yield_dominates_fermentation(self):
        from biology.biochemistry import atp_yield_by_pathway

        rows = list(atp_yield_by_pathway())
        fermentation = next(r for r in rows if "ferment" in r.pathway.lower())
        aerobic = next(r for r in rows if "aerobic" in r.pathway.lower())
        assert aerobic.total_atp >= fermentation.total_atp * 5
        assert aerobic.requires_oxygen
        assert not fermentation.requires_oxygen


# ---------------------------------------------------------------------------
# botany.pollen_tube_growth
# ---------------------------------------------------------------------------


class TestPollenTubeGrowth:
    def test_pollen_tube_growth_monotonic(self):
        from biology.botany import pollen_tube_growth

        result = pollen_tube_growth(
            max_length_um=2000.0, growth_rate_um_per_min=20.0
        )
        lengths = result.lengths_um
        assert all(b >= a for a, b in zip(lengths, lengths[1:]))

    def test_pollen_tube_saturates_below_max(self):
        from biology.botany import pollen_tube_growth

        result = pollen_tube_growth(
            max_length_um=2000.0, growth_rate_um_per_min=20.0
        )
        assert result.lengths_um[-1] <= 2000.0 + 1e-6

    def test_pollen_tube_growth_records_max(self):
        from biology.botany import pollen_tube_growth

        result = pollen_tube_growth(
            max_length_um=1000.0, growth_rate_um_per_min=8.0
        )
        assert result.saturation_length_um == pytest.approx(1000.0, rel=1e-9)
