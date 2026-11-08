"""Integrity checks for paper-based lab appendices."""

from __future__ import annotations

import os
import re
import subprocess
import sys
from pathlib import Path

PROJECT = Path(__file__).resolve().parent.parent
MANUSCRIPT = PROJECT / "docs" / "manuscript"
SRC = PROJECT / "src"


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


def test_optional_lab_python_snippets_execute(tmp_path: Path) -> None:
    environment = os.environ.copy()
    environment["PYTHONPATH"] = str(SRC)
    environment["MPLBACKEND"] = "Agg"
    for lab in _lab_files():
        text = lab.read_text(encoding="utf-8")
        for idx, code in enumerate(re.findall(r"```python\n(.*?)\n```", text, flags=re.DOTALL), start=1):
            if "from biology." not in code:
                continue
            snippet = tmp_path / f"{lab.stem}_snippet_{idx}.py"
            snippet.write_text(code, encoding="utf-8")
            subprocess.run(
                [sys.executable, str(snippet)],
                cwd=PROJECT,
                env=environment,
                check=True,
                timeout=60,
            )
