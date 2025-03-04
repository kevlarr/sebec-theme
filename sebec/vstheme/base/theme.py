import dataclasses
import enum
import json
from pathlib import Path

from sebec.color import Color, ColorStyle
from sebec.terminal import TerminalApp, VscodeTerminalColors
from .tokens import SemanticToken, TextmateToken, TokenStyle


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

    semantic_tokens: dict[TokenKey, list[SemanticToken | str]]
    """Map of foreground color literal or color/token style object to the list of semantic
    tokens names or `SemanticToken` objects to which the style should apply."""

    terminal_colors: VscodeTerminalColors

    textmate_tokens: dict[TokenKey, list[TextmateToken | str]]
    """Map of foreground colors or font styles to the list of Textmate
    tokens names or `TextmateToken` objects to which the style should apply."""

    ui_colors: dict[UiColorKey, list[str]]
    """Map of hexadecimal color codes (with or without alpha level) to
    the list of UI elements that use that color."""

    def save(self, package_path: Path):
        slug = self.name.lower().replace(" ", "-")
        filename = THEME_FILENAME_TEMPLATE.format(slug=slug)

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
                "semanticTokenColors": {
                    (
                        token if isinstance(token, str) else token.serialize()
                    ): (
                        style.serialize() if isinstance(style, TokenStyle) else str(style)
                    )
                    for style, token_list in self.semantic_tokens.items()
                    for token in token_list
                },
                "tokenColors": [
                    {
                        **({"scope": token} if isinstance(token, str) else token.serialize()),
                        "settings": {"foreground": style} if isinstance(style, str) else style.serialize()
                    }
                    for style, token_list in self.textmate_tokens.items()
                    for token in token_list
                ],
            }
            f.write(json.dumps(data, indent=4))
