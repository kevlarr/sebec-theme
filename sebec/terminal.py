"""Utilities for defining styles for terminals across different applications, including:

- iTerm2
- VS Code
"""
from dataclasses import dataclass
from enum import StrEnum
from typing import Annotated

from sebec.vstheme.base import Color


# color_name_map = {
    # "Ansi 0 Color": "ansiBlack",
    # "Ansi 8 Color": "ansiBrightBlack",
    # "Ansi 1 Color": "ansiRed",
    # "Ansi 2 Color": "ansiGreen",
    # "Ansi 3 Color": "ansiYellow",
    # "Ansi 4 Color": "ansiBlue",
    # "Ansi 5 Color": "ansiMagenta",
    # "Ansi 6 Color": "ansiCyan",
    # "Ansi 7 Color": "ansiWhite",
    # "Ansi 9 Color": "ansiBrightRed",
    # "Ansi 10 Color": "ansiBrightGreen",
    # "Ansi 11 Color": "ansiBrightYellow",
    # "Ansi 12 Color": "ansiBrightBlue",
    # "Ansi 13 Color": "ansiBrightMagenta",
    # "Ansi 14 Color": "ansiBrightCyan",
    # "Ansi 15 Color": "ansiBrightWhite",
    # "Background Color": "background",
    # "Foreground Color": "foreground",
    # "Selection Color": "selectionBackground",
# }


class TerminalApp(StrEnum):
    Iterm = "iterm"
    Vscode = "vscode"


class Alias:
    def __init__(self, app: TerminalApp, alias: str):
        self.app = app
        self.alias = alias


Iterm = lambda alias: Alias(TerminalApp.Iterm, alias)
Vscode = lambda alias: Alias(TerminalApp.Vscode, alias)


class Base:
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
                    if not isinstance(anno, Alias) or (app and anno.app != app):
                        continue

                    key = anno.alias

                rval[key] = str(value)

            stack = [*stack, *new_elements]

        return rval


@dataclass(frozen=True)
class AnsiColors(Base):
    """ANSI color options."""
    black:          Annotated[Color, Iterm("Ansi 0 Color"),  Vscode("terminal.ansiBlack")]
    black_bright:   Annotated[Color, Iterm("Ansi 8 Color"),  Vscode("terminal.ansiBrightBlack")]
    red:            Annotated[Color, Iterm("Ansi 1 Color"),  Vscode("terminal.ansiRed")]
    red_bright:     Annotated[Color, Iterm("Ansi 9 Color"),  Vscode("terminal.ansiBrightRed")]
    green:          Annotated[Color, Iterm("Ansi 2 Color"),  Vscode("terminal.ansiGreen")]
    green_bright:   Annotated[Color, Iterm("Ansi 10 Color"), Vscode("terminal.ansiBrightGreen")]
    yellow:         Annotated[Color, Iterm("Ansi 3 Color"),  Vscode("terminal.ansiYellow")]
    yellow_bright:  Annotated[Color, Iterm("Ansi 11 Color"), Vscode("terminal.ansiBrightYellow")]
    blue:           Annotated[Color, Iterm("Ansi 4 Color"),  Vscode("terminal.ansiBlue")]
    blue_bright:    Annotated[Color, Iterm("Ansi 12 Color"), Vscode("terminal.ansiBrightBlue")]
    magenta:        Annotated[Color, Iterm("Ansi 5 Color"),  Vscode("terminal.ansiMagenta")]
    magenta_bright: Annotated[Color, Iterm("Ansi 13 Color"), Vscode("terminal.ansiBrightMagenta")]
    cyan:           Annotated[Color, Iterm("Ansi 6 Color"),  Vscode("terminal.ansiCyan")]
    cyan_bright:    Annotated[Color, Iterm("Ansi 14 Color"), Vscode("terminal.ansiBrightCyan")]
    white:          Annotated[Color, Iterm("Ansi 7 Color"),  Vscode("terminal.ansiWhite")]
    white_bright:   Annotated[Color, Iterm("Ansi 15 Color"), Vscode("terminal.ansiBrightWhite")]


@dataclass(frozen=True)
class TerminalColors(Base):
    """Common color options across different application terminals."""
    ansi: AnsiColors

    foreground:           Annotated[Color, Iterm("Foreground Color"),       Vscode("terminal.foreground")]
    background:           Annotated[Color, Iterm("Background Color"),       Vscode("terminal.background")]
    selection_foreground: Annotated[Color, Iterm("Selected Text Color"),    Vscode("terminal.selectionForeground")]
    selection_background: Annotated[Color, Iterm("Selection Color"),        Vscode("terminal.selectionBackground")]
    match_background:     Annotated[Color, Iterm("Match Background Color"), Vscode("terminal.findMatchBackground")]
    cursor_color:         Annotated[Color, Iterm("Cursor Color"),           Vscode("terminalCursor.foreground")]
    cursor_text_color:    Annotated[Color, Iterm("Cursor Text Color"),      Vscode("terminalCursor.background")]


@dataclass(frozen=True)
class ItermColors(Base):
    """Color options for iTerm2."""
    terminal: TerminalColors

    badge_color:         Annotated[Color, Iterm("Badge Color")]
    bold_color:          Annotated[Color, Iterm("Bold Color")]
    cursor_guide_color:  Annotated[Color, Iterm("Cursor Guide Color")]
    link_color:          Annotated[Color, Iterm("Link Color")]
    tab_color:           Annotated[Color, Iterm("Tab Color")]
    underline_color:     Annotated[Color, Iterm("Underline Color")]

@dataclass(frozen=True)
class VscodeColors(Base):
    """Color options for VS Code's integrated terminal."""
    terminal: TerminalColors
