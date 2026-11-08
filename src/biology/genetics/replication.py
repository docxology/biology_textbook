"""Replication fork progression model."""

from __future__ import annotations

import math
from dataclasses import dataclass

from textbook_logging import get_logger

logger = get_logger(__name__)


@dataclass(frozen=True)
class ReplicationForkProfile:
    """Time-series for two diverging forks per simultaneously active origin."""

    times_s: tuple[float, ...]
    bases_replicated: tuple[float, ...]
    velocity_bp_per_s: float
    origins: int


def replication_fork_progression(
    *,
    velocity_bp_per_s: float = 1000.0,
    duration_s: float = 1800.0,
    origins: int = 1,
    steps: int = 60,
) -> ReplicationForkProfile:
    """Two forks/origin, no collisions/cap; require a representable duration/steps."""
    if not math.isfinite(velocity_bp_per_s) or velocity_bp_per_s <= 0:
        raise ValueError("velocity_bp_per_s must be finite and positive.")
    if not math.isfinite(duration_s) or duration_s <= 0:
        raise ValueError("duration_s must be finite and positive.")
    if isinstance(origins, bool) or not isinstance(origins, int):
        raise TypeError("origins must be a positive integer.")
    if origins <= 0:
        raise ValueError("origins must be a positive integer.")
    if isinstance(steps, bool) or not isinstance(steps, int):
        raise TypeError("steps must be a positive integer.")
    if steps <= 0:
        raise ValueError("steps must be a positive integer.")

    if steps > duration_s / math.ulp(duration_s):
        raise ValueError("Sampling time step is not representable; reduce steps.")
    times = tuple(duration_s if i == steps else (i / steps) * duration_s for i in range(steps + 1))
    bases = tuple(2.0 * origins * velocity_bp_per_s * t for t in times)
    if not all(math.isfinite(value) for value in bases):
        raise ValueError("Replicated base count exceeds the finite model range.")
    logger.debug(
        "Replication fork: v=%.1f bp/s, origins=%d, total bases at %.0fs = %.2e",
        velocity_bp_per_s,
        origins,
        duration_s,
        bases[-1],
    )
    return ReplicationForkProfile(
        times_s=times,
        bases_replicated=bases,
        velocity_bp_per_s=velocity_bp_per_s,
        origins=origins,
    )
