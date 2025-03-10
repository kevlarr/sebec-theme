
import pathlib

from sebec.exporters import iterm, vscode, windows_terminal
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


def main():
    package_path = ROOT_PATH / "package"
    vscode_themes_path = package_path / "vscode/themes"
    yml_path = ROOT_PATH / "ymls"

    sunrise = parse_yml(yml_path / "sunrise.yml")
    twilight = parse_yml(yml_path / "twilight.yml")

    iterm.export(
        package_path / "Sebec.itermcolors",
        light=sunrise.terminal,
        dark=twilight.terminal,
    )
    vscode.export(
        package_path=vscode_themes_path,
        theme=sunrise,
    )
    vscode.export(
        package_path=vscode_themes_path,
        theme=twilight,
    )
    windows_terminal.export(
        package_path=package_path,
        light=sunrise.terminal,
        dark=twilight.terminal,
    )

    # export_palette_html(package_path / "palette.html")

    # Sunrise.save(themes)
    # Twilight.save(themes)
    breakpoint()

    print("Themes and palette generated successfully!")
