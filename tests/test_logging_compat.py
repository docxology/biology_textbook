"""Tests for standalone-safe project logging."""

from __future__ import annotations

import logging


def test_project_logger_falls_back_to_stdlib_logger() -> None:
    from textbook_logging import get_logger

    logger = get_logger("biology_textbook.test")

    assert isinstance(logger, logging.Logger)
    assert logger.name == "biology_textbook.test"


def test_project_logger_uses_stdlib_when_template_missing(monkeypatch) -> None:
    import builtins

    real_import = builtins.__import__

    def blocked_import(name, *args, **kwargs):
        if name == "infrastructure.core.logging.utils":
            raise ModuleNotFoundError(name)
        return real_import(name, *args, **kwargs)

    monkeypatch.setattr(builtins, "__import__", blocked_import)
    import textbook_logging

    importlib = __import__("importlib")
    importlib.reload(textbook_logging)
    logger = textbook_logging.get_logger("biology_textbook.fallback")
    assert isinstance(logger, logging.Logger)
    assert logger.name == "biology_textbook.fallback"
