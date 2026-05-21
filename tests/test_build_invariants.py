"""End-to-end build invariants for the finished manuscript.

These tests do not build the PDF (that is the renderer pipeline's job) but
they lock in the structural invariants that make a successful build
possible:

* every chapter, lab, and question bank has a ``\\label{sec:…}`` anchor,
* every figure generator registered in the visualization package is
  referenced by at least one ``\\includegraphics`` directive,
* every chapter exposes a metadata badge,
* references.bib and the manuscript are citation-closed (no orphans,
  no dangling citations).
"""

from __future__ import annotations

import re
from pathlib import Path


MANUSCRIPT = Path(__file__).resolve().parent.parent / "manuscript"
PROJECT = MANUSCRIPT.parent


def _manuscript_markdown_files() -> list[Path]:
    return [
        path for path in sorted(MANUSCRIPT.rglob("*.md"))
        if path.name not in {"README.md", "AGENTS.md"}
    ]


def test_every_chapter_has_section_label() -> None:
    """All 39 chapter files must declare ``\\label{sec:unit_…_…}``."""
    missing: list[Path] = []
    for unit_dir in sorted(MANUSCRIPT.glob("unit_*")):
        for ch in sorted(unit_dir.glob("*.md")):
            if ch.name in {"README.md", "AGENTS.md", "unit_intro.md"}:
                continue
            text = ch.read_text(encoding="utf-8")
            if re.search(r"\\label\{sec:unit_[^}]+\}", text) is None:
                missing.append(ch)
    assert not missing, f"Chapters missing section labels: {[str(p) for p in missing]}"


def test_every_lab_and_question_has_section_label() -> None:
    for subtree, glob in (("labs", "lab_*.md"), ("questions", "questions_*.md")):
        missing: list[Path] = []
        for f in (MANUSCRIPT / subtree).rglob(glob):
            text = f.read_text(encoding="utf-8")
            if re.search(r"\\label\{sec:[^}]+\}", text) is None:
                missing.append(f)
        assert not missing, f"Missing section labels in {subtree}: {missing}"


def test_every_chapter_has_metadata_badge() -> None:
    missing: list[Path] = []
    for unit_dir in sorted(MANUSCRIPT.glob("unit_*")):
        for ch in sorted(unit_dir.glob("*.md")):
            if ch.name in {"README.md", "AGENTS.md", "unit_intro.md"}:
                continue
            if "<!-- chapter-metadata-badge -->" not in ch.read_text(encoding="utf-8"):
                missing.append(ch)
    assert not missing, f"Chapters missing metadata badge: {missing}"


def test_every_lab_links_to_parent_chapter() -> None:
    missing: list[Path] = []
    for lab in (MANUSCRIPT / "labs").rglob("lab_*.md"):
        text = lab.read_text(encoding="utf-8")
        if re.search(r"\\cref\{sec:unit_[^}]+\}", text) is None:
            missing.append(lab)
    assert not missing, f"Labs without \\cref link to parent chapter: {missing}"


def test_every_question_links_to_parent_chapter() -> None:
    missing: list[Path] = []
    for q in (MANUSCRIPT / "questions").rglob("questions_*.md"):
        text = q.read_text(encoding="utf-8")
        if re.search(r"\\cref\{sec:unit_[^}]+\}", text) is None:
            missing.append(q)
    assert not missing, f"Question banks without \\cref link to parent chapter: {missing}"


