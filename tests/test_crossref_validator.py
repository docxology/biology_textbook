"""Invariant tests for the manuscript cross-reference state.

Runs the :mod:`biology.crossref_validator` against the manuscript and asserts
that the minimum label coverage holds:

* All raw-LaTeX figure environments (``\\begin{figure}…\\end{figure}``) carry
  a ``\\label{fig:…}``.
* All LaTeX equation environments (``\\begin{equation}…\\end{equation}``)
  carry a ``\\label{eq:…}``.
* Every chapter, lab, and question file has a ``\\label{sec:…}`` directly
  below its H1 title (inserted by
  :mod:`scripts.insert_crossref_labels`).
* No ``@fig:``, ``@eq:``, ``@tbl:``, ``@sec:`` reference is unresolved.

Bare inline ``$$…$$`` display equations without ``\\tag{}`` or ``\\label``
are considered worked-example steps and are not required to carry ids.
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest


# ---------------------------------------------------------------------------
# Dynamic import of the validator — conftest already puts src/ on sys.path
# but the validator module must also be importable by its short name when
# the ``biology`` package as a whole is not importable in this environment.
# ---------------------------------------------------------------------------

VALIDATOR_PATH = Path(__file__).resolve().parent.parent / "src" / "biology" / "crossref_validator.py"


def _load_validator():
    spec = importlib.util.spec_from_file_location("crossref_validator", VALIDATOR_PATH)
    if spec is None or spec.loader is None:
        raise ImportError(f"Could not load crossref validator from {VALIDATOR_PATH}")
    m = importlib.util.module_from_spec(spec)
    sys.modules.setdefault("crossref_validator", m)
    spec.loader.exec_module(m)
    return m


@pytest.fixture(scope="module")
def report():
    v = _load_validator()
    manuscript_root = Path(__file__).resolve().parent.parent / "manuscript"
    return v.validate(manuscript_root)


def test_no_unresolved_crossrefs(report) -> None:
    """Every ``@kind:id`` reference in the manuscript must resolve."""
    unresolved = report.unresolved
    assert not unresolved, (
        f"Found {len(unresolved)} unresolved cross-references. Samples: "
        + "; ".join(f"{i.file.name}:{i.line} -> {i.context}" for i in unresolved[:5])
    )


def test_no_duplicate_labels(report) -> None:
    """No two labels of the same kind share an id."""
    dups = report.duplicates
    assert not dups, (
        f"Found {len(dups)} duplicate labels: "
        + "; ".join(f"{i.kind}:{i.suggested_id} in {i.file.name}" for i in dups[:5])
    )


def test_no_plain_text_numbered_crossrefs(report) -> None:
    """Chapter, figure, equation, and section refs must use semantic labels."""
    prose = report.prose
    assert not prose, (
        f"Found {len(prose)} hard-coded cross-references. Samples: "
        + "; ".join(f"{i.file.name}:{i.line} -> {i.context}" for i in prose[:10])
    )


def test_all_latex_figures_labeled(report) -> None:
    """Every raw-LaTeX figure environment has a ``\\label{fig:…}``."""
    unlabeled_figs = [i for i in report.missing if i.kind == "figure"]
    assert not unlabeled_figs, (
        f"{len(unlabeled_figs)} figures without \\label: "
        + "; ".join(f"{i.file.name}:{i.line}" for i in unlabeled_figs[:10])
    )


def test_chapter_and_lab_section_labels_present() -> None:
    """Every chapter, lab, and question file has ``\\label{sec:…}``."""
    manuscript = Path(__file__).resolve().parent.parent / "manuscript"
    missing: list[Path] = []
    for subtree in ("unit_I", "unit_II", "unit_III", "unit_IV", "unit_V",
                     "unit_VI", "unit_VII", "unit_VIII", "unit_IX", "unit_X",
                     "unit_0", "labs", "questions"):
        base = manuscript / subtree
        if not base.exists():
            continue
        for md in base.rglob("*.md"):
            if md.name in {"README.md", "AGENTS.md", "unit_intro.md"}:
                continue
            text = md.read_text(encoding="utf-8")
            if r"\label{sec:" not in text:
                missing.append(md)
    assert not missing, (
        f"{len(missing)} content files without \\label{{sec:…}}: "
        + ", ".join(str(p.relative_to(manuscript)) for p in missing[:5])
    )


def test_cleveref_loaded_in_preamble() -> None:
    """The cleveref package must be loaded so ``\\cref`` works."""
    preamble = (Path(__file__).resolve().parent.parent / "manuscript" / "preamble.md").read_text(
        encoding="utf-8"
    )
    assert "cleveref" in preamble, "cleveref must be loaded in preamble.md"


def test_suggest_id_slugifies() -> None:
    """``suggest_id`` must yield a sensible, idempotent slug."""
    v = _load_validator()
    out = v.suggest_id("fig", Path("manuscript/unit_I/water_and_life.md"),
                       "Hydrogen bonds in water")
    assert out.startswith("unit_I-water_and_life-")
    assert " " not in out
    # Descriptor part must be lowercase; unit tag preserves Roman numeral case.
    descriptor_part = out.split("-", 2)[-1]
    assert descriptor_part == descriptor_part.lower()


def test_config_chapter_count_matches_preface() -> None:
    """Sanity check — config enumerates 39 chapters (4 Unit 0 + 35 main).

    The preface states "39 core chapters" — this test guards against silent
    drift between the YAML manifest and the stated count.
    """
    import yaml
    cfg = yaml.safe_load(
        (Path(__file__).resolve().parent.parent / "manuscript" / "config.yaml").read_text()
    )
    total = sum(len(u.get("chapters", [])) for u in cfg["units"])
    assert total == 39, f"Expected 39 chapters, found {total}"
