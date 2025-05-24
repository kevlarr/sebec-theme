
import pathlib

from sebec.exporters import iterm, vscode #, windows_terminal
from sebec.parser import parse_yml
# from sebec.vstheme import Sunrise, Twilight
# from sebec.vstheme.base import Color

from .palette import export_palette_html


ROOT_PATH = (
    pathlib.Path(__file__)
    .parent # generate
    .parent # scripts
    .parent # sebec
    .parent # root
)


def main() -> None:
    package_path = ROOT_PATH / "package"
    vscode_themes_path = package_path / "vscode/themes"
    yml_path = ROOT_PATH / "ymls"

    dawn = parse_yml(yml_path / "dawn.yml")
    usk = parse_yml(yml_path / "dusk.yml")

    iterm.export(
        package_path / "Sebec.itermcolors",
        light=dawn.terminal,
        dark=usk.terminal,
    )
    vscode.export(
        package_path=vscode_themes_path,
        theme=dawn,
    )
    vscode.export(
        package_path=vscode_themes_path,
        theme=usk,
    )
    # windows_terminal.export(
        # package_path=package_path,
        # light=sunrise.terminal,
        # dark=twilight.terminal,
    # )

    export_palette_html(package_path / "palette.html")

    # Sunrise.save(themes)
    # Twilight.save(themes)

    print("Themes and palette generated successfully!")
