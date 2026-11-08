"""Independent mathematical references and scientific admissibility boundaries."""

import math
from typing import cast

import pytest

from biology.botany import (
    photosynthesis_rate,
    plant_biomass_growth,
    pollen_tube_growth,
    transpiration_flux,
    water_potential,
)
from biology.ecology import (
    allee_strong_growth,
    biodiversity_indices,
    connectance,
    logistic_growth,
    lotka_volterra,
)
from biology.evolution import (
    Population,
    fitness_landscape_1d,
    isolation_index,
    molecular_clock_divergence_time,
    selection_one_generation,
    simulate_drift,
    wright_fisher_drift,
)
from biology.microbiology import bacterial_growth_curve, sir_model
from biology.neuroscience import (
    action_potential_hh,
    cable_voltage_attenuation,
    hebbian_weight_update,
)
from biology.neuroscience.neuroscience import _alpha_m, _alpha_n
from biology.physiology import homeostasis_response, oxygen_saturation, poiseuille_flow


def test_transpiration_molar_conductance_uses_dimensionless_gradient():
    # Independent gas conversion: concentrations .5/.3 mol m^-3 in air
    # containing 40 mol m^-3 imply a mole-fraction difference of .005.
    result = transpiration_flux(0.2, 0.5 / 40, 0.3 / 40)
    assert result.delta_mole_fraction == pytest.approx(0.005)
    assert result.flux_mol_m2_s == pytest.approx(0.001)
    assert result.flux_mmol_m2_s == pytest.approx(1.0)
    assert transpiration_flux(0.4, 0.0125, 0.0075).flux_mmol_m2_s == pytest.approx(2.0)
    assert transpiration_flux(0.2, 0.0075, 0.0125).flux_mmol_m2_s == pytest.approx(-1.0)
    assert transpiration_flux(0.2, 0.01, 0.01).flux_mol_m2_s == 0.0


@pytest.mark.parametrize("fraction", [-0.1, 1.1, math.nan, math.inf])
def test_transpiration_rejects_invalid_mole_fractions(fraction):
    with pytest.raises(ValueError):
        transpiration_flux(0.2, fraction, 0.01)
    with pytest.raises(ValueError):
        transpiration_flux(0.2, 0.01, fraction)


def test_sir_rejects_population_creating_coarse_resolution():
    # Independent old-Euler transfers would be 250 infections and 50
    # recoveries. Clipping S=-200 to zero would create a total of 300.
    with pytest.raises(ValueError):
        sir_model(100, 50, 10.0, 1.0, days=1.0, steps_per_day=1)
    with pytest.raises(ValueError):
        sir_model(100, 50, 0.0, 10.0, days=1.0, steps_per_day=1)


@pytest.mark.parametrize("days", [0.1, 1.1, 2.0])
def test_sir_fractional_horizon_and_conservation(days):
    result = sir_model(100, 50, 0.4, 0.1, days, steps_per_day=4)
    assert result.times_days[-1] == days
    assert len(result.times_days) == math.ceil(days * 4) + 1
    assert all(b > a for a, b in zip(result.times_days, result.times_days[1:]))
    assert len(result.infected) == len(result.susceptible) == len(result.recovered) == len(result.times_days)
    for s, i, r in zip(result.susceptible, result.infected, result.recovered):
        assert all(0 <= value <= 100 for value in (s, i, r))
        assert s + i + r == pytest.approx(100, abs=1e-10)
    assert result.infected[-1] != result.infected[0]


def test_sir_recovery_only_converges_to_exponential_solution():
    expected = 50 * math.exp(-0.6 * 3)
    errors = []
    for resolution in (4, 8, 16):
        result = sir_model(100, 50, 0.0, 0.6, 3.0, steps_per_day=resolution)
        errors.append(abs(result.infected[-1] - expected))
        assert result.susceptible == [50.0] * len(result.times_days)
        assert result.recovered[-1] == pytest.approx(50 - result.infected[-1])
    assert errors[1] < 0.6 * errors[0]
    assert errors[2] < 0.6 * errors[1]


