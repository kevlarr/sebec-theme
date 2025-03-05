"""UI Colors

See: https://code.visualstudio.com/api/references/theme-color#editor-groups-tabs

NOTE: Any terminal colors that are assiged here and are duplicative of those defined
in `sebec.shared` will be overridden.
"""

from sebec.color import Color
from sebec.util import merge_color_maps


# TODO: editor colors

_SPRUCE_ELEMENTS = {
    Color.Spruce1.alpha(0.5): [
    ],
    Color.Spruce1: [
    ],
    Color.Spruce2: [
    ],
    Color.Spruce3: [
    ],
}
_SOLAR_ELEMENTS = {
    Color.SolarPurple0: [
    ],
    Color.SolarPurple0.alpha(0.25): [
        "editorMinimap.inlineChatInserted",
        "list.dropBackground",
        "sash.hoverBorder", # The drag border indicator on hover
    ],
    Color.SolarPurple0.alpha(0.75): [
        "list.filterMatchBackground",
    ],
    Color.SolarPurple1: [
        "tab.dragAndDropBorder",
    ],
    Color.SolarPurple1.alpha(0.25): [
        "editorGroup.dropBackground",
        "sideBar.dropBackground",
    ],
    Color.SolarRed0: [
        "activityErrorBadge.background",
        "editorGutter.deletedBackground",
        "inputValidation.errorBorder",
        "inputValidation.errorBackground",
        "list.errorForeground", # foreground colors for filenames AND tab titles when error
        "minimap.errorHighlight",
        "minimapGutter.deletedBackground",
    ],
    Color.SolarRed0.alpha(0.75): [
        "editorWarning.foreground",
        "editorError.foreground",
    ],
    Color.SolarRed1: [
        "errorForeground",
    ],
    Color.SolarOrange0: [
        "activityWarningBadge.background",
        "inputValidation.warningBorder",
        "inputValidation.warningBackground",
        "list.warningForeground",
    ],
    Color.SolarOrange0.alpha(0.75): [
        "minimap.warningHighlight",
    ],
    Color.SolarYellow0: [
        "editorGutter.modifiedBackground",
    ],
    Color.SolarYellow0.alpha(0.75): [
        "minimapGutter.modifiedBackground",
    ],
}
_TWILIGHT_ELEMENTS = {
    Color.Twilight0: [
        # "inputValidation.errorBackground",
    ],
    Color.Twilight1: [
        "dropdown.listBackground",
    ],
    Color.Twilight2: [
    ],
    Color.Twilight3: [
        "textBlockQuote.background",
    ],
    Color.Twilight4: [
        "listFilterWidget.background",
    ],
    Color.Twilight5: [
        "activityBar.inactiveForeground",
    ],
    Color.Twilight6: [
        "disabledForeground",
        "input.placeholderForeground",
        "scrollbar.shadow",
        "tab.inactiveForeground",
    ],
}

# Opacity controls - only the alpha level is considered, not the color
_OPACITY_CONTROLS = {
    Color.Twilight0.alpha(0): [
        "list.focusOutline",
        "panel.border",

        "editorGroup.border",
        "sideBarSectionHeader.border",
    ],
    Color.Twilight0.alpha(0.5): [
        "minimap.foregroundOpacity",
    ],
}

_temp = {

}

_todo = [
    "tab.activeBorder", # Bottom border of active tab
    "textLink.activeForeground", # Foreground on link hover/click (eg. in Welcome page)

    # Cerulean1 but.. did I see these?
    "inputValidation.infoBorder",
    "inputValidation.infoBackground",
    "minimap.infoHighlight",

    # Sapphire0
    "textBlockQuote.border",

    # Sapphire1
    "toolbar.hoverOutline", # eg. hovering over "..." icons, etc. in panels

]

