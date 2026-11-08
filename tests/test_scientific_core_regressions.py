"""Independent mathematical and real-consumer regressions for scientific models."""

import math
from dataclasses import FrozenInstanceError

import numpy as np
import pytest

from biology.biochemistry import (
    GLYCOLYSIS_STEPS,
    atp_free_energy,
    atp_yield_by_pathway,
    glycolysis_summary,
    michaelis_menten,
    reaction_free_energy,
)
from biology.cell import (
    IonConcentration,
    count_membrane_bound_organelles,
    get_organelles_by_cell_type,
    goldman_equation,
    hill_equation,
    nernst_potential,
    receptor_occupancy,
)
from biology.constants import FARADAY_CONSTANT, GAS_CONSTANT
from biology.foundations import (
    MACROMOLECULE_TIERS,
    poisson_degree_distribution,
    powerlaw_degree_distribution,
    prediction_error_precision_curve,
)
from biology.genetics import (
    chi_squared_test,
    cpg_methylation_remaining,
    gc_content,
    infer_three_point_order,
    jukes_cantor_distance,
    mutation_rate_spectrum,
    punnett_square,
    replication_fork_progression,
    synthetic_methylation_beta_matrix,
)
from biology.numerics import euler_integrate_pair, euler_integrate_scalar


@pytest.mark.parametrize("initial,divisions,efficiency,expected", [
    (0.8, 0, 0.9, 0.8), (0.8, 2, 0.9, 0.722),
    (0.9, 3, 0.0, 0.1125), (0.9, 8, 1.0, 0.9),
    (0.95, 4, 0.5, 0.3005859375), (0.95, 5, 0.5, 0.225439453125),
])
def test_semiconservative_methylated_cytosine_fraction(initial, divisions, efficiency, expected):
    assert cpg_methylation_remaining(initial, divisions, efficiency) == pytest.approx(expected)


@pytest.mark.parametrize("args", [(-0.1, 2, 0.9), (1.1, 2, 0.9), (0.8, -1, 0.9),
    (0.8, 2, -0.1), (0.8, 2, 1.1),
    (math.nan, 2, 0.9), (0.8, 2, math.inf)])
def test_methylation_rejects_invalid_domains(args):
    with pytest.raises(ValueError):
        cpg_methylation_remaining(*args)


@pytest.mark.parametrize("divisions", [1.5, True])
def test_methylation_rejects_invalid_division_types(divisions):
    with pytest.raises(TypeError):
        cpg_methylation_remaining(0.8, divisions, 0.9)


@pytest.mark.parametrize("alpha", [0.1, 0.05, 0.01, 0.001])
def test_chi_square_decision_uses_requested_alpha(alpha):
    result = chi_squared_test([65, 35], [50, 50], alpha=alpha)
    # A squared standard normal has chi-square(1) survival erfc(sqrt(x/2)).
    p = math.erfc(3 / math.sqrt(2))
    assert result.chi_squared == pytest.approx(9)
    assert result.p_value_approx == pytest.approx(p)
    assert result.reject_null == (p < alpha)


@pytest.mark.parametrize("categories", [7, 11])
def test_chi_square_high_degrees_of_freedom(categories):
    observed = [235, 165] + [200] * (categories - 2)
    result = chi_squared_test(observed, [200] * categories)
    # For even df=2m, survival is e^-z * sum(z^j/j!, j=0..m-1).
    z = 12.25 / 2
    m = (categories - 1) // 2
    p = math.exp(-z) * sum(z ** j / math.factorial(j) for j in range(m))
    assert result.p_value_approx == pytest.approx(p)
    assert result.reject_null == (p < 0.05)
    assert not result.reject_null


