"""Publication-readiness audit gate for the biology textbook.

The default check runs project-local source, assessment, visual, lint, type,
and manuscript gates. ``--full`` additionally tests with coverage, hydrates
the live manuscript, renders through the installed template library without
running template-root scripts, and checks the resulting PDF log.

The thin CLI is at ``scripts/audit_publication_readiness.py``.
"""

from __future__ import annotations

import json
import os
import platform
import subprocess
import sys
import time
from collections.abc import Callable, Sequence
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path
from threading import Lock
from typing import TypeVar

from biology.maintenance.models import PROJECT
from textbook_io import write_text_atomic
from textbook_paths import (
    discover_template_root,
    ensure_project_paths,
    require_project_output_directory,
)

MANUSCRIPT = PROJECT / "docs" / "manuscript"
PROJECT_PDF_LOG = PROJECT / "output" / "pdf" / "_combined_manuscript.log"
DEFAULT_REVIEW_ARTIFACT_DIR = PROJECT / "output" / "publication_readiness"


@dataclass(frozen=True)
class CommandStep:
    """One subprocess-backed audit step."""

    name: str
    command: tuple[str, ...]
    cwd: Path
    full_only: bool = False
    depends_on: frozenset[str] = frozenset()


@dataclass(frozen=True)
class PythonStep:
    """One in-process audit step."""

    name: str
    check: Callable[[], list[str]]
    full_only: bool = False
    depends_on: frozenset[str] = frozenset()


_StepT = TypeVar("_StepT", bound=CommandStep | PythonStep)


def build_command_steps(*, full: bool, artifact_dir: Path | None = None) -> list[CommandStep]:
    """Return subprocess checks for the selected audit depth."""

    py = sys.executable
    review_artifacts = PROJECT / "output" if full else (artifact_dir or DEFAULT_REVIEW_ARTIFACT_DIR)
    review_figures = review_artifacts / "figures"
    review_mermaid = review_figures / "mermaid"
    review_manifest = review_figures / "visual_manifest.json"
    steps = [
        CommandStep(
            "quality-audit",
            (py, "scripts/audit_textbook_quality.py", "--check", "--max-advisories", "0"),
            PROJECT,
        ),
        CommandStep("current-claims", (py, "scripts/audit_current_claims.py", "--check"), PROJECT),
        CommandStep("assessment-sync", (py, "scripts/sync_assessment_metadata.py", "--check"), PROJECT),
        CommandStep("mermaid-alt-sync", (py, "scripts/add_mermaid_alt_text.py", "--check"), PROJECT),
        CommandStep(
            "figures-strict",
            (py, "scripts/generate_figures.py", "--output-dir", str(review_figures)),
            PROJECT,
        ),
        CommandStep(
            "diagrams-strict",
            (py, "scripts/generate_diagrams.py", "--strict-png", "--output-dir", str(review_mermaid)),
            PROJECT,
            depends_on=frozenset({"figures-strict"}),
        ),
        CommandStep(
            "visual-contracts",
            (
                py,
                "scripts/audit_visual_contracts.py",
                "--figures-root",
                str(review_figures),
                "--output",
                str(review_manifest),
                *(("--render-inline",) if not full else ()),
                "--check",
            ),
            PROJECT,
            depends_on=frozenset({"render"} if full else {"diagrams-strict"}),
        ),
        CommandStep(
            "ruff",
            (py, "-m", "ruff", "check", "src", "scripts", "tests", "--ignore", "E402"),
            PROJECT,
        ),
        CommandStep("mypy", (py, "-m", "mypy", "src", "scripts", "tests"), PROJECT),
        CommandStep(
            "project-tests-gate",
            (
                py,
                "-m",
                "pytest",
                "tests",
                "--cov=src",
                "--cov-fail-under=90",
                "--cov-report=term-missing",
                "-q",
            ),
            PROJECT,
            full_only=True,
            depends_on=frozenset({"quality-audit", "current-claims", "assessment-sync"}),
        ),
        CommandStep(
            "analysis",
            (py, "scripts/biology_analysis.py"),
            PROJECT,
            full_only=True,
            depends_on=frozenset({"project-tests-gate", "diagrams-strict"}),
        ),
        CommandStep(
            "render",
            (py, "scripts/render_textbook.py"),
            PROJECT,
            full_only=True,
            depends_on=frozenset({"analysis"}),
        ),
        CommandStep(
            "pdf-log",
            (
                sys.executable,
                "scripts/check_pdf_log.py",
                str(PROJECT_PDF_LOG),
                "--max-overfull-pt",
                "50",
            ),
            PROJECT,
            full_only=True,
            depends_on=frozenset({"render"}),
        ),
    ]
    return [step for step in steps if full or not step.full_only]


