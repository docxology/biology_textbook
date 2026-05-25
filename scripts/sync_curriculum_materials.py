#!/usr/bin/env python3
"""Synchronize curriculum scaffolds — thin CLI."""

from __future__ import annotations

from _bootstrap import ensure_project_paths

ensure_project_paths()

from biology.curriculum_sync import engine
from biology.curriculum_sync.cli import main

CHAPTER_MARKER = engine.CHAPTER_MARKER
LAB_MARKER = engine.LAB_MARKER
QUESTION_MARKER = engine.QUESTION_MARKER
NAV_MARKER = engine.NAV_MARKER
READING_PATHS_MARKER = engine.READING_PATHS_MARKER
CONCEPT_MAP_MARKER = engine.CONCEPT_MAP_MARKER
PREFACE_SCOPE_MARKER = engine.PREFACE_SCOPE_MARKER
build_front_matter_navigation = engine.build_front_matter_navigation
build_suggested_reading_paths = engine.build_suggested_reading_paths
build_textbook_concept_map = engine.build_textbook_concept_map
build_preface_scope_table = engine.build_preface_scope_table

__all__ = [
    "CHAPTER_MARKER",
    "CONCEPT_MAP_MARKER",
    "LAB_MARKER",
    "NAV_MARKER",
    "PREFACE_SCOPE_MARKER",
    "QUESTION_MARKER",
    "READING_PATHS_MARKER",
    "build_front_matter_navigation",
    "build_preface_scope_table",
    "build_suggested_reading_paths",
    "build_textbook_concept_map",
    "main",
]

if __name__ == "__main__":
    raise SystemExit(main())
