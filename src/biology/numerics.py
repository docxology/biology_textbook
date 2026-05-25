"""Shared numerical integration helpers for teaching simulations."""

from __future__ import annotations

from collections.abc import Callable


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
        ValueError: If ``t_end`` or ``steps`` is not positive.
    """
    if t_end <= 0:
        raise ValueError("t_end must be positive.")
    if steps <= 0:
        raise ValueError("steps must be positive.")

    dt = t_end / steps
    times = [0.0]
    values = [y0]
    y = y0
    for _ in range(steps):
        y = y + derivative(y) * dt
        if clip_nonnegative:
            y = max(0.0, y)
        times.append(times[-1] + dt)
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
        ValueError: If ``t_end`` or ``steps`` is not positive.
    """
    if t_end <= 0:
        raise ValueError("t_end must be positive.")
    if steps <= 0:
        raise ValueError("steps must be positive.")

    dt = t_end / steps
    times = [0.0]
    series1 = [y0[0]]
    series2 = [y0[1]]
    y1, y2 = y0
    for _ in range(steps):
        d1, d2 = derivatives(y1, y2)
        y1 = y1 + d1 * dt
        y2 = y2 + d2 * dt
        if clip_nonnegative:
            y1 = max(0.0, y1)
            y2 = max(0.0, y2)
        times.append(times[-1] + dt)
        series1.append(y1)
        series2.append(y2)
    return times, series1, series2


__all__ = ["euler_integrate_scalar", "euler_integrate_pair"]
