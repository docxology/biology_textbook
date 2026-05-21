#!/usr/bin/env python3
"""Generate the biology textbook cover montage asset.

The cover image is intentionally text-free. Title, subtitle, and author
metadata are added by the LaTeX opening renderer so the image can be reused
across editions without embedding stale typography.
"""

from __future__ import annotations

import argparse
import math
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter


PROJECT = Path(__file__).resolve().parent.parent
DEFAULT_OUTPUT = PROJECT / "manuscript" / "assets" / "cover" / "biology_textbook_cover.png"


def _blend(a: tuple[int, int, int], b: tuple[int, int, int], t: float) -> tuple[int, int, int]:
    return (
        int(a[0] * (1 - t) + b[0] * t),
        int(a[1] * (1 - t) + b[1] * t),
        int(a[2] * (1 - t) + b[2] * t),
    )


def _draw_gradient(draw: ImageDraw.ImageDraw, width: int, height: int) -> None:
    top = (9, 29, 55)
    middle = (18, 93, 92)
    bottom = (229, 242, 221)
    for y in range(height):
        t = y / max(1, height - 1)
        if t < 0.58:
            color = _blend(top, middle, t / 0.58)
        else:
            color = _blend(middle, bottom, (t - 0.58) / 0.42)
        draw.line([(0, y), (width, y)], fill=color)


def _draw_dna(draw: ImageDraw.ImageDraw, width: int, height: int) -> None:
    left = int(width * 0.12)
    right = int(width * 0.42)
    top = int(height * 0.08)
    bottom = int(height * 0.62)
    points_a: list[tuple[float, float]] = []
    points_b: list[tuple[float, float]] = []
    for i in range(220):
        t = i / 219
        y = top + t * (bottom - top)
        phase = t * math.tau * 4.8
        center = left + (right - left) * 0.5
        amp = (right - left) * 0.33
        x1 = center + math.sin(phase) * amp
        x2 = center + math.sin(phase + math.pi) * amp
        points_a.append((x1, y))
        points_b.append((x2, y))
        if i % 10 == 0:
            color = (203, 241, 221) if i % 20 == 0 else (255, 209, 102)
            draw.line([(x1, y), (x2, y)], fill=color, width=5)
    draw.line(points_a, fill=(178, 230, 255), width=7, joint="curve")
    draw.line(points_b, fill=(247, 255, 184), width=7, joint="curve")


def _draw_cell(draw: ImageDraw.ImageDraw, width: int, height: int) -> None:
    cx, cy = int(width * 0.63), int(height * 0.37)
    rx, ry = int(width * 0.22), int(height * 0.16)
    membrane = [cx - rx, cy - ry, cx + rx, cy + ry]
    draw.ellipse(membrane, fill=(214, 247, 238, 220), outline=(6, 95, 99), width=8)
    draw.ellipse([cx - 68, cy - 58, cx + 68, cy + 58], fill=(80, 50, 120, 210), outline=(237, 225, 255), width=4)
    organelles = [
        (-130, -45, 45, 24, (255, 178, 122)),
        (105, -20, 54, 28, (93, 196, 165)),
        (-30, 82, 58, 24, (255, 222, 128)),
        (132, 65, 42, 22, (117, 187, 255)),
    ]
    for dx, dy, ox, oy, color in organelles:
        box = [cx + dx - ox, cy + dy - oy, cx + dx + ox, cy + dy + oy]
        draw.ellipse(box, fill=color, outline=(10, 68, 82), width=3)
    for k in range(12):
        angle = k * math.tau / 12
        x = cx + math.cos(angle) * rx * 0.82
        y = cy + math.sin(angle) * ry * 0.72
        draw.ellipse([x - 7, y - 7, x + 7, y + 7], fill=(11, 75, 89))


def _draw_leaf_network(draw: ImageDraw.ImageDraw, width: int, height: int) -> None:
    base_x, base_y = int(width * 0.18), int(height * 0.82)
    draw.line([(base_x, base_y), (int(width * 0.45), int(height * 0.61))], fill=(28, 91, 62), width=12)
    for i in range(7):
        t = (i + 1) / 8
        x = base_x + (int(width * 0.45) - base_x) * t
        y = base_y + (int(height * 0.61) - base_y) * t
        spread = 150 * (1 - abs(t - 0.45))
        for side in (-1, 1):
            end = (x + side * spread, y - 80 * (0.2 + t))
            draw.line([(x, y), end], fill=(58, 135, 83), width=5)
            leaf_box = [end[0] - 42, end[1] - 24, end[0] + 42, end[1] + 24]
            draw.ellipse(leaf_box, fill=(117, 184, 103), outline=(31, 95, 65), width=3)


def _draw_ecology_web(draw: ImageDraw.ImageDraw, width: int, height: int) -> None:
    nodes = [
        (0.55, 0.73, 34),
        (0.67, 0.68, 28),
        (0.76, 0.78, 24),
        (0.60, 0.88, 26),
        (0.83, 0.90, 30),
        (0.90, 0.72, 22),
    ]
    centers = [(int(width * x), int(height * y), r) for x, y, r in nodes]
    for i, (x1, y1, _r1) in enumerate(centers):
        for j, (x2, y2, _r2) in enumerate(centers):
            if i < j and (i + j) % 2 == 0:
                draw.line([(x1, y1), (x2, y2)], fill=(20, 80, 76, 155), width=4)
    colors = [(255, 211, 105), (94, 196, 165), (102, 182, 255), (184, 232, 134), (255, 161, 118), (217, 198, 255)]
    for (x, y, r), color in zip(centers, colors, strict=True):
        draw.ellipse([x - r, y - r, x + r, y + r], fill=color, outline=(11, 55, 70), width=4)


def generate_cover(path: Path, *, width: int = 2400, height: int = 1800) -> Path:
    """Generate the cover PNG and return its path."""
    path.parent.mkdir(parents=True, exist_ok=True)
    image = Image.new("RGB", (width, height), (255, 255, 255))
    draw = ImageDraw.Draw(image, "RGBA")
    _draw_gradient(draw, width, height)

    # Soft luminous field behind the biological forms.
    glow = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    glow_draw = ImageDraw.Draw(glow, "RGBA")
    upper_glow = [int(width * 0.18), int(height * 0.15), int(width * 0.95), int(height * 0.72)]
    lower_glow = [int(width * 0.02), int(height * 0.58), int(width * 0.82), int(height * 1.02)]
    glow_draw.ellipse(upper_glow, fill=(144, 233, 215, 55))
    glow_draw.ellipse(lower_glow, fill=(246, 222, 138, 50))
    image = Image.alpha_composite(image.convert("RGBA"), glow.filter(ImageFilter.GaussianBlur(70)))
    draw = ImageDraw.Draw(image, "RGBA")

    _draw_dna(draw, width, height)
    _draw_cell(draw, width, height)
    _draw_leaf_network(draw, width, height)
    _draw_ecology_web(draw, width, height)

    # Fine particulate texture, deterministic and subtle.
    for i in range(420):
        x = (i * 1543) % width
        y = (i * 2741) % height
        radius = 2 + (i % 5)
        alpha = 28 + (i % 40)
        draw.ellipse([x - radius, y - radius, x + radius, y + radius], fill=(255, 255, 255, alpha))

    image.convert("RGB").save(path, "PNG", optimize=True)
    return path


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args(argv)
    output = generate_cover(args.output)
    print(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