def build_python_steps(*, full: bool, artifact_dir: Path | None = None) -> list[PythonStep]:
    """Return in-process checks for the selected audit depth."""

    review_artifacts = PROJECT / "output" if full else (artifact_dir or DEFAULT_REVIEW_ARTIFACT_DIR)
    steps = [
        PythonStep("recursive-markdown", lambda: check_recursive_markdown(review_artifacts / "figures"), depends_on=frozenset({"visual-contracts"})),
        PythonStep("recursive-prerender", check_recursive_prerender, depends_on=frozenset({"visual-contracts"})),
        PythonStep("artifact-counts", lambda: check_artifact_counts(review_artifacts), depends_on=frozenset({"visual-contracts"})),
        PythonStep("tracked-artifact-hygiene", check_tracked_artifact_hygiene),
    ]
    return [step for step in steps if full or not step.full_only]


def run_command_step(step: CommandStep) -> int:
    """Run one command step and return its exit code."""
    print(f"\n== {step.name} ==")
    print(f"$ {' '.join(step.command)}")
    try:
        result = subprocess.run(
            step.command, cwd=step.cwd, check=False, stdin=subprocess.DEVNULL,
            env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"},
        )
    except OSError as exc:
        print(f"{step.name}: FAIL ({exc})")
        return 1
    if result.returncode:
        print(f"{step.name}: FAIL ({result.returncode})")
    else:
        print(f"{step.name}: PASS")
    return result.returncode


def run_python_step(step: PythonStep) -> int:
    """Run one Python check and return its exit code."""
    print(f"\n== {step.name} ==")
    issues = step.check()
    for issue in issues:
        print(issue)
    if issues:
        print(f"{step.name}: FAIL ({len(issues)} issue(s))")
        return 1
    print(f"{step.name}: PASS")
    return 0


def _recursive_manuscript_markdown() -> list[str]:
    from biology.maintenance.manuscript_walker import manuscript_markdown_files

    return [str(path) for path in manuscript_markdown_files(MANUSCRIPT, project_root=PROJECT) if path.name != "preamble.md"]


def check_recursive_markdown(figures_root: Path | None = None) -> list[str]:
    """Run infrastructure markdown validators over the recursive manuscript set."""
    if discover_template_root(PROJECT) is None:
        return ["template infrastructure not found; set BIOLOGY_TEXTBOOK_TEMPLATE_ROOT"]

    from infrastructure.validation.content.markdown_validator import (  # type: ignore[import-not-found]
        collect_symbols,
        validate_citations,
        validate_images,
        validate_math,
        validate_pandoc_pitfalls,
        validate_refs,
    )

    md_paths = _recursive_manuscript_markdown()
    labels, anchors = collect_symbols(md_paths)
    problems = []
    figures = figures_root or PROJECT / "output" / "figures"
    problems += validate_images(md_paths, PROJECT, extra_search_dirs=[figures, figures / "mermaid"])
    problems += validate_refs(md_paths, PROJECT, labels, anchors)
    problems += validate_math(md_paths, PROJECT)
    problems += validate_pandoc_pitfalls(md_paths, PROJECT)
    problems += validate_citations(md_paths, PROJECT, bib_file=MANUSCRIPT / "references.bib")
    formatted: list[str] = []
    for problem in problems:
        severity = getattr(problem.severity, "name", str(problem.severity))
        code = getattr(problem.code, "value", str(problem.code))
        formatted.append(f"{severity} {code} [{problem.file_path}] {problem.message}")
    return formatted


def check_recursive_prerender() -> list[str]:
    """Run the render-blocking source markdown gate over recursive manuscript files."""
    if discover_template_root(PROJECT) is None:
        return ["template infrastructure not found; set BIOLOGY_TEXTBOOK_TEMPLATE_ROOT"]

    from infrastructure.core.exceptions import RenderingError  # type: ignore[import-not-found]
    from infrastructure.validation.content.prerender import prevalidate_for_render  # type: ignore[import-not-found]

    try:
        prevalidate_for_render(
            _recursive_manuscript_markdown(),
            repo_root=PROJECT,
            bib_file=MANUSCRIPT / "references.bib",
        )
    except RenderingError as exc:
        return str(exc).splitlines()
    return []


