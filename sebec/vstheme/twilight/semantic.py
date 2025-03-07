from sebec.color import Color
from sebec.vstheme.base import SemanticToken as Token, TokenStyle as Style
from sebec.util import merge_color_maps

_todo = [
    "method",
    "function",
    "function.decorator",
    "parameter.declaration", # declaration of params
    "selfParameter",
    "variable.readonly", # usage of CONSTANTS
    "variable.readonly.declaration", # declaration of CONSTANTS

    # `paramter` is tough because it overrides textmate grammer
    # for keyword args
    #
    # "parameter", # usage/declaration of params
]


_final = {
    ##
    ## Twilight
    ##
    **{
    },
    ##
    ## Shine
    ##
    **{
    },
    ##
    ## Sunrise
    ##
    **{
        Color.Sunrise0: [
        ],
        Style(Color.Sunrise0, italic=True): [
            "class.typeHint",
        ],
        Color.Sunrise1: [
        ],
        Color.Sunrise2: [
        ],
        Color.Sunrise3: [
            "property.declaration",
        ],
        Style(Color.Sunrise3, bold=True): [
        ],
        Style(Color.Sunrise1, underline=True): [
            "module",
        ],
        Color.Sunrise4: [
        ],
        Color.Sunrise5: [
        ],
        Color.Sunrise6: [
        ],
        Color.Sunrise7: [
            "class",
            "property.declaration",
        ],
        Style(Color.Sunrise7, bold=True): [
        ],
    },
    ##
    ## Blues
    ##
    **{
        Color.Sapphire0: [
        ],
        Color.Cerulean2: [
            "function",
        ],
        Style(Color.Cerulean3, bold=True): [
            "class",
            "class.declaration",
            "function.declaration",
            "method.declaration",
        ],
    },
    ##
    ## Greens
    ##
    **{
    },
    ##
    ## Solar
    ##
    **{
        Color.SolarPurple0: [
        ],
        Style(Color.SolarPurple0, bold=True): [
        ],
    },
}

SEMANTIC_TOKENS = merge_color_maps(_final)
