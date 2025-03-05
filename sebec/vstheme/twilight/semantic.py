from sebec.color import Color
from sebec.vstheme.base import SemanticToken as Token, TokenStyle as Style
from sebec.util import merge_color_maps


_final = {

}


SEMANTIC_TOKENS = merge_color_maps(_final)

xSEMANTIC_TOKENS = {
    ##
    ## Blue
    ##
    Color.Sapphire2: [
        Token("class", "typeHint"),
    ],
    Color.Cerulean0: [
        Token("function", "decorator"),
        "parameter",
    ],
    Style(Color.Cerulean1, bold=True): [
        "selfParameter",
    ],

    ##
    ## Accent
    ##
    Color.SolarPurple0: [
    ],
    Style(Color.SolarPurple0, bold=True): [
    ],
    Color.SolarPurple1: [
        "class",
    ],

    ##
    ## White
    ##
    Color.Sunrise0: [
        Token("property", "declaration"),
    ],
    Style(Color.Sunrise0, bold=True): [
        Token("class", "declaration"),
        Token("method", "declaration"),
        Token("variable", "readonly"),
    ],
    Style(Color.Shine2, bold=True): [
    ],

    # Color.Cerulean0: [
    # ],
}
