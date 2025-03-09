from sebec.shared import TERMINAL_DARK
from sebec.terminal import VscodeTerminalColors
from sebec.vstheme.base import Theme, ThemeCategory
from .tokens import COLOR_TOKENS
from .ui import UI_COLORS


__all__ = ["Twilight"]


Twilight = Theme(
    name="Sebec Twilight",
    category=ThemeCategory.dark,
    terminal_colors=VscodeTerminalColors(terminal=TERMINAL_DARK),
    token_colors=COLOR_TOKENS,
    ui_colors=UI_COLORS,
)
