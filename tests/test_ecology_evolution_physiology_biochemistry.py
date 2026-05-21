"""Tests for evolution, ecology, physiology, biochemistry modules."""

import math
import pytest

# ---- Evolution ----
from biology.evolution import (
    Population, simulate_selection, simulate_drift,
    fitness_landscape_1d, isolation_index, molecular_clock_divergence_time,
    wright_fisher_drift,
)

# ---- Ecology ----
from biology.ecology import (
    exponential_growth, logistic_growth, allee_strong_growth, lotka_volterra,
    food_web_trophic_levels, connectance, biodiversity_indices, BIOMES,
)

# ---- Physiology ----
from biology.physiology import (
    poiseuille_flow, oxygen_saturation, oxygen_dissociation_curve,
    homeostasis_response, ORGAN_SYSTEMS,
)

# ---- Biochemistry ----
from biology.biochemistry import (
    michaelis_menten, competitive_inhibition, enzyme_rate_curve,
    reaction_free_energy, atp_free_energy, glycolysis_summary,
    GLYCOLYSIS_STEPS,
)


# ===========================================================================
# EVOLUTION TESTS
# ===========================================================================

class TestNaturalSelection:
    def test_selection_increases_dominant_allele(self):
        """When fitness_aa < 1, p should increase over time."""
        pop = Population("test", p=0.2, q=0.8, fitness_AA=1.0, fitness_Aa=1.0, fitness_aa=0.5)
        results = simulate_selection(pop, generations=20)
        assert results[-1].p > 0.2

    def test_selection_neutral_no_change(self):
        """With equal fitnesses, p should remain constant."""
        pop = Population("neutral", p=0.3, q=0.7, fitness_AA=1.0, fitness_Aa=1.0, fitness_aa=1.0)
        results = simulate_selection(pop, generations=10)
        assert abs(results[-1].p - 0.3) < 1e-6

    def test_invalid_p_q_raises(self):
        with pytest.raises(ValueError):
            Population("bad", p=0.6, q=0.6)

    def test_zero_generations_raises(self):
        pop = Population("test", p=0.5, q=0.5)
        with pytest.raises(ValueError):
            simulate_selection(pop, generations=0)

    def test_mean_fitness_range(self):
        pop = Population("test", p=0.5, q=0.5, fitness_AA=1.0, fitness_Aa=0.8, fitness_aa=0.5)
        assert 0.5 <= pop.mean_fitness <= 1.0


class TestGeneticDrift:
    def test_drift_keeps_frequency_in_range(self):
        p_new = wright_fisher_drift(p=0.5, N=100, rng_seed=1)
        assert 0.0 <= p_new <= 1.0

    def test_simulate_drift_length(self):
        history = simulate_drift(0.5, N=100, generations=50, rng_seed=42)
        assert len(history) == 51  # initial + 50 generations

    def test_drift_fixed_allele_stays(self):
        p_new = wright_fisher_drift(p=1.0, N=100)
        assert p_new == 1.0

    def test_drift_lost_allele_stays(self):
        p_new = wright_fisher_drift(p=0.0, N=100)
        assert p_new == 0.0


class TestEvolutionaryModels:
    def test_fitness_landscape_peak(self):
        """Heterozygote advantage: max W at p between 0 and 1."""
        freqs = [i * 0.05 for i in range(21)]
        W = fitness_landscape_1d(freqs, fitness_AA=0.8, fitness_Aa=1.0, fitness_aa=0.6)
        max_idx = W.index(max(W))
        assert 0 < max_idx < 20  # peak in middle

    def test_isolation_index_zero_flow(self):
        assert isolation_index(gene_flow_rate=0.0, mutation_rate=1e-5) == 1.0

    def test_isolation_index_dominant_flow(self):
        # High gene flow → near zero isolation
        idx = isolation_index(gene_flow_rate=1.0, mutation_rate=0.0)
        assert idx == 0.0

    def test_molecular_clock(self):
        """1% divergence at 2×10⁻⁹ substitutions/site/yr → 2.5M years (t = d / 2μ)."""
        t = molecular_clock_divergence_time(2e-9, 0.01)
        assert abs(t - 2.5e6) < 1e5


# ===========================================================================
# ECOLOGY TESTS
# ===========================================================================

