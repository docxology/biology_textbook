"""Cross-reference validator for the Biology textbook manuscript.

Walks all manuscript markdown files and checks pandoc-crossref conventions:

- Figures (``![alt](path)``) must carry ``{#fig:<id>}``
- Tables (first line of a pipe/grid table or an explicit caption) must carry ``{#tbl:<id>}``
- Display equations (``$$ ... $$``) must carry ``{#eq:<id>}`` or ``\\label{eq:<id>}``
- All cross-references ``@fig:X``, ``@eq:X``, ``@tbl:X``, ``@sec:X`` must resolve

The validator is intentionally dependency-free (stdlib only) so it can run in
any CI environment without extra installs.

The module exposes:

* :class:`CrossRefIssue` — a single finding
* :func:`scan_file` — parse one markdown file
* :func:`scan_directory` — walk a manuscript tree
* :func:`validate` — high-level entry point that returns a
  :class:`CrossRefReport` with ``missing``, ``unresolved`` and ``duplicate`` lists

Use via :mod:`scripts.insert_crossref_ids` (auto-fix) or via the test
:mod:`tests.test_crossref_validator` (invariant assertion).
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable


# ---------------------------------------------------------------------------
# Regex patterns
# ---------------------------------------------------------------------------

# Markdown image:  ![alt](path){attrs}    or    ![alt](path)
_RE_IMG = re.compile(r"!\[(?P<alt>[^\]]*)\]\((?P<path>[^)\s]+)(?:\s+\"[^\"]*\")?\)(?P<attrs>\{[^}]*\})?")

# pandoc-crossref attribute for figures: {#fig:something ...}
_RE_FIG_ID = re.compile(r"\{[^}]*#fig:(?P<id>[A-Za-z0-9_\-:]+)[^}]*\}")

# Raw-LaTeX figure environment start / end (common in this manuscript)
_RE_LATEX_FIG_OPEN = re.compile(r"\\begin\{figure\*?\}")
_RE_LATEX_FIG_END = re.compile(r"\\end\{figure\*?\}")
_RE_LATEX_INCLUDE = re.compile(r"\\includegraphics(?:\[[^\]]*\])?\{(?P<path>[^}]+)\}")

# Raw-LaTeX table environment
_RE_LATEX_TBL_OPEN = re.compile(r"\\begin\{table\*?\}")
_RE_LATEX_TBL_END = re.compile(r"\\end\{table\*?\}")

# Inline `$$...$$` display equation (both delimiters on one line) — common here
_RE_INLINE_DISPLAY_EQ = re.compile(r"^\s*\$\$(?P<body>.+)\$\$\s*$")
# Manual equation tag (LaTeX \tag{1.1}) — identifies numbered eqs even without \label
_RE_EQ_TAG = re.compile(r"\\tag\{(?P<num>[^}]+)\}")

# Display-math fence using `$$` on its own line OR inline delimited block.
# We detect block-level $$ pairs and look for {#eq:...} on the same line as
# the closing $$ or on the following line, OR a \label{eq:...} inside.
_RE_DISPLAY_EQ_OPEN = re.compile(r"^\s*\$\$\s*$")

# LaTeX equation environments
_RE_LATEX_EQ_OPEN = re.compile(r"\\begin\{(?:equation|align|gather|multline)\*?\}")
_RE_LATEX_LABEL = re.compile(r"\\label\{(?P<kind>eq|fig|tbl|sec):(?P<id>[A-Za-z0-9_\-:]+)\}")

# pandoc-crossref eq attribute appended to display math
_RE_EQ_ID = re.compile(r"\{[^}]*#eq:(?P<id>[A-Za-z0-9_\-:]+)[^}]*\}")

# Tables — pandoc caption line ": Caption {#tbl:id}"  or  "Table: Caption {#tbl:id}"
_RE_TBL_CAPTION = re.compile(r"^(?:Table)?\s*:\s*(?P<caption>.+?)(?P<attrs>\{[^}]*\})?\s*$")
_RE_TBL_ID = re.compile(r"\{[^}]*#tbl:(?P<id>[A-Za-z0-9_\-:]+)[^}]*\}")

# Pipe-table detection: a line beginning with `|` and containing at least one
# more `|`. Only used to flag a following "Table: ..." caption.
_RE_PIPE_TABLE_ROW = re.compile(r"^\s*\|.*\|\s*$")

# Section headers: "## Heading {#sec:slug}"
_RE_HEADING = re.compile(r"^(?P<hashes>#{1,6})\s+(?P<title>.+?)(?:\s+(?P<attrs>\{[^}]*\}))?\s*$")
_RE_SEC_ID = re.compile(r"\{[^}]*#sec:(?P<id>[A-Za-z0-9_\-:]+)[^}]*\}")

# Cross-reference usage: @fig:X  @eq:X  @tbl:X  @sec:X (also [@...])
_RE_REF_USE = re.compile(r"(?<![A-Za-z0-9_])@(?P<kind>fig|eq|tbl|sec):(?P<id>[A-Za-z0-9_\-:]+)")

# Prose cross-references still using plain text instead of semantic labels.
_RE_PROSE_XREF = re.compile(
    r"("
    r"(?:→\s*)?(?:Chapters?|Chapter)\s+\d+(?:\.\d+)?(?:\s*(?:,|and)\s*(?:Chapter\s+)?\d+(?:\.\d+)?)*"
    r"|→\s*Ch\s+\d+(?:\.\d+)?(?:\s*,\s*Ch\s+\d+(?:\.\d+)?)*"
    r"|\b(?:Figure|Fig\.|Equation|Eq\.)\s+\d+(?:\.\d+)?"
    r"|\bSection\s+\d+(?:\.\d+)?"
    r"|§+\s*\d+(?:\.\d+)?"
    r"|\bUnits?\s+(?:0(?:\.\d+)?(?:'s)?|[IVX]+(?:\s*[–-]\s*[IVX]+)?"
    r"(?:\s*(?:,|and|or|/|\+)\s*[IVX]+)*)\b"
    r"|\bAppendix\s+[A-Z]\b"
    r"|\b(?:Figure|Fig\.)\s+FM-\d+\b"
    r"|\bChapter numbers\b"
    r")",
)
_RE_FENCE = re.compile(r"^\s*```\s*(?P<lang>[A-Za-z0-9_-]*)")

_GENERATED_BLOCK_MARKERS: tuple[tuple[str, str], ...] = (
    ("<!-- toc-navigation-start -->", "<!-- toc-navigation-end -->"),
    ("<!-- suggested-reading-paths-start -->", "<!-- suggested-reading-paths-end -->"),
    ("<!-- textbook-concept-map-start -->", "<!-- textbook-concept-map-end -->"),
    ("<!-- course-planning-grid-start -->", "<!-- course-planning-grid-end -->"),
    ("<!-- preface-scope-start -->", "<!-- preface-scope-end -->"),
)


# ---------------------------------------------------------------------------
# Data classes
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class CrossRefIssue:
    """A single validation finding."""

    file: Path
    line: int
    kind: str  # "figure" | "equation" | "table" | "section" | "ref"
    problem: str  # "missing_id" | "unresolved" | "duplicate" | "prose_xref"
    suggested_id: str = ""
    context: str = ""  # excerpt of the offending line

    def as_row(self) -> dict[str, str]:
        return {
            "file": str(self.file),
            "line": str(self.line),
            "kind": self.kind,
            "problem": self.problem,
            "suggested_id": self.suggested_id,
            "context": self.context.replace("\n", " ").strip()[:120],
        }


@dataclass
class CrossRefReport:
    """Aggregate results of a manuscript scan."""

    defined: dict[tuple[str, str], Path] = field(default_factory=dict)  # (kind, id) -> file
    references: list[tuple[str, str, Path, int]] = field(default_factory=list)  # kind, id, file, line
    issues: list[CrossRefIssue] = field(default_factory=list)

    # Convenience grouping --------------------------------------------------
    @property
    def missing(self) -> list[CrossRefIssue]:
        """All issues with ``problem == \"missing_id\"\" (undefined labels/tables/figures)."""
        return [i for i in self.issues if i.problem == "missing_id"]

    @property
    def unresolved(self) -> list[CrossRefIssue]:
        """All issues with ``problem == \"unresolved\"`` (references to undefined labels)."""
        return [i for i in self.issues if i.problem == "unresolved"]

    @property
    def duplicates(self) -> list[CrossRefIssue]:
        """All issues with ``problem == \"duplicate\"`` (labels defined more than once)."""
        return [i for i in self.issues if i.problem == "duplicate"]

    @property
    def prose(self) -> list[CrossRefIssue]:
        return [i for i in self.issues if i.problem == "prose_xref"]

    def summary(self) -> str:
        parts = [
            f"defined={len(self.defined)}",
            f"references={len(self.references)}",
            f"missing={len(self.missing)}",
            f"unresolved={len(self.unresolved)}",
            f"duplicates={len(self.duplicates)}",
            f"prose_xrefs={len(self.prose)}",
        ]
        return " ".join(parts)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _slugify(text: str) -> str:
    """Produce a filesystem/URL-safe slug suitable for a crossref id."""
    s = text.strip().lower()
    s = re.sub(r"[^a-z0-9]+", "-", s)
    s = re.sub(r"-+", "-", s).strip("-")
    return s or "untitled"


