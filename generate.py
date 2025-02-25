import dataclasses
import enum
import json


PATH_TEMPLATE = "themes/{name}-color-theme.json"


class Color(enum.StrEnum):
    # Base Polar colors
    polar0 = "#2E3440"
    polar1 = "#3B4352"
    polar2 = "#444D5E"
    polar3 = "#4C566A"
    # Extended Polar (darker)
    polarDark0 = "#15181E"
    polarDark1 = "#1B1F27"
    polarDark2 = "#212630"
    # Snow Storm
    snow0 = "#D8DEE9"
    snow1 = "#E5E9F0"
    snow2 = "#EDEFF5"
    # Extended Snow Storm (darker)
    snowDark0 = "#BFC8D9"
    snowDark1 = "#CDD3DF"


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


Sunrise = Theme(
    name="sebec-sunrise",
    category=ThemeCategory.light,
    color_sections=[],
    # token_colors=[],
)

Twilight = Theme(
    name="sebec-twilight",
    category=ThemeCategory.dark,
    color_sections=[
        # https://code.visualstudio.com/api/references/theme-color#base-colors
        {
            # "focusBorder": C.waveAqua1,
            # "foreground": C.dragonWhite,
        },

        # https://code.visualstudio.com/api/references/theme-color#editor-colors
        {
            "editor.background": Color.polarDark2,
            "editor.foreground": Color.snowDark0,
        },

        # https://code.visualstudio.com/api/references/theme-color#editor-widget-colors
        {
            "editorWidget.background": Color.polar1,
            # "editorWidget.resizeBorder": C.waveAqua1,
            # "editorWidget.foreground": C.dragonWhite,
        },

        # https://code.visualstudio.com/api/references/theme-color#side-bar
        {
            "sideBar.background": Color.polarDark1,
            # "sideBar.foreground": Color.snowDark0,
            # "sideBarSectionHeader.background": Color.polarDark1,
            # "sideBarSectionHeader.foreground": Color.snowDark0,
        }
    ]
)


def main():
    # Sunrise.save()
    Twilight.save()
    print("Themes generated successfully!")


if __name__ == "__main__":
    main()
