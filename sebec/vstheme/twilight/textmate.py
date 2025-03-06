"""
Textmate token color assignments.

See:
- https://macromates.com/manual/en/language_grammars#naming_conventions
"""
from sebec.color import Color
from sebec.vstheme.base import TextmateToken as Token, TokenStyle as Style
from sebec.util import merge_color_maps


_final = {
    Color.Sapphire1: [
        "punctuation.separator",
    ],
    Color.Sapphire2: [
        "keyword.control",
    ],
    Style(Color.Cerulean1, italic=True): [
        Token("comment"),
    ],
    Color.Spruce0: [
        "punctuation.definition.string",
    ],
    Color.Spruce2: [
        "string",
    ]
}


TEXTMATE_TOKENS = merge_color_maps(_final)


xTEXTMATE_TOKENS = {
    Color.Sapphire2: [
        Token("keyword.control", "keyword.operator", "keyword.other", name="Keywords"),
    ],
    Style(Color.Sapphire2, bold=True): [
        Token("storage.type.class", "storage.type.function"),
    ],

    Color.Cerulean0: [
        "punctuation.definition.decorator",
    ],

    Color.SolarPurple0: [
        "variable.parameter.function-call",
    ],


    Color.Spruce0: [
        "string",
    ]
}