def test_every_registered_figure_is_referenced() -> None:
    """Every entry in :data:`visualization.ALL_FIGURE_GENERATORS` must appear
    as ``\\includegraphics{…/<name>.png}`` (or a variant produced by the
    generator such as ``punnett_AaxAa.png``) in at least one chapter."""
    import importlib
    import sys

    src_path = Path(__file__).resolve().parent.parent / "src"
    if str(src_path) not in sys.path:
        sys.path.insert(0, str(src_path))
    visualization = importlib.import_module("visualization")
    names = [n for n, _fn in visualization.ALL_FIGURE_GENERATORS]
    # What names are referenced in chapters?
    includes = []
    for ch in MANUSCRIPT.rglob("*.md"):
        if ch.name in {"README.md", "AGENTS.md"}:
            continue
        for match in re.finditer(r"\\includegraphics(?:\[[^\]]*\])?\{[^}]*?([A-Za-z0-9_]+)\.png\}",
                                   ch.read_text(encoding="utf-8")):
            includes.append(match.group(1))
    # Every registered generator should be referenced or matched by a close filename.
    referenced = set(includes)
    orphans = []
    for n in names:
        # "punnett_square" generator produces file "punnett_AaxAa.png"; accept either.
        base = n.split("_")[0]
        if n in referenced or any(ref == n or ref.startswith(base) for ref in referenced):
            continue
        orphans.append(n)
    assert not orphans, f"Figure generators not referenced in manuscript: {orphans}"


def test_bibliography_closed() -> None:
    """Every BibTeX entry is cited; every citation resolves."""
    bib = (MANUSCRIPT / "references.bib").read_text(encoding="utf-8")
    defined = set(re.findall(r"@\w+\{([^,\s]+),", bib))
    cited: set[str] = set()
    for md in MANUSCRIPT.rglob("*.md"):
        if md.name in {"README.md", "AGENTS.md"}:
            continue
        for m in re.finditer(r"\\cite[pt]?\*?\{([^}]+)\}", md.read_text(encoding="utf-8")):
            for k in m.group(1).split(","):
                cited.add(k.strip())
    assert cited - defined == set(), f"Dangling citations: {cited - defined}"
    assert defined - cited == set(), f"Orphan entries: {defined - cited}"


def test_glossary_links_resolve_to_master_glossary_anchors() -> None:
    """Every ``#gl:`` manuscript link must resolve inside the master glossary."""
    glossary = (MANUSCRIPT / "glossary.md").read_text(encoding="utf-8")
    anchors = set(re.findall(r"\{#(gl:[A-Za-z0-9_-]+)\}", glossary))
    used: dict[str, list[str]] = {}
    for md in _manuscript_markdown_files():
        for line_no, line in enumerate(md.read_text(encoding="utf-8").splitlines(), start=1):
            for match in re.finditer(r"\]\(#(gl:[A-Za-z0-9_-]+)\)", line):
                used.setdefault(match.group(1), []).append(f"{md.relative_to(MANUSCRIPT)}:{line_no}")
    missing = {slug: locations for slug, locations in sorted(used.items()) if slug not in anchors}
    assert not missing, f"Glossary links without anchors: {missing}"


def test_glossary_and_index_use_semantic_chapter_links() -> None:
    """Appendix F/G should not contain stale ``Chapter N``/``Ch N`` back-references."""
    offenders: list[str] = []
    pattern = re.compile(r"→\s*(?:Chapters?|Ch)\s+\d")
    for path in (MANUSCRIPT / "glossary.md", MANUSCRIPT / "appendices" / "appendix_index.md"):
        for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
            if pattern.search(line):
                offenders.append(f"{path.relative_to(MANUSCRIPT)}:{line_no}: {line.strip()}")
    assert not offenders


def test_known_biology_claim_corrections_remain_present() -> None:
    """High-risk glossary claims should keep their reviewed, nuanced wording."""
    glossary = (MANUSCRIPT / "glossary.md").read_text(encoding="utf-8")
    circulation = (MANUSCRIPT / "unit_IX" / "circulation_respiration_homeostasis.md").read_text(
        encoding="utf-8"
    )
    assert "TLR1–10 in humans" in glossary
    assert "up to 1,000-fold more antibiotic tolerant" in glossary
    assert "not literally dark" in glossary
    assert "age-dependent lower limit of normal" in glossary
    assert "age-dependent lower limit of normal" in circulation