def test_hwe_fitted_allele_frequency_changes_reference_distribution():
    observed = [20, 60, 20]
    p = (2 * observed[0] + observed[1]) / (2 * sum(observed))
    expected = [sum(observed) * p * p, sum(observed) * 2 * p * (1 - p),
                sum(observed) * (1 - p) ** 2]
    hwe = chi_squared_test(observed, expected, ddof=1)
    assert hwe.chi_squared == pytest.approx(4)
    assert hwe.degrees_of_freedom == 1
    assert hwe.p_value_approx == pytest.approx(math.erfc(math.sqrt(2)))
    assert hwe.reject_null
    fixed = chi_squared_test(observed, expected)
    assert fixed.degrees_of_freedom == 2
    assert fixed.p_value_approx == pytest.approx(math.exp(-2))
    assert not fixed.reject_null
    mendelian = chi_squared_test([450, 130], [435, 145])
    assert mendelian.chi_squared == pytest.approx(60 / 29)
    assert mendelian.degrees_of_freedom == 1


@pytest.mark.parametrize("observed,expected,kwargs", [
    ([-1, 11], [5, 5], {}), ([math.nan, 5], [5, 5], {}),
    ([math.inf, 5], [5, 5], {}), ([5, 5], [math.inf, 5], {}),
    ([5, 5], [math.nan, 5], {}), ([5, 6], [5, 5], {}),
    ([5, 5], [5, 5], {"alpha": 0}), ([5, 5], [5, 5], {"alpha": 1}),
    ([5, 5], [5, 5], {"alpha": math.nan}),
    ([5, 5], [5, 5], {"ddof": 1}), ([5, 5], [5, 5], {"ddof": -1}),
])
def test_chi_square_rejects_invalid_inputs(observed, expected, kwargs):
    with pytest.raises(ValueError):
        chi_squared_test(observed, expected, **kwargs)


@pytest.mark.parametrize("ddof", [0.5, True])
def test_chi_square_rejects_invalid_ddof_types(ddof):
    with pytest.raises(TypeError):
        chi_squared_test([5, 5], [5, 5], ddof=ddof)


@pytest.mark.parametrize("bad", [math.nan, math.inf, -math.inf])
@pytest.mark.parametrize("clip", [True, False])
def test_euler_nonfinite_rates_fail_before_clipping(bad, clip):
    with pytest.raises(ValueError):
        euler_integrate_scalar(1, 1, 1, lambda _: bad, clip_nonnegative=clip)
    for derivative in (lambda x, y: (bad, 0), lambda x, y: (0, bad)):
        with pytest.raises(ValueError):
            euler_integrate_pair((1, 1), 1, 1, derivative, clip_nonnegative=clip)


@pytest.mark.parametrize("bad", [math.nan, math.inf, -math.inf])
def test_euler_nonfinite_initial_values_and_horizons_fail(bad):
    with pytest.raises(ValueError):
        euler_integrate_scalar(bad, 1, 1, lambda _: 0)
    with pytest.raises(ValueError):
        euler_integrate_scalar(1, bad, 1, lambda _: 0)
    with pytest.raises(ValueError):
        euler_integrate_pair((1, bad), 1, 1, lambda x, y: (0, 0))
    with pytest.raises(ValueError):
        euler_integrate_pair((1, 1), bad, 1, lambda x, y: (0, 0))


def test_euler_overflow_is_not_extinction():
    with pytest.raises(ValueError):
        euler_integrate_scalar(-1e308, 2, 1, lambda _: -1e308)
    with pytest.raises(ValueError):
        euler_integrate_pair((1, -1e308), 2, 1, lambda x, y: (0, -1e308))
    assert euler_integrate_scalar(1, 1, 1, lambda _: -2)[1] == [1, 0]
    assert euler_integrate_pair((1, 1), 1, 1, lambda x, y: (-2, -3))[1:] == ([1, 0], [1, 0])


@pytest.mark.parametrize("steps", [0, -1])
def test_euler_requires_positive_steps(steps):
    with pytest.raises(ValueError):
        euler_integrate_scalar(1, 1, steps, lambda _: 0)
    with pytest.raises(ValueError):
        euler_integrate_pair((1, 1), 1, steps, lambda x, y: (0, 0))


