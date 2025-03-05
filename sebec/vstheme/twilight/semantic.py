from sebec.color import Color
from sebec.vstheme.base import SemanticToken as Token, TokenStyle as Style
from sebec.util import merge_color_maps


_final = {
    ##
    ## Twilight
    ##
    **{
    },
    ##
    ## Sunrise
    ##
    **{
    },
    ##
    ## Shine
    ##
    **{
        Color.Shine0: [
            Token("property", "declaration"),
        ],
        Style(Color.Shine0, bold=True): [
            Token("class", "declaration"),
            Token("method", "declaration"),
            Token("variable", "readonly"),
        ],
        Style(Color.Shine2, bold=True): [
        ],
    },
    ##
    ## Blues
    ##
    **{
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
    },
}

SEMANTIC_TOKENS = merge_color_maps(_final)