def check_artifact_counts(artifact_dir: Path | None = None) -> list[str]:
    """Verify strict generation produced enough figure and Mermaid PNG artifacts."""
    from mermaid import ALL_BIOLOGY_DIAGRAMS
    from visualization import ALL_FIGURE_GENERATORS

    issues: list[str] = []
    figures_dir = (artifact_dir or DEFAULT_REVIEW_ARTIFACT_DIR) / "figures"
    mermaid_dir = figures_dir / "mermaid"
    figure_pngs = [path for path in figures_dir.glob("*.png") if path.is_file()]
    mermaid_pngs = [path for path in mermaid_dir.glob("*.png") if path.is_file()]

    expected_figures = len(ALL_FIGURE_GENERATORS)
    expected_diagrams = len(ALL_BIOLOGY_DIAGRAMS)
    if len(figure_pngs) < expected_figures:
        issues.append(f"expected at least {expected_figures} figure PNGs, found {len(figure_pngs)}")
    if len(mermaid_pngs) < expected_diagrams:
        issues.append(f"expected at least {expected_diagrams} Mermaid PNGs, found {len(mermaid_pngs)}")
    return issues


def check_tracked_artifact_hygiene() -> list[str]:
    """Fail if this project's index tracks generated/cache artifacts."""
    from biology.pipeline.release_assets import _git

    try:
        tracked = _git(PROJECT, "ls-files", "-z", "--", ".")
    except subprocess.CalledProcessError as exc:
        return [(exc.stderr or "").strip() or "git ls-files failed"]

    forbidden = (
        "/output/",
        "/.mypy_cache/",
        "/__pycache__/",
        ".pyc",
        ".pyo",
        ".pytest_cache/",
    )
    offenders = [
        path
        for path in tracked.split("\0")
        if any(fragment in f"/{path}" for fragment in forbidden)
    ]
    return [f"tracked generated/cache artifact: {path}" for path in offenders]




def _run_step_batches(
    steps: Sequence[_StepT],
    runner: Callable[[_StepT], int],
    *,
    max_workers: int,
    outcomes: dict[str, int] | None = None,
) -> int:
    """Run independent peers, but never consume a failed prerequisite's outputs."""
    names = {step.name for step in steps}
    if len(names) != len(steps):
        raise ValueError("publication gate step names must be unique")
    for step in steps:
        unknown = step.depends_on - names
        if unknown:
            raise ValueError(f"{step.name}: unknown dependencies {sorted(unknown)}")
    remaining = list(steps)
    outcomes = {} if outcomes is None else outcomes
    while remaining:
        ready = [step for step in remaining if step.depends_on.issubset(outcomes)]
        if not ready:
            pending = ", ".join(step.name for step in remaining)
            raise RuntimeError(f"publication gate dependency deadlock among: {pending}")
        runnable: list[_StepT] = []
        for step in ready:
            failed = sorted(name for name in step.depends_on if outcomes[name])
            if failed:
                print(f"{step.name}: BLOCKED (failed dependencies: {', '.join(failed)})")
                outcomes[step.name] = 1
            else:
                runnable.append(step)
        if max_workers <= 1:
            for step in runnable:
                outcomes[step.name] = runner(step)
        elif runnable:
            with ThreadPoolExecutor(max_workers=min(max_workers, len(runnable))) as pool:
                futures = {pool.submit(runner, step): step for step in runnable}
                for future in as_completed(futures):
                    outcomes[futures[future].name] = future.result()
        remaining = [step for step in remaining if step.name not in outcomes]
    return sum(bool(status) for status in outcomes.values())


