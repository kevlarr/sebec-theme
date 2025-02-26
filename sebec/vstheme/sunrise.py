from sebec.palette import Color
from .base import Theme, ThemeCategory


__all__ = ["Sunrise"]


Sunrise = Theme(
    name="sebec-sunrise",
    category=ThemeCategory.light,
    color_sections=[
        {
            # "editor.background": "#f5f5f5",
            # "editor.foreground": "#333333",
            # "list.activeSelectionIconForeground": "#fff"
            "editor.background": Color.sunrise5,
            # "sideBar.background": "#E0E0D6",
            # "sideBar.foreground": Color.polar3,
            # "panel.background": "#EAE8E1",
            # "editorWidth.background": "#F6F6F3",
        },
    ],
    # token_colors=[],
)
