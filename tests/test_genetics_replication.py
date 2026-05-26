"""Tests for ``biology.genetics.replication``."""

import pytest

from biology.genetics import replication_fork_progression


class TestReplicationForkProgression:
    def test_replication_fork_progression_monotonic(self):
        profile = replication_fork_progression(
            velocity_bp_per_s=1000.0, duration_s=600.0, origins=1, steps=60
        )
        bases = profile.bases_replicated
        assert all(b_next >= b_prev for b_prev, b_next in zip(bases, bases[1:]))

    def test_parallel_origins_scale_linearly(self):
        single = replication_fork_progression(
            velocity_bp_per_s=1000.0, duration_s=600.0, origins=1, steps=30
        )
        many = replication_fork_progression(
            velocity_bp_per_s=1000.0, duration_s=600.0, origins=10, steps=30
        )
        assert many.bases_replicated[-1] == pytest.approx(
            single.bases_replicated[-1] * 10, rel=1e-6
        )
