"""Replication fork progression model."""

from __future__ import annotations

from dataclasses import dataclass

from textbook_logging import get_logger


logger = get_logger(__name__)


@dataclass(frozen=True)
class ReplicationForkProfile:
    """Time-series of replication progress for a single fork."""

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
    """Compute bases replicated over time at constant fork velocity."""
    if velocity_bp_per_s <= 0:
        raise ValueError("velocity_bp_per_s must be positive.")
    if duration_s <= 0:
        raise ValueError("duration_s must be positive.")
    if origins <= 0:
        raise ValueError("origins must be positive.")
    if steps <= 0:
        raise ValueError("steps must be positive.")

    dt = duration_s / steps
    times = tuple(i * dt for i in range(steps + 1))
    bases = tuple(2.0 * origins * velocity_bp_per_s * t for t in times)
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
