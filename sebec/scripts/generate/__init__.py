
import pathlib

from sebec.iterm.themes import ITERM_DARK, ITERM_LIGHT
from sebec.iterm.writer import write_itermcolors
from sebec.vstheme import Sunrise, Twilight
from sebec.vstheme.base import Color

from .palette import export_palette_html


PACKAGE_PATH = (
    pathlib.Path(__file__)
    .parent # generate
    .parent # scripts
    .parent # sebec
    .parent # root
    / "package"
)


def main():
    export_palette_html(PACKAGE_PATH / "palette.html")
    write_itermcolors(PACKAGE_PATH / "Sebec.itermcolors", light=ITERM_LIGHT, dark=ITERM_DARK)

    themes = PACKAGE_PATH / "vscode/themes"
    Sunrise.save(themes)
    Twilight.save(themes)

    print("Themes and palette generated successfully!")
