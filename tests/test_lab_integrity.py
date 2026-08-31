"""Integrity checks for paper-based lab appendices."""

from __future__ import annotations

import contextlib
import io
import re
import sys
from pathlib import Path


PROJECT = Path(__file__).resolve().parent.parent
MANUSCRIPT = PROJECT / "docs" / "manuscript"
SRC = PROJECT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from textbook_paths import discover_template_root  # noqa: E402
from biology.toc import load_toc  # noqa: E402

TEMPLATE_ROOT = discover_template_root(PROJECT)


def _lab_files() -> list[Path]:
    return sorted((MANUSCRIPT / "labs").rglob("lab_*.md"))


def test_labs_do_not_reference_hidden_notebooks_or_data_files() -> None:
    forbidden = (
        "provided Jupyter Notebook",
        ".ipynb",
        "pd.read_csv",
        "import pandas",
        "plt.show()",
        ".csv",
    )
    offenders: list[str] = []
    for lab in _lab_files():
        text = lab.read_text(encoding="utf-8")
        for phrase in forbidden:
            if phrase in text:
                offenders.append(f"{lab.relative_to(MANUSCRIPT)} contains {phrase!r}")
    assert not offenders


def test_lab_source_module_links_resolve() -> None:
    missing: list[str] = []
    for lab in _lab_files():
        text = lab.read_text(encoding="utf-8")
        for rel in re.findall(r"`(src/biology/[^`]+?\.py)`", text):
            if not (PROJECT / rel).exists():
                missing.append(f"{lab.relative_to(MANUSCRIPT)} -> {rel}")
    assert not missing


def test_configured_labs_include_source_governance_materials() -> None:
    toc = load_toc(PROJECT)
    assert len(toc.labs) == 44
    missing: list[str] = []
    required = (
        "Source-governance card for",
        "### Source-Governance Checkpoint",
        "printed evidence object, not as a live web lookup",
    )
    for lab in toc.labs:
        text = lab.path.read_text(encoding="utf-8")
        for needle in required:
            if needle not in text:
                missing.append(f"{lab.path.relative_to(MANUSCRIPT)} missing {needle!r}")
    assert not missing


def test_configured_labs_use_chapter_specific_context_heading() -> None:
    toc = load_toc(PROJECT)
    offenders: list[str] = []
    for lab in toc.labs:
        text = lab.path.read_text(encoding="utf-8")
        expected = f"## Lab Context: {lab.chapter.title} {{.unnumbered}}"
        if text.count(expected) != 1:
            offenders.append(f"{lab.path.relative_to(MANUSCRIPT)} missing {expected!r}")
        if "## Background {.unnumbered}" in text:
            offenders.append(f"{lab.path.relative_to(MANUSCRIPT)} still uses generic Background heading")
    assert not offenders


def test_optional_lab_python_snippets_execute() -> None:
    if str(SRC) not in sys.path:
        sys.path.insert(0, str(SRC))
    if TEMPLATE_ROOT is not None and str(TEMPLATE_ROOT) not in sys.path:
        sys.path.insert(0, str(TEMPLATE_ROOT))

    failures: list[str] = []
    for lab in _lab_files():
        text = lab.read_text(encoding="utf-8")
        for idx, code in enumerate(re.findall(r"```python\n(.*?)\n```", text, flags=re.DOTALL), start=1):
            if "from biology." not in code:
                continue
            namespace = {"__name__": "__lab_snippet__"}
            try:
                with contextlib.redirect_stdout(io.StringIO()):
                    exec(compile(code, str(lab), "exec"), namespace)
            except Exception as exc:  # pragma: no cover - assertion path carries details
                failures.append(f"{lab.relative_to(MANUSCRIPT)} snippet {idx}: {exc}")
    assert not failures