@pytest.mark.parametrize("steps", [1.5, True])
def test_euler_requires_integral_step_types(steps):
    with pytest.raises(TypeError):
        euler_integrate_scalar(1, 1, steps, lambda _: 0)
    with pytest.raises(TypeError):
        euler_integrate_pair((1, 1), 1, steps, lambda x, y: (0, 0))


def test_euler_rejects_unrepresentable_time_resolution():
    tiny = math.ulp(0.0)
    with pytest.raises(ValueError):
        euler_integrate_scalar(1, tiny, 2, lambda _: 0)
    with pytest.raises(ValueError):
        euler_integrate_pair((1, 1), tiny, 2, lambda x, y: (0, 0))


@pytest.mark.parametrize("charge", [-1, 1])
def test_single_monovalent_goldman_matches_independent_equilibrium(charge):
    ion = IonConcentration("X", charge, 1, 10)
    expected = GAS_CONSTANT * 310 / FARADAY_CONSTANT * 1000 * math.log(10) / charge
    assert nernst_potential(ion) == pytest.approx(expected)
    assert goldman_equation([ion], [1]) == pytest.approx(expected)


@pytest.mark.parametrize("charge,inside,outside,permeability", [
    (2, 1, 10, 1), (0, 1, 10, 1), (1, -1, -10, 1),
    (1, math.nan, 1, 1), (1, 1, math.inf, 1), (1, 1, 10, math.nan),
    (1, 1, 10, math.inf), (1, 1, 10, -1), (1, 0, 0, 1), (1, 1, 10, 0),
])
def test_goldman_rejects_unsupported_or_invalid_physics(charge, inside, outside, permeability):
    with pytest.raises(ValueError):
        goldman_equation([IonConcentration("X", charge, inside, outside)], [permeability])


def test_goldman_product_overflow_does_not_destroy_equilibrium():
    ion = IonConcentration("X", 1, 1e307, 1e308)
    expected = GAS_CONSTANT * 310 / FARADAY_CONSTANT * 1000 * math.log(10)
    assert goldman_equation([ion], [1e308]) == pytest.approx(expected)


@pytest.mark.parametrize("scale", [1e-200, 1, 1e200, 1e308])
def test_half_saturation_is_invariant_to_common_concentration_scale(scale):
    assert receptor_occupancy(scale, scale) == 0.5
    assert hill_equation(scale, scale, 2) == 0.5
    result = michaelis_menten(scale, scale, scale)
    assert result.efficiency == 0.5
    assert result.reaction_rate == pytest.approx(scale / 2, rel=1e-14, abs=0)


def test_log_quotients_do_not_underflow():
    expected_log = -600 * math.log(10)
    expected_energy = GAS_CONSTANT * 310 / 1000 * expected_log
    assert reaction_free_energy(0, 1e-300, 1e300) == pytest.approx(expected_energy)
    expected_voltage = GAS_CONSTANT * 310 / FARADAY_CONSTANT * 1000 * expected_log
    assert nernst_potential(IonConcentration("X", 1, 1e300, 1e-300)) == pytest.approx(expected_voltage)
    assert atp_free_energy(1, 1, 1) == pytest.approx(-30.5 + GAS_CONSTANT * 310 / 1000 * math.log(0.001))


def test_glycolysis_standard_table_and_glucose_multiplicities():
    # UC Davis Table 1 standard column, independently transcribed; not cellular ΔG.
    energies = (-16.7, 1.67, -14.2, 23.9, 7.56, 6.30, -18.9, 4.4, 1.8, -31.7)
    multiplicities = (1, 1, 1, 1, 1, 2, 2, 2, 2, 2)
    assert tuple(s.delta_G_prime_kJ for s in GLYCOLYSIS_STEPS) == energies
    assert tuple(s.reactions_per_glucose for s in GLYCOLYSIS_STEPS) == multiplicities
    result = glycolysis_summary()
    assert result.total_delta_G_kJ == pytest.approx(-73.97)
    assert (result.net_atp, result.net_nadh) == (2, 2)
    assert "Pi" in result.steps[5].reactants


