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


@dataclass
class TerminalColors:
    ansi_black:           Annotated[Color, Iterm("Ansi 0 Color"),     Vscode("ansiBlack")]
    ansi_black_bright:    Annotated[Color, Iterm("Ansi 8 Color"),     Vscode("ansiBrightBlack")]
    ansi_red:             Annotated[Color, Iterm("Ansi 1 Color"),     Vscode("ansiRed")]
    ansi_red_bright:      Annotated[Color, Iterm("Ansi 9 Color"),     Vscode("ansiBrightRed")]
    ansi_green:           Annotated[Color, Iterm("Ansi 2 Color"),     Vscode("ansiGreen")]
    ansi_green_bright:    Annotated[Color, Iterm("Ansi 10 Color"),    Vscode("ansiBrightGreen")]
    ansi_yellow:          Annotated[Color, Iterm("Ansi 3 Color"),     Vscode("ansiYellow")]
    ansi_yellow_bright:   Annotated[Color, Iterm("Ansi 11 Color"),    Vscode("ansiBrightYellow")]
    ansi_blue:            Annotated[Color, Iterm("Ansi 4 Color"),     Vscode("ansiBlue")]
    ansi_blue_bright:     Annotated[Color, Iterm("Ansi 12 Color"),    Vscode("ansiBrightBlue")]
    ansi_magenta:         Annotated[Color, Iterm("Ansi 5 Color"),     Vscode("ansiMagenta")]
    ansi_magenta_bright:  Annotated[Color, Iterm("Ansi 13 Color"),    Vscode("ansiBrightMagenta")]
    ansi_cyan:            Annotated[Color, Iterm("Ansi 6 Color"),     Vscode("ansiCyan")]
    ansi_cyan_bright:     Annotated[Color, Iterm("Ansi 14 Color"),    Vscode("ansiBrightCyan")]
    ansi_white:           Annotated[Color, Iterm("Ansi 7 Color"),     Vscode("ansiWhite")]
    ansi_white_bright:    Annotated[Color, Iterm("Ansi 15 Color"),    Vscode("ansiBrightWhite")]
    background:           Annotated[Color, Iterm("Background Color"), Vscode("background")]
    foreground:           Annotated[Color, Iterm("Foreground Color"), Vscode("foreground")]
    selection_background: Annotated[Color, Iterm("Selection Color"),  Vscode("selectionBackground")]


colors = TerminalColors(
    ansi_black="#000000",
    ansi_black_bright="#808080",
    ansi_red="#FF0000",
    ansi_green="#00FF00",
    ansi_yellow="#FFFF00",
    ansi_blue="#0000FF",
    ansi_magenta="#FF00FF",
    ansi_cyan="#00FFFF",
    ansi_white="#FFFFFF",
    ansi_red_bright="#FF5555",
    ansi_green_bright="#55FF55",
    ansi_yellow_bright="#FFFF55",
    ansi_blue_bright="#5555FF",
    ansi_magenta_bright="#FF55FF",
    ansi_cyan_bright="#55FFFF",
    ansi_white_bright="#FFFFFF",
    background="#1E1E1E",
    foreground="#D4D4D4",
    selection_background="#264F78"
)