@pytest.mark.parametrize("initial", [10.0, 150.0])
def test_logistic_euler_bounds_and_analytic_convergence(initial):
    K, r, horizon = 100.0, 0.3, 5.0
    expected = K / (1 + (K / initial - 1) * math.exp(-r * horizon))
    errors = []
    for steps in (100, 200, 400):
        result = logistic_growth(initial, r, K, horizon, steps)
        assert all(min(initial, K) <= n <= max(initial, K) for n in result.populations)
        errors.append(abs(result.populations[-1] - expected))
    assert errors[1] < 0.6 * errors[0]
    assert errors[2] < 0.6 * errors[1]
    assert logistic_growth(K, r, K, horizon, 100).populations == [K] * 101


def test_growth_wrappers_reject_unstable_euler_instead_of_clipping():
    with pytest.raises(ValueError):
        logistic_growth(90, 10, 100, 1, steps=2)
    with pytest.raises(ValueError):
        plant_biomass_growth(90, 10, 100, 1, steps=2)
    with pytest.raises(ValueError):
        allee_strong_growth(90, 10, 50, 100, 1, steps=1)
    with pytest.raises(ValueError):
        lotka_volterra(1, 1, 1, 10, 1, 1, 1, steps=1)


def test_biomass_converges_to_independent_logistic_solution():
    expected = 100 / (1 + 99 * math.exp(-0.1 * 30))
    coarse = plant_biomass_growth(1, 0.1, 100, 30, steps=100)
    fine = plant_biomass_growth(1, 0.1, 100, 30, steps=200)
    assert all(1 <= mass < 100 for mass in fine.biomass_g)
    assert abs(fine.biomass_g[-1] - expected) < 0.6 * abs(coarse.biomass_g[-1] - expected)


@pytest.mark.parametrize("initial", [0.0, 50.0, 100.0])
def test_allee_equilibria_are_preserved(initial):
    result = allee_strong_growth(initial, 0.5, 50, 100, 5, steps=100)
    assert result.populations == [initial] * 101


@pytest.mark.parametrize("initial", [10.0, 60.0])
def test_allee_converges_to_separated_implicit_solution(initial):
    # Integral of dN/[r*N*(N/A-1)*(1-N/K)] from N0 to N is t.
    def primitive(n):
        return (-math.log(n) + 2 * math.log(abs(n - 50)) - math.log(abs(100 - n))) / 0.5

    residuals = []
    for steps in (100, 200):
        result = allee_strong_growth(initial, 0.5, 50, 100, 1, steps)
        residuals.append(abs(primitive(result.populations[-1]) - primitive(initial) - 1))
        if initial < 50:
            assert all(b <= a for a, b in zip(result.populations, result.populations[1:]))
        else:
            assert all(a <= b <= 100 for a, b in zip(result.populations, result.populations[1:]))
    assert residuals[1] < 0.6 * residuals[0]


def _lv_invariant(n, p):
    return 0.01 * n - 0.2 * math.log(n) + 0.02 * p - 0.5 * math.log(p)


def test_predator_prey_equilibrium_and_invariant_convergence():
    equilibrium = lotka_volterra(20, 25, 0.5, 0.02, 0.01, 0.2, 10, steps=100)
    assert equilibrium.prey == pytest.approx([20] * 101)
    assert equilibrium.predator == pytest.approx([25] * 101)
    errors = []
    for steps in (200, 400):
        result = lotka_volterra(40, 9, 0.5, 0.02, 0.01, 0.2, 10, steps)
        h0 = _lv_invariant(40, 9)
        errors.append(max(abs(_lv_invariant(n, p) - h0) for n, p in zip(result.prey, result.predator)))
    assert errors[1] < 0.6 * errors[0]
    assert errors[1] < 0.02


def test_publication_predator_prey_grid_has_bounded_invariant_drift():
    # These are the registered plot's actual parameters/grid, not an exact orbit.
    result = lotka_volterra(40, 9, 0.5, 0.02, 0.01, 0.2, 100, steps=100000)
    h0 = _lv_invariant(40, 9)
    assert max(abs(_lv_invariant(n, p) - h0) for n, p in zip(result.prey, result.predator)) < 0.01


