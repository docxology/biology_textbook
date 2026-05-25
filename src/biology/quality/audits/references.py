"""Quality audit helpers — extracted from engine.py."""

from __future__ import annotations

import re


from biology.citations import bib_keys, citation_keys
from biology.maintenance.manuscript_walker import (
    iter_prose_lines,
    manuscript_markdown_files,
)
from biology.quality import paths
from biology.quality.models import Finding
from biology.quality.audits.helpers import (
    _generated_block_line_numbers,
)
from biology.quality.patterns import (
    BROKEN_CREF_RE,
    BROKEN_NAMEREF_RE,
    BROKEN_NAMEREF_TAIL_RE,
    COLLAPSED_UNIT_CREF_RE,
    DOLLAR_TAG_LABEL_RE,
    HARDCODED_REF,
    HARDCODED_STRUCTURAL_REF,
    INLINE_CIRC_PRIME_RE,
    LATEX_EQUATION_TAG_RE,
    RAW_LATEX_RENDERED_REF,
)

def audit_broken_crossrefs(findings: list[Finding]) -> None:
    for path in manuscript_markdown_files():
        for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
            if (
                BROKEN_CREF_RE.search(line)
                or BROKEN_NAMEREF_RE.search(line)
                or BROKEN_NAMEREF_TAIL_RE.search(line)
                or COLLAPSED_UNIT_CREF_RE.search(line)
            ):
                findings.append(Finding("error", "broken-crossref", path, line_no, line.strip()))

def audit_references(findings: list[Finding]) -> None:
    for path in manuscript_markdown_files():
        generated_lines = _generated_block_line_numbers(path)
        for line_no, line in iter_prose_lines(path):
            if line_no in generated_lines:
                continue
            if HARDCODED_REF.search(line):
                findings.append(Finding("error", "hardcoded-rendered-reference", path, line_no, line.strip()))
            if RAW_LATEX_RENDERED_REF.search(line):
                findings.append(Finding("error", "raw-latex-rendered-reference", path, line_no, line.strip()))
            if DOLLAR_TAG_LABEL_RE.search(line):
                findings.append(Finding("error", "dollar-tag-label-equation", path, line_no, line.strip()))
            if LATEX_EQUATION_TAG_RE.search(line):
                findings.append(Finding("error", "hardcoded-equation-tag", path, line_no, line.strip()))
            if INLINE_CIRC_PRIME_RE.search(line):
                findings.append(Finding("error", "unsafe-inline-circ-prime", path, line_no, line.strip()))
            if HARDCODED_STRUCTURAL_REF.search(line):
                findings.append(
                    Finding(
                        "error",
                        "hardcoded-rendered-structural-reference",
                        path,
                        line_no,
                        line.strip(),
                    )
                )

def audit_glossary_and_citations(findings: list[Finding]) -> None:
    bib = (paths.MANUSCRIPT / "references.bib").read_text(encoding="utf-8")
    defined = bib_keys(bib)
    cited: set[str] = set()
    for path in manuscript_markdown_files():
        text = path.read_text(encoding="utf-8")
        cited.update(citation_keys(text))
    for key in sorted(cited - defined):
        findings.append(Finding("error", "dangling-citation", paths.MANUSCRIPT / "references.bib", 1, key))
    for key in sorted(defined - cited):
        findings.append(Finding("error", "orphan-bibentry", paths.MANUSCRIPT / "references.bib", 1, key))

    glossary = (paths.MANUSCRIPT / "glossary.md").read_text(encoding="utf-8")
    anchors = re.findall(r"\{#(gl:[A-Za-z0-9_-]+)\}", glossary)
    duplicates = sorted({anchor for anchor in anchors if anchors.count(anchor) > 1})
    for anchor in duplicates:
        findings.append(Finding("error", "duplicate-glossary-anchor", paths.MANUSCRIPT / "glossary.md", 1, anchor))

    anchor_set = set(anchors)
    for path in manuscript_markdown_files():
        for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
            for slug in re.findall(r"\]\(#(gl:[A-Za-z0-9_-]+)\)", line):
                if slug not in anchor_set:
                    findings.append(Finding("error", "dangling-glossary-link", path, line_no, slug))
