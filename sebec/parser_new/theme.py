from enum import StrEnum

from pydantic import Field

from .base import Base
from .terminal import TerminalColors
from .vscode import VscodeColors


class ThemeStyle(StrEnum):
    light = "light"
    dark = "dark"


class ThemeStyleNames(Base):
    light: str
    dark: str


class ThemeModel(Base):
    name: str
    style_names: ThemeStyleNames = Field(alias="styleNames")
    terminal: TerminalColors
    # vscode: VscodeColors
