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
    Semantic("variable.readonly"), # usage of CONSTANTS
    Semantic("variable.readonly.declaration"), # declaration of CONSTANTS

    Textmate("variable.parameter.function-call"), # eg. keyword arguments
]

_twilight = {
    Color.Twilight7: [
        Textmate([
            "punctuation.definition",
            "punctuation.separator",              # eg. `,`, `.` in method calls, or `:` in dicts
            "punctuation.section.class.begin",    # eg. `:` after class def
            "punctuation.section.function.begin", # eg. `:` after function def
        ], name="low-contrast punctuation"),
        Textmate("meta.function-call.arguments keyword.operator.assignment", name="keyword argument '=' sign"),
    ],
}
_sunrise = {
    Style(Color.Sunrise0, underline=True): [
        Semantic("module"),
    ],
    Style(Color.Sunrise1, bold=True): [
        # Semantic("parameter"),
        Semantic("selfParameter"),
    ],
    Color.Sunrise4: [
    ],
    Style(Color.Sunrise5, bold=True): [
    ],
    Color.Sunrise5: [
    ],
    Style(Color.Sunrise5, bold=True): [
    ],
    Color.Sunrise6: [
    ],
}
_sapphire = {
    Style(Color.Sapphire0, italic=True): [
    ],
    Color.Sapphire1: [
        Textmate("keyword.control.flow"), # eg. `if`, `while`
        Textmate("keyword.control.import"),
    ],
    Style(Color.Sapphire1, bold=True): [
        Textmate(["storage.type.class", "storage.type.function"], name="class & def keywords"),
    ],
    Color.Sapphire2: [
        Textmate("variable.parameter.function-call", name="keyword arguments"),
    ],
}
_cerulean = {
    Style(Color.Cerulean0, italic=True): [
    ],
    Color.Cerulean1: [
        Textmate("punctuation.definition.decorator"), # `@` for decorators
    ],
    Style(Color.Cerulean1, italic=True): [
        Semantic("class.typeHint"),
    ],
    Color.Cerulean3: [
        Semantic("class"),
        Semantic("function"),
        Semantic("method"),
        Semantic("function.decorator"),
    ],
    Style(Color.Cerulean3, bold=True): [
        Semantic("class.declaration"),
        Semantic("function.declaration"),
        Semantic("method.declaration"),
    ],
}
_cedar = {

}
_spruce = {
    Style(Color.Spruce0, italic=True): [
        Textmate(["comment", "punctuation.definition.comment"]),
    ],
}
_solar = {
    Color.SolarOrange1: [
        Semantic("property"),
        Semantic("property.declaration"),
    ],
    Style(Color.SolarPurple0, italic=True): [
        Textmate("punctuation.definition.string"), # quotes around the string
    ],
    Style(Color.SolarPurple1, italic=True): [
        Textmate("string"),
    ],
    Color.SolarPurple1: [
        Textmate("constant.numeric"),
        Textmate("constant.language"),
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
