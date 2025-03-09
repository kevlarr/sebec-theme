from sebec.shared import TERMINAL_LIGHT
from sebec.vstheme.base.tokens import Semantic, Textmate, TokenStyle as Style
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
    terminal_colors=VscodeTerminalColors(terminal=TERMINAL_LIGHT),
    token_colors={
        Color.Sunrise0: [
            Textmate([
                "punctuation.definition",
                "punctuation.separator",              # eg. `,`, `.` in method calls, or `:` in dicts
                "punctuation.section.class.begin",    # eg. `:` after class def
                "punctuation.section.function.begin", # eg. `:` after function def
            ], name="low-contrast punctuation"),
        ],
        Color.SolarOrange0: [
            Semantic("property"),
            Semantic("property.declaration"),
        ],
        Style(Color.Cedar0, italic=True): [
            Textmate("comment"),
        ],
        Color.Sapphire1: [
            Semantic("class"),
            Semantic("function"),
            Semantic("method"),
        ],
        Style(Color.Sapphire1, bold=True): [
            Semantic("class.declaration"),
            Semantic("function.declaration"),
            Semantic("method.declaration"),
        ],
        Style(Color.Cerulean1, bold=True): [
            Textmate(["storage.type.class", "storage.type.function"]),
        ],
        Color.Cerulean1: [
            Textmate("keyword"),
        ],
        Color.SolarPurple0: [
            Textmate("constant.numeric"),
            Textmate("constant.language"),
        ],
        Style(Color.SolarPurple0, italic=True): [
            Textmate("string"),
        ],
    },
    ui_colors={
        Color.Twilight7: [
            "editor.foreground",
        ],
        Color.Sunrise5: [
            "sideBar.background",
        ],
        Color.Sunrise6: [
            "editor.background",
        ],
    },
)
