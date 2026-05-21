"""Pytest configuration for biology_textbook tests."""

import os
import sys

# Force headless backend for matplotlib in tests — MUST be before any import of matplotlib
os.environ.setdefault("MPLBACKEND", "Agg")

# Add src/ to path so project modules can be imported without package install
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SRC = os.path.join(ROOT, "src")
TEMPLATE_ROOT = os.path.abspath(os.path.join(ROOT, "..", ".."))
if SRC not in sys.path:
    sys.path.insert(0, SRC)
if TEMPLATE_ROOT not in sys.path:
    sys.path.insert(0, TEMPLATE_ROOT)
