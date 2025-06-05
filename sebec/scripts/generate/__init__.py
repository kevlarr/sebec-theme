
import pathlib

from sebec.exporters import iterm, vscode #, windows_terminal
from sebec.parser import parse_yml
from sebec.parser_new import parse_yml_new
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

    # dawn = parse_yml(yml_path / "dawn.yml")
    # dusk = parse_yml(yml_path / "dusk.yml")

    theme = parse_yml_new(yml_path / "theme.yml")

    breakpoint()

    iterm.export(
        package_path / "Twilight Lake.itermcolors",
        light=dawn.terminal,
        dark=dusk.terminal,
    )

    # vscode.export(
    #     package_path=vscode_themes_path,
    #     theme=dawn,
    # )
    # vscode.export(
    #     package_path=vscode_themes_path,
    #     theme=dusk,
    # )

    # windows_terminal.export(
        # package_path=package_path,
        # light=sunrise.terminal,
        # dark=twilight.terminal,
    # )

    export_palette_html(package_path / "palette.html")

    # Sunrise.save(themes)
    # Twilight.save(themes)

    print("Themes and palette generated successfully!")
