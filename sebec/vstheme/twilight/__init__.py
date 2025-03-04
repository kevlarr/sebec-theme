from sebec.shared import TERMINAL_DARK
from sebec.terminal import VscodeTerminalColors
from sebec.vstheme.base import Theme, ThemeCategory
from .semantic import SEMANTIC_TOKENS
from .textmate import TEXTMATE_TOKENS
from .ui import UI_COLORS


__all__ = ["Twilight"]


Twilight = Theme(
    name="Sebec Twilight",
    category=ThemeCategory.dark,
    semantic_tokens=SEMANTIC_TOKENS,
    terminal_colors=VscodeTerminalColors(terminal=TERMINAL_DARK),
    textmate_tokens=TEXTMATE_TOKENS,
    ui_colors=UI_COLORS,
)