def test_pollen_saturating_linear_law_is_grid_independent_and_bounded():
    expected = 100 - 50 * math.exp(-12 * 20 / 100)
    for steps in (1, 20, 200):
        result = pollen_tube_growth(max_length_um=100, initial_length_um=50,
                                    growth_rate_um_per_min=12, duration_min=20, steps=steps)
        assert result.lengths_um[0] == 50
        assert result.lengths_um[-1] == pytest.approx(expected)
        assert all(50 <= a <= b <= 100 for a, b in zip(result.lengths_um, result.lengths_um[1:]))
    short = pollen_tube_growth(max_length_um=100, initial_length_um=50,
                              growth_rate_um_per_min=12, duration_min=1e-5, steps=1)
    assert (short.lengths_um[-1] - 50) / 1e-5 == pytest.approx(6, rel=1e-5)


def test_bacterial_stationary_transition_preserves_reached_population():
    before = bacterial_growth_curve(1e4, 0.5, 7 - 1e-6, steps=1, lag_phase_hr=1,
                                    stationary_phase_start_hr=7, carrying_capacity=5e9)
    at = bacterial_growth_curve(1e4, 0.5, 7, steps=1, lag_phase_hr=1,
                                stationary_phase_start_hr=7, carrying_capacity=5e9)
    after = bacterial_growth_curve(1e4, 0.5, 8, steps=8, lag_phase_hr=1,
                                   stationary_phase_start_hr=7, carrying_capacity=5e9)
    expected = 1e4 * 2**12
    assert before.populations[-1] == pytest.approx(expected, rel=2e-6)
    assert at.populations[-1] == pytest.approx(expected)
    assert after.populations[-1] == pytest.approx(expected)
    assert after.populations[-2] == pytest.approx(after.populations[-1])


def test_bacterial_onset_without_capacity_and_capacity_without_onset():
    stationary = bacterial_growth_curve(10, 1, 5, steps=5, lag_phase_hr=1, stationary_phase_start_hr=3)
    assert stationary.populations == pytest.approx([10, 10, 20, 40, 40, 40])
    capped = bacterial_growth_curve(10, 1, 5, steps=5, lag_phase_hr=1, carrying_capacity=30)
    assert capped.populations == pytest.approx([10, 10, 20, 30, 30, 30])
    fractional = bacterial_growth_curve(0.1, 1, 1, steps=1, lag_phase_hr=1)
    assert fractional.log_populations == pytest.approx([-1, -1])


@pytest.mark.parametrize("kwargs", [
    {"lag_phase_hr": -1}, {"lag_phase_hr": math.nan},
    {"stationary_phase_start_hr": 0.5}, {"stationary_phase_start_hr": math.inf},
    {"carrying_capacity": -1}, {"carrying_capacity": 9}, {"carrying_capacity": math.nan},
])
def test_bacterial_invalid_phase_parameters_fail(kwargs):
    with pytest.raises(ValueError):
        bacterial_growth_curve(10, 1, 5, **kwargs)


def test_flow_direction_preserves_reynolds_regime_and_unit_conversion():
    forward = poiseuille_flow(1000, 0.002, 0.1)
    reverse = poiseuille_flow(-1000, 0.002, 0.1)
    expected = math.pi * 0.002**4 * 1000 / (8 * 0.003 * 0.1)
    assert forward.volumetric_flow_m3s == pytest.approx(expected)
    assert forward.volumetric_flow_mL_min == pytest.approx(expected * 60e6)
    assert reverse.volumetric_flow_m3s == pytest.approx(-expected)
    assert reverse.reynolds_number == pytest.approx(forward.reynolds_number)
    assert forward.flow_regime == reverse.flow_regime == "turbulent"
    assert poiseuille_flow(0, 0.002, 0.1).reynolds_number == 0
    small = poiseuille_flow(1000, 0.001, 0.1)
    assert forward.volumetric_flow_m3s / small.volumetric_flow_m3s == pytest.approx(16)


@pytest.mark.parametrize("scale", [1e-200, 26, 1e200])
def test_hill_half_saturation_is_scale_invariant(scale):
    assert oxygen_saturation(scale, scale).saturation == 0.5


