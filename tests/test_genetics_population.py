"""Tests for ``biology.genetics.population``."""

import pytest

from biology.genetics import chi_squared_test, hardy_weinberg


class TestHardyWeinberg:
    def test_hw_from_p_q(self):
        result = hardy_weinberg(p=0.6, q=0.4)
        assert abs(result.p_squared - 0.36) < 1e-9
        assert abs(result.two_pq - 0.48) < 1e-9
        assert abs(result.q_squared - 0.16) < 1e-9
        assert result.is_valid

    def test_hw_from_recessive_freq(self):
        result = hardy_weinberg(recessive_homozygous_freq=0.09)
        assert abs(result.q - 0.3) < 1e-9
        assert abs(result.p - 0.7) < 1e-9

    def test_hw_genotype_freqs_sum_to_one(self):
        result = hardy_weinberg(p=0.3, q=0.7)
        total = result.p_squared + result.two_pq + result.q_squared
        assert abs(total - 1.0) < 1e-9

    def test_hw_invalid_p_raises(self):
        with pytest.raises(ValueError):
            hardy_weinberg(p=1.5, q=0.7)

    def test_hw_no_args_raises(self):
        with pytest.raises(ValueError):
            hardy_weinberg()


class TestChiSquared:
    def test_3_to_1_expected(self):
        observed = [75.0, 25.0]
        expected = [75.0, 25.0]
        result = chi_squared_test(observed, expected)
        assert result.chi_squared == pytest.approx(0.0, abs=1e-9)
        assert not result.reject_null

    def test_chi2_deviation_detected(self):
        observed = [90.0, 10.0]
        expected = [75.0, 25.0]
        result = chi_squared_test(observed, expected)
        assert result.chi_squared > 5.0

    def test_df1_p_value_matches_critical_threshold(self):
        result = chi_squared_test([113.86, 86.14], [100.0, 100.0])
        assert result.chi_squared == pytest.approx(3.841, rel=1e-3)
        assert result.p_value_approx == pytest.approx(0.05, rel=1e-2)
        strong = chi_squared_test([138.591, 61.409], [100.0, 100.0])
        assert strong.chi_squared == pytest.approx(29.7853, rel=1e-4)
        assert strong.p_value_approx < 0.001

    def test_chi2_length_mismatch_raises(self):
        with pytest.raises(ValueError, match="equal length"):
            chi_squared_test([10, 20], [10, 20, 30])

    def test_chi2_zero_expected_raises(self):
        with pytest.raises(ValueError, match="positive"):
            chi_squared_test([10.0, 0.0], [10.0, 0.0])
