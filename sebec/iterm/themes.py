from sebec.color import Color
from sebec.terminal import ItermColors
from sebec.shared import TERMINAL_DARK, TERMINAL_LIGHT


ITERM_DARK = ItermColors(
    terminal=TERMINAL_DARK,
    badge_color=Color.Cerulean0,
    bold_color=Color.Shine5,
    cursor_guide_color=Color.Twilight4,
    link_color=Color.Cerulean1,
    tab_color=Color.Twilight2,
    underline_color=Color.Cerulean0,
)

ITERM_LIGHT = ItermColors(
    terminal=TERMINAL_LIGHT,
    badge_color=Color.Cerulean0,
    bold_color=Color.Twilight2,
    cursor_guide_color=Color.Sunrise6,
    link_color=Color.Cerulean0,
    tab_color=Color.Sunrise7,
    underline_color=Color.Cerulean0,
)
