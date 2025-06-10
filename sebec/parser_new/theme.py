from enum import StrEnum

from pydantic import Field

from .base import Base
from .styles import ThemeStyleNames
from .terminal import TerminalColors
from .vscode import VsCodeColors


class ThemeModel(Base):
    name: str
    style_names: ThemeStyleNames = Field(alias="styleNames")
    terminal: TerminalColors
    vscode: VsCodeColors
