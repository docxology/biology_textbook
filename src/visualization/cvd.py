"""Colour-vision-deficiency (CVD)–aware palette defaults for matplotlib figures.

Implements the intent of ``accessibility.color_blindness_safe: true`` in
``manuscript/config.yaml``: prefer distinct hues (not red–green–only) and
encode differences with line style or edge contrast where a second channel
helps (e.g. Punnett cells).

Reference: Paul Tol–style distinct hues (approximate) suitable for line and
bar work; not a replacement for user testing in print.
"""

from __future__ import annotations

# Primary series (line plots): blue and orange are distinguishable for common CVD
BLUE = "#0077bb"
ORANGE = "#ee7733"
TEAL = "#009988"
PURPLE = "#7b4ea3"
GRAY = "#666666"

SERIES2: tuple[str, str] = (BLUE, ORANGE)
SERIES3: tuple[str, str, str] = (BLUE, ORANGE, TEAL)
SERIES4: tuple[str, str, str, str] = (BLUE, ORANGE, TEAL, PURPLE)

# Punnett: avoid green vs red; use cool vs warm with visible edges
PUNNETT_DOMINANT = "#6BAED6"
PUNNETT_RECESSIVE = "#FDB863"

# Dichotomous bar (e.g. positive/negative Nernst)
BAR_POS = BLUE
BAR_NEG = ORANGE
