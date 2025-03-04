from sebec.shared import TERMINAL_LIGHT
from sebec.terminal import VscodeTerminalColors
from sebec.vstheme.base import Color, Theme, ThemeCategory


__all__ = ["Sunrise"]


Sunrise = Theme(
    name="Sebec Sunrise",
    category=ThemeCategory.light,

    # "editor.background": "#f5f5f5",
    # "editor.foreground": "#333333",
    # "list.activeSelectionIconForeground": "#fff"
    # "sideBar.background": "#E0E0D6",
    # "sideBar.foreground": Color.polar3,
    # "panel.background": "#EAE8E1",
    # "editorWidth.background": "#F6F6F3",
    semantic_tokens={},
    terminal_colors=VscodeTerminalColors(terminal=TERMINAL_LIGHT),
    textmate_tokens={},
    ui_colors={
        Color.Sunrise5: [
            "editor.background",
        ]
    },
)
