"""Tests for ``biology.genetics.replication``."""

import pytest

from biology.genetics import ReplicationForkProfile, replication_fork_progression


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

    def test_times_grid_and_sampling(self):
        profile = replication_fork_progression(
            velocity_bp_per_s=500.0, duration_s=1000.0, origins=1, steps=20
        )
        assert isinstance(profile, ReplicationForkProfile)
        assert len(profile.times_s) == 21
        assert len(profile.bases_replicated) == 21
        assert profile.times_s[0] == pytest.approx(0.0)
        assert profile.times_s[-1] == pytest.approx(1000.0)
        dt = 1000.0 / 20
        assert profile.times_s[7] == pytest.approx(7 * dt)
        # Uniform grid: consecutive spacing is constant.
        gaps = {
            round(b - a, 9) for a, b in zip(profile.times_s, profile.times_s[1:])
        }
        assert len(gaps) == 1

    def test_biphasic_replication_at_origin_matches_analytic_value(self):
        velocity = 50.0
        origins = 2
        duration = 120.0
        profile = replication_fork_progression(
            velocity_bp_per_s=velocity, duration_s=duration, origins=origins, steps=60
        )
        # Bidirectional forks: 2 * origins * v * t (constant velocity model).
        expected_final = 2 * origins * velocity * duration
        assert profile.bases_replicated[-1] == pytest.approx(expected_final)
        assert profile.bases_replicated[-1] == pytest.approx(
            profile.bases_replicated[len(profile.bases_replicated) // 2] * 2, rel=1e-9
        )
        assert profile.velocity_bp_per_s == pytest.approx(velocity)
        assert profile.origins == origins

    def test_defaults_are_documented_values(self):
        profile = replication_fork_progression()
        assert profile.velocity_bp_per_s == pytest.approx(1000.0)
        assert profile.origins == 1
        assert len(profile.times_s) == 61  # steps=60 default

    @pytest.mark.parametrize(
        "kwargs, match",
        [
            ({"velocity_bp_per_s": 0.0}, "velocity_bp_per_s must be positive"),
            ({"velocity_bp_per_s": -10.0}, "velocity_bp_per_s must be positive"),
            ({"duration_s": 0.0}, "duration_s must be positive"),
            ({"duration_s": -1.0}, "duration_s must be positive"),
            ({"origins": 0}, "origins must be positive"),
            ({"origins": -3}, "origins must be positive"),
            ({"steps": 0}, "steps must be positive"),
            ({"steps": -5}, "steps must be positive"),
        ],
    )
    def test_invalid_parameters_raise_value_error(self, kwargs, match):
        with pytest.raises(ValueError, match=match):
            replication_fork_progression(**kwargs)

    def test_half_replication_time_scaling(self):
        # Doubling velocity halves the time to replicate a fixed genome length:
        # a classic quantitative claim from the manuscript chapter.
        slow = replication_fork_progression(
            velocity_bp_per_s=500.0, duration_s=1000.0, origins=1, steps=50
        )
        fast = replication_fork_progression(
            velocity_bp_per_s=1000.0, duration_s=1000.0, origins=1, steps=50
        )
        genome = 1_000_000.0
        t_slow = genome / (2 * 500.0)
        t_fast = genome / (2 * 1000.0)
        assert t_fast == pytest.approx(t_slow / 2)
        # Both profiles are linear, so the base count at the half-time scales.
        idx_slow = int(round(t_slow / slow.times_s[-1] * (len(slow.times_s) - 1)))
        idx_fast = int(round(t_fast / fast.times_s[-1] * (len(fast.times_s) - 1)))
        assert slow.bases_replicated[idx_slow] > genome - 2 * 500.0 * 20
        assert fast.bases_replicated[idx_fast] > genome - 2 * 1000.0 * 20
