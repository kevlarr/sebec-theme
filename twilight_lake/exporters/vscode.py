
import json
from pathlib import Path

from twilight_lake.models.styles import ThemeStyle
from twilight_lake.models.terminal import TerminalApp
from twilight_lake.models.theme import ThemeModel
from twilight_lake.models.vscode import UiSection, VsCodeColors


THEME_FILENAME_TEMPLATE = "{slug}-color-theme.json"


def export(package_path: Path, theme: ThemeModel, style: ThemeStyle):
    theme_name = f"{theme.name} {theme.style_names.__dict__[style]}"
    slug = theme_name.lower().replace(" ", "-").replace("(", "").replace(")", "")
    filename = THEME_FILENAME_TEMPLATE.format(slug=slug)

    terminal_colors = theme.terminal.serialize(TerminalApp.Vscode, style)
    vscode_colors = theme.vscode.serialize(style)

    # Merge UI & terminal colors together but prioritize UI such that
    # they can override terminal colors if desired.
    colors = {**terminal_colors, **vscode_colors["ui"]}

    with open(package_path / filename, "w") as f:
        data = {
            "name": theme_name,
            "type": style,
            "semanticHighlighting": True,
            "colors": colors,
            "semanticTokenColors": vscode_colors["semantic_tokens"],
            "tokenColors": vscode_colors["textmate_tokens"],
        }
        f.write(json.dumps(data, indent=4))
