import dataclasses
import enum
import json
import pathlib

from sebec.palette import Color


PATH_TEMPLATE = str(pathlib.Path(__file__).parent.parent.parent / "themes/{name}-color-theme.json")


class ThemeCategory(enum.StrEnum):
    light = "light"
    dark = "dark"


@dataclasses.dataclass
class Theme:
    name: str
    category: ThemeCategory
    color_sections: list[dict[str, Color]]
    # token_colors: list

    def save(self):
        with open(PATH_TEMPLATE.format(name=self.name), "w") as f:
            data = {
                "name": self.name,
                "type": self.category,
                "semanticHighlighting": True,
                "colors": {
                    k: v for section in self.color_sections
                    for k, v in section.items()
                },
                "token_colors": [],
            }
            f.write(json.dumps(data, indent=4))
