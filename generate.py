import dataclasses
import enum
import json


PATH_TEMPLATE = "themes/{name}-color-theme.json"


class ThemeCategory(enum.StrEnum):
    light = "light"
    dark = "dark"


class Color(enum.StrEnum):
    # Muted light beige spectrum inspired by the faint light of dawn before the sun breaks
    sunrise0 = "#C2C0B7"
    sunrise1 = "#CBCAC2"
    sunrise2 = "#D7D5CC"
    sunrise3 = "#E0DFD6"
    sunrise4 = "#EAE8E1"
    sunrise5 = "#F0EFEA"
    sunrise6 = "#F6F6F3"

    # Muted dark blue spectrum inspired by the deepening sky at dusk after the sun sets
    twilight0 = "#15181E"
    twilight1 = "#1B1F27"
    twilight2 = "#212630"
    twilight3 = "#2E3440"
    twilight4 = "#3B4352"
    twilight5 = "#444D5E"
    twilight6 = "#4C566A"

    # Spectrum of soft whites resembling the shine of stars or the highlights on waves
    shine0 = "#ABB3C4"
    shine1 = "#B6BECE"
    shine2 = "#C0C8D8"
    shine3 = "#CCD3E0"
    shine4 = "#D9DEE8"
    shine5 = "#E5E9F0"
    shine6 = "#EDF0F5"

    # Brighter, warmer blues of the water reflecting the midday sky
    cerulean0 = "#4C9DB8"
    cerulean1 = "#69ADC4"
    cerulean2 = "#88BED0"

    # Darker, cooler blues of the water reflecting the dusk sky
    sapphire0 = "#405C82"
    sapphire1 = "#4A6A96"
    sapphire2 = "#5C7EAE"
    sapphire3 = "#819CC1"

    # Cooler greens of spruce
    spruce0 = "#5E9C87"
    spruce1 = "#76AD9B"
    spruce2 = "#8FBCAD"

    # Warmer greens of cedar
    cedar0 = "#7DA05A"
    cedar1 = "#91B073"
    cedar2 = "#A5BE8C"

    # Accent colors reminiscent of the rising and setting sun
    solarPurple0 = "#A3759C"
    solarPurple1 = "#B48EAE"
    solarRed0 = "#AE474F"
    solarRed1 = "#BF6169"
    solarOrange0 = "#C66F52"
    solarOrange1 = "#D08870"
    solarYellow0 = "#E5BB67"
    solarYellow1 = "#EBCB8B"


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
    color_sections=[
        {
            # "editor.background": "#f5f5f5",
            # "editor.foreground": "#333333",
            # "list.activeSelectionIconForeground": "#fff"
            "editor.background": Color.sunrise5,
            # "sideBar.background": "#E0E0D6",
            # "sideBar.foreground": Color.polar3,
            # "panel.background": "#EAE8E1",
            # "editorWidth.background": "#F6F6F3",
        },
    ],
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
            "editor.background": Color.twilight2,
            # "editor.foreground": Color.snowDark1,
        },
        # https://code.visualstudio.com/api/references/theme-color#editor-widget-colors
        {
            # "editorWidget.background": Color.polar0,
            # "editorWidget.foreground": Color.snowDark2,
            # "editorWidget.resizeBorder": C.waveAqua1,
        },
        # https://code.visualstudio.com/api/references/theme-color#side-bar
        {
            # "sideBar.background": Color.polarDark0,
            # "sideBar.foreground": Color.snowDark0,
            # "sideBarSectionHeader.background": Color.polarDark1,
            # "sideBarSectionHeader.foreground": Color.snowDark0,
        },
        # https://code.visualstudio.com/api/references/theme-color#panel-colors
        {
            # "panel.background": Color.polarDark2,
        },
        # https://code.visualstudio.com/api/references/theme-color#integrated-terminal-colors
        {
            # "terminal.foreground": Color.snowDark1,
        },
    ]
)


def export_palette():
    midpoint = int("ffffff", 16) // 2
    body = ""

    for i, (color_name, color_value) in enumerate(Color.__members__.items()):
        color_int = int(color_value[1:], 16)
        relative_difference = abs(color_int - midpoint) / midpoint

        if color_int < midpoint:
            if relative_difference > 0.88:
                brightness = 10
            elif relative_difference > 0.8:
                brightness = 7
            elif relative_difference > 0.6:
                brightness = 4
            elif relative_difference > 0.4:
                brightness = 2.25
            else:
                brightness = 1.75
        else:
            if relative_difference > 0.88:
                brightness = 0.7
            elif relative_difference > 0.8:
                brightness = 0.6
            elif relative_difference > 0.6:
                brightness = 0.5
            elif relative_difference > 0.4:
                brightness = 0.4
            else:
                brightness = 0.3

        divStyle = f'style="background-color: {color_value};"'
        buttonStyle = f'style="color: {color_value}; filter: brightness({brightness})"'

        body += f'''<div
            class="swatch" {divStyle}
            data-color-value="{color_value}"
            data-color-name="{color_name}"
        >'''
        body += f'''<button
            class="swatch-name"
            {buttonStyle}>{color_name}</button>'''
        body += f'''<button
            class="swatch-value"
            {buttonStyle}>{color_value}</button>'''
        body += f'</div>'

    script = f"""
    function copyText(text) {{
        const textArea = document.createElement('textarea');
        textArea.value = text;
        document.body.appendChild(textArea);
        textArea.focus({{preventScroll:true}});
        textArea.select();

        try {{
            document.execCommand('copy');
        }} catch (err) {{
            alert('Unable to copy to clipboard', err);
        }}

        document.body.removeChild(textArea);
    }}

    window.onload = function() {{
        const swatchNames = document.querySelectorAll('.swatch-name');
        swatchNames.forEach(name => {{
            const paletteColor = `Color.${{name.textContent}}`;
            name.addEventListener('click', () => copyText(paletteColor));
        }});
        const swatchValues = document.querySelectorAll('.swatch-value');
        swatchValues.forEach(value => {{
            const hex = value.textContent.slice(1);
            value.addEventListener('click', () => copyText(hex));
        }});
    }};
    """

    page = f'''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Nunito:wght@200..1000&display=swap" rel="stylesheet">
        <script>{script}</script>
    </head>
    <body>{body}</body>
    <style>
        body {{
            background-color: black;
            display: flex;
            flex-wrap: wrap;
            font-family: 'Nunito', sans-serif;
            gap: 1rem;
            padding: 1rem;
        }}
        button {{
            background-color: transparent;
            border: 0;
            cursor: pointer;
        }}
        button:hover {{
            transform: scale(1.1);
        }}
        button:active {{
            transform: scale(1.05);
        }}
        button, button:hover, button:active {{
            transition: all 0.1s ease;
        }}
        .swatch {{
            align-items: center;
            border-radius: 8px;
            display: flex;
            flex-direction: column;
            gap: 0.25rem;
            height: 64px;
            justify-content: center;
            width: 128px;
        }}
        .swatch-name,
        .swatch-value {{
            font-size: 16px;
        }}
        .swatch-name {{
            font-weight: 900;
        }}
        .swatch-value {{
            font-style: italic;
            font-weight: 100;
        }}
    </html>
    '''

    with open("output/palette.html", "w") as f:
        f.write(page)


def main():
    export_palette()
    Sunrise.save()
    Twilight.save()
    print("Themes and palette generated successfully!")


if __name__ == "__main__":
    main()
