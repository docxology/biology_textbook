"""Standalone-safe logging helpers for the biology textbook project."""

from __future__ import annotations

import logging


def get_logger(name: str) -> logging.Logger:
    """Return the template logger when available, otherwise stdlib logging."""
    try:
        from infrastructure.core.logging.utils import get_logger as template_get_logger  # type: ignore[import-not-found]
    except ModuleNotFoundError:
        return logging.getLogger(name)
    return template_get_logger(name)
