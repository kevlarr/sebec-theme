import dataclasses
import enum
import json
import pathlib

from sebec.palette import Color


PATH_TEMPLATE = str(pathlib.Path(__file__).parent.parent.parent / "themes/{name}-color-theme.json")


Element = str


class ThemeCategory(enum.StrEnum):
    light = "light"
    dark = "dark"


@dataclasses.dataclass
class TokenColor:
    name: str
    scope: str | list[str]
    settings: dict[str, str]


@dataclasses.dataclass
class Theme:
    name: str
    category: ThemeCategory
    colors: dict[str, list[Element]]
    """Map of hexadecimal color codes (with or without alpha level) to
    the list of elements that use that color."""
    token_colors: list[TokenColor]

    def save(self):
        with open(PATH_TEMPLATE.format(name=self.name), "w") as f:
            data = {
                "name": self.name,
                "type": self.category,
                "semanticHighlighting": True,
                "colors": {
                    element: color
                    for color, element_list in self.colors.items()
                    for element in element_list
                },
                "tokenColors": [
                    token_color.__dict__
                    for token_color in self.token_colors
                ],
            }
            f.write(json.dumps(data, indent=4))
