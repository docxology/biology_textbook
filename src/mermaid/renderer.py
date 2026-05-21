"""Mermaid diagram renderer.

Converts Mermaid source (.mmd) to PNG via the Mermaid CLI (mmdc).
If mmdc is not installed, writes the raw .mmd source as a graceful fallback.

Usage:
    from mermaid.renderer import MermaidRenderer
    renderer = MermaidRenderer(output_dir=Path("output/figures/mermaid"))
    png_path = renderer.render("my_diagram", mermaid_source)
"""

from __future__ import annotations

import subprocess  # nosec B404 - wrapper invokes the local Mermaid CLI with fixed arguments.
import shutil
import os
from dataclasses import dataclass
from pathlib import Path
from tempfile import NamedTemporaryFile
from typing import Optional

from infrastructure.core.logging.utils import get_logger

logger = get_logger(__name__)


def _write_text_atomic(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp_path: Path | None = None
    try:
        with NamedTemporaryFile(
            "w",
            encoding="utf-8",
            dir=path.parent,
            prefix=f".{path.name}.",
            suffix=".tmp",
            delete=False,
        ) as handle:
            handle.write(text)
            tmp_path = Path(handle.name)
        os.replace(tmp_path, path)
    finally:
        if tmp_path is not None and tmp_path.exists():
            tmp_path.unlink()


def _find_puppeteer_config() -> Optional[Path]:
    """Walk up from this file's directory to find a .puppeteer.json config.

    Returns the first .puppeteer.json found in the directory tree, or None.
    This allows the renderer to point mmdc at a system Chrome installation
    rather than requiring the puppeteer browser download.
    """
    candidate = Path(__file__).resolve()
    for _ in range(10):  # search up to 10 levels
        candidate = candidate.parent
        config = candidate / ".puppeteer.json"
        if config.exists():
            return config
    return None


@dataclass
class MermaidDiagram:
    """A Mermaid diagram with its source and an optional label."""

    name: str  # stem used for output filename
    source: str  # Mermaid diagram source (.mmd content)
    title: str = ""  # human-readable title for embedding

    def render(
        self,
        output_dir: Path,
        width: int = 1200,
        height: int = 800,
        background_color: str = "white",
    ) -> Path:
        """Render this diagram to PNG using the module-level renderer.

        Args:
            output_dir: Directory to write the PNG (or .mmd) into.
            width: Output image width in pixels.
            height: Output image height in pixels.
            background_color: Background colour (hex or name).

        Returns:
            Path to the generated PNG (or .mmd fallback).
        """
        renderer = MermaidRenderer(output_dir=output_dir)
        return renderer.render(self.name, self.source, width=width, height=height, background_color=background_color)


class MermaidRenderer:
    """Renders Mermaid source to PNG via mmdc (Mermaid CLI).

    If mmdc is not available, falls back to writing .mmd source files unless
    ``strict_png`` is enabled for publication build paths.
    """

    def __init__(self, output_dir: Path, *, strict_png: bool = False) -> None:
        """Initialise renderer with an output directory.

        Args:
            output_dir: Directory for output PNG / .mmd files.
            strict_png: Require Mermaid CLI output to be a PNG instead of
                accepting a ``.mmd`` fallback.
        """
        self.output_dir = Path(output_dir)
        self.strict_png = strict_png
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self._mmdc_available: Optional[bool] = None

    def _check_mmdc(self) -> bool:
        if self._mmdc_available is None:
            self._mmdc_available = shutil.which("mmdc") is not None
            if self._mmdc_available:
                logger.info("mmdc found — will render Mermaid diagrams as PNG.")
            else:
                logger.warning("mmdc not found — falling back to .mmd source output.")
        return self._mmdc_available

    def render(
        self,
        name: str,
        source: str,
        width: int = 1200,
        height: int = 800,
        background_color: str = "white",
    ) -> Path:
        """Render Mermaid source to PNG or fallback .mmd file.

        Args:
            name: Output file stem (no extension).
            source: Mermaid diagram source code.
            width: PNG width in pixels (only used if mmdc available).
            height: PNG height in pixels.
            background_color: Background color.

        Returns:
            Path to the generated file (.png or .mmd).
        """
        if not name:
            raise ValueError("Diagram name must not be empty.")
        if not source.strip():
            raise ValueError(f"Mermaid source for '{name}' must not be empty.")

        if self._check_mmdc():
            return self._render_with_mmdc(name, source, width, height, background_color)
        if self.strict_png:
            raise RuntimeError("Mermaid CLI 'mmdc' is required when strict_png=True")
        return self._write_mmd_source(name, source)

    def _write_mmd_source(self, name: str, source: str) -> Path:
        mmd_path = self.output_dir / f"{name}.mmd"
        _write_text_atomic(mmd_path, source)
        logger.debug(f"Wrote Mermaid source: {mmd_path}")
        return mmd_path

    def _render_with_mmdc(
        self,
        name: str,
        source: str,
        width: int,
        height: int,
        background_color: str,
    ) -> Path:
        """Render via mmdc subprocess to PNG."""
        # Write temporary .mmd input
        mmd_path = self.output_dir / f"{name}.mmd"
        _write_text_atomic(mmd_path, source)

        png_path = self.output_dir / f"{name}.png"

        # Locate puppeteer config (project-level .puppeteer.json points to system Chrome)
        puppeteer_config = _find_puppeteer_config()

        cmd = [
            "mmdc",
            "--input",
            str(mmd_path),
            "--output",
            str(png_path),
            "--width",
            str(width),
            "--height",
            str(height),
            "--backgroundColor",
            background_color,
            "--quiet",
        ]
        if puppeteer_config:
            cmd += ["--puppeteerConfigFile", str(puppeteer_config)]

        try:
            result = subprocess.run(  # nosec B603 - command is fixed; only local temp/output paths vary.
                cmd,
                capture_output=True,
                text=True,
                timeout=60,
            )
            if result.returncode != 0:
                message = (
                    f"mmdc returned exit code {result.returncode} for '{name}': "
                    f"{result.stderr[:200]}"
                )
                if self.strict_png:
                    raise RuntimeError(message)
                logger.warning(
                    f"{message}. Falling back to .mmd."
                )
                return mmd_path
            logger.info(f"Rendered Mermaid PNG: {png_path}")
            return png_path
        except subprocess.TimeoutExpired:
            if self.strict_png:
                raise RuntimeError(f"mmdc timed out for '{name}'") from None
            logger.warning(f"mmdc timed out for '{name}'. Falling back to .mmd.")
            return mmd_path
        except OSError as e:
            if self.strict_png:
                raise RuntimeError(f"mmdc OSError for '{name}': {e}") from e
            logger.warning(f"mmdc OSError for '{name}': {e}. Falling back to .mmd.")
            return mmd_path

    def render_all(self, diagrams: list[MermaidDiagram], **kwargs) -> list[Path]:
        """Render a list of MermaidDiagram objects.

        Args:
            diagrams: List of MermaidDiagram objects.
            **kwargs: Passed to each render() call.

        Returns:
            List of output paths (PNG or .mmd).
        """
        paths = []
        failures: list[str] = []
        for diagram in diagrams:
            try:
                path = self.render(diagram.name, diagram.source, **kwargs)
                paths.append(path)
            except (OSError, ValueError) as e:
                logger.error(f"Failed to render '{diagram.name}': {e}")
                failures.append(f"{diagram.name}: {e}")
        logger.info(f"Rendered {len(paths)}/{len(diagrams)} Mermaid diagrams.")
        if failures:
            raise RuntimeError("Mermaid rendering failed for " + "; ".join(failures))
        return paths
