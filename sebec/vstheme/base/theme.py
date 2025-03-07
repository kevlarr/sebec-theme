import dataclasses
import enum
import json
from pathlib import Path

from sebec.color import Color, ColorStyle
from sebec.terminal import TerminalApp, VscodeTerminalColors
from .tokens import Semantic, Textmate, TokenStyle


THEME_FILENAME_TEMPLATE = "{slug}-color-theme.json"


TokenKey = Color | ColorStyle | TokenStyle | str
UiColorKey = Color | ColorStyle | str


class ThemeCategory(enum.StrEnum):
    light = "light"
    dark = "dark"


@dataclasses.dataclass
class Theme:
    name: str

    category: ThemeCategory

    terminal_colors: VscodeTerminalColors

    token_colors: dict[TokenKey, list[Textmate | Semantic]]
    """Map of foreground colors or font styles to the list of Textmate or
    Semantic token objects to which the style should apply."""

    ui_colors: dict[UiColorKey, list[str]]
    """Map of hexadecimal color codes (with or without alpha level) to
    the list of UI elements that use that color."""

    def save(self, package_path: Path):
        slug = self.name.lower().replace(" ", "-")
        filename = THEME_FILENAME_TEMPLATE.format(slug=slug)

        semantic_token_colors = {}
        textmate_token_colors = []

        for color_or_style, token_list in self.token_colors.items():
            style = color_or_style.serialize() if isinstance(color_or_style, TokenStyle) else str(color_or_style)

            for token in token_list:
                if isinstance(token, Semantic):
                    semantic_token_colors[token.value] = style
                else:
                    settings = {"foreground": style} if isinstance(style, str) else style
                    textmate_token_colors.append({"scope": [token.value], "settings": settings})

        ui_colors = {
            element: str(color)
            for color, element_list in self.ui_colors.items()
            for element in element_list
        }
        terminal_colors = self.terminal_colors.serialize(app=TerminalApp.Vscode)

        with open(package_path / filename, "w") as f:
            data = {
                "name": self.name,
                "type": self.category,
                "semanticHighlighting": True,
                "colors": {**ui_colors, **terminal_colors},
                "semanticTokenColors": semantic_token_colors,
                "tokenColors": textmate_token_colors,
            }
            f.write(json.dumps(data, indent=4))
