from enum import StrEnum

from .base import Base
from .terminal import TerminalColors
from .vscode import VscodeColors


class ThemeStyle(StrEnum):
    light = "light"
    dark = "dark"


class ThemeModel(Base):
    name: str
    style: ThemeStyle
    terminal: TerminalColors
    vscode: VscodeColors
