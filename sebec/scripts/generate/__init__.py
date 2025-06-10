
import pathlib

from sebec.exporters import iterm, vscode #, windows_terminal
from sebec.parser_new import parse_yml_new
from sebec.parser_new.styles import ThemeStyle
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

    theme = parse_yml_new(ROOT_PATH / "theme.yml")

    iterm.export(package_path, theme)
    vscode.export(vscode_themes_path, theme, ThemeStyle.Light)
    vscode.export(vscode_themes_path, theme, ThemeStyle.Dark)

    # windows_terminal.export(
        # package_path=package_path,
        # light=sunrise.terminal,
        # dark=twilight.terminal,
    # )

    export_palette_html(package_path / "palette.html")

    # Sunrise.save(themes)
    # Twilight.save(themes)

    print("Themes and palette generated successfully!")
