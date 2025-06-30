"""Utilities for writing the JSON for Windows Terminal"""
import json
from pathlib import Path

from twilight_lake.models.styles import ThemeStyle
from twilight_lake.models.terminal import TerminalApp
from twilight_lake.models.theme import ThemeModel


FILENAME = "twilight-lake-windows-terminal.json"


def export(destination: Path, theme: ThemeModel):
    light_colors = theme.terminal.serialize(TerminalApp.WindowsTerminal, ThemeStyle.Light)
    dark_colors = theme.terminal.serialize(TerminalApp.WindowsTerminal, ThemeStyle.Dark)

    light_theme_name = f"{theme.name} {theme.style_names.__dict__[ThemeStyle.Light]}"
    dark_theme_name = f"{theme.name} {theme.style_names.__dict__[ThemeStyle.Dark]}"

    with open(destination / FILENAME, "w") as color_file:
        color_file.write(json.dumps([
            {**light_colors, "name": light_theme_name},
            {**dark_colors, "name": dark_theme_name},
        ], indent=4))
