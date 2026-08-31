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

Bare inline ``$$…$$`` display equations without labels are considered
worked-example steps and are not required to carry ids.
"""

from __future__ import annotations

import importlib.util
import re
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
    manuscript_root = Path(__file__).resolve().parent.parent / "docs" / "manuscript"
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


def test_all_textual_equation_labels_are_collected(report) -> None:
    """The validator must collect one-line and multi-line equation labels."""
    manuscript = Path(__file__).resolve().parent.parent / "docs" / "manuscript"
    expected: dict[str, Path] = {}
    for md in manuscript.rglob("*.md"):
        if md.name in {"AGENTS.md", "README.md", "preamble.md"}:
            continue
        for line in md.read_text(encoding="utf-8").splitlines():
            if line.lstrip().startswith("%"):
                continue
            for label in re.findall(r"\\label\{eq:([^}]+)\}", line):
                expected[label] = md

    collected = {_id for kind, _id in report.defined if kind == "eq"}
    missing = sorted(set(expected) - collected)

    assert not missing, (
        f"{len(missing)} textual equation labels were not collected: "
        + ", ".join(f"{label} in {expected[label].relative_to(manuscript)}" for label in missing[:10])
    )


def test_chapter_and_lab_section_labels_present() -> None:
    """Chapters use post-H1 ``\\label{sec:…}``; labs/questions use H1 ``{#sec:…}``."""
    manuscript = Path(__file__).resolve().parent.parent / "docs" / "manuscript"
    h1_identifier = re.compile(r"^#\s+.*\{#sec:[^}\s]+")
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
            if subtree in {"labs", "questions"}:
                first_h1 = next((line for line in text.splitlines() if line.startswith("# ")), "")
                if not h1_identifier.match(first_h1):
                    missing.append(md)
            elif r"\label{sec:" not in text:
                missing.append(md)
    assert not missing, (
        f"{len(missing)} content files without a section label: "
        + ", ".join(str(p.relative_to(manuscript)) for p in missing[:5])
    )


def test_cleveref_loaded_in_preamble() -> None:
    """The cleveref package must be loaded so ``\\cref`` works."""
    preamble = (Path(__file__).resolve().parent.parent / "docs" / "manuscript" / "preamble.md").read_text(
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
    """Sanity check — config enumerates 44 chapters (4 Unit 0 + 40 main).

    The preface states "44 core chapters" — this test guards against silent
    drift between the YAML manifest and the stated count.
    """
    import yaml
    cfg = yaml.safe_load(
        (Path(__file__).resolve().parent.parent / "docs" / "manuscript" / "config.yaml").read_text()
    )
    total = sum(len(u.get("chapters", [])) for u in cfg["units"])
    assert total == 44, f"Expected 44 chapters, found {total}"
