"""
Textmate token color assignments.

See:
- https://macromates.com/manual/en/language_grammars#naming_conventions
"""
from sebec.vstheme.base import Color, TextmateToken as Token

TEXTMATE_TOKENS = {
    Color.Sapphire0.style(italic=True): [
        Token("comment"),
    ],
    Color.Sapphire2: [
        Token("keyword.control", "keyword.operator", "keyword.other"),
    ],
    Color.Sapphire2.style(bold=True): [
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
