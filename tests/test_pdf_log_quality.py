"""Tests for project PDF-log quality gates."""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path


PROJECT = Path(__file__).resolve().parent.parent
CHECKER = PROJECT / "scripts" / "check_pdf_log.py"


def _load_checker():
    spec = importlib.util.spec_from_file_location("check_pdf_log_for_test", CHECKER)
    assert spec is not None
    assert spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def test_pdf_log_checker_flags_undefined_references_and_severe_overfull_boxes() -> None:
    checker = _load_checker()
    issues = checker.find_pdf_log_issues(
        "\n".join(
            [
                "LaTeX Warning: Hyper reference `gl:fatty-acid' on page 117 undefined",
                "Missing character: There is no ★ (U+2605) in font [lmroman10-regular]:mapping=tex-text;!",
                "! Double superscript.",
                "Overfull \\hbox (12.0pt too wide) in paragraph at lines 1--2",
                "Overfull \\vbox (143.18613pt too high) has occurred while \\output is active",
            ]
        ),
        max_overfull_pt=50,
    )

    assert len(issues) == 4
    assert "undefined" in issues[0].message
    assert "Missing character" in issues[1].message
    assert "Double superscript" in issues[2].message
    assert "143.18613pt" in issues[3].message


def test_pdf_log_checker_allows_minor_overfull_boxes() -> None:
    checker = _load_checker()
    assert checker.find_pdf_log_issues(
        "Overfull \\hbox (6.5pt too wide) in paragraph at lines 1--2",
        max_overfull_pt=50,
    ) == []
