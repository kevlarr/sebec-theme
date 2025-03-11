from typing import Annotated

from pydantic import BeforeValidator, Field

from .base import Base, ColorStyle
from .formatters import parse_color_style, parse_token_style


def flatten_ui_settings(value):
    # value = [{'Twilight0': ['sideBar.background', ...]}, ...]

    # If the key had no items nested under it, the value element will
    # just be a string instead of a key mapping to an empty list
    values = (v for v in value if not isinstance(v, str))

    return [
        dict(style=color, scope=scope)
        for color_and_scopes in values
        for color, scope_list in color_and_scopes.items()
        for scope in scope_list
    ]


def flatten_tokens(value):
    # value = ['Sapphire0', {'Sapphire0(bold)': [{'semantic': 'class'}, {'textmate': ['one.scope', 'second.scope']}]}]

    # If the key had no items nested under it, the value element will
    # just be a string instead of a key mapping to an empty list
    values = (v for v in value if not isinstance(v, str))

    return [
        dict(style=color, **token)
        for color_and_scopes in values
        for color, token_list in color_and_scopes.items()
        for token in token_list
    ]


class TokenStyle(ColorStyle):
    bold: bool = False
    italic: bool = False
    strikethrough: bool = False
    underline: bool = False

    def serialize(self) -> dict | str:
        """Returns a dict with the foreground color and a font style string
        suitable for Textmate and semantic tokens if any styles arepresent,
        otherwise returns the foreground color as a string."""
        color = super().__str__()

        font_style = ""
        if self.bold:          font_style += "bold"
        if self.italic:        font_style += " italic"
        if self.strikethrough: font_style += " strikethrough"
        if self.underline:     font_style += " underline"

        if font_style:
            return {"foreground": color, "fontStyle": font_style.strip()}

        return color


class SemanticToken(Base):
    scope: Annotated[str, Field(alias="semantic")]
    style: Annotated[TokenStyle, BeforeValidator(parse_token_style)]


class TextmateToken(Base):
    name: str | None = None
    scope: Annotated[str | list[str], Field(alias="textmate")]
    style: Annotated[TokenStyle, BeforeValidator(parse_token_style)]


GenericToken = Annotated[
    SemanticToken | TextmateToken,
    Field(union_mode="left_to_right"),
]


class UiSetting(Base):
    style: Annotated[
        ColorStyle,
        BeforeValidator(parse_color_style),
    ]
    scope: str


class VscodeColors(Base):
    tokens: Annotated[
        list[GenericToken],
        BeforeValidator(flatten_tokens),
    ]
    ui: Annotated[
        list[UiSetting],
        BeforeValidator(flatten_ui_settings),
    ]
