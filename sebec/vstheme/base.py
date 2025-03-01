import dataclasses
import enum
import json
import pathlib
import typing

from sebec.palette import Color


PATH_TEMPLATE = str(pathlib.Path(__file__).parent.parent.parent / "themes/{name}-color-theme.json")


Element = str


class ThemeCategory(enum.StrEnum):
    light = "light"
    dark = "dark"


class Scope:
    name: str | None
    scope: str | list[str]
    settings: dict[str, str]

    def __init__(self, *scopes: str, name: str | None = None, **settings):
        self.name = name
        self.scope = scopes
        self.settings = settings


@dataclasses.dataclass
class Theme:
    name: str
    category: ThemeCategory
    colors: dict[str, list[Element]]
    """Map of hexadecimal color codes (with or without alpha level) to
    the list of elements that use that color."""
    scopes: dict[str, list[Scope | str]]
    """Map of hexadecimal color codes (with or without alpha level) to
    the list of scope names or Scope objects that use that color."""

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
                    self._scope_to_token_color(scope, color)
                    for color, scope_setting_list in self.scopes.items()
                    for scope in scope_setting_list
                ],
            }
            f.write(json.dumps(data, indent=4))

    @staticmethod
    def _scope_to_token_color(scope: Scope | str, color: str):
        if isinstance(scope, str):
            return {"scope": scope, "settings": {"foreground": color}}

        val = {
            "scope": scope.scope,
            "settings": {
                "foreground": color,
                **scope.settings,
            }
        }
        if scope.name:
            val["name"] = scope.name
        return val
