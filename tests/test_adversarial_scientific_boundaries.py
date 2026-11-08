"""Real public-consumer boundaries for the independently refuted API cases."""

from __future__ import annotations

import math
from decimal import Decimal, localcontext

import pytest

from biology.biochemistry import competitive_inhibition, enzyme_rate_curve
from biology.botany import light_response_curve, pollen_tube_growth
from biology.ecology import exponential_growth
from biology.evolution import molecular_clock_divergence_time
from biology.genetics import replication_fork_progression
from biology.microbiology import bacterial_growth_curve, doubling_time, sir_model
from biology.neuroscience import action_potential_hh, cable_voltage_attenuation


def test_pollen_large_finite_horizon_matches_exact_growth_law() -> None:
    result = pollen_tube_growth(
        max_length_um=100.0, initial_length_um=50.0,
        growth_rate_um_per_min=1e-306, duration_min=1e308, steps=2,
    )
    assert result.times_min == [0.0, 5e307, 1e308]
    assert result.lengths_um == pytest.approx(
        [50.0, 100.0 - 50.0 * math.exp(-0.5), 100.0 - 50.0 / math.e],
        rel=1e-14,
    )
    assert all(math.isfinite(t) for t in result.times_min)


def test_zero_initial_pollen_matches_printed_thirty_minute_example() -> None:
    result = pollen_tube_growth(
        max_length_um=400.0, initial_length_um=0.0,
        growth_rate_um_per_min=4.0, duration_min=30.0, steps=3,
    )
    assert result.times_min == [0.0, 10.0, 20.0, 30.0]
    assert result.lengths_um == pytest.approx(
        [400.0 * (1.0 - math.exp(-t / 100.0)) for t in (0.0, 10.0, 20.0, 30.0)],
        rel=1e-14, abs=0.0,
    )
    assert result.lengths_um[-1] == pytest.approx(103.67271172731285, rel=1e-14)


def test_pollen_at_saturation_is_an_equilibrium() -> None:
    result = pollen_tube_growth(
        max_length_um=400.0, initial_length_um=400.0,
        growth_rate_um_per_min=4.0, duration_min=30.0, steps=3,
    )
    assert result.lengths_um == [400.0] * 4


@pytest.mark.parametrize("initial", [-1.0, 401.0, math.inf, math.nan])
def test_pollen_rejects_initial_length_outside_closed_domain(initial: float) -> None:
    with pytest.raises(ValueError):
        pollen_tube_growth(max_length_um=400.0, initial_length_um=initial)


def test_cable_large_finite_distance_retains_requested_endpoint() -> None:
    result = cable_voltage_attenuation(10.0, max_distance_µm=1e308, n_points=2)
    assert result.distances_µm == [0.0, 5e307, 1e308]
    assert result.voltages_mV == [10.0, 0.0, 0.0]
    assert result.lambda_µm == pytest.approx(math.sqrt(0.125) * 1e4, rel=1e-14)
    assert all(math.isfinite(d) for d in result.distances_µm)


def test_independent_growth_and_replication_grids_retain_large_endpoint() -> None:
    ecological = exponential_growth(2.0, 0.0, 1e308, steps=2)
    assert ecological.times == [0.0, 5e307, 1e308]
    assert ecological.populations == [2.0, 2.0, 2.0]
    bacterial = bacterial_growth_curve(
        2.0, 1.0, 1e308, steps=2, stationary_phase_start_hr=1.0,
    )
    assert bacterial.times_hr == [0.0, 5e307, 1e308]
    assert bacterial.populations == [2.0, 2.0, 2.0]
    profile = replication_fork_progression(
        velocity_bp_per_s=1e-308, duration_s=1e308, steps=2,
    )
    assert profile.times_s == (0.0, 5e307, 1e308)
    assert profile.bases_replicated == pytest.approx((0.0, 1.0, 2.0), rel=1e-14)


def test_sampled_enzyme_and_light_curves_preserve_exact_endpoint() -> None:
    endpoint = 0.7  # (endpoint / 3) * 3 need not round back to endpoint.
    enzymes = enzyme_rate_curve(10.0, endpoint, n_points=3, max_conc=endpoint)
    light = light_response_curve(
        max_rate=10.0, light_saturation_point=endpoint,
        dark_respiration=0.0, n_points=3, max_par=endpoint,
    )
    assert enzymes[-1].substrate_concentration == endpoint
    assert enzymes[-1].reaction_rate == pytest.approx(5.0, rel=1e-14)
    assert light[-1] == (endpoint, 5.0)
    assert enzymes[1].reaction_rate == pytest.approx(2.5, rel=1e-14)
    assert light[1][1] == pytest.approx(2.5, rel=1e-14)