class TestPopulationGrowth:
    def test_exponential_growth_doubles(self):
        result = exponential_growth(N0=100.0, r=math.log(2), t_end=1.0, steps=100)
        assert abs(result.populations[-1] - 200.0) < 1.0

    def test_logistic_approaches_K(self):
        result = logistic_growth(N0=10.0, r=0.5, K=1000.0, t_end=40.0, steps=500)
        assert result.populations[-1] > 900.0

    def test_exponential_invalid_N0_raises(self):
        with pytest.raises(ValueError):
            exponential_growth(0.0, r=1.0, t_end=10.0)

    def test_logistic_invalid_K_raises(self):
        with pytest.raises(ValueError):
            logistic_growth(N0=100.0, r=1.0, K=0.0, t_end=10.0)

    def test_logistic_model_label(self):
        result = logistic_growth(10.0, 0.3, 100.0, 20.0)
        assert result.model == "logistic"


class TestAlleeStrongGrowth:
    def test_below_threshold_declines_toward_zero(self):
        result = allee_strong_growth(
            N0=45.0, r=0.5, A=50.0, K=1000.0, t_end=25.0, steps=2500,
        )
        assert result.model == "allee_strong"
        assert result.populations[-1] < 5.0

    def test_above_threshold_increases_toward_K(self):
        result = allee_strong_growth(
            N0=55.0, r=0.5, A=50.0, K=1000.0, t_end=40.0, steps=4000,
        )
        assert result.populations[-1] > 500.0

    def test_invalid_A_ge_K_raises(self):
        with pytest.raises(ValueError):
            allee_strong_growth(60.0, 0.5, 100.0, 80.0, t_end=10.0)


class TestLotkaVolterra:
    def test_lv_runs_and_returns_history(self):
        result = lotka_volterra(40.0, 9.0, 0.5, 0.02, 0.01, 0.2, 50.0, 1000)
        assert len(result.times) > 0
        assert len(result.prey) == len(result.predator)

    def test_lv_populations_non_negative(self):
        result = lotka_volterra(40.0, 9.0, 0.5, 0.02, 0.01, 0.2, 100.0)
        assert all(p >= 0 for p in result.prey)
        assert all(p >= 0 for p in result.predator)

    def test_lv_invalid_parameter_raises(self):
        with pytest.raises(ValueError):
            lotka_volterra(0.0, 9.0, 0.5, 0.02, 0.01, 0.2, 50.0)


class TestFoodWeb:
    def test_trophic_levels_producers(self):
        adjacency = {"Plants": [], "Insects": ["Plants"], "Birds": ["Insects"]}
        levels = food_web_trophic_levels(adjacency)
        assert levels["Plants"] == 1
        assert levels["Insects"] == 2
        assert levels["Birds"] == 3

    def test_connectance_formula(self):
        c = connectance(num_species=5, num_links=10)
        assert abs(c - 0.4) < 1e-9

    def test_connectance_invalid_raises(self):
        with pytest.raises(ValueError):
            connectance(num_species=0, num_links=10)


class TestBiodiversity:
    def test_shannon_maximum_evenness(self):
        """Equal counts give maximum Shannon diversity for S species."""
        result = biodiversity_indices([50, 50])
        assert abs(result.shannon_index - math.log(2)) < 1e-9

    def test_simpson_zero_at_one_species(self):
        result = biodiversity_indices([100])
        assert result.simpson_index == 0.0

    def test_evenness_one_for_equal_counts(self):
        result = biodiversity_indices([25, 25, 25, 25])
        assert abs(result.evenness - 1.0) < 1e-9

    def test_biodiversity_empty_raises(self):
        with pytest.raises(ValueError):
            biodiversity_indices([])

    def test_biomes_data_present(self):
        assert "Tropical Rainforest" in BIOMES
        assert "Desert" in BIOMES


# ===========================================================================
# PHYSIOLOGY TESTS
# ===========================================================================

class TestPoiseuille:
    def test_larger_radius_gives_larger_flow(self):
        """Q ∝ r⁴."""
        q1 = poiseuille_flow(1000.0, 0.001, 0.1)
        q2 = poiseuille_flow(1000.0, 0.002, 0.1)
        assert q2.volumetric_flow_m3s > q1.volumetric_flow_m3s * 10

    def test_zero_radius_raises(self):
        with pytest.raises(ValueError):
            poiseuille_flow(1000.0, 0.0, 0.1)

    def test_laminar_flow_regime(self):
        result = poiseuille_flow(133.0, 0.0015, 0.05)
        assert result.flow_regime == "laminar"


