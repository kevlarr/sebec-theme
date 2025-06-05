"""Utility classes for defining VS Code color selections for UI elements
and semantic & textmate tokens.

https://macromates.com/manual/en/language_grammars#naming_conventions
https://code.visualstudio.com/api/language-extensions/semantic-highlight-guide
https://code.visualstudio.com/api/language-extensions/semantic-highlight-guide#semantic-token-scope-map
"""
import re
from typing import Annotated, Any

from pydantic import BeforeValidator, Field

from .base import Base, ColorStyle
from .formatters import parse_color_style, parse_token_style


def match_vscode_property_format(value: str) -> str:
    if not re.match(r"^[a-zA-Z]+(\.[a-zA-Z]+)?$", value):
        raise ValueError("must be valid VS Code property format, eg. 'abcd' or 'abcd.efgh'")

    return value


def flatten_ui_settings(value: Any):
    # value = [{'Twilight0': ['sideBar.background', ...]}, ...]

    # If the key had no items nested under it, the value element will
    # just be a string instead of a key mapping to an empty list
    values = (v for v in value if not isinstance(v, str))

    return [
        dict(style=color, scope=scope)
        for color_and_scopes in values
        for color, scope_list in color_and_scopes.items()
        for scope in scope_list or []
    ]


def flatten_ui_new_settings(value: Any) -> dict[str, str]:
    """
    Given a value of `dict[T0, dict[T1, T2] | T3 ]`, return a flattened value of `dict[str, T2 | T3]`.

    This function iterates through the input dictionary `value`. For each key-val pair:
        - If the val is a dict, each of its own key-val pairs are added to the result with new keys
          formed by concatenating the parent key and child keys
        - Otherwise, the key/val are added to the result as-is
    """
    if not isinstance(value, dict):
        raise ValueError("must be `dict[str, str | dict[str, str]]")

    flattened = {}

    for parent_key, parent_val in value.items():
        if isinstance(parent_val, dict):
            for child_key, child_val in parent_val.items():
                flattened[f"{parent_key}.{child_key}"] = child_val
            continue

        flattened[parent_key] = parent_val

    return flattened


def flatten_tokens(value):
    # value = ['Sapphire0', {'Sapphire0(bold)': [{'semantic': 'class'}, {'textmate': ['one.scope', 'second.scope']}]}]

    # If the key had no items nested under it, the value element will
    # just be a string instead of a key mapping to an empty list
    values = (v for v in value if not isinstance(v, str))

    return [
        dict(style=color, **token)
        for color_and_scopes in values
        for color, token_list in color_and_scopes.items()
        for token in token_list or []
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

ParsedColorStyle = Annotated[
    ColorStyle,
    BeforeValidator(parse_color_style),
]

class UiSetting(Base):
    style: ParsedColorStyle
    scope: str


VsCodeProperty = Annotated[str, BeforeValidator(match_vscode_property_format)]


class UiSection(Base):
    parent_scope: str
    settings: dict[VsCodeProperty, UiSetting]

class VscodeColors(Base):
    tokens: Annotated[
        list[GenericToken],
        BeforeValidator(flatten_tokens),
    ]
    ui: Annotated[
        list[UiSetting] | None,
        BeforeValidator(flatten_ui_settings),
    ] = None
    ui_new: Annotated[
        dict[VsCodeProperty, ParsedColorStyle] | None,
        BeforeValidator(flatten_ui_new_settings),
    ] = None
