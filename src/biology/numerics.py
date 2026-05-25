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


__all__ = ["euler_integrate_scalar"]
