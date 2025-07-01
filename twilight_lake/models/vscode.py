"""
Utility classes for defining VS Code color selections for UI elements
and semantic & textmate tokens.
"""
import re
from typing import Annotated, TypedDict

from pydantic import BeforeValidator

from .base import Base
from .colors import ColorSetting, FontStyle, TokenColorSetting
from .styles import ThemeStyle


def assert_alphabetic(value: str) -> str:
    assert re.match(r"^[a-zA-Z\.0-9]+?$", value), "must be alphabetic"
    return value


Alphabetic = Annotated[str, BeforeValidator(assert_alphabetic)]
UiSection = dict[Alphabetic, ColorSetting]


class TokenGroup(Base):
    style: TokenColorSetting
    semantic: str | list[str] | None = None
    textmate: str | list[str] | None = None


class SerializedColors(TypedDict):
    semantic_tokens: dict[str, FontStyle | str]
    textmate_tokens: list[dict]
    ui: dict[str, str]


class VsCodeColors(Base):
    tokens: list[TokenGroup]
    ui: dict[Alphabetic, ColorSetting | UiSection]

    def serialize(self, style: ThemeStyle) -> dict:
        semantic_tokens, textmate_tokens, ui = {}, [], {}

        for token_group in self.tokens:
            font_style = token_group.style.serialize(style)

            if semantic := token_group.semantic:
                for s in (semantic if isinstance(semantic, list) else [semantic]):
                    # Semantic tokens are just a map of token scope to either
                    # hex string or font style object
                    semantic_tokens[s] = font_style

            if textmate := token_group.textmate:
                if isinstance(font_style, str):
                    settings = {"foreground": font_style}
                else:
                    settings = font_style

                # The textmate scope can either be a single str or a list of strings
                textmate_tokens.append({"scope": textmate, "settings": settings})

        for key, val in self.ui.items():
            if isinstance(val, dict):
                for section_key, section_val in val.items():
                    concat_key = f"{key}.{section_key}"
                    ui[concat_key] = section_val.serialize(style)
                    pass
            else:
                ui[key] = val.serialize(style)

        return {
            "semantic_tokens": semantic_tokens,
            "textmate_tokens": textmate_tokens,
            "ui": ui,
        }