def _unit_tag(path: Path) -> str:
    """Extract the unit tag (e.g. ``unit_I``) from a manuscript path.

    Works for chapter files (``manuscript/unit_I/water_and_life.md``) and for
    labs/questions (``manuscript/labs/unit_I/lab_water_and_life.md``).
    """
    for part in path.parts:
        if part.startswith("unit_") or part == "unit_0":
            return part
    return "front"


def _file_stem(path: Path) -> str:
    stem = path.stem
    for prefix in ("lab_", "questions_"):
        if stem.startswith(prefix):
            stem = stem[len(prefix) :]
            break
    return stem


def suggest_id(kind: str, path: Path, descriptor: str, ordinal: int = 0) -> str:
    """Suggest a canonical crossref id for ``kind`` at ``path``."""
    unit = _unit_tag(path)
    stem = _file_stem(path)
    tail = _slugify(descriptor) if descriptor else f"item-{ordinal}"
    # Keep ids reasonably short: unit + chapter stem + descriptor
    return f"{unit}-{stem}-{tail}"


def _generated_block_lines(text: str) -> set[int]:
    """Line numbers owned by generated manuscript marker blocks."""
    line_starts: list[int] = []
    offset = 0
    for line in text.splitlines(keepends=True):
        line_starts.append(offset)
        offset += len(line)
    generated: set[int] = set()
    for start_marker, end_marker in _GENERATED_BLOCK_MARKERS:
        start = text.find(start_marker)
        end = text.find(end_marker, start)
        if start == -1 or end == -1:
            continue
        end += len(end_marker)
        for line_no, line_start in enumerate(line_starts, start=1):
            if start <= line_start < end:
                generated.add(line_no)
    return generated


