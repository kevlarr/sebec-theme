"""
Textmate token color assignments.

See:
- https://macromates.com/manual/en/language_grammars#naming_conventions
"""
from sebec.color import Color
from sebec.vstheme.base import TextmateToken as Token, TokenStyle as Style
from sebec.util import merge_color_maps


_todo = [
    "comment",
    "punctuation.definition.decorator", # `@` for decorators
    "variable.parameter.function-call", # eg. keyword arguments
    "variable.parameter.function-call",
]


_final = {
    ##
    ## Twilight
    ##
    **{
        Color.Twilight7: [
        ],
    },
    ##
    ## Sapphire
    ##
    **{
        Style(Color.Sapphire0, italic=True): [
            "comment"
        ],
        Color.Sapphire1: [
            "keyword.control.flow", # eg. `if`, `while`
            "keyword.control.import",
            "punctuation.separator", # eg. `,`, `.` in method calls, or `:` in dicts
            "punctuation.section.class.begin", # eg. `:` after class def
            "punctuation.section.function.begin", # eg. `:` after function def
        ],
        Style(Color.Sapphire1, bold=True): [
            "storage.type.class",
            "storage.type.function",
        ],
    },
    ##
    ## Sunrise
    ##
    **{
        Color.Sunrise0: [
        ],
        Style(Color.Sunrise0, italic=True): [
        ],
        Color.Sunrise1: [
        ],
        Color.Sunrise2: [
        ],
        Color.Sunrise3: [
        ],
        Color.Sunrise4: [
        ],
        Color.Sunrise5: [
        ],
        Color.Sunrise6: [
        ],
        Color.Sunrise7: [
        ],
    },
    ##
    ## Cerulean
    ##
    **{
        Color.Cerulean0: [
            "meta.function-call.arguments keyword.operator.assignment", # The `=` in keyword args
            "variable.parameter.function-call",
        ],
    },
    ##
    ## Spruce
    ##
    Style(Color.Spruce0, italic=True): [
        "punctuation.definition.string", # quotes around the string
    ],
    Style(Color.Spruce2, italic=True): [
        "string",
    ],
    Color.Spruce2: [
        "constant.numeric",
        "constant.language",
    ],

    "#ff0000": [
    ]
}


TEXTMATE_TOKENS = merge_color_maps(_final)