def run_publication_gate(*, full: bool, artifact_dir: Path | None = None, max_workers: int = 1) -> int:
    """Run the graph and atomically replace evidence, never retaining an old PASS."""
    review = require_project_output_directory(PROJECT, artifact_dir or DEFAULT_REVIEW_ARTIFACT_DIR)
    receipt_path = review / "receipt.json"
    if receipt_path.is_symlink() or (receipt_path.exists() and (not receipt_path.is_file() or receipt_path.stat().st_nlink != 1)):
        raise ValueError("Publication receipts must be independent regular files")
    evidence: dict[str, object] = {
        "schema": 1, "full": full, "status": "running", "failures": None,
        "started_at": datetime.now(UTC).isoformat(),
    }

    def persist() -> None:
        require_project_output_directory(PROJECT, review)
        write_text_atomic(receipt_path, json.dumps(evidence, indent=2) + "\n")

    # Invalidate old success before Git, renderer reads or graph construction.
    persist()
    observations: dict[str, dict[str, object]] = {}
    observation_lock = Lock()

    def run(step: CommandStep | PythonStep) -> int:
        started = time.monotonic()
        status = run_command_step(step) if isinstance(step, CommandStep) else run_python_step(step)
        record: dict[str, object] = {"returncode": status, "seconds": time.monotonic() - started}
        if isinstance(step, CommandStep):
            record["command"] = list(step.command)
            record["cwd"] = str(step.cwd)
        with observation_lock:
            observations[step.name] = record
        return status

    outcomes: dict[str, int] = {}
    previous_bytecode = sys.dont_write_bytecode
    sys.dont_write_bytecode = True
    try:
        ensure_project_paths()
        from biology.pipeline.release_assets import (
            _renderer_sources,
            sha256_file,
            source_state,
        )

        renderer_root = discover_template_root(PROJECT)
        artifacts_root = PROJECT / "output" if full else review
        for directory in (artifacts_root, artifacts_root / "figures", artifacts_root / "figures/mermaid", PROJECT / "output/pdf"):
            require_project_output_directory(PROJECT, directory)
        before = source_state(PROJECT)
        if renderer_root is None:
            raise ValueError("Publication requires a verified frozen renderer snapshot")
        _, renderer_members = _renderer_sources(renderer_root)
        renderer_before = renderer_members[-1][2]
        evidence.update(
            source_before=before, renderer_manifest_before=renderer_before,
            runtime={
                "python": sys.version, "platform": platform.platform(),
                "source_date_epoch": os.environ.get("SOURCE_DATE_EPOCH"),
                "template_deterministic": os.environ.get("TEMPLATE_DETERMINISTIC"),
            },
        )
        persist()
        steps: list[CommandStep | PythonStep] = [
            *build_command_steps(full=full, artifact_dir=review),
            *build_python_steps(full=full, artifact_dir=review),
        ]
        failures = _run_step_batches(steps, run, max_workers=max_workers, outcomes=outcomes)
        after = source_state(PROJECT)
        _, renderer_members = _renderer_sources(renderer_root)
        renderer_after = renderer_members[-1][2]
        if renderer_before != renderer_after:
            print("renderer-binding: FAIL (frozen renderer changed during validation)")
            failures += 1
        if before != after:
            print("source-binding: FAIL (Git source state changed during validation)")
            failures += 1
        artifacts = {}
        if full:
            for relative in ("output/pdf/biology_textbook_combined.pdf", "output/figures/visual_manifest.json"):
                path = PROJECT / relative
                require_project_output_directory(PROJECT, path.parent)
                if path.is_file():
                    artifacts[relative] = sha256_file(path)
        evidence.update(
            status="completed", failures=failures, source_after=after,
            renderer_manifest_after=renderer_after,
            finished_at=datetime.now(UTC).isoformat(), artifacts=artifacts,
            steps=[{
                "name": step.name, "depends_on": sorted(step.depends_on),
                **observations.get(step.name, {"returncode": outcomes[step.name], "blocked": True}),
            } for step in steps],
        )
        persist()
        return failures
    except BaseException as exc:
        evidence.update(status="interrupted", failures=1, error_type=type(exc).__name__)
        persist()
        raise
    finally:
        sys.dont_write_bytecode = previous_bytecode


__all__ = [
    "DEFAULT_REVIEW_ARTIFACT_DIR",
    "MANUSCRIPT",
    "PROJECT_PDF_LOG",
    "CommandStep",
    "PythonStep",
    "build_command_steps",
    "build_python_steps",
    "check_artifact_counts",
    "check_recursive_markdown",
    "check_recursive_prerender",
    "check_tracked_artifact_hygiene",
    "run_command_step",
    "run_publication_gate",
    "run_python_step",
]
