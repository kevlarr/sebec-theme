from sebec.palette import Color
from sebec.vstheme.base import Scope as Scope


ColorScopes = dict[str, list[Scope | str]]


def merge_scopes(*css: ColorScopes) -> ColorScopes:
    merged = {}
    for cs in css:
        for color, scopes in cs.items():
            existing_scopes = merged.setdefault(color, [])
            existing_scopes.extend(scopes)
    return merged


# For help on scopes see:
# https://github.com/dunstontc/textmate/blob/master/scopes.md

TEMP: ColorScopes = {
    "#ff0000": [
        # "storage.type",
        # "support.type",
        # "punctuation", # Includes `@` in decorator, ->, `.` in method calls, etc.
    ],
    Color.shine2: [
        "variable.parameter.function",
    ],
    Color.sapphire2: [
        "meta.function",
        "constant.language meta.function", # Constant in function signature, type or return
        "meta.function.parameters",
        "keyword.operator",
    ],
    Color.cerulean0: [
    ],
    Color.cerulean1: [
    ],
    Color.cerulean2: [
    ],
}

_literals = {
    Color.solarPurple1: [
        "constant.numeric",
        "constant.character",
        "constant.language", # Eg. `True`
    ],
    Color.spruce0: [
        "punctuation.definition.string",
    ],
    Color.spruce1: [
        "string",
    ],
}

_misc = {
    Color.shine2: [
        Scope("constant.other", fontStyle="bold"), # Eg. CONSTANT variable names, css colors, etc.},
    ],
    Color.cerulean0: [
        Scope("entity.name.function.decorator", fontStyle="regular"), # regular to override bold
    ],
    Color.cerulean1: [
        # "variable.other",
        # "support.variable",
        Scope("entity.name.function.member", fontStyle="bold"),
        Scope("entity.name.type.class", fontStyle="bold"),
    ],
    Color.sapphire2: [
        "keyword",
        "storage.type",
    ],
}

# ALL = merge(TEMP, _literals, _misc, {
SCOPE_SETTINGS = merge_scopes(_literals, _misc, {
    # Color.sapphire1: [
        # Scope(
            # "comment",
            # "comment.documentation",
            # "comment.block.documentation",
            # "punctuation.definition.comment",
            # fontStyle="italic",
        # ),
    # ],

    # Color.sapphire2: [
        # "keyword",
        # "storage.type",
    # ],

    # Color.solarPurple0: [
        # "constant.other", # Eg. CONSTANT variable names, css colors, etc.
        # "constant.numeric",
        # "constant.character",
        # "constant.language", # Eg. `True`
    # ],

    # Color.cedar0: [
        # "punctuation.definition.string",
    # ],
    # Color.cedar1: [
        # "string",
    # ]
})