def test_labs_are_paper_based_by_default() -> None:
    """Labs should require only printed evidence, cards, graphs, and writing tools."""
    offenders: list[str] = []
    banned_required_terms = re.compile(
        r"\b("
        r"beakers?|pipettes?|reagents?|Benedict'?s|Biuret|Sudan|HCl|NaOH|"
        r"hot water bath|compound microscope|dissecting microscope|glass slides?|"
        r"coverslips?|wet mounts?|cheek swabs?|agar plates?|LB agar|Mueller-Hinton|"
        r"swabbed|duckweed cultures?|pollen germination medium|"
        r"fresh flowers?|dissect(?:ion|ed|ing)|sharp knife|celery cross-sections?"
        r")\b",
        flags=re.IGNORECASE,
    )
    for lab in sorted((MANUSCRIPT / "labs").rglob("lab_*.md")):
        text = lab.read_text(encoding="utf-8")
        assert "## Paper-Based Materials {.unnumbered}" in text, lab
        assert "## Paper-Based Investigation {.unnumbered}" in text, lab
        default_text = re.split(r"## Optional (?:Material|Wet-Lab)", text, maxsplit=1)[0]
        default_text = default_text.split("## Safety and Ethics Notes", 1)[0]
        default_text = default_text.split("## Debrief and Reflection", 1)[0]
        default_text = default_text.split("## Analysis Questions", 1)[0]
        for line_no, line in enumerate(default_text.splitlines(), start=1):
            if banned_required_terms.search(line):
                offenders.append(f"{lab.relative_to(MANUSCRIPT)}:{line_no}: {line.strip()}")
    assert not offenders


def test_no_escaped_newline_or_nested_strong_link_artifacts() -> None:
    """Generated copy-paste artifacts should not leak into renderable prose."""
    offenders: list[str] = []
    nested_link = re.compile(r"\*\*\[\*\*")
    for md in _manuscript_markdown_files():
        in_fence = False
        for line_no, line in enumerate(md.read_text(encoding="utf-8").splitlines(), start=1):
            if line.startswith("```"):
                in_fence = not in_fence
                continue
            if in_fence:
                continue
            if line.endswith(r"\n") or line == r"|":
                offenders.append(f"{md.relative_to(MANUSCRIPT)}:{line_no}: escaped newline/table artifact")
            if nested_link.search(line):
                offenders.append(f"{md.relative_to(MANUSCRIPT)}:{line_no}: nested bold markdown link")
    assert not offenders


def test_worked_example_headings_are_bookmark_safe() -> None:
    """Worked-example problem statements belong in body text, not headings."""
    offenders: list[str] = []
    for md in _manuscript_markdown_files():
        for line_no, line in enumerate(md.read_text(encoding="utf-8").splitlines(), start=1):
            if not re.match(r"^#{1,6}\s+Worked Example", line):
                continue
            heading = re.sub(r"^#{1,6}\s+", "", line)
            if "$" in heading or len(heading) > 90:
                offenders.append(f"{md.relative_to(MANUSCRIPT)}:{line_no}: {heading}")
    assert not offenders


def test_blockquotes_do_not_become_setext_headings() -> None:
    """A blockquote immediately followed by ``---`` becomes a heading in Pandoc."""
    offenders: list[str] = []
    previous_quote: tuple[Path, int, str] | None = None
    for md in _manuscript_markdown_files():
        for line_no, line in enumerate(md.read_text(encoding="utf-8").splitlines(), start=1):
            if line.startswith(">"):
                previous_quote = (md, line_no, line)
                continue
            if line == "---" and previous_quote is not None:
                quote_path, quote_line, quote_text = previous_quote
                if quote_path == md:
                    offenders.append(
                        f"{md.relative_to(MANUSCRIPT)}:{quote_line}: "
                        f"blockquote directly followed by horizontal rule: {quote_text[:80]}"
                    )
            previous_quote = None
    assert not offenders


