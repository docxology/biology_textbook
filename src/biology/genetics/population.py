"""Population genetics: Hardy-Weinberg and chi-squared goodness-of-fit."""

from __future__ import annotations

import math
from dataclasses import dataclass

from textbook_logging import get_logger

logger = get_logger(__name__)


@dataclass
class HardyWeinbergResult:
    """Hardy-Weinberg equilibrium calculations."""

    p: float
    q: float
    p_squared: float
    two_pq: float
    q_squared: float
    is_valid: bool


@dataclass
class ChiSquaredResult:
    """Chi-squared goodness-of-fit test result."""

    chi_squared: float
    degrees_of_freedom: int
    p_value_approx: float
    observed: list[float]
    expected: list[float]
    reject_null: bool


def hardy_weinberg(
    p: float | None = None,
    q: float | None = None,
    dominant_homozygous_freq: float | None = None,
    recessive_homozygous_freq: float | None = None,
) -> HardyWeinbergResult:
    """Compute Hardy-Weinberg equilibrium frequencies."""
    if p is not None and q is not None:
        pass
    elif recessive_homozygous_freq is not None:
        q = math.sqrt(recessive_homozygous_freq)
        p = 1.0 - q
    elif dominant_homozygous_freq is not None:
        p = math.sqrt(dominant_homozygous_freq)
        q = 1.0 - p
    else:
        raise ValueError("Provide (p, q) or at least one homozygous frequency.")

    if not (0.0 <= p <= 1.0 and 0.0 <= q <= 1.0):
        raise ValueError(f"p={p} and q={q} must be in [0, 1].")

    is_valid = abs(p + q - 1.0) < 1e-9
    result = HardyWeinbergResult(
        p=p,
        q=q,
        p_squared=p**2,
        two_pq=2 * p * q,
        q_squared=q**2,
        is_valid=is_valid,
    )
    logger.debug(
        "HW: p=%.4f, q=%.4f, AA=%.4f, Aa=%.4f, aa=%.4f",
        p,
        q,
        result.p_squared,
        result.two_pq,
        result.q_squared,
    )
    return result


def chi_squared_test(
    observed: list[float],
    expected: list[float],
    alpha: float = 0.05,
    *,
    ddof: int = 0,
) -> ChiSquaredResult:
    """Pearson goodness-of-fit test with equal observed/expected totals.

    ``ddof`` counts parameters fitted from these observations: use 1 for a
    biallelic HWE test with estimated allele frequency, 0 for fixed Mendelian
    ratios. The asymptotic reference distribution requires adequate expected
    counts; this function does not make a small-sample exact test.
    """
    if len(observed) != len(expected):
        raise ValueError("observed and expected must have equal length.")
    if len(observed) < 2:
        raise ValueError("Need at least 2 categories.")
    if any(not math.isfinite(o) or o < 0 for o in observed):
        raise ValueError("Observed values must be finite and non-negative.")
    if any(not math.isfinite(e) or e <= 0 for e in expected):
        raise ValueError("All expected values must be finite and positive.")
    if not math.isfinite(alpha) or not 0 < alpha < 1:
        raise ValueError("alpha must be finite and in (0, 1).")
    if isinstance(ddof, bool) or not isinstance(ddof, int):
        raise TypeError("ddof must be a non-negative integer leaving positive degrees of freedom.")
    if not 0 <= ddof < len(observed) - 1:
        raise ValueError("ddof must be a non-negative integer leaving positive degrees of freedom.")
    # Scale before summing so even large finite counts have comparable totals.
    scale = max(max(observed), max(expected))
    if not math.isclose(math.fsum(o / scale for o in observed),
                        math.fsum(e / scale for e in expected), rel_tol=1e-12, abs_tol=0.0):
        raise ValueError("observed and expected must have equal totals.")

    chi2 = 0.0
    for o, e in zip(observed, expected):
        standardized = (o - e) / math.sqrt(e)
        chi2 += standardized * standardized
    df = len(observed) - 1 - ddof

    from scipy.stats import chi2 as chi2_dist

    p_value = float(chi2_dist.sf(chi2, df))

    reject_null = p_value < alpha

    logger.debug("Chi-squared=%.4f, df=%d, p≈%.4f, reject=%s", chi2, df, p_value, reject_null)
    return ChiSquaredResult(
        chi_squared=chi2,
        degrees_of_freedom=df,
        p_value_approx=p_value,
        observed=list(observed),
        expected=list(expected),
        reject_null=reject_null,
    )