TOKEN_COLORS = [
    # TokenColor(
        # name="Punctuation",
        # scope="punctuation",
        # settings={
            # "foreground": Color.sapphire0,
        # }
    # ),
    # TokenColor(
        # name="Comments: Preprocessor",
        # scope="comment.block.preprocessor",
        # settings={
            # "fontStyle": "",
            # "foreground": "#AAAAAA"
        # }
    # ),
    # TokenColor(
        # name="Invalid - Illegal",
        # scope="invalid.illegal",
        # settings={
            # "foreground": "#660000"
        # }
    # ),
    # TokenColor(
        # name="Language Constants",
        # scope=[
            # "constant.language",
            # "support.constant",
            # "variable.language"
        # ],
        # settings={
            # "foreground": "#AB6526"
        # }
    # ),

    # FIXME: Too much color
    # TokenColor(
        # name="Variables",
        # scope=[
            # "variable",
            # "support.variable"
        # ],
        # settings={
            # "foreground": Color.cerulean0,
        # }
    # ),

    # TokenColor(
        # name="Functions",
        # scope=[
            # "entity.name.function",
            # "support.function"
        # ],
        # settings={
            # "fontStyle": "bold",
            # "foreground": Color.sapphire3,
        # }
    # ),

    # FIXME: This colorizes types (dataclass attributes, )
    # TokenColor(
        # name="Classes",
        # scope=[
            # "entity.name.type",
            # "entity.other.inherited-class",
            # "support.class"
        # ],
        # settings={
            # "fontStyle": "bold",
            # "foreground": Color.sapphire3,
        # }
    # ),

    # TokenColor(
        # name="Exceptions",
        # scope="entity.name.exception",
        # settings={
            # "foreground": "#660000"
        # }
    # ),
    # TokenColor(
        # name="Sections",
        # scope="entity.name.section",
        # settings={
            # "fontStyle": "bold"
        # }
    # ),


    # TokenColor(
        # name="Strings: Escape Sequences",
        # scope="constant.character.escape",
        # settings={
            # "foreground": "#777777"
        # }
    # ),
    # TokenColor(
        # name="Strings: Regular Expressions",
        # scope="string.regexp",
        # settings={
            # "foreground": "#4B83CD"
        # }
    # ),
    # TokenColor(
        # name="Strings: Symbols",
        # scope="constant.other.symbol",
        # settings={
            # "foreground": "#AB6526"
        # }
    # ),

    # TokenColor(
        # name="HTML: Doctype Declaration",
        # scope=[
            # "meta.tag.sgml.doctype",
            # "meta.tag.sgml.doctype string",
            # "meta.tag.sgml.doctype entity.name.tag",
            # "meta.tag.sgml punctuation.definition.tag.html"
        # ],
        # settings={
            # "foreground": "#AAAAAA"
        # }
    # ),
    # TokenColor(
        # name="HTML: Tags",
        # scope=[
            # "meta.tag",
            # "punctuation.definition.tag.html",
            # "punctuation.definition.tag.begin.html",
            # "punctuation.definition.tag.end.html"
        # ],
        # settings={
            # "foreground": "#91B3E0"
        # }
    # ),
    # TokenColor(
        # name="HTML: Tag Names",
        # scope="entity.name.tag",
        # settings={
            # "foreground": "#4B83CD"
        # }
    # ),
    # TokenColor(
        # name="HTML: Attribute Names",
        # scope=[
            # "meta.tag entity.other.attribute-name",
            # "entity.other.attribute-name.html"
        # ],
        # settings={
            # "fontStyle": "italic",
            # "foreground": "#91B3E0"
        # }
    # ),
    # TokenColor(
        # name="HTML: Entities",
        # scope=[
            # "constant.character.entity",
            # "punctuation.definition.entity"
        # ],
        # settings={
            # "foreground": "#AB6526"
        # }
    # ),
    # TokenColor(
        # name="CSS: Selectors",
        # scope=[
            # "meta.selector",
            # "meta.selector entity",
            # "meta.selector entity punctuation",
            # "entity.name.tag.css"
        # ],
        # settings={
            # "foreground": "#7A3E9D"
        # }
    # ),
    # TokenColor(
        # name="CSS: Property Names",
        # scope=[
            # "meta.property-name",
            # "support.type.property-name"
        # ],
        # settings={
            # "foreground": "#AB6526"
        # }
    # ),
    # TokenColor(
        # name="CSS: Property Values",
        # scope=[
            # "meta.property-value",
            # "meta.property-value constant.other",
            # "support.constant.property-value"
        # ],
        # settings={
            # "foreground": "#448C27"
        # }
    # ),
    # TokenColor(
        # name="CSS: Important Keyword",
        # scope="keyword.other.important",
        # settings={
            # "fontStyle": "bold"
        # }
    # ),
    # TokenColor(
        # name="Markup: Changed",
        # scope="markup.changed",
        # settings={
            # "foreground": "#000000"
        # }
    # ),
    # TokenColor(
        # name="Markup: Deletion",
        # scope="markup.deleted",
        # settings={
            # "foreground": "#000000"
        # }
    # ),
    # TokenColor(
        # name="Markup: Emphasis",
        # scope="markup.italic",
        # settings={
            # "fontStyle": "italic"
        # }
    # ),
    # TokenColor(
        # name="Markup: Error",
        # scope="markup.error",
        # settings={
            # "foreground": "#660000"
        # }
    # ),
    # TokenColor(
        # name="Markup: Insertion",
        # scope="markup.inserted",
        # settings={
            # "foreground": "#000000"
        # }
    # ),
    # TokenColor(
        # name="Markup: Link",
        # scope="meta.link",
        # settings={
            # "foreground": "#4B83CD"
        # }
    # ),
    # TokenColor(
        # name="Markup: Output",
        # scope=[
            # "markup.output",
            # "markup.raw"
        # ],
        # settings={
            # "foreground": "#777777"
        # }
    # ),
    # TokenColor(
        # name="Markup: Prompt",
        # scope="markup.prompt",
        # settings={
            # "foreground": "#777777"
        # }
    # ),
    # TokenColor(
        # name="Markup: Heading",
        # scope="markup.heading",
        # settings={
            # "foreground": "#AA3731"
        # }
    # ),
    # TokenColor(
        # name="Markup: Strong",
        # scope="markup.bold",
        # settings={
            # "fontStyle": "bold"
        # }
    # ),
    # TokenColor(
        # name="Markup: Traceback",
        # scope="markup.traceback",
        # settings={
            # "foreground": "#660000"
        # }
    # ),
    # TokenColor(
        # name="Markup: Underline",
        # scope="markup.underline",
        # settings={
            # "fontStyle": "underline"
        # }
    # ),
    # TokenColor(
        # name="Markup Quote",
        # scope="markup.quote",
        # settings={
            # "foreground": "#7A3E9D"
        # }
    # ),
    # TokenColor(
        # name="Markup Lists",
        # scope="markup.list",
        # settings={
            # "foreground": "#4B83CD"
        # }
    # ),
    # TokenColor(
        # name="Markup Styling",
        # scope=[
            # "markup.bold",
            # "markup.italic"
        # ],
        # settings={
            # "foreground": "#448C27"
        # }
    # ),
    # TokenColor(
        # name="Markup Inline",
        # scope="markup.inline.raw",
        # settings={
            # "fontStyle": "",
            # "foreground": "#AB6526"
        # }
    # ),
    # TokenColor(
        # name="Extra: Diff Range",
        # scope=[
            # "meta.diff.range",
            # "meta.diff.index",
            # "meta.separator"
        # ],
        # settings={
            # "foreground": "#434343"
        # }
    # ),
    # TokenColor(
        # name="Extra: Diff From",
        # scope="meta.diff.header.from-file",
        # settings={
            # "foreground": "#434343"
        # }
    # ),
    # TokenColor(
        # name="Extra: Diff To",
        # scope="meta.diff.header.to-file",
        # settings={
            # "foreground": "#434343"
        # }
    # ),
]
