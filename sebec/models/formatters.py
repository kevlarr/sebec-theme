import re
import logging
from typing import Any

from sebec.color import Color


_logger = logging.getLogger(__name__)

_COLOR_STYLE_RGX = "^([a-zA-Z0-9]+|#[a-f0-9]{6})(\s+\d{1,2}%)?$"
_TOKEN_STYLE_RGX = f"{_COLOR_STYLE_RGX[:-1]}(\s+bold)?(\s+italic)?(\s+strikethrough)?(\s+underline)?\s*$"


def parse_color_style(value: Any) -> dict:
    assert isinstance(value, str), "must be string"

    match = re.match(_COLOR_STYLE_RGX, value)
    assert match, "invalid color"

    foreground = match.group(1)

    if alpha := match.group(2):
        return dict(
            foreground=_parse_foreground(foreground),
            alpha=float(alpha[:-1]) / 100.0
        )

    return dict(foreground=_parse_foreground(foreground))


def parse_token_color_style(value: Any) -> dict:
    assert isinstance(value, str), "must be string"

    match = re.match(_TOKEN_STYLE_RGX, value)
    assert match, "invalid token style"

    foreground, alpha, bold, italic, strikethrough, underline = match.groups()

    if alpha:
        alpha = float(alpha[:-1]) / 100.0

    return dict(
        foreground=_parse_foreground(foreground),
        alpha=alpha,
        bold=bool(bold),
        italic=bool(italic),
        strikethrough=bool(strikethrough),
        underline=bool(underline),
    )


def _parse_foreground(value: str) -> Color | str:
    if value.startswith("#"):
        _logger.warning("Found unnamed color '%s'.", value)
        return value.lower()

    return Color[value.lower()]