def test_canonical_pathway_is_deeply_immutable():
    result = glycolysis_summary()
    with pytest.raises(FrozenInstanceError):
        result.steps[0].atp_yield = 100
    with pytest.raises(TypeError):
        result.steps[0].reactants[0] = "changed"
    with pytest.raises(FrozenInstanceError):
        result.steps = ()
    assert glycolysis_summary() == result


def test_atp_stacks_conserve_total_and_explicit_shuttle_adjustment():
    rows = atp_yield_by_pathway()
    for row in rows:
        assert row.total_atp == row.substrate_level_atp + row.oxidative_atp
    aerobic = rows[-1]
    assert aerobic.shuttle_adjustment_atp == -2
    assert aerobic.oxidative_atp == 10 * 2.5 + 2 * 1.5 + aerobic.shuttle_adjustment_atp == 26
    assert aerobic.total_atp == 30


def test_precision_weighting_avoids_large_intermediate_products():
    point = prediction_error_precision_curve(1e200, 1e200, 1e200, (1e200,)).points[0]
    assert point.posterior_mean == pytest.approx(1e200)
    assert point.posterior_precision == pytest.approx(2e200)
    point = prediction_error_precision_curve(-1e200, 1e200, 1e200, (1e200,)).points[0]
    assert point.posterior_mean == pytest.approx(0, abs=1e185)


def test_jukes_cantor_preserves_small_distance_limit():
    assert jukes_cantor_distance(1e-20) == pytest.approx(1e-20, rel=1e-14, abs=0)


def test_powerlaw_normalizes_after_unscaled_weights_would_underflow():
    result = powerlaw_degree_distribution(2000, 2, 3)
    assert result.probabilities == (1.0, 0.0)
    assert result.mean_degree == 2


@pytest.mark.parametrize("bad", [math.nan, math.inf, -math.inf])
def test_nonfinite_scientific_inputs_are_rejected(bad):
    calls = [lambda: michaelis_menten(bad, 10, 1), lambda: michaelis_menten(1, bad, 1),
        lambda: michaelis_menten(1, 10, bad), lambda: receptor_occupancy(bad, 1),
        lambda: hill_equation(1, 1, bad), lambda: atp_free_energy(bad, 1, 1),
        lambda: atp_free_energy(1, bad, 1), lambda: atp_free_energy(1, 1, bad),
        lambda: atp_free_energy(temperature_K=bad), lambda: poisson_degree_distribution(bad),
        lambda: powerlaw_degree_distribution(bad),
        lambda: prediction_error_precision_curve(prior_precision=bad),
        lambda: prediction_error_precision_curve(precisions=(bad,)),
        lambda: replication_fork_progression(duration_s=bad)]
    for call in calls:
        with pytest.raises(ValueError):
            call()


@pytest.mark.parametrize("args", [(-3, -1, 10), (0, 1, 10), (3, 0, 10), (3, 1, -10)])
def test_atp_rejects_nonpositive_pools(args):
    with pytest.raises(ValueError):
        atp_free_energy(*args)


@pytest.mark.parametrize("coefficient", [0, -1])
def test_hill_requires_positive_coefficient_even_at_zero_ligand(coefficient):
    with pytest.raises(ValueError):
        hill_equation(0, 1, coefficient)


def test_monohybrid_and_gc_do_not_silently_reinterpret_invalid_data():
    for parents in (("Aa", "Bb"), ("AB", "Aa"), ("12", "12")):
        with pytest.raises(ValueError):
            punnett_square(*parents)
    assert punnett_square("Aa", "Aa").genotype_ratios == {"AA": 0.25, "Aa": 0.5, "aa": 0.25}
    for sequence in ("XXXX", "ACGN", "AC G"):
        with pytest.raises(ValueError):
            gc_content(sequence)
    assert gc_content("ATGCGCGCATAA") == 0.5
    assert gc_content("AUGC") == 0.5


