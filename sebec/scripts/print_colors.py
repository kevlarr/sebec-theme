from enum import StrEnum

import termcolor as tc


# BG  FG   Color
# --------------
# 30  40   Black
# 31  41   Red
# 32  42   Green
# 33  43   Yellow
# 34  44   Blue
# 35  45   Magenta
# 36  46   Cyan
# 37  47   White
# 90  100  Bright Black (Gray)
# 91  101  Bright Red
# 92  102  Bright Green
# 93  103  Bright Yellow
# 94  104  Bright Blue
# 95  105  Bright Magenta
# 96  106  Bright Cyan
# 97  107  Bright White


class C(StrEnum):
    """Map of ANSI color name to termcolor name."""
    Black         = 'black'
    BrightBlack   = 'dark_grey'
    Red           = 'red'
    BrightRed     = 'light_red'
    Green         = 'green'
    BrightGreen   = 'light_green'
    Yellow        = 'yellow'
    BrightYellow  = 'light_yellow'
    Blue          = 'blue'
    BrightBlue    = 'light_blue'
    Magenta       = 'magenta'
    BrightMagenta = 'light_magenta'
    Cyan          = 'cyan'
    BrightCyan    = 'light_cyan'
    White         = 'light_grey'
    BrightWhite   = 'white'


def main():
    text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit"
    print()
    for color in C:
        color_code = tc.COLORS[color.value]
        print(tc.colored(f"[{color_code}] {color.name:15} {text}", color.value))

    print()
    for color in C:
        color_code = tc.COLORS[color.value]
        print(tc.colored(f"[{color_code}] {color.name + ' Bold':20} {text}", color.value, attrs=["bold"]))
