from sebec.vstheme.base import Color, SemanticToken as Token

SEMANTIC_TOKENS = {
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
    Color.Cerulean1.style(bold=True): [
        "selfParameter",
    ],

    ##
    ## Accent
    ##
    Color.SolarPurple0: [
    ],
    Color.SolarPurple0.style(bold=True): [
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
    Color.Sunrise0.style(bold=True): [
        Token("class", "declaration"),
        Token("method", "declaration"),
        Token("variable", "readonly"),
    ],
    Color.Shine2.style(bold=True): [
    ],

    # Color.Cerulean0: [
    # ],
}
