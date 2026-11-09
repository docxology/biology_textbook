"""Shared numerical integration helpers for teaching simulations."""

from __future__ import annotations

import math
import sys
from collections.abc import Callable


def _euler_time_step(t_end: float, steps: int) -> float:
    """Admit one uniform binary64 grid without changing its requested horizon."""
    if not math.isfinite(t_end) or t_end <= 0:
        raise ValueError("t_end must be finite and positive.")
    if isinstance(steps, bool) or not isinstance(steps, int):
        raise TypeError("steps must be a positive integer.")
    if steps <= 0:
        raise ValueError("steps must be a positive integer.")
    if steps > t_end / math.ulp(t_end):
        raise ValueError("Euler time grid is not representable; reduce steps or increase t_end.")
    dt = t_end / steps
    if (steps - 1) * dt >= t_end or (dt < sys.float_info.min and dt * steps != t_end):
        raise ValueError("Rounded Euler steps do not represent the requested time grid.")
    return dt


def euler_integrate_scalar(
    y0: float,
    t_end: float,
    steps: int,
    derivative: Callable[[float], float],
    *,
    clip_nonnegative: bool = True,
) -> tuple[list[float], list[float]]:
    """Euler integration for a scalar ODE dy/dt = derivative(y).

    Args:
        y0: Initial value.
        t_end: Integration horizon (must be positive).
        steps: Number of Euler steps (must be positive).
        derivative: Rate function evaluated at the current state.
        clip_nonnegative: When true, clamp each step to y >= 0.

    Returns:
        ``(times, values)`` with length ``steps + 1``.

    Raises:
        TypeError: If steps is not an integer (excluding bool).
        ValueError: For invalid domains, nonfinite rates/updates or unrepresentable time steps.
    """
    if not math.isfinite(y0):
        raise ValueError("y0 must be finite.")
    dt = _euler_time_step(t_end, steps)
    times = [0.0]
    values = [y0]
    y = y0
    for step in range(1, steps + 1):
        rate = derivative(y)
        if not math.isfinite(rate):
            raise ValueError("Euler derivative must be finite.")
        y = y + rate * dt
        if not math.isfinite(y):
            raise ValueError("Euler update must be finite.")
        if clip_nonnegative:
            y = max(0.0, y)
        times.append(t_end if step == steps else step * dt)
        values.append(y)
    return times, values


def euler_integrate_pair(
    y0: tuple[float, float],
    t_end: float,
    steps: int,
    derivatives: Callable[[float, float], tuple[float, float]],
    *,
    clip_nonnegative: bool = True,
) -> tuple[list[float], list[float], list[float]]:
    """Euler integration for a two-component ODE system.

    Args:
        y0: Initial ``(y1, y2)`` values.
        t_end: Integration horizon (must be positive).
        steps: Number of Euler steps (must be positive).
        derivatives: Rate function ``(y1, y2) -> (dy1/dt, dy2/dt)``.
        clip_nonnegative: When true, clamp each component to ``>= 0``.

    Returns:
        ``(times, series1, series2)`` each with length ``steps + 1``.

    Raises:
        TypeError: If steps is not an integer (excluding bool).
        ValueError: For invalid domains, nonfinite rates/updates or unrepresentable time steps.
    """
    if not all(math.isfinite(value) for value in y0):
        raise ValueError("y0 components must be finite.")
    dt = _euler_time_step(t_end, steps)
    times = [0.0]
    series1 = [y0[0]]
    series2 = [y0[1]]
    y1, y2 = y0
    for step in range(1, steps + 1):
        d1, d2 = derivatives(y1, y2)
        if not math.isfinite(d1) or not math.isfinite(d2):
            raise ValueError("Euler derivatives must be finite.")
        y1 = y1 + d1 * dt
        y2 = y2 + d2 * dt
        if not math.isfinite(y1) or not math.isfinite(y2):
            raise ValueError("Euler updates must be finite.")
        if clip_nonnegative:
            y1 = max(0.0, y1)
            y2 = max(0.0, y2)
        times.append(t_end if step == steps else step * dt)
        series1.append(y1)
        series2.append(y2)
    return times, series1, series2


__all__ = ["euler_integrate_pair", "euler_integrate_scalar"]