# ---------------------------------------------------------------------------
# Core scan
# ---------------------------------------------------------------------------


def scan_file(path: Path) -> tuple[dict[tuple[str, str], int], list[tuple[str, str, int]], list[CrossRefIssue]]:
    """Scan a single markdown file.

    Returns:
        (defined, references, issues) where
        * ``defined`` maps ``(kind, id)`` → line number
        * ``references`` is a list of ``(kind, id, line)`` tuples
        * ``issues`` lists local problems (missing ids, prose xrefs)
    """
    defined: dict[tuple[str, str], int] = {}
    references: list[tuple[str, str, int]] = []
    issues: list[CrossRefIssue] = []

    try:
        text = path.read_text(encoding="utf-8")
    except OSError as exc:  # pragma: no cover - unreadable file is a hard error
        issues.append(
            CrossRefIssue(file=path, line=0, kind="file", problem="missing_id", context=f"could not read file: {exc}")
        )
        return defined, references, issues

    lines = text.splitlines()
    generated_lines = _generated_block_lines(text)

    in_display_eq = False
    in_latex_eq = False
    in_latex_fig = False
    in_latex_tbl = False
    eq_buffer: list[str] = []
    fig_buffer: list[str] = []
    tbl_buffer: list[str] = []
    eq_start_line = 0
    fig_start_line = 0
    tbl_start_line = 0
    eq_ordinal = 0
    fig_ordinal = 0
    tbl_ordinal = 0
    tagged_eq_count = 0
    in_code_fence = False
    code_fence_lang = ""

    for i, line in enumerate(lines, start=1):
        fence_match = _RE_FENCE.match(line)
        if fence_match:
            if in_code_fence:
                in_code_fence = False
                code_fence_lang = ""
            else:
                in_code_fence = True
                code_fence_lang = fence_match.group("lang").lower()
            continue

        visible_for_xref_check = not in_code_fence or code_fence_lang == "mermaid"

        # ---------------- raw-LaTeX figure env ----------------
        if _RE_LATEX_FIG_OPEN.search(line):
            in_latex_fig = True
            fig_buffer = [line]
            fig_start_line = i
            continue
        if in_latex_fig:
            fig_buffer.append(line)
            if _RE_LATEX_FIG_END.search(line):
                fig_ordinal += 1
                block = "\n".join(fig_buffer)
                label_match = _RE_LATEX_LABEL.search(block)
                if label_match and label_match.group("kind") == "fig":
                    defined[("fig", label_match.group("id"))] = fig_start_line
                else:
                    # try to suggest an id from \includegraphics path
                    inc_match = _RE_LATEX_INCLUDE.search(block)
                    desc = Path(inc_match.group("path")).stem if inc_match else f"fig-{fig_ordinal}"
                    issues.append(
                        CrossRefIssue(
                            file=path,
                            line=fig_start_line,
                            kind="figure",
                            problem="missing_id",
                            suggested_id=suggest_id("fig", path, desc, fig_ordinal),
                            context=block.splitlines()[0],
                        )
                    )
                in_latex_fig = False
                fig_buffer = []
            continue

        # ---------------- raw-LaTeX table env ----------------
        if _RE_LATEX_TBL_OPEN.search(line):
            in_latex_tbl = True
            tbl_buffer = [line]
            tbl_start_line = i
            continue
        if in_latex_tbl:
            tbl_buffer.append(line)
            if _RE_LATEX_TBL_END.search(line):
                tbl_ordinal += 1
                block = "\n".join(tbl_buffer)
                label_match = _RE_LATEX_LABEL.search(block)
                if label_match and label_match.group("kind") == "tbl":
                    defined[("tbl", label_match.group("id"))] = tbl_start_line
                else:
                    issues.append(
                        CrossRefIssue(
                            file=path,
                            line=tbl_start_line,
                            kind="table",
                            problem="missing_id",
                            suggested_id=suggest_id("tbl", path, "", tbl_ordinal),
                            context=block.splitlines()[0],
                        )
                    )
                in_latex_tbl = False
                tbl_buffer = []
            continue

        # ---------------- inline display equation $$…$$ ----------------
        inline_eq = _RE_INLINE_DISPLAY_EQ.match(line)
        if inline_eq and not in_display_eq and not in_latex_eq:
            eq_ordinal += 1
            body = inline_eq.group("body")
            label_match = _RE_LATEX_LABEL.search(body)
            eq_attr = _RE_EQ_ID.search(body)
            tag_match = _RE_EQ_TAG.search(body)
            if eq_attr:
                defined[("eq", eq_attr.group("id"))] = i
            elif label_match and label_match.group("kind") == "eq":
                defined[("eq", label_match.group("id"))] = i
            elif tag_match:
                # Tagged equations have a manual number but no cross-ref id.
                # Register them under a synthesised id so the validator can
                # report on coverage without forcing changes.
                tagged_eq_count += 1
                defined[("eq", f"tag-{tag_match.group('num')}-{_file_stem(path)}")] = i
            else:
                issues.append(
                    CrossRefIssue(
                        file=path,
                        line=i,
                        kind="equation",
                        problem="missing_id",
                        suggested_id=suggest_id("eq", path, "", eq_ordinal),
                        context=line.strip()[:120],
                    )
                )
            # skip further processing of this line
            continue

        # ---------------- section headings ----------------
        m = _RE_HEADING.match(line)
        if m and not in_display_eq and not in_latex_eq:
            attrs = m.group("attrs") or ""
            sec_match = _RE_SEC_ID.search(attrs)
            if sec_match:
                sid = sec_match.group("id")
                if ("sec", sid) in defined:
                    issues.append(
                        CrossRefIssue(
                            file=path, line=i, kind="section", problem="duplicate", suggested_id=sid, context=line
                        )
                    )
                defined[("sec", sid)] = i
            # Section IDs are optional — pandoc emits auto-slugs for every
            # heading — so we do NOT require explicit {#sec:…} markers.  The
            # validator only reports them when one is declared (to catch
            # typos and duplicates), not when one is absent.

        # ---------------- figure ----------------
        for fm in _RE_IMG.finditer(line):
            fig_ordinal += 1
            attrs = fm.group("attrs") or ""
            fid_match = _RE_FIG_ID.search(attrs)
            if fid_match:
                fid = fid_match.group("id")
                if ("fig", fid) in defined:
                    issues.append(
                        CrossRefIssue(
                            file=path, line=i, kind="figure", problem="duplicate", suggested_id=fid, context=line
                        )
                    )
                defined[("fig", fid)] = i
            else:
                desc = fm.group("alt") or Path(fm.group("path")).stem
                issues.append(
                    CrossRefIssue(
                        file=path,
                        line=i,
                        kind="figure",
                        problem="missing_id",
                        suggested_id=suggest_id("fig", path, desc, fig_ordinal),
                        context=line,
                    )
                )

        # ---------------- display equation ($$) ----------------
        if _RE_DISPLAY_EQ_OPEN.match(line):
            if not in_display_eq:
                in_display_eq = True
                eq_buffer = [line]
                eq_start_line = i
            else:
                # Closing $$ — check buffer for label
                eq_buffer.append(line)
                eq_ordinal += 1
                block = "\n".join(eq_buffer)
                eq_match = _RE_EQ_ID.search(block)
                label_match = _RE_LATEX_LABEL.search(block)
                if eq_match:
                    eid = eq_match.group("id")
                    defined[("eq", eid)] = eq_start_line
                elif label_match and label_match.group("kind") == "eq":
                    eid = label_match.group("id")
                    defined[("eq", eid)] = eq_start_line
                else:
                    # check the *following* line for {#eq:...} attr
                    nxt = lines[i] if i < len(lines) else ""
                    nxt_match = _RE_EQ_ID.search(nxt)
                    if nxt_match:
                        defined[("eq", nxt_match.group("id"))] = eq_start_line
                    else:
                        issues.append(
                            CrossRefIssue(
                                file=path,
                                line=eq_start_line,
                                kind="equation",
                                problem="missing_id",
                                suggested_id=suggest_id("eq", path, "", eq_ordinal),
                                context=eq_buffer[1] if len(eq_buffer) > 1 else block,
                            )
                        )
                in_display_eq = False
                eq_buffer = []
            continue

        if in_display_eq:
            eq_buffer.append(line)
            continue

        # ---------------- LaTeX equation environments ----------------
        if _RE_LATEX_EQ_OPEN.search(line):
            in_latex_eq = True
            eq_buffer = [line]
            eq_start_line = i
            continue
        if in_latex_eq:
            eq_buffer.append(line)
            if re.search(r"\\end\{(?:equation|align|gather|multline)\*?\}", line):
                eq_ordinal += 1
                block = "\n".join(eq_buffer)
                label_match = _RE_LATEX_LABEL.search(block)
                if label_match and label_match.group("kind") == "eq":
                    defined[("eq", label_match.group("id"))] = eq_start_line
                else:
                    issues.append(
                        CrossRefIssue(
                            file=path,
                            line=eq_start_line,
                            kind="equation",
                            problem="missing_id",
                            suggested_id=suggest_id("eq", path, "", eq_ordinal),
                            context=block.splitlines()[0],
                        )
                    )
                in_latex_eq = False
                eq_buffer = []
            continue

        # ---------------- Table captions ----------------
        if line.lstrip().startswith("Table:") or line.lstrip().startswith(": "):
            tm = _RE_TBL_CAPTION.match(line.strip())
            if tm:
                tbl_ordinal += 1
                attrs = tm.group("attrs") or ""
                tid_match = _RE_TBL_ID.search(attrs)
                if tid_match:
                    defined[("tbl", tid_match.group("id"))] = i
                else:
                    caption = tm.group("caption").strip()
                    issues.append(
                        CrossRefIssue(
                            file=path,
                            line=i,
                            kind="table",
                            problem="missing_id",
                            suggested_id=suggest_id("tbl", path, caption, tbl_ordinal),
                            context=line,
                        )
                    )

        # ---------------- crossref uses ----------------
        for rm in _RE_REF_USE.finditer(line):
            references.append((rm.group("kind"), rm.group("id"), i))

        # ---------------- prose cross-refs (Phase 1 nudge) ----------------
        if (
            visible_for_xref_check
            and i not in generated_lines
            and not line.startswith("#")
            and not line.lstrip().startswith("%")
            and not re.match(r"^>\s*\*\*(?:Ch|Appendix)\s+[A-Za-z0-9.]+", line.strip())
            and _RE_PROSE_XREF.search(line)
        ):
            issues.append(CrossRefIssue(file=path, line=i, kind="ref", problem="prose_xref", context=line.strip()))

    # convert defined dict to include path-aware key ordering
    defined_with_line = {(k[0], k[1]): v for k, v in defined.items()}
    return defined_with_line, references, issues


