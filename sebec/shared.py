"""Color settings shared between different applications' color schemes."""
from sebec.color import Color
from sebec.terminal import AnsiColors, TerminalColors, ItermColors


ANSI_DARK = AnsiColors(
    black=Color.Twilight0,
    black_bright=Color.Twilight3,
    red=Color.SolarRed0,
    red_bright=Color.SolarRed1,
    green=Color.Spruce1,
    green_bright=Color.Spruce2,
    yellow=Color.SolarYellow0,
    yellow_bright=Color.SolarYellow1,
    blue=Color.Sapphire1,
    blue_bright=Color.Sapphire2,
    magenta=Color.SolarPurple0,
    magenta_bright=Color.SolarPurple1,
    cyan=Color.Cerulean1,
    cyan_bright=Color.Cerulean2,
    white=Color.Shine2,
    white_bright=Color.Shine4,
)

# Most colors are the same except for Sapphire/Cerulean being darker variants
# and replacing Spruce with Cedar
ANSI_LIGHT = AnsiColors(
    black=Color.Twilight0,
    black_bright=Color.Twilight3,
    red=Color.SolarRed0,
    red_bright=Color.SolarRed1,
    green=Color.Cedar0,
    green_bright=Color.Cedar1,
    yellow=Color.SolarYellow0,
    yellow_bright=Color.SolarYellow1,
    blue=Color.Sapphire0,
    blue_bright=Color.Sapphire1,
    magenta=Color.SolarPurple0,
    magenta_bright=Color.SolarPurple1,
    cyan=Color.Cerulean0,
    cyan_bright=Color.Cerulean1,
    white=Color.Shine2,
    white_bright=Color.Shine4,
)

TERMINAL_DARK = TerminalColors(
    ansi=ANSI_DARK,
    foreground=Color.Sunrise2,
    background=Color.Twilight2,
    selection_foreground=Color.Sunrise4,
    selection_background=Color.Sapphire0,
    match_background=Color.SolarPurple0,
    cursor_color=Color.Cerulean3,
    cursor_text_color=Color.Twilight0,
)

TERMINAL_LIGHT = TerminalColors(
    ansi=ANSI_LIGHT,
    foreground=Color.Twilight6,
    background=Color.Sunrise7,
    selection_foreground=Color.Twilight2,
    selection_background=Color.Sapphire3,
    match_background=Color.SolarPurple1,
    cursor_color=Color.Cerulean0,
    cursor_text_color=Color.Shine6,
)
