"""Tests for shared numerical integration helpers."""

from __future__ import annotations

import math
from itertools import pairwise

import pytest

from biology.numerics import euler_integrate_pair, euler_integrate_scalar


def test_euler_scalar_converges_to_exponential_solution() -> None:
    errors = []
    for steps in (20, 40, 80):
        times, values = euler_integrate_scalar(1.0, 1.0, steps, lambda y: y)
        assert times[0] == 0.0
        assert times[-1] == 1.0
        assert all(a < b for a, b in pairwise(times))
        errors.append(abs(values[-1] - math.e))
    assert errors[1] < 0.55 * errors[0]
    assert errors[2] < 0.55 * errors[1]


def test_euler_integrate_scalar_rejects_nonpositive_horizon() -> None:
    with pytest.raises(ValueError):
        euler_integrate_scalar(1.0, 0.0, 10, lambda y: y)


def test_euler_pair_converges_to_independent_decay_solutions() -> None:
    errors = []
    for steps in (40, 80, 160):
        times, first, second = euler_integrate_pair(
            (1.0, 2.0), 1.0, steps, lambda x, y: (-x, -2 * y)
        )
        assert len(times) == len(first) == len(second) == steps + 1
        assert times[-1] == 1.0
        errors.append(abs(first[-1] - math.exp(-1)) + abs(second[-1] - 2 * math.exp(-2)))
    assert errors[1] < 0.55 * errors[0]
    assert errors[2] < 0.55 * errors[1]


def test_euler_integrate_scalar_can_allow_negative_values() -> None:
    _, values = euler_integrate_scalar(
        1.0,
        1.0,
        3,
        lambda _y: -2.0,
        clip_nonnegative=False,
    )
    assert values[-1] < 0.0


def test_euler_integrate_pair_clips_negative_values() -> None:
    _, series1, series2 = euler_integrate_pair(
        (1.0, 1.0),
        1.0,
        5,
        lambda _y1, _y2: (-10.0, -10.0),
    )
    assert all(value >= 0.0 for value in series1)
    assert all(value >= 0.0 for value in series2)


def test_subnormal_scalar_steps_cannot_integrate_a_different_horizon() -> None:
    calls: list[float] = []

    def rate(value: float) -> float:
        calls.append(value)
        return 1.0

    with pytest.raises(ValueError):
        euler_integrate_scalar(0.0, 3 * math.ulp(0.0), 2, rate, clip_nonnegative=False)
    assert calls == []


def test_pair_time_grid_cannot_repeat_the_requested_endpoint() -> None:
    calls: list[tuple[float, float]] = []

    def rates(first: float, second: float) -> tuple[float, float]:
        calls.append((first, second))
        return 1.0, -1.0

    with pytest.raises(ValueError):
        euler_integrate_pair((0.0, 0.0), 2 * math.ulp(0.0), 3, rates, clip_nonnegative=False)
    assert calls == []


@pytest.mark.parametrize("horizon,steps,rate", [
    (0.7, 3, 2.0),
    (2 * math.ulp(0.0), 2, 1e308),
])
def test_admitted_constant_rate_grids_preserve_elapsed_time(
    horizon: float, steps: int, rate: float,
) -> None:
    times, values = euler_integrate_scalar(0.0, horizon, steps, lambda _: rate, clip_nonnegative=False)
    assert times[-1] == horizon
    assert all(left < right for left, right in pairwise(times))
    assert math.isclose(values[-1], rate * horizon, rel_tol=1e-14, abs_tol=0.0)


@pytest.mark.parametrize("horizon,steps,rate", [
    (0.7, 3, 2.0),
    (2 * math.ulp(0.0), 2, 1e308),
])
def test_admitted_paired_constant_rates_preserve_elapsed_time(
    horizon: float, steps: int, rate: float,
) -> None:
    times, first, second = euler_integrate_pair(
        (0.0, 0.0), horizon, steps, lambda _first, _second: (rate, -rate),
        clip_nonnegative=False,
    )
    assert all(left < right for left, right in pairwise(times))
    assert math.isclose(first[-1], rate * horizon, rel_tol=1e-14, abs_tol=0.0)
    assert math.isclose(second[-1], -rate * horizon, rel_tol=1e-14, abs_tol=0.0)
