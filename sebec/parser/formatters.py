import re
import logging

from sebec.color import Color


_LOGGER = logging.getLogger(__name__)


_COLOR_STYLE_RGX = "^([a-zA-Z0-9]+|#[a-f0-9]{6})(\s+alpha=[\d\.]+)?$"
_TOKEN_STYLE_RGX = f"{_COLOR_STYLE_RGX[:-1]}(\s+bold)?(\s+italic)?(\s+strikethrough)?(\s+underline)?\s*$"


def parse_color_style(value: str) -> dict:
    match = re.match(_COLOR_STYLE_RGX, value)
    assert match, "invalid color"

    foreground = match.group(1)

    if alpha := match.group(2):
        return dict(
            foreground=_parse_foreground(foreground),
            alpha=_clamp_alpha(float(alpha.split("=")[1])),
        )

    return dict(foreground=_parse_foreground(foreground))


def parse_token_style(value: str) -> dict:
    match = re.match(_TOKEN_STYLE_RGX, value)
    assert match, "invalid token style"

    foreground, alpha, bold, italic, strikethrough, underline = match.groups()

    if alpha:
        alpha = alpha.split("=")[1]

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
        _LOGGER.warning("Found unnamed color '%s'.", value)
        return value.lower()

    return Color[value.lower()]


def _clamp_alpha(alpha: float) -> float:
    # Restricts alpha to [0.0, 1.0]
    return max(0.0, min(1.0, alpha))
