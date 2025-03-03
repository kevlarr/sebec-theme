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


class App(StrEnum):
    iterm = "iterm"
    vscode = "vscode"


class Alias:
    def __init__(self, app: App, alias: str):
        self.app = app
        self.alias = alias


Iterm = lambda alias: Alias(App.iterm, alias)
Vscode = lambda alias: Alias(App.vscode, alias)


@dataclass(frozen=True)
class AnsiTerminalColors:
    """ANSI color options."""
    ansi_black:          Annotated[Color, Iterm("Ansi 0 Color"),  Vscode("terminal.ansiBlack")]
    ansi_black_bright:   Annotated[Color, Iterm("Ansi 8 Color"),  Vscode("terminal.ansiBrightBlack")]
    ansi_red:            Annotated[Color, Iterm("Ansi 1 Color"),  Vscode("terminal.ansiRed")]
    ansi_red_bright:     Annotated[Color, Iterm("Ansi 9 Color"),  Vscode("terminal.ansiBrightRed")]
    ansi_green:          Annotated[Color, Iterm("Ansi 2 Color"),  Vscode("terminal.ansiGreen")]
    ansi_green_bright:   Annotated[Color, Iterm("Ansi 10 Color"), Vscode("terminal.ansiBrightGreen")]
    ansi_yellow:         Annotated[Color, Iterm("Ansi 3 Color"),  Vscode("terminal.ansiYellow")]
    ansi_yellow_bright:  Annotated[Color, Iterm("Ansi 11 Color"), Vscode("terminal.ansiBrightYellow")]
    ansi_blue:           Annotated[Color, Iterm("Ansi 4 Color"),  Vscode("terminal.ansiBlue")]
    ansi_blue_bright:    Annotated[Color, Iterm("Ansi 12 Color"), Vscode("terminal.ansiBrightBlue")]
    ansi_magenta:        Annotated[Color, Iterm("Ansi 5 Color"),  Vscode("terminal.ansiMagenta")]
    ansi_magenta_bright: Annotated[Color, Iterm("Ansi 13 Color"), Vscode("terminal.ansiBrightMagenta")]
    ansi_cyan:           Annotated[Color, Iterm("Ansi 6 Color"),  Vscode("terminal.ansiCyan")]
    ansi_cyan_bright:    Annotated[Color, Iterm("Ansi 14 Color"), Vscode("terminal.ansiBrightCyan")]
    ansi_white:          Annotated[Color, Iterm("Ansi 7 Color"),  Vscode("terminal.ansiWhite")]
    ansi_white_bright:   Annotated[Color, Iterm("Ansi 15 Color"), Vscode("terminal.ansiBrightWhite")]


@dataclass(frozen=True)
class TerminalColors(AnsiTerminalColors):
    """Common color options across different application terminals."""
    foreground:           Annotated[Color, Iterm("Foreground Color"),       Vscode("terminal.foreground")]
    background:           Annotated[Color, Iterm("Background Color"),       Vscode("terminal.background")]
    selection_foreground: Annotated[Color, Iterm("Selected Text Color"),    Vscode("terminal.selectionForeground")]
    selection_background: Annotated[Color, Iterm("Selection Color"),        Vscode("terminal.selectionBackground")]
    match_background:     Annotated[Color, Iterm("Match Background Color"), Vscode("terminal.findMatchBackground")]
    cursor_color:         Annotated[Color, Iterm("Cursor Color"),           Vscode("terminalCursor.foreground")]
    cursor_text_color:    Annotated[Color, Iterm("Cursor Text Color"),      Vscode("terminalCursor.background")]


@dataclass(frozen=True)
class ItermColors(TerminalColors):
    """Color options for iTerm2."""
    badge_color:         Annotated[Color, Iterm("Badge Color")]
    bold_color:          Annotated[Color, Iterm("Bold Color")]
    cursor_guide_color:  Annotated[Color, Iterm("Cursor Guide Color")]
    link_color:          Annotated[Color, Iterm("Link Color")]
    tab_color:           Annotated[Color, Iterm("Tab Color")]
    underline_color:     Annotated[Color, Iterm("Underline Color")]

