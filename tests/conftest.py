"""Pytest configuration for biology_textbook tests."""

from __future__ import annotations

import os
from pathlib import Path
import sys

# Force headless backend for matplotlib in tests — MUST be before any import of matplotlib
os.environ.setdefault("MPLBACKEND", "Agg")

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "src"
# coverage.py reads this when pytest-cov starts (before conftest hooks on some pytest versions).
os.environ.setdefault("COVERAGE_RCFILE", str(ROOT / "pyproject.toml"))
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from textbook_paths import ensure_project_paths  # noqa: E402

ensure_project_paths(include_scripts=True)


def pytest_load_initial_conftests(early_config, parser, args) -> None:
    """Point pytest-cov at this project's pyproject.toml when invoked from template root."""
    if early_config.known_args_namespace.cov_source:
        early_config.known_args_namespace.cov_config = str(ROOT / "pyproject.toml")
