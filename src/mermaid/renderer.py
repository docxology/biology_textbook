"""Mermaid diagram renderer.

Converts Mermaid source (.mmd) to PNG via the Mermaid CLI (mmdc).
If mmdc is not installed, writes the raw .mmd source as a graceful fallback.

Usage:
    from mermaid.renderer import MermaidRenderer
    renderer = MermaidRenderer(output_dir=Path("output/figures/mermaid"))
    png_path = renderer.render("my_diagram", mermaid_source)
"""

from __future__ import annotations

import os
import shutil
import subprocess  # nosec B404 - wrapper invokes the local Mermaid CLI with fixed arguments.
import tempfile
from dataclasses import dataclass
from pathlib import Path

from PIL import Image

from textbook_io import write_text_atomic
from textbook_logging import get_logger
from textbook_visuals import pad_png_to_square

logger = get_logger(__name__)

def _find_puppeteer_config(project_root: Path | None = None) -> Path | None:
    """Use only this project's config, never an unrelated ancestor's config."""
    root = project_root if project_root is not None else Path(__file__).resolve().parents[2]
    config = root / ".puppeteer.json"
    return config if config.is_file() else None


@dataclass
class MermaidDiagram:
    """A Mermaid diagram with its source and an optional label."""

    name: str  # stem used for output filename
    source: str  # Mermaid diagram source (.mmd content)
    title: str = ""  # human-readable title for embedding

    def render(
        self,
        output_dir: Path,
        size: int = 1200,
        background_color: str = "white",
        square: bool = True,
    ) -> Path:
        """Render this diagram to PNG using the module-level renderer.

        Args:
            output_dir: Directory to write the PNG (or .mmd) into.
            size: Maximum PNG dimension in CSS pixels (Mermaid CLI 12.2).
            background_color: Background color (hex or name).
            square: Pad PNG output to a square canvas when rendering succeeds.

        Returns:
            Path to the generated PNG (or .mmd fallback).
        """
        renderer = MermaidRenderer(output_dir=output_dir)
        return renderer.render(
            self.name,
            self.source,
            size=size,
            background_color=background_color,
            square=square,
        )


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
        self._mmdc_available: bool | None = None

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
        size: int = 1200,
        background_color: str = "white",
        square: bool = True,
    ) -> Path:
        """Render Mermaid source to PNG or fallback .mmd file.

        Args:
            name: Output file stem (no extension).
            source: Mermaid diagram source code.
            size: Positive maximum PNG dimension in CSS pixels.
            background_color: Background color.
            square: Pad PNG output to a square canvas when rendering succeeds.

        Returns:
            Path to the generated file (.png or .mmd).

        Raises:
            TypeError: If size is not an integer, including bool.
            ValueError: If size is nonpositive or a name/source is invalid.
        """
        if not name:
            raise ValueError("Diagram name must not be empty.")
        if Path(name).name != name or name in {".", ".."} or "\\" in name:
            raise ValueError("Diagram name must be a single portable filename stem.")
        if not source.strip():
            raise ValueError(f"Mermaid source for '{name}' must not be empty.")
        if isinstance(size, bool) or not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size <= 0:
            raise ValueError("size must be positive")

        if self._check_mmdc():
            return self._render_with_mmdc(name, source, size, background_color, square)
        if self.strict_png:
            raise RuntimeError("Mermaid CLI 'mmdc' is required when strict_png=True")
        return self._write_mmd_source(name, source)

    def _write_mmd_source(self, name: str, source: str) -> Path:
        mmd_path = self.output_dir / f"{name}.mmd"
        write_text_atomic(mmd_path, source)
        logger.debug(f"Wrote Mermaid source: {mmd_path}")
        return mmd_path

    def _render_with_mmdc(
        self,
        name: str,
        source: str,
        size: int,
        background_color: str,
        square: bool,
    ) -> Path:
        """Render via mmdc subprocess to PNG."""
        # Write temporary .mmd input
        mmd_path = self.output_dir / f"{name}.mmd"
        write_text_atomic(mmd_path, source)

        png_path = self.output_dir / f"{name}.png"
        fd, temporary_name = tempfile.mkstemp(prefix=f".{name}-", suffix=".png", dir=self.output_dir)
        os.close(fd)
        temporary_png = Path(temporary_name)

        # Locate puppeteer config (project-level .puppeteer.json points to system Chrome)
        puppeteer_config = _find_puppeteer_config()

        cmd = [
            "mmdc",
            "--input",
            str(mmd_path),
            "--output",
            str(temporary_png),
            "--size",
            str(size),
            "--backgroundColor",
            background_color,
            "--quiet",
        ]
        if puppeteer_config:
            cmd += ["--puppeteerConfigFile", str(puppeteer_config)]

        try:
            result = subprocess.run(  # nosec B603 - command is fixed; only local temp/output paths vary.
                cmd,
                check=False,
                capture_output=True,
                text=True,
                timeout=60,
                stdin=subprocess.DEVNULL,
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
            with Image.open(temporary_png) as image:
                if image.format != "PNG":
                    raise OSError("Mermaid output is not PNG")
                image.verify()
            with Image.open(temporary_png) as image:
                image.load()
            if square:
                pad_png_to_square(temporary_png)
            temporary_png.replace(png_path)
            logger.info(f"Rendered Mermaid PNG: {png_path}")
            return png_path
        except subprocess.TimeoutExpired:
            if self.strict_png:
                raise RuntimeError(f"mmdc timed out for '{name}'") from None
            logger.warning(f"mmdc timed out for '{name}'. Falling back to .mmd.")
            return mmd_path
        except (OSError, SyntaxError, ValueError) as e:
            if self.strict_png:
                raise RuntimeError(f"mmdc OSError for '{name}': {e}") from e
            logger.warning(f"mmdc OSError for '{name}': {e}. Falling back to .mmd.")
            return mmd_path
        finally:
            temporary_png.unlink(missing_ok=True)

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
            except (OSError, TypeError, ValueError) as e:
                logger.error(f"Failed to render '{diagram.name}': {e}")
                failures.append(f"{diagram.name}: {e}")
        logger.info(f"Rendered {len(paths)}/{len(diagrams)} Mermaid diagrams.")
        if failures:
            raise RuntimeError("Mermaid rendering failed for " + "; ".join(failures))
        return paths
