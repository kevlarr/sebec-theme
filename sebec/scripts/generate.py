from sebec.vstheme import Sunrise, Twilight
from sebec.vstheme.base import Color
import xml.etree.ElementTree as ET


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


def export_iterm_colors():
    """

LIGHT

** Basic **

foreground      twilight3
background      sunrise5
bold            twilight2
links           sapphire0
find match      solarYellow0
selection       sunrise1
selected text   twilight2

** ANSI **

black   todo     todo
red     todo     todo
green   cedar1 cedar0
yellow  todo  todo
blue    sapphire1     todo
magenta todo  todo
cyan    cerulean1     cerulean0
white   todo        todo


DARK

** Basic **

foreground      shine5
background      twilight2
bold            shine6
links           sapphire2
find match      sapphire3
selection       twilight6
selected text   shine6


** ANSI **

black   twilight2     twilight3
red     solarRed1     solarRed0
green   spruce1       spruce0
yellow  solarYellow1  solarYellow0
blue    sapphire2     sapphire1
magenta solarPurple1  solarPurple0
cyan    cerulean2     cerulean1
white   shine5        shine6
    """
    raise NotImplementedError()


# iterm name to vscode name
color_name_map = {
    "Ansi 0 Color": "ansiBlack",
    "Ansi 1 Color": "ansiRed",
    "Ansi 2 Color": "ansiGreen",
    "Ansi 3 Color": "ansiYellow",
    "Ansi 4 Color": "ansiBlue",
    "Ansi 5 Color": "ansiMagenta",
    "Ansi 6 Color": "ansiCyan",
    "Ansi 7 Color": "ansiWhite",
    "Ansi 8 Color": "ansiBrightBlack",
    "Ansi 9 Color": "ansiBrightRed",
    "Ansi 10 Color": "ansiBrightGreen",
    "Ansi 11 Color": "ansiBrightYellow",
    "Ansi 12 Color": "ansiBrightBlue",
    "Ansi 13 Color": "ansiBrightMagenta",
    "Ansi 14 Color": "ansiBrightCyan",
    "Ansi 15 Color": "ansiBrightWhite",
    "Background Color": "background",
    "Foreground Color": "foreground",
    "Selection Color": "selectionBackground",
}




def generate_iterm_colors():

    # ansi 0-15 each have 3:
    # - Ansi N Color
    # - Ansi N Color (Dark)
    # - Ansi N Color (Light)


    colors = {
        "Ansi 0 Color": Color.,
        "Ansi 1 Color": "#ff0000",
        "Ansi 2 Color": "#00ff00",
        "Ansi 3 Color": "#ffff00",
        "Ansi 4 Color": "#0000ff",
        "Ansi 5 Color": "#ff00ff",
        "Ansi 6 Color": "#00ffff",
        "Ansi 7 Color": "#ffffff",
        "Ansi 8 Color": "#808080",
        "Ansi 9 Color": "#ff0000",
        "Ansi 10 Color": "#00ff00",
        "Ansi 11 Color": "#ffff00",
        "Ansi 12 Color": "#0000ff",
        "Ansi 13 Color": "#ff00ff",
        "Ansi 14 Color": "#00ffff",
        "Ansi 15 Color": "#ffffff",
        "Background Color": "#000000",
        "Foreground Color": "#ffffff",
        "Cursor Color": "#ffffff",
        "Selection Color": "#44475a",
        "Selected Text Color": "#ffffff",
    }

    root = ET.Element("plist", version="1.0")
    dict_elem = ET.SubElement(root, "dict")

    for key, value in colors.items():
        key_elem = ET.SubElement(dict_elem, "key")
        key_elem.text = key
        dict_elem.append(key_elem)

        dict_color = ET.SubElement(dict_elem, "dict")
        color_space = ET.SubElement(dict_color, "key")
        color_space.text = "Color Space"
        color_space_value = ET.SubElement(dict_color, "string")
        color_space_value.text = "sRGB"

        red = ET.SubElement(dict_color, "key")
        red.text = "Red Component"
        red_value = ET.SubElement(dict_color, "real")
        red_value.text = str(int(value[1:3], 16) / 255.0)

        green = ET.SubElement(dict_color, "key")
        green.text = "Green Component"
        green_value = ET.SubElement(dict_color, "real")
        green_value.text = str(int(value[3:5], 16) / 255.0)

        blue = ET.SubElement(dict_color, "key")
        blue.text = "Blue Component"
        blue_value = ET.SubElement(dict_color, "real")
        blue_value.text = str(int(value[5:7], 16) / 255.0)

        alpha = ET.SubElement(dict_color, "key")
        alpha.text = "Alpha Component"
        alpha_value = ET.SubElement(dict_color, "real")
        alpha_value.text = "1"

    tree = ET.ElementTree(root)
    ET.indent(tree, "\t")
    with open("output/Sebec-test.itermcolors", "wb") as f:
        tree.write(f, encoding="utf-8", xml_declaration=True)

def main():
    export_palette()
    generate_iterm_colors()
    # Sunrise.save()
    Twilight.save()
    print("Themes and palette generated successfully!")