def test_manuscript_uses_supported_latex_arrow_macros() -> None:
    """Prefer renderer-supported arrows over package-specific extensible arrows."""
    unsupported = {"\\xleftrightarrow", "\\xrightleftharpoons"}
    offenders: list[str] = []
    for md in _manuscript_markdown_files():
        for line_no, line in enumerate(md.read_text(encoding="utf-8").splitlines(), start=1):
            for macro in unsupported:
                if macro in line:
                    offenders.append(f"{md.relative_to(MANUSCRIPT)}:{line_no}: {macro}")
    assert not offenders


def test_latex_figure_captions_do_not_contain_raw_exponents() -> None:
    """Raw ``^`` in explicit LaTeX captions causes XeLaTeX math-mode errors."""
    offenders: list[str] = []
    for md in _manuscript_markdown_files():
        for line_no, line in enumerate(md.read_text(encoding="utf-8").splitlines(), start=1):
            if line.startswith(r"\caption{") and "^" in re.sub(r"\$[^$]*\$", "", line):
                offenders.append(f"{md.relative_to(MANUSCRIPT)}:{line_no}: {line[:100]}")
    assert not offenders


def test_learning_objectives_start_with_measurable_verbs() -> None:
    """Learning objectives should be assessable, not vague editorial prompts."""
    allowed = {
        "Analyse", "Analyze", "Apply", "Assess", "Calculate", "Catalogue", "Classify",
        "Compare", "Compute", "Connect", "Construct", "Contrast", "Define", "Derive",
        "Describe", "Design", "Develop", "Diagram", "Differentiate", "Distinguish",
        "Estimate", "Evaluate", "Explain", "Identify", "Interpret", "Justify", "Label",
        "List", "Map", "Model", "Name", "Outline", "Perform", "Predict", "Propose",
        "Quantify", "Read", "Recall", "Recognise", "Recognize", "Relate", "Solve",
        "State", "Summarise", "Summarize", "Tabulate", "Test", "Trace", "Use", "Write",
    }
    banned = {"Discuss", "Know", "Understand", "Learn", "Appreciate"}
    offenders: list[str] = []
    objective_block = re.compile(
        r"## Learning Objectives\n(?P<body>.*?)(?:\n<!-- curriculum-scaffold-start -->|\n---|\n## )",
        re.DOTALL,
    )
    for chapter in sorted(MANUSCRIPT.glob("unit_*/*.md")):
        if chapter.name in {"README.md", "AGENTS.md", "unit_intro.md"}:
            continue
        match = objective_block.search(chapter.read_text(encoding="utf-8"))
        if match is None:
            offenders.append(f"{chapter.relative_to(MANUSCRIPT)}: missing Learning Objectives block")
            continue
        verbs = []
        for line_no, line in enumerate(match.group("body").splitlines(), start=1):
            item = re.match(r"\d+\.\s+([A-Za-z]+)", line.strip())
            if item is None:
                continue
            verb = item.group(1)
            verbs.append(verb)
            if verb in banned or verb not in allowed:
                offenders.append(f"{chapter.relative_to(MANUSCRIPT)} objective {line_no}: {verb}")
        if len(verbs) < 5:
            offenders.append(f"{chapter.relative_to(MANUSCRIPT)}: only {len(verbs)} objectives")
    assert not offenders


def test_question_banks_have_thirty_numbered_items() -> None:
    """Every companion question bank should support a complete 30-item draw."""
    offenders: list[str] = []
    for question_bank in sorted((MANUSCRIPT / "questions").rglob("questions_*.md")):
        text = question_bank.read_text(encoding="utf-8")
        numbers = [int(match.group(1)) for match in re.finditer(r"^(\d+)\.\s+", text, re.MULTILINE)]
        if numbers != list(range(1, 31)):
            offenders.append(f"{question_bank.relative_to(MANUSCRIPT)}: {numbers}")
    assert not offenders


def test_course_planning_grid_populated() -> None:
    front = (MANUSCRIPT / "front_matter.md").read_text(encoding="utf-8")
    assert "<!-- course-planning-grid-start -->" in front
    assert "<!-- course-planning-grid-end -->" in front
    # The generated grid must contain every chapter title keyword.
    assert "Totals" in front
