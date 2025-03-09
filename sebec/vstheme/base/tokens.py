"""Utility classes for defining semantic & textmate tokens.

https://macromates.com/manual/en/language_grammars#naming_conventions
https://code.visualstudio.com/api/language-extensions/semantic-highlight-guide
https://code.visualstudio.com/api/language-extensions/semantic-highlight-guide#semantic-token-scope-map
"""
from dataclasses import dataclass

from sebec.color import ColorStyle


__all__ = ["Semantic", "Textmate"]


@dataclass(frozen=True)
class Semantic:
    """Semantic token selector in the form `name[.mod]*[:lang]?`."""
    value: str


@dataclass(frozen=True)
class Textmate:
    """Textmate token selector with optional name."""
    value: list[str] | str
    name: str | None = None


@dataclass(eq=True, frozen=True)
class TokenStyle(ColorStyle):
    """Style object suitable for theming Textmate and semantic tokens."""

    bold: bool | None = None
    """Whether or not the text should be rendered in bold"""

    italic: bool | None = None
    """Whether or not the text should be rendered in italic"""

    strikethrough: bool | None = None
    """Whether or not the text should be struck through"""

    underline: bool | None = None
    """Whether or not the text should be underlined"""

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
