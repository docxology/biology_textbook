"""American English spelling gate for manuscript and docs."""

from __future__ import annotations

import re
from pathlib import Path

from biology.maintenance.american_english import (
    MANUSCRIPT,
    find_british_spellings,
    iter_target_files,
    normalize_text,
)
from biology.maintenance.models import PROJECT


def test_manuscript_and_docs_use_american_english() -> None:
    failures: list[str] = []
    for path in iter_target_files(PROJECT):
        text = path.read_text(encoding="utf-8")
        for line_no, token, excerpt in find_british_spellings(text):
            rel = path.relative_to(PROJECT)
            failures.append(f"{rel}:{line_no}: {token!r} in {excerpt[:120]}")
    assert not failures, "British spellings found:\n" + "\n".join(failures[:40])


def test_american_english_normalization_is_idempotent() -> None:
    sample = "\n".join(
        [
            "## Signalling and behaviour",
            "",
            "Germinal centres organise tumour defence and colour vision.",
            "",
            "```python",
            "colour = '#0072B2'  # keep code unchanged",
            "```",
        ]
    )
    once, count = normalize_text(sample)
    twice, _ = normalize_text(once)
    assert count >= 5
    assert once == twice
    assert "Signaling and behavior" in once
    assert "colour = '#0072B2'" in once


def test_claims_ledger_anchor_paths_exist() -> None:
    claims = MANUSCRIPT / "current_claims.yaml"
    assert claims.exists()


def test_visualization_guide_uses_american_filename() -> None:
    guide = PROJECT / "docs" / "visualization_guide.md"
    legacy = PROJECT / "docs" / "visualisation_guide.md"
    assert guide.is_file()
    assert not legacy.exists()


def test_bloom_html_comments_use_american_analyze() -> None:
    pattern = re.compile(r"<!--\s*bloom:\s*analyse\s*-->", re.IGNORECASE)
    offenders: list[str] = []
    for path in iter_target_files(PROJECT):
        for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
            if pattern.search(line):
                rel = path.relative_to(PROJECT)
                offenders.append(f"{rel}:{line_no}")
    assert not offenders, "Use <!-- bloom: analyze --> (American spelling):\n" + "\n".join(offenders)