_final = {
    ##
    ## Twilight
    ##
    **{
        Color.Twilight0: [
            # Primary backgrounds
            "editorGroupHeader.tabsBackground",
            "minimap.background",
            "sideBar.background",
            "sideBarSectionHeader.background",
            "tab.inactiveBackground",
            "textCodeBlock.background", # Eg. blocks in markdown

            # Input & control elements
            "checkbox.background",
            "dropdown.background",
            "input.background",
            "inputOption.activeBorder", # match input color to hide the border

            # Foreground colors
            "activityBarBadge.foreground",
            "activityErrorBadge.foreground",
            "activityWarningBadge.foreground",
            "badge.foreground", # Eg. the "Changes" count badge in Source Control sidebar
        ],
        Color.Twilight1: [
            # Primary backgrounds
            "activityBar.background",
            "breadcrumb.background",
            "editor.background",
            "sideBarTitle.background",
            "tab.activeBackground",
            "tab.hoverBackground",
        ],
        Color.Twilight2: [
            # Primary backgrounds
            "list.activeSelectionBackground",
            "list.hoverBackground",
            "list.inactiveSelectionBackground",
            "panel.background",
        ],
        Color.Twilight3: [
            # Primary backgrounds
            "editorWidget.background",

            # Input & control elements
            "checkbox.border",
            "dropdown.border",
            "input.border",
        ],
        Color.Twilight4: [
            # Primary backgrounds
            "scrollbarSlider.background",
        ],
        Color.Twilight5: [
        ],
        Color.Twilight6: [
        ],
        Color.Twilight7: [
        ],
    },

    ##
    ## Sunrise
    ##
    **{
        Color.Sunrise0: [
        ],
        Color.Sunrise0: [
        ],
        Color.Sunrise2: [
        ],
        Color.Sunrise3: [
        ],
        Color.Sunrise4: [
        ],
        Color.Sunrise5: [
        ],
        Color.Sunrise6: [
        ],
        Color.Sunrise7: [
        ],
    },

    ##
    ## Shine
    ##
    **{
        Color.Shine0: [
        ],
        Color.Shine1: [
            # Foreground colors
            "descriptionForeground", # Eg. extension descriptions in search
            "editor.foreground",
            "foreground",
            "icon.foreground",
            "sideBar.foreground",
            "sideBarTitle.foreground",
            "sideBarSectionHeader.foreground",
        ],
        Color.Shine2: [
        ],
        Color.Shine3: [
        ],
        Color.Shine4: [
        ],
        Color.Shine5: [
            # Foreground colors
            "button.foreground",
            "checkbox.foreground",
            "dropdown.foreground",
            "editorWidget.foreground",
            "input.foreground",
            "inputValidation.errorForeground",
            "inputValidation.infoForeground",
            "inputValidation.warningForeground",
            "list.activeSelectionForeground",
            "list.activeSelectionIconForeground",
            "list.inactiveSelectionForeground",
            "list.inactiveSelectionIconForeground",
        ],
        Color.Shine6: [
        ],
        Color.Shine7: [
        ],
    },

    ##
    ## Blues
    ##
    **{
        ##
        ## Sapphire
        ##
        ## Good for elements that need some distinction from background
        ## but without popping or distracting.
        ##
        Color.Sapphire0: [
            # Input & control elements
            "button.background",
            "inputOption.hoverBackground",
            "toolbar.hoverBackground", # eg. hovering over icons in panels/widgets

            "scrollbarSlider.hoverBackground",
            "selection.background",
            "tree.indentGuidesStroke",
            "tree.inactiveIndentGuidesStroke",
        ],
        Color.Sapphire1: [
            # Input & control elements
            "button.hoverBackground",
        ],
        Color.Sapphire2: [
            # Input & control elements
            "inputOption.activeBackground", # eg. the regex button in Find widget when activated

            "scrollbarSlider.activeBackground",
        ],
        Color.Sapphire3: [
            "editorGutter.foldingControlForeground", # The > carets for folding
        ],
        ##
        ## Cerulean
        ##
        ## Secondary accents, not as attention-grabbing as SolarPurple
        ##
        Color.Cerulean0: [
        ],
        Color.Cerulean1: [
            "activityBar.activeBorder",
            "activityBar.foreground",
            "tab.selectedBorderTop",
            "textLink.foreground",
        ],
        Color.Cerulean2: [
        ],
        Color.Cerulean3: [
            "tab.activeForeground",
        ],
    },

    ##
    ## Greens
    ##
    **{
        ##
        ## Cedar
        ##
        Color.Cedar0: [
        ],
        Color.Cedar0: [
        ],
        Color.Cedar2: [
        ],
        Color.Cedar3: [
        ],
        ##
        ## Spruce
        ##
        Color.Spruce0: [
            "editorGutter.addedBackground",
            "minimapGutter.addedBackground",
        ],
        Color.Spruce1: [
        ],
        Color.Spruce2: [
        ],
        Color.Spruce3: [
        ],
    },

    ##
    ## Solar
    ##
    **{
        ##
        ## Purple
        ##
        Color.SolarPurple0: [
            "focusBorder",
            "minimap.selectionHighlight",
            "toolbar.activeBackground", # Eg. the "..." icons when opened or other buttons when clicked
            "progressBar.background",
        ],
        Color.SolarPurple1: [
            "minimap.findMatchHighlight",
        ],
        ##
        ## Red
        ##
        Color.SolarRed0: [
        ],
        Color.SolarRed1: [
        ],
        ##
        ## Orange
        ##
        Color.SolarOrange0: [
        ],
        Color.SolarOrange1: [
        ],
        ## Yellow
        ##
        Color.SolarYellow0: [
            "activityBarBadge.background",
            "badge.background", # Eg. the "Changes" count badge in Source Control sidebar
        ],
        Color.SolarYellow1: [
        ],
    },
}

UI_COLORS = merge_color_maps(_final)

xUI_COLORS = {
    # **_CERULEAN_ELEMENTS,
    # **_SAPPHIRE_ELEMENTS,
    # **_CEDAR_ELEMENTS,
    # **_SPRUCE_ELEMENTS,
    # **_SOLAR_ELEMENTS,
    # **_SHINE_ELEMENTS,
    # **_TWILIGHT_ELEMENTS,
    # **_OPACITY_CONTROLS,



    "red": [
        # "editorActionList.background",
        # "editorActionList.foreground",
        # "editorActionList.focusForeground",
        # "editorActionList.focusBackground",

        # "sideBySideEditor.horizontalBorder",
        # "sideBySideEditor.verticalBorder",
        # "tab.border",
        # "editorGroup.border", # border between editor groups
        # "editorGroupHeader.border",
        # "editorGroupHeader.tabsBorder",
        # "sideBar.border",

        # "checkbox.selectBackground",
        # "checkbox.selectBorder",
        # "radio.activeForeground",
        # "radio.activeBackground",
        # "radio.activeBorder",
        # "radio.inactiveForeground",
        # "radio.inactiveBackground",
        # "radio.inactiveBorder",
        # "radio.inactiveHoverBackground",
    ],
}