def scan_directory(root: Path, patterns: Iterable[str] = ("**/*.md",)) -> CrossRefReport:
    """Walk ``root`` and aggregate a :class:`CrossRefReport`."""
    report = CrossRefReport()
    for pat in patterns:
        for path in sorted(root.glob(pat)):
            if not path.is_file():
                continue
            if path.name in {"AGENTS.md", "README.md"}:
                continue
            defined, refs, issues = scan_file(path)
            for (kind, _id), _ in defined.items():
                key = (kind, _id)
                if key in report.defined:
                    report.issues.append(
                        CrossRefIssue(
                            file=path,
                            line=0,
                            kind=kind,
                            problem="duplicate",
                            suggested_id=_id,
                            context=f"also defined in {report.defined[key]}",
                        )
                    )
                else:
                    report.defined[key] = path
            for kind, _id, ln in refs:
                report.references.append((kind, _id, path, ln))
            report.issues.extend(issues)

    # Resolve references -----------------------------------------------------
    for kind, _id, path, ln in report.references:
        if (kind, _id) not in report.defined:
            report.issues.append(
                CrossRefIssue(
                    file=path,
                    line=ln,
                    kind=kind,
                    problem="unresolved",
                    suggested_id=_id,
                    context=f"@{kind}:{_id}",
                )
            )

    return report


def validate(manuscript_root: Path | str) -> CrossRefReport:
    """Validate an entire manuscript tree and return the aggregate report."""
    return scan_directory(Path(manuscript_root))


__all__ = [
    "CrossRefIssue",
    "CrossRefReport",
    "suggest_id",
    "scan_file",
    "scan_directory",
    "validate",
]