def test_bounded_hill_and_photosynthesis_extreme_finite_inputs():
    values = [oxygen_saturation(p).saturation for p in (0, 1e-200, 26, 100, 1e200)]
    assert values == sorted(values)
    assert all(0 <= s <= 1 for s in values)
    assert values[-1] == 1
    assert photosynthesis_rate(1e200, 1e200, 1e200, 0) == pytest.approx(5e199)
    assert photosynthesis_rate(800, 20, 800, 1.5) == pytest.approx(8.5)


@pytest.mark.parametrize("start,duration,capacitance", [(0, 1, 1), (0, 0, 1), (0.25, 1, 1), (0.25, 0.5, 2)])
def test_hh_injected_charge_including_zero_and_off_grid_pulses(start, duration, capacitance):
    result = action_potential_hh(stimulus_current_µA=10, t_end_ms=2, steps=2,
                                 g_Na_mS=0, g_K_mS=0, g_L_mS=0, C_m_µF=capacitance,
                                 stimulus_start_ms=start, stimulus_duration_ms=duration)
    assert result.voltage_mV[-1] == pytest.approx(-70 + 10 * duration / capacitance)


def test_hh_removable_rate_singularities_and_waveform_convergence():
    for delta in (-1e-8, 0, 1e-8):
        assert _alpha_m(-40 + delta) == pytest.approx(1)
        assert _alpha_n(-55 + delta) == pytest.approx(0.1)
    coarse = action_potential_hh(steps=6000)
    fine = action_potential_hh(steps=12000)
    reference = action_potential_hh(steps=24000)
    coarse_error = max(abs(a - b) for a, b in zip(coarse.voltage_mV, reference.voltage_mV[::4]))
    fine_error = max(abs(a - b) for a, b in zip(fine.voltage_mV, reference.voltage_mV[::2]))
    assert fine_error < coarse_error
    assert fine_error < 2.0
    unstimulated = action_potential_hh(stimulus_current_µA=0, t_end_ms=10, steps=1000)
    assert all(math.isfinite(v) for v in unstimulated.voltage_mV)


def test_cable_specific_units_and_exact_one_space_constant():
    expected_lambda = math.sqrt(20000 * 5e-5 / (2 * 100)) * 1e4
    result = cable_voltage_attenuation(10, 100, 20, 5e-5, expected_lambda, n_points=1)
    assert result.lambda_µm == pytest.approx(707.1067811865476)
    assert result.voltages_mV[-1] == pytest.approx(10 / math.e)
    thicker = cable_voltage_attenuation(10, 100, 20, 2e-4)
    assert thicker.lambda_µm == pytest.approx(2 * expected_lambda)


def test_clipped_hebb_is_additive_potentiation_even_at_low_activity():
    assert hebbian_weight_update(0.5, 0.1, 0.1, 0.01) == pytest.approx(0.5001)
    assert hebbian_weight_update(0.5, 0, 1) == 0.5
    assert hebbian_weight_update(0.99, 1, 1, 0.1) == 1


@pytest.mark.parametrize("p", [-0.1, 1.5, math.nan, math.inf])
def test_drift_entrypoints_reject_invalid_frequency(p):
    with pytest.raises(ValueError):
        simulate_drift(p, 2, 1)
    with pytest.raises(ValueError):
        wright_fisher_drift(p, 2)
    with pytest.raises(ValueError):
        Population("bad", p, 1 - p)


@pytest.mark.parametrize("N", [0, -1])
def test_drift_entrypoints_require_positive_population(N):
    with pytest.raises(ValueError):
        simulate_drift(0.5, N, 1)
    with pytest.raises(ValueError):
        wright_fisher_drift(0.5, N)


@pytest.mark.parametrize("N", [1.5, True])
def test_drift_entrypoints_require_integral_population_types(N):
    with pytest.raises(TypeError):
        simulate_drift(0.5, N, 1)
    with pytest.raises(TypeError):
        wright_fisher_drift(0.5, N)


