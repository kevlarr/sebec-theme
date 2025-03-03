from sebec.vstheme.base import Color, TextmateToken as Token

TEXTMATE_TOKENS = {
    Color.sapphire0.style(italic=True): [
        Token("comment"),
    ],
    Color.sapphire2: [
        Token("keyword.control", "keyword.operator", "keyword.other"),
    ],
    Color.sapphire2.style(bold=True): [
        Token("storage.type.class", "storage.type.function"),
    ],

    Color.cerulean0: [
        "punctuation.definition.decorator",
    ],

    Color.solarPurple0: [
        "variable.parameter.function-call",
    ],


    Color.spruce0: [
        "string",
    ]
}
