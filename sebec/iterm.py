"""
Single file has three different key/dict pairs for all colors:

  - Default, eg. "Ansi 0 Color"
  - Dark, eg. "Ansi 0 Color (Dark)"
  - Light, eg. "Ansi 0 Color (Light)"

Generating the file requires both light & dark terminal themes.
"""

from sebec.terminal import TerminalColors, ItermColors

tc = TerminalColors(
    ansi_black="#000000",
    ansi_black_bright="#808080",
    ansi_red="#ff0000",
    ansi_red_bright="#ff8080",
    ansi_green="#00ff00",
    ansi_green_bright="#80ff80",
    ansi_yellow="#ffff00",
    ansi_yellow_bright="#ffff80",
    ansi_blue="#0000ff",
    ansi_blue_bright="#8080ff",
    ansi_magenta="#ff00ff",
    ansi_magenta_bright="#ff80ff",
    ansi_cyan="#00ffff",
    ansi_cyan_bright="#80ffff",
    ansi_white="#ffffff",
    ansi_white_bright="#f0f0f0",
    foreground="#d4d4d4",
    background="#1e1e1e",
    selection_foreground="#d4d4d4",
    selection_background="#1e1e1e",
    match_background="#1e1e1e",
    cursor_color="#d4d4d4",
    cursor_text_color="#d4d4d4",
)
ic = ItermColors(
    **tc.__dict__,
    badge_color="#ff0000",
    bold_color="#ff0000",
    cursor_guide_color="#ff0000",
    link_color="#ff0000",
    tab_color="#ff0000",
    underline_color="#ff0000",
)
