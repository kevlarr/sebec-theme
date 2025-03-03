
import pathlib
import xml.etree.ElementTree as ET

from sebec.vstheme import Sunrise, Twilight
from sebec.vstheme.base import Color

from .palette import export_palette_html


PACKAGE_PATH = str(
    pathlib.Path(__file__)
    .parent # generate
    .parent # scripts
    .parent # sebec
    .parent # root
    / "package"
)

def main():
    export_palette_html(PACKAGE_PATH)
    # generate_iterm_colors()
    # Sunrise.save()
    Twilight.save()
    print("Themes and palette generated successfully!")
