from sebec.palette import Color
from .base import Theme, ThemeCategory


__all__ = ["Twilight"]


Twilight = Theme(
    name="sebec-twilight",
    category=ThemeCategory.dark,
    color_sections=[
        # Base Colors
        # https://code.visualstudio.com/api/references/theme-color#base-colors
        {
            "focusBorder": Color.cerulean0,
            "foreground": Color.shine2,
            "disabledForeground": Color.twilight6,
            "widget.border": Color.sapphire1,
            # "widget.shadow": Color.twilight4,
        },
        # https://code.visualstudio.com/api/references/theme-color#editor-colors
        {
            "editor.background": Color.twilight2,
            "editor.foreground": Color.shine2,
        },
        # https://code.visualstudio.com/api/references/theme-color#editor-widget-colors
        {
            "editorWidget.background": Color.twilight4,
            "editorWidget.foreground": Color.shine3,
            # "editorWidget.resizeBorder": C.waveAqua1,
        },
        # https://code.visualstudio.com/api/references/theme-color#side-bar
        {
            "sideBar.background": Color.twilight0,
            "sideBar.foreground": Color.shine0,
            # "sideBarSectionHeader.background": Color.polarDark1,
            # "sideBarSectionHeader.foreground": Color.snowDark0,
        },
        # https://code.visualstudio.com/api/references/theme-color#panel-colors
        {
            "panel.background": Color.twilight1,
        },
        # https://code.visualstudio.com/api/references/theme-color#integrated-terminal-colors
        {
            "terminal.foreground": Color.shine1,
        },
    ]
)
