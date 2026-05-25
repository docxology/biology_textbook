"""Tests for shared numerical integration helpers."""

from __future__ import annotations

import pytest

from biology.ecology.ecology import lotka_volterra, logistic_growth
from biology.numerics import euler_integrate_pair, euler_integrate_scalar


def test_euler_integrate_scalar_logistic_matches_ecology_helper() -> None:
    direct_times, direct_values = euler_integrate_scalar(
        10.0,
        5.0,
        100,
        lambda n: 0.5 * n * (1.0 - n / 100.0),
    )
    result = logistic_growth(N0=10.0, r=0.5, K=100.0, t_end=5.0, steps=100)
    assert direct_times == result.times
    assert direct_values == result.populations


def test_euler_integrate_scalar_rejects_nonpositive_horizon() -> None:
    with pytest.raises(ValueError, match="t_end"):
        euler_integrate_scalar(1.0, 0.0, 10, lambda y: y)


def test_euler_integrate_pair_lotka_volterra_matches_ecology_helper() -> None:
    times, prey, predators = euler_integrate_pair(
        (40.0, 9.0),
        10.0,
        200,
        lambda n, p: (0.1 * n - 0.02 * n * p, 0.01 * n * p - 0.1 * p),
    )
    result = lotka_volterra(
        prey0=40.0,
        predator0=9.0,
        alpha=0.1,
        beta=0.02,
        delta=0.01,
        gamma=0.1,
        t_end=10.0,
        steps=200,
    )
    assert times == result.times
    assert prey == result.prey
    assert predators == result.predator


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
