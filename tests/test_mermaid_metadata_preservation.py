"""Caption normalization must not consume following authored teaching material."""

from __future__ import annotations

import pytest

from biology.maintenance.text_normalize import normalize_text


@pytest.mark.parametrize("paragraph", [
    "**Worked Example — carbon budget:** 100 removals protect distinct areas; production is not retained storage.",
    "*Source boundary: these are stipulated synthetic inputs, not observations or a sequestration measurement.*",
])
def test_caption_does_not_own_following_authored_paragraph(paragraph: str) -> None:
    source = (
        "# Carbon accounting\n\n```mermaid\nflowchart TD\n A[Production] --> B[Respiration]\n```\n"
        "<!-- alt: Flowchart of the supplied carbon-accounting model. -->\n\n"
        "*Production is separated from respiration in the supplied carbon model.*\n\n"
        + paragraph + "\n\nA second authored explanation remains separate.\n"
    )

    normalized = normalize_text(source).text

    assert paragraph in normalized
    assert "A second authored explanation remains separate." in normalized
    assert normalize_text(normalized).text == normalized
