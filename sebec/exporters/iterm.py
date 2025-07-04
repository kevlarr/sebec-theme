"""Utilities for writing .itermcolors files.

A single file has three different key/dict pairs for all colors:

    * Default, eg. "Ansi 0 Color"
    * Dark, eg. "Ansi 0 Color (Dark)"
    * Light, eg. "Ansi 0 Color (Light)"

Generating the file requires both light & dark terminal themes.
"""
from pathlib import Path
from xml.etree import ElementTree

from sebec.models.styles import ThemeStyle
from sebec.models.terminal import TerminalApp
from sebec.models.theme import ThemeModel


# `xml` does not have facility for writing the `<!DOCTYPE>` element, so the header
# should be written manually to include it.
_header = (
    b'<?xml version="1.0" encoding="UTF-8"?>\n'
    b'<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">\n'
)


def export(destination: Path, theme: ThemeModel):
    filename = f"{theme.name}.itermcolors"

    root = ElementTree.Element("plist", version="1.0")
    root_dict = ElementTree.SubElement(root, "dict")

    default_colors = dark_colors = theme.terminal.serialize(TerminalApp.Iterm, ThemeStyle.Dark)
    light_colors = theme.terminal.serialize(TerminalApp.Iterm, ThemeStyle.Light)

    _append_colors(root_dict, default_colors)

    # The additional color specifications with these exact suffixes are
    # what enable this to be a dual-mode theme
    _append_colors(root_dict, dark_colors, suffix="(Dark)")
    _append_colors(root_dict, light_colors, suffix="(Light)")

    tree = ElementTree.ElementTree(root)
    ElementTree.indent(tree, "\t")

    with open(destination / filename, "wb") as color_file:
        color_file.write(_header)
        tree.write(color_file, encoding="utf-8", xml_declaration=False)


def _append_colors(parent, color_map: dict[str, str], *, suffix: str = None):
    for key, value in color_map.items():
        if suffix:
            key += f" {suffix}"

        key_elem = ElementTree.SubElement(parent, "key")
        key_elem.text = key

        dict_color = ElementTree.SubElement(parent, "dict")
        color_space = ElementTree.SubElement(dict_color, "key")
        color_space.text = "Color Space"
        color_space_value = ElementTree.SubElement(dict_color, "string")
        color_space_value.text = "P3"

        if len(value) == 4:
            r, g, b = value[1:]
        elif len(value) in (7, 9):
            r, g, b = value[1:3], value[3:5], value[5:]
        else:
            raise ValueError(f"expected 3- or 6- character hex string; received {value}")

        red = ElementTree.SubElement(dict_color, "key")
        red.text = "Red Component"
        red_value = ElementTree.SubElement(dict_color, "real")
        red_value.text = str(int(r, 16) / 255.0)

        green = ElementTree.SubElement(dict_color, "key")
        green.text = "Green Component"
        green_value = ElementTree.SubElement(dict_color, "real")
        green_value.text = str(int(g, 16) / 255.0)

        blue = ElementTree.SubElement(dict_color, "key")
        blue.text = "Blue Component"
        blue_value = ElementTree.SubElement(dict_color, "real")
        blue_value.text = str(int(b, 16) / 255.0)

        alpha = ElementTree.SubElement(dict_color, "key")
        alpha.text = "Alpha Component"
        alpha_value = ElementTree.SubElement(dict_color, "real")
        alpha_value.text = "1"
