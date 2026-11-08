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