class TestOxygenSaturation:
    def test_zero_pO2_gives_zero_saturation(self):
        result = oxygen_saturation(pO2_mmHg=0.0)
        assert result.saturation == 0.0

    def test_high_pO2_approaches_one(self):
        result = oxygen_saturation(pO2_mmHg=150.0)
        assert result.saturation > 0.99

    def test_p50_gives_half_saturation(self):
        result = oxygen_saturation(pO2_mmHg=26.0, p50_mmHg=26.0)
        assert abs(result.saturation - 0.5) < 0.01

    def test_dissociation_curve_length(self):
        curve = oxygen_dissociation_curve(n_points=100)
        assert len(curve) == 101

    def test_invalid_p50_raises(self):
        with pytest.raises(ValueError):
            oxygen_saturation(pO2_mmHg=50.0, p50_mmHg=0.0)


class TestHomeostasis:
    def test_negative_feedback_direction(self):
        result = homeostasis_response(set_point=37.0, measured_value=38.5)
        assert result.corrective_response < 0  # must decrease temperature

    def test_within_tolerance(self):
        result = homeostasis_response(set_point=37.0, measured_value=37.02, tolerance=0.05)
        assert result.is_within_tolerance

    def test_outside_tolerance(self):
        result = homeostasis_response(set_point=7.4, measured_value=7.8, tolerance=0.05)
        assert not result.is_within_tolerance

    def test_organ_systems_complete(self):
        assert "Cardiovascular" in ORGAN_SYSTEMS
        assert "Nervous" in ORGAN_SYSTEMS
        assert len(ORGAN_SYSTEMS) >= 8


# ===========================================================================
# BIOCHEMISTRY TESTS
# ===========================================================================

class TestMichaelisMenten:
    def test_at_km_rate_is_half_vmax(self):
        result = michaelis_menten(substrate_conc=5.0, Vmax=10.0, Km=5.0)
        assert abs(result.reaction_rate - 5.0) < 1e-9

    def test_zero_substrate_gives_zero_rate(self):
        result = michaelis_menten(substrate_conc=0.0, Vmax=10.0, Km=5.0)
        assert result.reaction_rate == 0.0

    def test_high_substrate_approaches_vmax(self):
        result = michaelis_menten(substrate_conc=1000.0, Vmax=10.0, Km=0.5)
        assert result.efficiency > 0.99

    def test_competitive_inhibition_reduces_rate(self):
        v_normal = michaelis_menten(5.0, 10.0, 5.0).reaction_rate
        v_inhibited = competitive_inhibition(5.0, 10.0, 5.0, 10.0, 5.0).reaction_rate
        assert v_inhibited < v_normal

    def test_invalid_km_raises(self):
        with pytest.raises(ValueError):
            michaelis_menten(1.0, Vmax=10.0, Km=0.0)

    def test_invalid_vmax_raises(self):
        with pytest.raises(ValueError):
            michaelis_menten(1.0, Vmax=-1.0, Km=5.0)

    def test_enzyme_curve_length(self):
        curve = enzyme_rate_curve(Vmax=10.0, Km=5.0, n_points=20)
        assert len(curve) == 21


class TestBioenergetics:
    def test_atp_hydrolysis_negative_dG(self):
        """ATP hydrolysis in cells is always spontaneous (ΔG < 0)."""
        dG = atp_free_energy()
        assert dG < 0

    def test_glycolysis_net_atp(self):
        """Glycolysis produces net 2 ATP per glucose."""
        result = glycolysis_summary()
        assert result.net_atp == 2

    def test_glycolysis_net_nadh(self):
        """Glycolysis produces net 2 NADH per glucose."""
        result = glycolysis_summary()
        assert result.net_nadh == 2

    def test_glycolysis_total_steps(self):
        assert len(GLYCOLYSIS_STEPS) == 10

    def test_reaction_free_energy_exergonic(self):
        dG = reaction_free_energy(-30.0, product_conc=1e-5, reactant_conc=1e-3)
        assert dG < 0