@pytest.mark.parametrize("endpoint, intervals", [(5e-324, 2), (1e-323, 3)])
@pytest.mark.parametrize(
    "consumer, kwargs, endpoint_key, intervals_key",
    [
        (pollen_tube_growth, {}, "duration_min", "steps"),
        (cable_voltage_attenuation, {"V0_mV": 10.0}, "max_distance_μm", "n_points"),
        (action_potential_hh, {}, "t_end_ms", "steps"),
        (exponential_growth, {"N0": 1.0, "r": 0.0}, "t_end", "steps"),
        (bacterial_growth_curve, {"N0": 1.0, "doubling_time_hr": 1.0}, "t_end_hr", "steps"),
        (replication_fork_progression, {}, "duration_s", "steps"),
        (enzyme_rate_curve, {"Vmax": 10.0, "Km": 1.0}, "max_conc", "n_points"),
        (light_response_curve, {}, "max_par", "n_points"),
    ],
)
def test_unrepresentable_grid_resolution_raises_domain_error(
    consumer, kwargs, endpoint_key: str, intervals_key: str,
    endpoint: float, intervals: int,
) -> None:
    arguments = {**kwargs, endpoint_key: endpoint, intervals_key: intervals}
    with pytest.raises(ValueError):
        consumer(**arguments)


def test_representable_subnormal_grid_is_not_rejected_as_a_tiny_horizon() -> None:
    result = exponential_growth(3.0, 0.0, 1e-323, steps=2)
    assert result.times == [0.0, 5e-324, 1e-323]
    assert result.populations == [3.0, 3.0, 3.0]


def test_sir_interval_count_overflow_is_a_domain_error() -> None:
    with pytest.raises(ValueError):
        sir_model(100, 1, 0.0, 1.0, days=1e308, steps_per_day=4)


@pytest.mark.parametrize(
    "substrate, km, inhibitor, ki, apparent_km",
    [
        (1e200, 1e-200, 1e200, 1e-200, 1e200),
        (2e-300, 1e-300, 1e300, 1e300, 2e-300),
        (15.0, 5.0, 10.0, 5.0, 15.0),
    ],
)
def test_competitive_inhibition_uses_representable_apparent_km(
    substrate: float, km: float, inhibitor: float, ki: float, apparent_km: float,
) -> None:
    result = competitive_inhibition(substrate, 10.0, km, inhibitor, ki)
    assert result.Km == pytest.approx(apparent_km, rel=1e-14, abs=0.0)
    assert result.reaction_rate == pytest.approx(5.0, rel=1e-14)
    assert result.efficiency == pytest.approx(0.5, rel=1e-14)
    assert result.Vmax == 10.0
    assert result.substrate_concentration == substrate


def test_competitive_inhibition_rejects_genuinely_unrepresentable_apparent_km() -> None:
    with pytest.raises(ValueError):
        competitive_inhibition(1e308, 10.0, 1e308, 1.0, 1.0)


def test_doubling_time_uses_log_difference_instead_of_overflowing_count_ratio() -> None:
    expected = math.log(2.0) / (600.0 * math.log(10.0))
    assert doubling_time(1e-300, 1e300, 1.0) == pytest.approx(expected, rel=1e-14, abs=0.0)
    assert doubling_time(100.0, 200.0, 1.0) == pytest.approx(1.0, rel=1e-14)


def test_doubling_time_resolves_nearly_equal_large_counts() -> None:
    initial = 1e300
    final = math.nextafter(initial, math.inf)
    with localcontext() as context:
        context.prec = 80
        expected = float(Decimal(2).ln() / (Decimal(final) / Decimal(initial)).ln())
    assert doubling_time(initial, final, 1.0) == pytest.approx(expected, rel=1e-14)


@pytest.mark.parametrize(
    "rate, divergence, expected",
    [
        (1e308, 1e308, 0.5),
        (1e-308, 3.0, 1.5e308),
        (5e-324, 1.5e-323, 1.5),
        (2e-9, 0.01, 2.5e6),
        (1e308, 0.0, 0.0),
    ],
)
def test_molecular_clock_scaled_division_preserves_finite_answers(
    rate: float, divergence: float, expected: float,
) -> None:
    assert molecular_clock_divergence_time(rate, divergence) == pytest.approx(
        expected, rel=1e-14, abs=0.0,
    )


@pytest.mark.parametrize("rate, divergence", [(5e-324, 1e308), (1e308, 5e-324)])
def test_clock_rejects_positive_time_outside_representable_range(
    rate: float, divergence: float,
) -> None:
    with pytest.raises(ValueError):
        molecular_clock_divergence_time(rate, divergence)
