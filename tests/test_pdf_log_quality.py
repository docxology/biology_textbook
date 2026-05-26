"""Tests for project PDF-log quality gates."""

from __future__ import annotations

from biology.quality.pdf_log import find_pdf_log_issues


def test_pdf_log_checker_flags_undefined_references_and_severe_overfull_boxes() -> None:
    issues = find_pdf_log_issues(
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
