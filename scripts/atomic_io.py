#!/usr/bin/env python3
"""Atomic file writes — thin wrapper."""

from __future__ import annotations

from _bootstrap import ensure_project_paths

ensure_project_paths()

from textbook_io import write_text_atomic

__all__ = ["write_text_atomic"]
