
import json
from pathlib import Path

from sebec.parser.terminal import TerminalApp
from sebec.parser.theme import ThemeModel
from sebec.parser.vscode import SemanticToken


THEME_FILENAME_TEMPLATE = "{slug}-color-theme.json"


def export(*, package_path: Path, theme: ThemeModel):

    slug = theme.name.lower().replace(" ", "-").replace("(", "").replace(")", "")
    filename = THEME_FILENAME_TEMPLATE.format(slug=slug)

    semantic_token_colors = {}
    textmate_token_colors = []

    for token in theme.vscode.tokens:
        style = token.style.serialize()
        if isinstance(token, SemanticToken):
            semantic_token_colors[token.scope] = style
        else:
            settings = {"foreground": style} if isinstance(style, str) else style
            textmate_token_colors.append({"scope": token.scope, "settings": settings})

    terminal_colors = theme.terminal.serialize(app=TerminalApp.Vscode)
    ui_colors = {ui.scope: str(ui.style) for ui in theme.vscode.ui}

    # Merge UI & terminal colors together but prioritize UI such that
    # they can override terminal colors if desired.
    colors = {**terminal_colors, **ui_colors}

    with open(package_path / filename, "w") as f:
        data = {
            "name": theme.name,
            "type": theme.style,
            "semanticHighlighting": True,
            "colors": colors,
            "semanticTokenColors": semantic_token_colors,
            "tokenColors": textmate_token_colors,
        }
        f.write(json.dumps(data, indent=4))
