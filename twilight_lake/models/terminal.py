"""
Utilities for defining styles for terminals across different applications, including:
    * iTerm2
    * VS Code
    * Windows Terminal
"""
from enum import StrEnum
from typing import Annotated

from pydantic import Field

from .base import Base
from .colors import ColorSetting, MultiColorStyle
from .styles import ThemeStyle


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


class BaseTerminalModel(Base):
    """
    Base class for all terminal setting groups for exposing a `serialize` method
    that serializes the settings with the appropriate keys for the given app.
    """

    def serialize(self, app: TerminalApp, style: ThemeStyle) -> dict[str, str]:
        """
        Iterate through all of own and `BaseTerminalModel` children properties,
        serializing into a flat `dict` with keys corresponding to the given `TerminalApp`.
        """
        stack = [self]
        rval = {}

        while stack:
            new_elements = []
            element = stack.pop()

            for key, value in element.__dict__.items():
                serialized_key = None

                if isinstance(value, BaseTerminalModel):
                    new_elements.append(value)
                    continue

                field_annotations = element.__annotations__[key]

                for anno in field_annotations.__metadata__:
                    if isinstance(anno, Alias) and anno.app == app:
                        serialized_key = anno.alias
                        break

                if serialized_key:
                    if isinstance(value, MultiColorStyle):
                        rval[serialized_key] = value.serialize(style)
                    else:
                        rval[serialized_key] = value.serialize()

            stack = [*stack, *new_elements]

        return rval


class AnsiColors(BaseTerminalModel):
    """ANSI color options with annotations specifying the key names for each terminal application."""

    black: Annotated[
        ColorSetting,
        Iterm("Ansi 0 Color"),
        Vscode("terminal.ansiBlack"),
        WindowsTerminal("black"),
    ]
    black_bright: Annotated[
        ColorSetting,
        Field(alias="blackBright"),
        Iterm("Ansi 8 Color"),
        Vscode("terminal.ansiBrightBlack"),
        WindowsTerminal("brightblack"),
    ]
    blue: Annotated[
        ColorSetting,
        Iterm("Ansi 4 Color"),
        Vscode("terminal.ansiBlue"),
        WindowsTerminal("blue"),
    ]
    blue_bright: Annotated[
        ColorSetting,
        Field(alias="blueBright"),
        Iterm("Ansi 12 Color"),
        Vscode("terminal.ansiBrightBlue"),
        WindowsTerminal("brightBlue"),
    ]
    cyan: Annotated[
        ColorSetting,
        Iterm("Ansi 6 Color"),
        Vscode("terminal.ansiCyan"),
        WindowsTerminal("cyan"),
    ]
    cyan_bright: Annotated[
        ColorSetting,
        Field(alias="cyanBright"),
        Iterm("Ansi 14 Color"),
        Vscode("terminal.ansiBrightCyan"),
        WindowsTerminal("brightCyan"),
    ]
    green: Annotated[
        ColorSetting,
        Iterm("Ansi 2 Color"),
        Vscode("terminal.ansiGreen"),
        WindowsTerminal("green"),
    ]
    green_bright: Annotated[
        ColorSetting,
        Field(alias="greenBright"),
        Iterm("Ansi 10 Color"),
        Vscode("terminal.ansiBrightGreen"),
        WindowsTerminal("brightGreen"),
    ]
    magenta: Annotated[
        ColorSetting,
        Iterm("Ansi 5 Color"),
        Vscode("terminal.ansiMagenta"),
        WindowsTerminal("purple"),
    ]
    magenta_bright: Annotated[
        ColorSetting,
        Field(alias="magentaBright"),
        Iterm("Ansi 13 Color"),
        Vscode("terminal.ansiBrightMagenta"),
        WindowsTerminal("brightPurple"),
    ]
    red: Annotated[
        ColorSetting,
        Iterm("Ansi 1 Color"),
        Vscode("terminal.ansiRed"),
        WindowsTerminal("red"),
    ]
    red_bright: Annotated[
        ColorSetting,
        Field(alias="redBright"),
        Iterm("Ansi 9 Color"),
        Vscode("terminal.ansiBrightRed"),
        WindowsTerminal("brightRed"),
    ]
    yellow: Annotated[
        ColorSetting,
        Iterm("Ansi 3 Color"),
        Vscode("terminal.ansiYellow"),
        WindowsTerminal("yellow"),
    ]
    yellow_bright: Annotated[
        ColorSetting,
        Field(alias="yellowBright"),
        Iterm("Ansi 11 Color"),
        Vscode("terminal.ansiBrightYellow"),
        WindowsTerminal("brightYellow"),
    ]
    white: Annotated[
        ColorSetting,
        Iterm("Ansi 7 Color"),
        Vscode("terminal.ansiWhite"),
        WindowsTerminal("white"),
    ]
    white_bright: Annotated[
        ColorSetting,
        Field(alias="whiteBright"),
        Iterm("Ansi 15 Color"),
        Vscode("terminal.ansiBrightWhite"),
        WindowsTerminal("brightWhite"),
    ]


class GeneralTerminalColors(BaseTerminalModel):
    """Common color options across different terminals, with annotations specifying
    the key names for each terminal application. If no key name is specified, then
    the application does not support the specific setting."""
    ansi: AnsiColors
    background: Annotated[
        ColorSetting,
        Iterm("Background Color"),
        Vscode("terminal.background"),
        WindowsTerminal("background"),
    ]
    foreground: Annotated[
        ColorSetting,
        Iterm("Foreground Color"),
        Vscode("terminal.foreground"),
        WindowsTerminal("foreground"),
    ]
    selection_background: Annotated[
        ColorSetting,
        Field(alias="selectionBackground"),
        Iterm("Selection Color"),
        Vscode("terminal.selectionBackground"),
        WindowsTerminal("selectionBackground"),
    ]
    selection_foreground: Annotated[
        ColorSetting,
        Field(alias="selectionForeground"),
        Iterm("Selected Text Color"),
        Vscode("terminal.selectionForeground"),
    ]
    match_background: Annotated[
        ColorSetting,
        Field(alias="matchBackground"),
        Iterm("Match Background Color"),
        Vscode("terminal.findMatchHighlightBackground"),
    ]
    cursor_color: Annotated[
        ColorSetting,
        Field(alias="cursorColor"),
        Iterm("Cursor Color"),
        Vscode("terminalCursor.foreground"),
        WindowsTerminal("cursorColor"),
    ]
    cursor_text_color: Annotated[
        ColorSetting,
        Field(alias="cursorTextColor"),
        Iterm("Cursor Text Color"),
        Vscode("terminalCursor.background"),
    ]


class ItermColors(BaseTerminalModel):
    """Color options specific to iTerm2."""
    badge_color: Annotated[
        ColorSetting,
        Field(alias="badgeColor"),
        Iterm("Badge Color"),
    ]
    bold_color: Annotated[
        ColorSetting,
        Field(alias="boldColor"),
        Iterm("Bold Color"),
    ]
    cursor_guide_color: Annotated[
        ColorSetting,
        Field(alias="cursorGuideColor"),
        Iterm("Cursor Guide Color"),
    ]
    link_color: Annotated[
        ColorSetting,
        Field(alias="linkColor"),
        Iterm("Link Color"),
    ]
    tab_color: Annotated[
        ColorSetting,
        Field(alias="tabColor"),
        Iterm("Tab Color"),
    ]
    underline_color: Annotated[
        ColorSetting,
        Field(alias="underlineColor"),
        Iterm("Underline Color"),
    ]


class TerminalColors(BaseTerminalModel):
    base: GeneralTerminalColors
    iterm: ItermColors
