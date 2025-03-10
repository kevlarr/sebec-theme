from pathlib import Path

from sebec.color import Color


def export_palette_html(destination: Path):
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

    with open(destination, "w") as f:
        f.write(page)
