import dataclasses
import enum
import json
import pathlib

from sebec.color import Color, ColorStyle
from .tokens import SemanticToken, TextmateToken, TokenStyle


PATH_TEMPLATE = str(
    pathlib.Path(__file__)
    .parent # base
    .parent # vstheme
    .parent # sebec
    .parent # root
    / "package/vscode/themes/{slug}-color-theme.json"
)


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

    textmate_tokens: dict[TokenKey, list[TextmateToken | str]]
    """Map of foreground colors or font styles to the list of Textmate
    tokens names or `TextmateToken` objects to which the style should apply."""

    ui_colors: dict[UiColorKey, list[str]]
    """Map of hexadecimal color codes (with or without alpha level) to
    the list of UI elements that use that color."""

    def save(self):
        slug = self.name.lower().replace(" ", "-")
        with open(PATH_TEMPLATE.format(slug=slug), "w") as f:
            data = {
                "name": self.name,
                "type": self.category,
                "semanticHighlighting": True,
                "colors": {
                    element: str(color)
                    for color, element_list in self.ui_colors.items()
                    for element in element_list
                },
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
