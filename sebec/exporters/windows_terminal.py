"""Utilities for writing the JSON for Windows Terminal"""
import json
from pathlib import Path

from sebec.models.styles import ThemeStyle
from sebec.models.terminal import TerminalApp
from sebec.models.theme import ThemeModel


def export(destination: Path, theme: ThemeModel):
    filename = f"{theme.name}.json"

    light_colors = theme.terminal.serialize(TerminalApp.WindowsTerminal, ThemeStyle.Light)
    dark_colors = theme.terminal.serialize(TerminalApp.WindowsTerminal, ThemeStyle.Dark)

    light_theme_name = f"{theme.name} {theme.style_names.__dict__[ThemeStyle.Light]}"
    dark_theme_name = f"{theme.name} {theme.style_names.__dict__[ThemeStyle.Dark]}"

    with open(destination / filename, "w") as color_file:
        color_file.write(json.dumps([
            {**light_colors, "name": light_theme_name},
            {**dark_colors, "name": dark_theme_name},
        ], indent=4))
