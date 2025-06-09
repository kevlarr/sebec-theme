from typing import Annotated

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

from .formatters import parse_color_style, parse_token_color_style


class Base(BaseModel):
    model_config = ConfigDict(extra="forbid")


class ColorStyle(Base):
    foreground: str
    alpha: float | None = None

    def __str__(self) -> str:
        """Returns a string representation of the color with alpha level, if present."""
        if self.alpha is not None:
            return f"{self.foreground}{int(self.alpha * 255):02x}"
        return str(self.foreground)


class TokenColorStyle(ColorStyle):
    bold: bool = False
    italic: bool = False
    strikethrough: bool = False
    underline: bool = False

    def serialize(self) -> dict | str:
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


ParsedColorStyle = Annotated[
    ColorStyle,
    BeforeValidator(parse_color_style),
]


ParsedTokenColorStyle = Annotated[
    TokenColorStyle,
    BeforeValidator(parse_token_color_style),
]


class MultiColorStyle(Base):
    light: ParsedColorStyle
    dark: ParsedColorStyle


class MultiTokenColorStyle(Base):
    light: ParsedTokenColorStyle
    dark: ParsedTokenColorStyle


ColorSetting = ParsedColorStyle | MultiColorStyle
TokenColorSetting = ParsedTokenColorStyle | MultiTokenColorStyle
