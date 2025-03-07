"""
Textmate & semantic token color assignments.

See:
- https://macromates.com/manual/en/language_grammars#naming_conventions
"""
from sebec.color import Color
from sebec.vstheme.base.tokens import Semantic, Textmate, TokenStyle as Style
from sebec.util import merge_color_maps


_todo = [
    Semantic("method"),
    Semantic("function"),
    Semantic("function.decorator"),
    Semantic("variable.readonly"), # usage of CONSTANTS
    Semantic("variable.readonly.declaration"), # declaration of CONSTANTS

    # `paramter` is tough because it overrides textmate grammer
    # for keyword args
    #
    # Semantic("parameter"), # usage/declaration of params

    Textmate("punctuation.definition.decorator"), # `@` for decorators
    Textmate("variable.parameter.function-call"), # eg. keyword arguments

]

_twilight = {
    Color.Twilight7: [
    ],
}
_sunrise = {
    Color.Sunrise0: [
    ],
    Style(Color.Sunrise0, italic=True): [
        Semantic("class.typeHint"),
    ],
    Color.Sunrise1: [
    ],
    Style(Color.Sunrise1, underline=True): [
        Semantic("module"),
    ],
    Color.Sunrise2: [
    ],
    Color.Sunrise3: [
        Semantic("property.declaration"),
    ],
    Color.Sunrise4: [
    ],
    Color.Sunrise5: [
        Semantic("parameter"),
    ],
    Style(Color.Sunrise5, bold=True): [
    ],
    Color.Sunrise6: [
    ],
    Color.Sunrise7: [
        Semantic("class"),
        Semantic("parameter.declaration"),
        Semantic("property.declaration"),
    ],
    Style(Color.Sunrise7, bold=True): [
        Semantic("selfParameter"),
    ],
}
_sapphire = {
    Style(Color.Sapphire0, italic=True): [
        Textmate("comment"),
    ],
    Color.Sapphire1: [
        Textmate("keyword.control.flow"), # eg. `if`, `while`
        Textmate("keyword.control.import"),
        # Textmate([
            # "punctuation.separator",              # eg. `,`, `.` in method calls, or `:` in dicts
            # "punctuation.section.class.begin",    # eg. `:` after class def
            # "punctuation.section.function.begin", # eg. `:` after function def
        # ], name="low-contrast punctuation")
    ],
    Style(Color.Sapphire1, bold=True): [
        Textmate(["storage.type.class", "storage.type.function"], name="class & def keywords")
    ],

}
_cerulean = {
    Color.Cerulean0: [
    ],
    Color.Cerulean2: [
    ],
    Color.Cerulean3: [
        Semantic("function"),
        Semantic("method"),
    ],
    Style(Color.Cerulean3, bold=True): [
        Semantic("class"),
        Semantic("class.declaration"),
        Semantic("function.declaration"),
        Semantic("method.declaration"),
    ],
}
_cedar = {

}
_spruce = {
    Style(Color.Spruce0, italic=True): [
        Textmate("punctuation.definition.string"), # quotes around the string
    ],
    Style(Color.Spruce2, italic=True): [
        Textmate("string"),
    ],
    Color.Spruce2: [
        Textmate("constant.numeric"),
        Textmate("constant.language"),
    ],
}
_solar = {
    Color.SolarPurple0: [
        Textmate([
            "meta.function-call.arguments keyword.operator.assignment",
            "variable.parameter.function-call",
        ], name="Keyword arguments w/ = sign")
    ],

}

COLOR_TOKENS = {
    **_twilight,
    **_sunrise,
    **_sapphire,
    **_cerulean,
    **_cedar,
    **_spruce,
    **_solar,
    **{
        "#ff0000": [
        ]
    }
}
