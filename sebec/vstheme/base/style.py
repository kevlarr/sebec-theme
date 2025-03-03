import dataclasses


@dataclasses.dataclass(eq=True, frozen=True)
class ColorStyle:
    """Style object suitable for theming tokens and UI elements alike."""
    foreground: str
    """Hexadecimal color code, with or without alpha level"""

    alpha: float | None = None
    """Alpha level in the range [0.0, 1.0]"""

    def serialize(self) -> str:
        """Returns a string representation of the color with alpha level, if present."""
        if self.alpha is not None:
            return f"{self.foreground}{int(self.alpha * 255):02x}"
        return self.foreground


@dataclasses.dataclass(eq=True, frozen=True)
class TokenStyle(ColorStyle):
    """Style object suitable for theming Textmate and semantic tokens."""

    bold: bool | None = None
    """Whether the text should be rendered in bold"""

    italic: bool | None = None
    """Whether the text should be rendered in italic"""

    underline: bool | None = None
    """Whether the text should be underlined"""

    def serialize(self) -> dict | str:
        """Returns a dict with the foreground color and a font style string
        suitable for Textmate and semantic tokens if any styles arepresent,
        otherwise returns the foreground color as a string."""
        color = super().serialize()

        font_style = ""
        if self.bold is True:
            font_style += "bold"
        if self.italic is True:
            font_style += " italic"
        if self.underline is True:
            font_style += " underline"

        if font_style:
            return {"foreground": color, "fontStyle": font_style.strip()}

        return color
