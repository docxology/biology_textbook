"""Active-inference primitives for the Unit 0 chapter.

Provides the Bayesian update used in active-inference pedagogy: a Gaussian
posterior mean shifts toward the observation by an amount proportional to the
likelihood precision (sensory precision) and inversely proportional to the
total posterior precision. The matching prediction error is the observation
minus the prior. We tabulate both as functions of sensory precision so the
chapter figure can show the trade-off explicitly.

The model is fully deterministic; randomness is not used.
"""

from __future__ import annotations

from dataclasses import dataclass

from textbook_logging import get_logger

logger = get_logger(__name__)


@dataclass(frozen=True)
class PredictionPrecisionPoint:
    """One (precision, error, posterior) row in the trade-off table."""

    sensory_precision: float
    prediction_error: float
    posterior_mean: float
    posterior_precision: float


@dataclass(frozen=True)
class ActiveInferenceProfile:
    """Precision sweep used by the Unit 0 active-inference figure."""

    prior_mean: float
    prior_precision: float
    observation: float
    points: tuple[PredictionPrecisionPoint, ...]


def _posterior(
    prior_mean: float,
    prior_precision: float,
    observation: float,
    sensory_precision: float,
) -> tuple[float, float]:
    """Return the Gaussian posterior mean and precision.

    Closed-form precision-weighted combination:
        mu_post = (pi_p * mu_p + pi_s * y) / (pi_p + pi_s)
        pi_post = pi_p + pi_s
    """
    posterior_precision = prior_precision + sensory_precision
    posterior_mean = (
        prior_precision * prior_mean + sensory_precision * observation
    ) / posterior_precision
    return posterior_mean, posterior_precision


def prediction_error_precision_curve(
    prior_mean: float = 0.0,
    prior_precision: float = 1.0,
    observation: float = 1.0,
    precisions: tuple[float, ...] = (0.0625, 0.125, 0.25, 0.5, 1.0, 2.0, 4.0, 8.0, 16.0),
) -> ActiveInferenceProfile:
    """Tabulate the precision sweep used by the prediction-error figure.

    At low sensory precision the posterior stays near the prior (small update);
    at high precision the posterior collapses onto the observation (the
    prediction error drives the update). Both regimes are plotted on the same
    figure so students can see the trade-off explicitly.

    Args:
        prior_mean: Prior expectation ``mu_p``.
        prior_precision: Prior precision ``pi_p`` (must be positive).
        observation: Sensory observation ``y``.
        precisions: Strictly positive sensory precisions to sweep.

    Returns:
        ActiveInferenceProfile with the same length as ``precisions``.

    Raises:
        ValueError: If ``prior_precision`` is non-positive or any sensory
            precision is non-positive.
    """
    if prior_precision <= 0:
        raise ValueError("prior_precision must be positive.")
    if not precisions:
        raise ValueError("precisions must be non-empty.")
    if any(p <= 0 for p in precisions):
        raise ValueError("each sensory precision must be positive.")

    error = observation - prior_mean
    rows: list[PredictionPrecisionPoint] = []
    for sensory_precision in precisions:
        mu_post, pi_post = _posterior(
            prior_mean, prior_precision, observation, sensory_precision
        )
        rows.append(
            PredictionPrecisionPoint(
                sensory_precision=sensory_precision,
                prediction_error=error,
                posterior_mean=mu_post,
                posterior_precision=pi_post,
            )
        )
    logger.debug(
        "Active-inference sweep: prior_mu=%.2f, obs=%.2f, n=%d points",
        prior_mean,
        observation,
        len(rows),
    )
    return ActiveInferenceProfile(
        prior_mean=prior_mean,
        prior_precision=prior_precision,
        observation=observation,
        points=tuple(rows),
    )


def active_inference_profile(
    prior_mean: float = 0.0,
    prior_precision: float = 1.0,
    observation: float = 1.0,
) -> ActiveInferenceProfile:
    """Return the default precision sweep used by the textbook figure."""
    return prediction_error_precision_curve(
        prior_mean=prior_mean,
        prior_precision=prior_precision,
        observation=observation,
    )
