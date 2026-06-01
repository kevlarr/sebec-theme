from enum import StrEnum
from typing import Annotated, Any

from pydantic import Field

from .base import Base
from .styles import ThemeStyleNames
from .terminal import TerminalColors
from .vscode import VsCodeColors


class ThemeModelV1(Base):
    name: str
    style_names: ThemeStyleNames = Field(alias="styleNames")
    terminal: TerminalColors
    vscode: VsCodeColors


class ThemeModel(ThemeModelV1):
    # The design system tokens don't need to be known during generation since they are
    # intended as anchors in the yaml, and the yaml parser will handle inlining them
    # to the relevant properties for each application
    system: Annotated[Any, Field(..., exclude=True)]
