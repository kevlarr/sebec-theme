
import json
from pathlib import Path

from sebec.parser.theme import ThemeModel


THEME_FILENAME_TEMPLATE = "{slug}-color-theme.json"


def export(*, package_path: Path, theme: ThemeModel):

    slug = theme.name.lower().replace(" ", "-")
    filename = THEME_FILENAME_TEMPLATE.format(slug=slug)

    semantic_token_colors = {}
    textmate_token_colors = []

    for color_or_style, token_list in self.token_colors.items():
        style = color_or_style.serialize() if isinstance(color_or_style, TokenStyle) else str(color_or_style)

        for token in token_list:
            if isinstance(token, Semantic):
                semantic_token_colors[token.value] = style
            else:
                settings = {"foreground": style} if isinstance(style, str) else style
                textmate_token_colors.append({"scope": token.value, "settings": settings})

    ui_colors = {
        element: str(color)
        for color, element_list in self.ui_colors.items()
        for element in element_list
    }
    terminal_colors = self.terminal_colors.serialize(app=TerminalApp.Vscode)

    with open(package_path / filename, "w") as f:
        data = {
            "name": self.name,
            "type": self.category,
            "semanticHighlighting": True,
            "colors": {**ui_colors, **terminal_colors},
            "semanticTokenColors": semantic_token_colors,
            "tokenColors": textmate_token_colors,
        }
        f.write(json.dumps(data, indent=4))




def _serialize_token_style(style: TokenStyle) -> dict | str:
    """Returns a dict with the foreground color and a font style string
    suitable for Textmate and semantic tokens if any styles arepresent,
    otherwise returns the foreground color as a string."""
    color = super().__str__()

    font_style = ""
    if self.bold:          font_style += "bold"
    if self.italic:        font_style += " italic"
    if self.strikethrough: font_style += " strikethrough"
    if self.underline:     font_style += " underline"

    if font_style:
        return {"foreground": color, "fontStyle": font_style.strip()}

    return color
