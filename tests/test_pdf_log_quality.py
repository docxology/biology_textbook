"""Tests for project PDF-log quality gates."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import pytest

from biology.quality.pdf_log import find_pdf_log_issues
from textbook_paths import PROJECT


def test_pdf_log_checker_flags_undefined_references_and_severe_overfull_boxes() -> None:
    issues = find_pdf_log_issues(
        "LaTeX Warning: Hyper reference `gl:fatty-acid' on page 117 undefined\n"
        "Missing character: There is no ★ (U+2605) in font [lmroman10-regular]:mapping=tex-text;!\n"
        "! Double superscript.\n"
        "Overfull \\hbox (12.0pt too wide) in paragraph at lines 1--2\n"
        "Overfull \\vbox (143.18613pt too high) has occurred while \\output is active",
        max_overfull_pt=50,
    )

    assert len(issues) == 4
    assert "undefined" in issues[0].message
    assert "Missing character" in issues[1].message
    assert "Double superscript" in issues[2].message
    assert "143.18613pt" in issues[3].message


def test_pdf_log_checker_allows_minor_overfull_boxes() -> None:
    assert find_pdf_log_issues(
        "Overfull \\hbox (6.5pt too wide) in paragraph at lines 1--2",
        max_overfull_pt=50,
    ) == []


def test_pdf_log_checker_can_allow_missing_glyphs() -> None:
    issues = find_pdf_log_issues(
        "Missing character: There is no ★ (U+2605) in font!",
        allow_missing_glyphs=True,
    )
    assert issues == []


def test_run_pdf_log_check_returns_zero_on_clean_log(tmp_path) -> None:
    from biology.quality.pdf_log import run_pdf_log_check

    log_path = tmp_path / "clean.log"
    log_path.write_text("No issues here.\n", encoding="utf-8")
    assert run_pdf_log_check(log_path) == 0


def test_run_pdf_log_check_missing_log_returns_two(tmp_path) -> None:
    from biology.quality.pdf_log import run_pdf_log_check

    assert run_pdf_log_check(tmp_path / "missing.log") == 2


def test_run_pdf_log_check_returns_one_when_issues_present(tmp_path) -> None:
    from biology.quality.pdf_log import run_pdf_log_check

    log_path = tmp_path / "bad.log"
    log_path.write_text("LaTeX Warning: Reference `fig:missing' on page 1 undefined\n", encoding="utf-8")
    assert run_pdf_log_check(log_path) == 1


@pytest.mark.parametrize("interface", ["library", "cli"])
@pytest.mark.parametrize("vertical_limit,points,expected", [
    (None, 20.0, 0),
    (None, 20.01, 1),
    (None, 100.0, 1),
    (30.0, 20.01, 0),
    (30.0, 30.01, 1),
])
def test_pdf_checker_applies_one_budget_unless_vertical_is_explicit(
    tmp_path: Path, interface: str, vertical_limit: float | None,
    points: float, expected: int,
) -> None:
    from biology.quality.pdf_log import run_pdf_log_check

    log = tmp_path / "overflow.log"
    log.write_text(f"Overfull \\vbox ({points}pt too high) has occurred while \\output is active\n")
    if interface == "library":
        actual = (run_pdf_log_check(log, max_overfull_pt=20)
                  if vertical_limit is None else run_pdf_log_check(
                      log, max_overfull_pt=20, max_overfull_vbox_pt=vertical_limit))
    else:
        args = [sys.executable, str(PROJECT / "scripts/check_pdf_log.py"), str(log),
                "--max-overfull-pt", "20"]
        if vertical_limit is not None:
            args.extend(["--max-overfull-vbox-pt", str(vertical_limit)])
        actual = subprocess.run(args, cwd=PROJECT, capture_output=True, text=True,
                                stdin=subprocess.DEVNULL, check=False).returncode
    assert actual == expected
