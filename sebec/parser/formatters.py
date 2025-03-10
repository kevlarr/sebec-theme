import re

from sebec.color import Color


COLOR_STYLE_RGX = "^([a-zA-Z0-9]+|#[a-f0-9]{6})(\s+alpha=[\d\.]+)?$"
TOKEN_STYLE_RGX = f"{COLOR_STYLE_RGX[:-1]}(\s+bold)?(\s+italic)?(\s+strikethrough)?(\s+underline)?\s*$"


def parse_color_style(value):
    match = re.match(COLOR_STYLE_RGX, value)
    assert match, "invalid color"

    foreground = Color[match.group(1).lower()]

    if alpha := match.group(2):
        return dict(
            foreground=foreground,
            alpha=_clamp_alpha(float(alpha.split("=")[1])),
        )

    return dict(foreground=foreground)


def parse_token_style(value):
    match = re.match(TOKEN_STYLE_RGX, value)
    assert match, "invalid token style"

    foreground, alpha, bold, italic, strikethrough, underline = match.groups()

    if alpha:
        alpha = alpha.split("=")[1]

    return dict(
        foreground=Color[foreground.lower()],
        alpha=alpha,
        bold=bool(bold),
        italic=bool(italic),
        strikethrough=bool(strikethrough),
        underline=bool(underline),
    )

def _clamp_alpha(alpha: float) -> float:
    # Restricts alpha to [0.0, 1.0]
    return max(0.0, min(1.0, alpha))
