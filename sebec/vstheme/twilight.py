from sebec.palette import Color
from .base import Theme, ThemeCategory


__all__ = ["Twilight"]


# TODO:
#   - lists/trees:
#     https://code.visualstudio.com/api/references/theme-color#lists-and-trees


_CEDAR_ELEMENTS = {
    Color.cedar0.alpha(0.5): [
    ],
    Color.cedar1: [
    ],
    Color.cedar2: [
    ],
}
_CERULEAN_ELEMENTS = {
    Color.cerulean0: [
        "inputValidation.infoBorder",
        "inputValidation.infoBackground",
        "textLink.foreground",
    ],
    Color.cerulean1: [
        "textLink.activeForeground",
    ],
    Color.cerulean2: [
    ],
}
_SAPPHIRE_ELEMENTS = {
    Color.sapphire0: [
        "activityBar.activeBorder",
        "button.background",
        "inputOption.hoverBackground",
        "sash.hoverBorder", # The drag border indicator on hover
        "scrollbarSlider.hoverBackground",
        "selection.background",
        "textBlockQuote.border",
        "toolbar.hoverBackground", # eg. hovering over icons in panels/widgets
        # "toolbar.hoverOutline", # eg. hovering over "..." icons, etc. in panels
    ],
    Color.sapphire1: [
    ],
    Color.sapphire2: [
        "button.hoverBackground",
        "inputOption.activeBackground",
        "scrollbarSlider.activeBackground",
    ],
    Color.sapphire3: [
    ],
}
_SPRUCE_ELEMENTS = {
    Color.spruce0.alpha(0.5): [
        "minimap.findMatchHighlight",
    ],
    Color.spruce0: [
        "activityBarBadge.background",
        "badge.background",
        "progressBar.background",
    ],
    Color.spruce1: [
    ],
    Color.spruce2: [
    ],
}
_SOLAR_ELEMENTS = {
    Color.solarPurple0: [
        "focusBorder",
        "minimap.selectionHighlight",
        "toolbar.activeBackground", # Eg. the "..." icons when opened or other buttons when clicked
    ],
    Color.solarPurple1: [
    ],
    Color.solarPurple1.alpha(0.25): [
        "sideBar.dropBackground",
    ],
    Color.solarRed0: [
        "minimap.errorHighlight",
        "activityErrorBadge.background",
        "inputValidation.errorBorder",
        "inputValidation.errorBackground",
    ],
    Color.solarRed1: [
        "errorForeground",
    ],
    Color.solarOrange0: [
        "inputValidation.warningBorder",
        "inputValidation.warningBackground",
    ],
    Color.solarYellow0: [
        "activityWarningBadge.background",
    ],

    Color.solarYellow0.alpha(0.5): [
        "minimap.warningHighlight",
    ],
}
_SHINE_ELEMENTS = {
    Color.shine0: [
        "activityBar.foreground",
        "descriptionForeground", # Eg. extension descriptions in search
        "sideBar.foreground",
        "sideBarTitle.foreground",
        "sideBarSectionHeader.foreground",
        "icon.foreground",
        "foreground",
    ],
    Color.shine1: [
        "terminal.foreground",
    ],
    Color.shine2: [
        "editor.foreground",
    ],
    Color.shine3: [
    ],
    Color.shine4: [
        "button.foreground",
        "checkbox.foreground",
        "dropdown.foreground",
        "editorWidget.foreground",
        "input.foreground",
        "inputValidation.errorForeground",
        "inputValidation.infoForeground",
        "inputValidation.warningForeground",
    ],
    Color.shine5: [
    ],
    Color.shine6: [
    ],
}
_TWILIGHT_ELEMENTS = {
    Color.twilight0: [
        "activityBarBadge.foreground",
        "activityErrorBadge.foreground",
        "activityWarningBadge.foreground",
        "badge.foreground",
        "checkbox.background",
        "dropdown.background",
        "input.background",
        # "inputValidation.errorBackground",
        "inputOption.activeBorder", # match input color to hide the border
        "minimap.background",
        "sideBar.background",
        "sideBarSectionHeader.background",
        "textCodeBlock.background", # Eg. blocks in markdown
    ],
    Color.twilight1: [
        "activityBar.background",
        "dropdown.listBackground",
        "editor.background",
        "sideBarTitle.background",
    ],
    Color.twilight2: [
        "panel.background",
    ],
    Color.twilight3: [
        "checkbox.border",
        "dropdown.border",
        "input.border",
        "editorWidget.background",
        "textBlockQuote.background",
    ],
    Color.twilight4: [
            "scrollbarSlider.background",
    ],
    Color.twilight5: [
        "activityBar.inactiveForeground",
    ],
    Color.twilight6: [
        "disabledForeground",
        "input.placeholderForeground",
        "scrollbar.shadow",
    ],
}


Twilight = Theme(
    name="sebec-twilight",
    category=ThemeCategory.dark,
    colors={
        **_CEDAR_ELEMENTS,
        **_CERULEAN_ELEMENTS,
        **_SAPPHIRE_ELEMENTS,
        **_SPRUCE_ELEMENTS,
        **_SOLAR_ELEMENTS,
        **_SHINE_ELEMENTS,
        **_TWILIGHT_ELEMENTS,
        "red": [
            "editorActionList.background",
            "editorActionList.foreground",
            "editorActionList.focusForeground",
            "editorActionList.focusBackground",

            # "checkbox.selectBackground",
            # "checkbox.selectBorder",
            # "radio.activeForeground",
            # "radio.activeBackground",
            # "radio.activeBorder",
            # "radio.inactiveForeground",
            # "radio.inactiveBackground",
            # "radio.inactiveBorder",
            # "radio.inactiveHoverBackground",

            # "scrollbarSlider.background",
        ],
    },
)