@pytest.mark.parametrize("span", [20, 20 + 1e-10])
def test_linkage_accepts_additive_map_with_reversed_pair_keys(span):
    result = infer_three_point_order({("B", "A"): 12, ("C", "B"): 8, ("A", "C"): span})
    assert result.order == ("A", "B", "C")
    assert sum(result.adjacent_distances_cM) == pytest.approx(result.span_cM)


@pytest.mark.parametrize("distances", [(12, 8, 25), (10, 10, 10), (12, 8, math.nan), (12, 8, math.inf)])
def test_linkage_rejects_nonadditivity_not_just_negative_distances(distances):
    with pytest.raises(ValueError):
        infer_three_point_order(dict(zip((("A", "B"), ("B", "C"), ("A", "C")), distances)))


def test_colocated_markers_are_valid_even_with_tied_longest_distances():
    result = infer_three_point_order({("A", "B"): 0, ("A", "C"): 10, ("B", "C"): 10})
    assert result.order == ("A", "B", "C")
    assert result.adjacent_distances_cM == (0, 10)
    assert result.span_cM == 10


def test_organelle_inventory_distinguishes_membranes_from_protein_assemblies():
    animal = get_organelles_by_cell_type("animal")
    by_name = {row.name: row for row in animal}
    assert not by_name["Centriole"].membrane_bound
    assert not by_name["Ribosome"].membrane_bound
    assert by_name["Nucleus"].membrane_bound
    assert by_name["Peroxisome"].membrane_bound
    assert count_membrane_bound_organelles(animal) == 6


def test_lipid_path_is_not_a_polymer_family():
    polymer_families = {row.family for row in MACROMOLECULE_TIERS if row.is_polymer}
    assert polymer_families == {"Proteins", "Nucleic acids", "Carbohydrates"}
    assert not next(row for row in MACROMOLECULE_TIERS if row.family == "Lipids").is_polymer


def test_mutation_evidence_preserves_incompatible_denominators_without_conversion():
    rows = {row.mutation_class: row for row in mutation_rate_spectrum()}
    assert rows["Single-nucleotide substitution"].rate_range == (1.1e-8, 1.1e-8)
    assert rows["Microsatellite slippage"].rate_range == (2.73e-4, 2.73e-4)
    assert rows["Microsatellite slippage"].target == "dinucleotide microsatellite locus"
    assert rows["Copy-number variant >500 bp"].target == "haploid genome"
    duplication = rows["Whole-gene duplication"]
    assert (duplication.rate_range, duplication.target, duplication.time_basis) == ((0.01, 0.01), "gene", "million years")
    assert rows["Small insertion or deletion"].rate_range is None
    assert rows["CpG transition"].rate_range is None
    assert len({(row.target, row.time_basis) for row in rows.values() if row.rate_range is not None}) == 4


def test_synthetic_methylation_reproducible_without_global_rng_changes():
    before = np.random.get_state()
    first = synthetic_methylation_beta_matrix(rng_seed=91)
    second = synthetic_methylation_beta_matrix(rng_seed=91)
    after = np.random.get_state()
    np.testing.assert_array_equal(first, second)
    assert before[0] == after[0] and before[2:] == after[2:]
    np.testing.assert_array_equal(before[1], after[1])


def test_corrected_reference_tables_reach_real_figure_consumers(tmp_path):
    from visualization.plots_foundations import plot_polymer_hierarchy
    from visualization.plots_genetics import plot_mutation_rate_spectrum
    from visualization.plots_physiology import (
        plot_atp_yield_comparison,
        plot_glycolysis_summary,
    )

    before = glycolysis_summary()
    for generator in (plot_polymer_hierarchy, plot_mutation_rate_spectrum,
                      plot_atp_yield_comparison, plot_glycolysis_summary):
        path = generator(tmp_path)
        assert path.is_file() and path.stat().st_size > 0
    assert glycolysis_summary() == before
