"""Utilities for defining styles for terminals across different applications, including:

- iTerm2
- VS Code
"""
from enum import StrEnum
from typing import Annotated

from pydantic import BaseModel, Field, model_validator

from sebec.color import Color
from .base import Base


class TerminalApp(StrEnum):
    Iterm = "iterm"
    Vscode = "vscode"
    WindowsTerminal = "windowsTerminal"


class Alias:
    def __init__(self, app: TerminalApp, alias: str):
        self.app = app
        self.alias = alias


Iterm = lambda alias: Alias(TerminalApp.Iterm, alias)
Vscode = lambda alias: Alias(TerminalApp.Vscode, alias)
WindowsTerminal = lambda alias: Alias(TerminalApp.WindowsTerminal, alias)


# class Base:


class TerminalBase(Base):

    @model_validator(mode="before")
    @classmethod
    def convert_colors(cls, values):
        return {
            k: Color[v.lower()] if isinstance(v, str) else v
            for k, v in values.items()
        }

    def serialize(self, app: TerminalApp = None) -> dict[str, str]:
        stack = [self]
        rval = {}

        while stack:
            new_elements = []
            element = stack.pop()

            for key, value in element.__dict__.items():
                if not isinstance(value, Color) and not isinstance(value, str):
                    new_elements.append(value)
                    continue

                for anno in element.__annotations__[key].__metadata__:
                    if not isinstance(anno, Alias) or not app or anno.app != app:
                        continue

                    if not app:
                        breakpoint()

                    key = anno.alias

                rval[key] = str(value)

            stack = [*stack, *new_elements]

        return rval

class AnsiColors(TerminalBase):
    """ANSI color options with annotations specifying the key names for each terminal application."""

    black: Annotated[
        Color,
        Iterm("Ansi 0 Color"),
        Vscode("terminal.ansiBlack"),
        WindowsTerminal("black"),
    ]
    black_bright: Annotated[
        Color,
        Field(alias="blackBright"),
        Iterm("Ansi 8 Color"),
        Vscode("terminal.ansiBrightBlack"),
        WindowsTerminal("brightblack"),
    ]
    blue: Annotated[
        Color,
        Iterm("Ansi 4 Color"),
        Vscode("terminal.ansiBlue"),
        WindowsTerminal("blue"),
    ]
    blue_bright: Annotated[
        Color,
        Field(alias="blueBright"),
        Iterm("Ansi 12 Color"),
        Vscode("terminal.ansiBrightBlue"),
        WindowsTerminal("brightBlue"),
    ]
    cyan: Annotated[
        Color,
        Iterm("Ansi 6 Color"),
        Vscode("terminal.ansiCyan"),
        WindowsTerminal("cyan"),
    ]
    cyan_bright: Annotated[
        Color,
        Field(alias="cyanBright"),
        Iterm("Ansi 14 Color"),
        Vscode("terminal.ansiBrightCyan"),
        WindowsTerminal("brightCyan"),
    ]
    green: Annotated[
        Color,
        Iterm("Ansi 2 Color"),
        Vscode("terminal.ansiGreen"),
        WindowsTerminal("green"),
    ]
    green_bright: Annotated[
        Color,
        Field(alias="greenBright"),
        Iterm("Ansi 10 Color"),
        Vscode("terminal.ansiBrightGreen"),
        WindowsTerminal("brightGreen"),
    ]
    magenta: Annotated[
        Color,
        Iterm("Ansi 5 Color"),
        Vscode("terminal.ansiMagenta"),
        WindowsTerminal("purple"),
    ]
    magenta_bright: Annotated[
        Color,
        Field(alias="magentaBright"),
        Iterm("Ansi 13 Color"),
        Vscode("terminal.ansiBrightMagenta"),
        WindowsTerminal("brightPurple"),
    ]
    red: Annotated[
        Color,
        Iterm("Ansi 1 Color"),
        Vscode("terminal.ansiRed"),
        WindowsTerminal("red"),
    ]
    red_bright: Annotated[
        Color,
        Field(alias="redBright"),
        Iterm("Ansi 9 Color"),
        Vscode("terminal.ansiBrightRed"),
        WindowsTerminal("brightRed"),
    ]
    yellow: Annotated[
        Color,
        Iterm("Ansi 3 Color"),
        Vscode("terminal.ansiYellow"),
        WindowsTerminal("yellow"),
    ]
    yellow_bright: Annotated[
        Color,
        Field(alias="yellowBright"),
        Iterm("Ansi 11 Color"),
        Vscode("terminal.ansiBrightYellow"),
        WindowsTerminal("brightYellow"),
    ]
    white: Annotated[
        Color,
        Iterm("Ansi 7 Color"),
        Vscode("terminal.ansiWhite"),
        WindowsTerminal("white"),
    ]
    white_bright: Annotated[
        Color,
        Field(alias="whiteBright"),
        Iterm("Ansi 15 Color"),
        Vscode("terminal.ansiBrightWhite"),
        WindowsTerminal("brightWhite"),
    ]


class ItermColors(TerminalBase):
    """Color options specific to iTerm2."""
    badge_color: Annotated[
        Color,
        Field(alias="badgeColor"),
        Iterm("Badge Color"),
    ]
    bold_color: Annotated[
        Color,
        Field(alias="boldColor"),
        Iterm("Bold Color"),
    ]
    cursor_guide_color: Annotated[
        Color,
        Field(alias="cursorGuideColor"),
        Iterm("Cursor Guide Color"),
    ]
    link_color: Annotated[
        Color,
        Field(alias="linkColor"),
        Iterm("Link Color"),
    ]
    tab_color: Annotated[
        Color,
        Field(alias="tabColor"),
        Iterm("Tab Color"),
    ]
    underline_color: Annotated[
        Color,
        Field(alias="underlineColor"),
        Iterm("Underline Color"),
    ]


class TerminalColors(TerminalBase):
    """Common color options across different terminals, with annotations specifying
    the key names for each terminal application. If no key name is specified, then
    the application does not support the specific setting."""
    ansi: AnsiColors
    iterm: ItermColors

    background: Annotated[
        Color,
        Iterm("Background Color"),
        Vscode("terminal.background"),
        WindowsTerminal("background"),
    ]
    foreground: Annotated[
        Color,
        Iterm("Foreground Color"),
        Vscode("terminal.foreground"),
        WindowsTerminal("foreground"),
    ]
    selection_background: Annotated[
        Color,
        Field(alias="selectionBackground"),
        Iterm("Selection Color"),
        Vscode("terminal.selectionBackground"),
        WindowsTerminal("selectionBackground"),
    ]
    selection_foreground: Annotated[
        Color,
        Field(alias="selectionForeground"),
        Iterm("Selected Text Color"),
        Vscode("terminal.selectionForeground"),
    ]
    match_background: Annotated[
        Color,
        Field(alias="matchBackground"),
        Iterm("Match Background Color"),
        Vscode("terminal.findMatchBackground"),
    ]
    cursor_color: Annotated[
        Color,
        Field(alias="cursorColor"),
        Iterm("Cursor Color"),
        Vscode("terminalCursor.background"),
        WindowsTerminal("cursorColor"),
    ]
    cursor_text_color: Annotated[
        Color,
        Field(alias="cursorTextColor"),
        Iterm("Cursor Text Color"),
        Vscode("terminalCursor.foreground"),
    ]
