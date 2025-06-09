"""
Utility classes for defining VS Code color selections for UI elements
and semantic & textmate tokens.
"""
import re
from typing import Annotated

from pydantic import BeforeValidator

from .base import Base, ColorSetting, TokenColorSetting


def assert_alphabetic(value: str) -> str:
    assert re.match(r"^[a-zA-Z]+?$", value), "must be alphabetic"
    return value


Alphabetic = Annotated[str, BeforeValidator(assert_alphabetic)]
UiSection = dict[Alphabetic, ColorSetting]


class TokenGroup(Base):
    style: TokenColorSetting
    semantic: str | list[str] | None = None
    textmate: str | list[str] | None = None


class VscodeColors(Base):
    tokens: list[TokenGroup]
    ui: dict[Alphabetic, ColorSetting | UiSection]
