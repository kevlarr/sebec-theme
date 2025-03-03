from sebec.vstheme.base import Color, SemanticToken as Token

SEMANTIC_TOKENS = {
    ##
    ## Blue
    ##
    Color.sapphire2: [
        Token("class", "typeHint"),
    ],
    Color.cerulean0: [
        Token("function", "decorator"),
        "parameter",
    ],
    Color.cerulean1.style(bold=True): [
        "selfParameter",
    ],

    ##
    ## Accent
    ##
    Color.solarPurple0: [
    ],
    Color.solarPurple0.style(bold=True): [
    ],
    Color.solarPurple1: [
        "class",
    ],

    ##
    ## White
    ##
    Color.sunrise0: [
        Token("property", "declaration"),
    ],
    Color.sunrise0.style(bold=True): [
        Token("class", "declaration"),
        Token("method", "declaration"),
        Token("variable", "readonly"),
    ],
    Color.shine2.style(bold=True): [
    ],

    # Color.cerulean0: [
    # ],
}
