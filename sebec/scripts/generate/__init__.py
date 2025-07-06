import traceback
import pathlib

from watchfiles import watch
from yaml import safe_load

from sebec.exporters import iterm, vscode, windows_terminal
from sebec.models.styles import ThemeStyle
from sebec.models.theme import ThemeModel

from .palette import export_palette_html


ROOT_PATH = (
    pathlib.Path(__file__)
    .parent # generate
    .parent # scripts
    .parent # sebec
    .parent # root
)


def main() -> None:
    yml_path = ROOT_PATH / "theme.yml"
    package_path = ROOT_PATH / "package"

    with open(yml_path) as yml_file:
        content = safe_load(yml_file)
        theme = ThemeModel.model_validate(content)

    iterm.export(package_path / "iterm2", theme)
    vscode.export(package_path / "vscode/themes", theme, ThemeStyle.Light)
    vscode.export(package_path / "vscode/themes", theme, ThemeStyle.Dark)
    windows_terminal.export(package_path / "windows-terminal", theme)

    export_palette_html(package_path / "palette.html")

    print("Themes and palette generated successfully!")


def watch_main() -> None:
    files = [
        ROOT_PATH / "theme.yml",
        ROOT_PATH / "sebec" / "color.py",
    ]
    print("\nWatching files for changes:")
    for watched in files:
        print(f"  - {watched}")
    print()
    for _ in watch(*files):
        try:
            main()
        except Exception as exc:
            print(f"Error: {exc}")
            traceback.print_exc()
        print()
