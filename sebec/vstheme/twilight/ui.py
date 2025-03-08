"""UI Colors

See: https://code.visualstudio.com/api/references/theme-color#editor-groups-tabs

NOTE: Any terminal colors that are assiged here and are duplicative of those defined
in `sebec.shared` will be overridden.
"""

from sebec.color import Color
from sebec.util import merge_color_maps


_todo = [
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

    "textBlockQuote.background",

    "tab.activeBorder", # Bottom border of active tab
    "textLink.activeForeground", # Foreground on link hover/click (eg. in Welcome page)

    "inputValidation.errorBackground",

    # Cerulean1 but.. did I see these?
    "inputValidation.infoBorder",
    "inputValidation.infoBackground",
    "minimap.infoHighlight",

    # Sapphire0
    "textBlockQuote.border",

    # Sapphire1
    "toolbar.hoverOutline", # eg. hovering over "..." icons, etc. in panels

]

# For opacity controls, only the alpha level matters for the element
_opacities = {
    Color.Twilight0.alpha(0): [
        "list.focusOutline",
        "editorGroup.border",
        "sideBarSectionHeader.border",
    ],
    Color.Twilight0.alpha(0.5): [
        "minimap.foregroundOpacity",
    ],
}

_twilight = {
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
        "dropdown.listBackground",
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
        "panel.border",
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
    Color.Twilight7: [
    ],
}

_final = {
    ##
    ## Sunrise
    ##
    **{
        Color.Sunrise0: [
            # Foreground colors
            "descriptionForeground", # Eg. extension descriptions in search
            "editor.foreground",
            "foreground",
            "icon.foreground",
            "sideBar.foreground",
            "sideBarTitle.foreground",
            "sideBarSectionHeader.foreground",
        ],
        Color.Sunrise1: [
        ],
        Color.Sunrise2: [
        ],
        Color.Sunrise3: [
        ],
        Color.Sunrise4: [
        ],
        Color.Sunrise5: [
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
        Color.Sunrise6: [
        ],
        Color.Sunrise7: [
        ],
    },
    ##
    ## Shine
    ##
    # **{
        # Color.Shine0: [
        # ],
        # Color.Shine1: [
        # ],
        # Color.Shine2: [
        # ],
        # Color.Shine3: [
        # ],
        # Color.Shine4: [
        # ],
        # Color.Shine5: [
        # ],
        # Color.Shine6: [
        # ],
        # Color.Shine7: [
        # ],
    # },
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
        Color.Cerulean0.alpha(0.5): [
            # Drag and drop
            "editorGroup.dropBackground",
            "list.dropBackground",
            "sideBar.dropBackground",
        ],
        Color.Cerulean0: [
            # Drag and drop
            "tab.dragAndDropBorder",
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
        Color.SolarPurple0.alpha(0.75): [
            "list.filterMatchBackground",
        ],
        Color.SolarPurple0: [
            "focusBorder",
            "minimap.selectionHighlight",
            "toolbar.activeBackground", # Eg. the "..." icons when opened or other buttons when clicked
            "progressBar.background",
            "sash.hoverBorder", # The drag border indicator on hover
        ],
        Color.SolarPurple1: [
            "minimap.findMatchHighlight",
        ],
        ##
        ## Red
        ##
        Color.SolarRed0: [
            "activityErrorBadge.background",
            "editorGutter.deletedBackground",
            "inputValidation.errorBorder",
            "inputValidation.errorBackground",
            "list.errorForeground", # foreground colors for filenames AND tab titles when error
            "minimap.errorHighlight",
            "minimapGutter.deletedBackground",
        ],
        Color.SolarRed1.alpha(0.75): [
            "editorWarning.foreground",
            "editorError.foreground",
        ],
        Color.SolarRed1: [
            "errorForeground",
        ],
        ##
        ## Orange
        ##
        Color.SolarOrange0.alpha(0.75): [
            # "minimap.warningHighlight",
        ],
        Color.SolarOrange0: [
            # "activityWarningBadge.background",
            # "inputValidation.warningBorder",
            # "inputValidation.warningBackground",
            # "list.warningForeground",
        ],
        Color.SolarOrange1: [
        ],
        ##
        ## Yellow
        ##
        Color.SolarYellow0.alpha(0.75): [
            "minimapGutter.modifiedBackground",
        ],
        Color.SolarYellow0: [
            "activityBarBadge.background",
            "badge.background", # Eg. the "Changes" count badge in Source Control sidebar
            "editorGutter.modifiedBackground",
            "editorMinimap.inlineChatInserted",
        ],
        Color.SolarYellow1: [
        ],
    },
}

UI_COLORS = merge_color_maps(_opacities, _twilight, _final)