def test_selection_rejects_negative_fitness_and_mutated_invalid_population():
    with pytest.raises(ValueError):
        Population("bad", 0.5, 0.5, -1, 0, 2)
    with pytest.raises(ValueError):
        fitness_landscape_1d([0.5], -1, 0, 2)
    with pytest.raises(ValueError):
        fitness_landscape_1d([1.5], 1, 1, 1)
    pop = Population("mutated", 0.5, 0.5)
    pop.p, pop.q = 2, -1
    with pytest.raises(ValueError):
        selection_one_generation(pop)


def test_drift_reproducibility_distinct_seed_ensembles_and_absorption():
    first = simulate_drift(0.5, 5, 10, rng_seed=17)
    assert first == simulate_drift(0.5, 5, 10, rng_seed=17)
    assert first[1] == wright_fisher_drift(0.5, 5, rng_seed=17)
    ensemble = [tuple(simulate_drift(0.5, 5, 10, rng_seed=seed)) for seed in range(8)]
    assert len(set(ensemble)) > 1
    assert simulate_drift(0, 1, 10) == [0] * 11
    assert simulate_drift(1, 1, 10) == [1] * 11


def test_ratio_heuristic_and_molecular_clock_have_honest_numeric_contracts():
    assert isolation_index(0.01, 0.001) == pytest.approx(1 / 11)
    assert isolation_index(1e308, 1e308) == pytest.approx(0.5)
    with pytest.raises(ValueError):
        isolation_index(0, 0)
    distance = -0.75 * math.log1p(-4 * 0.015 / 3)
    recent = molecular_clock_divergence_time(2e-8, distance)
    assert recent == pytest.approx(378800.762203489)
    assert molecular_clock_divergence_time(1e-8, distance) == pytest.approx(2 * recent)
    assert molecular_clock_divergence_time(2e-8, 0) == 0
    assert water_potential(0.3, 0.5, 293).water_potential_MPa == pytest.approx(-0.2308006)


@pytest.mark.parametrize("call", [
    lambda: biodiversity_indices([-1, 2]),
    lambda: biodiversity_indices([cast(int, math.nan), 2]),
    lambda: connectance(2, 5),
    lambda: connectance(2, -1),
    lambda: photosynthesis_rate(0, dark_respiration_µmol_CO2_m2_s=-2),
    lambda: cable_voltage_attenuation(10, max_distance_µm=-1),
    lambda: hebbian_weight_update(0.5, 1, 1, weight_min=2, weight_max=1),
    lambda: hebbian_weight_update(0.5, 2, 1),
    lambda: homeostasis_response(37, 38, gain=-1),
    lambda: homeostasis_response(37, 38, tolerance=-1),
    lambda: action_potential_hh(C_m_µF=0),
    lambda: action_potential_hh(g_Na_mS=-1),
    lambda: action_potential_hh(stimulus_duration_ms=-1),
])
def test_impossible_scientific_domains_are_rejected(call):
    with pytest.raises(ValueError):
        call()


@pytest.mark.parametrize("bad", [math.nan, math.inf, -math.inf])
def test_nonfinite_inputs_are_not_hidden_by_clipping_or_bounded_outputs(bad):
    calls = [
        lambda: logistic_growth(10, bad, 100, 1),
        lambda: allee_strong_growth(10, 0.1, 50, 100, bad),
        lambda: lotka_volterra(40, 9, bad, 0.02, 0.01, 0.2, 10),
        lambda: plant_biomass_growth(1, bad, 100, 1),
        lambda: pollen_tube_growth(growth_rate_um_per_min=bad),
        lambda: bacterial_growth_curve(10, bad, 1),
        lambda: sir_model(100, 50, bad, 1, 1),
        lambda: oxygen_saturation(bad),
        lambda: poiseuille_flow(bad, 0.002, 0.1),
        lambda: photosynthesis_rate(bad),
        lambda: action_potential_hh(stimulus_current_µA=bad),
        lambda: homeostasis_response(37, bad),
        lambda: fitness_landscape_1d([0.5], 1, bad, 1),
        lambda: isolation_index(bad, 0.001),
    ]
    for call in calls:
        with pytest.raises(ValueError):
            call()
