import traceback
import pathlib

from watchfiles import watch
from yaml import safe_load

from twilight_lake.exporters import iterm, vscode, windows_terminal
from twilight_lake.models.styles import ThemeStyle
from twilight_lake.models.theme import ThemeModel

from .palette import export_palette_html


ROOT_PATH = (
    pathlib.Path(__file__)
    .parent # generate
    .parent # scripts
    .parent # twilight_lake
    .parent # root
)


def main() -> None:
    yml_path = ROOT_PATH / "theme.yml"
    package_path = ROOT_PATH / "package"
    vscode_themes_path = package_path / "vscode/themes"

    with open(yml_path) as yml_file:
        content = safe_load(yml_file)
        theme = ThemeModel.model_validate(content)

    iterm.export(package_path, theme)
    vscode.export(vscode_themes_path, theme, ThemeStyle.Light)
    vscode.export(vscode_themes_path, theme, ThemeStyle.Dark)

    windows_terminal.export(package_path, theme)

    export_palette_html(package_path / "palette.html")

    # Sunrise.save(themes)
    # Twilight.save(themes)

    print("Themes and palette generated successfully!")

def watch_main() -> None:
    files = [
        ROOT_PATH / "theme.yml",
        ROOT_PATH / "twilight_lake" / "color.py",
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
