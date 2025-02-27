"""UI Colors

See: https://code.visualstudio.com/api/references/theme-color#editor-groups-tabs
"""

from sebec.palette import Color





# TODO: editor colors

_CERULEAN_ELEMENTS = {
    Color.cerulean0: [
        "inputValidation.infoBorder",
        "inputValidation.infoBackground",
        "minimap.infoHighlight",
        "textLink.foreground",
        # "tab.activeBorder",
        "tab.selectedBorderTop",
        "activityBar.activeBorder",
        "activityBar.foreground",

"tree.indentGuidesStroke",
"tree.inactiveIndentGuidesStroke",
    ],
    Color.cerulean1: [
        "textLink.activeForeground",
    ],
    Color.cerulean2: [
        "tab.activeForeground",
    ],
}
_SAPPHIRE_ELEMENTS = {
    Color.sapphire0: [
        "button.background",
        "inputOption.hoverBackground",
        "scrollbarSlider.hoverBackground",
        "selection.background",
        "textBlockQuote.border",
        "toolbar.hoverBackground", # eg. hovering over icons in panels/widgets
    ],
    Color.sapphire1: [
        # "toolbar.hoverOutline", # eg. hovering over "..." icons, etc. in panels
    ],
    Color.sapphire2: [
        # "editorGroup.border",
        "button.hoverBackground",
        "inputOption.activeBackground",
        "scrollbarSlider.activeBackground",
    ],
    Color.sapphire3: [
            "editorGutter.foldingControlForeground",
    ],
}
_CEDAR_ELEMENTS = {
    Color.cedar0.alpha(0.5): [
    ],
    Color.cedar1: [
    ],
    Color.cedar2: [
    ],
}
_SPRUCE_ELEMENTS = {
    Color.spruce0.alpha(0.5): [
        "minimap.findMatchHighlight",
    ],
    Color.spruce0: [
        "activityBarBadge.background",
        "badge.background",
        "editorGutter.addedBackground",
        "minimapGutter.addedBackground",
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
    Color.solarPurple0.alpha(0.25): [
        "editorMinimap.inlineChatInserted",
        "list.dropBackground",
        "sash.hoverBorder", # The drag border indicator on hover
    ],
    Color.solarPurple0.alpha(0.75): [
        "list.filterMatchBackground",
    ],
    Color.solarPurple1: [
        "tab.dragAndDropBorder",
    ],
    Color.solarPurple1.alpha(0.25): [
        "editorGroup.dropBackground",
        "sideBar.dropBackground",
    ],
    Color.solarRed0: [
        "activityErrorBadge.background",
        "editorGutter.deletedBackground",
        "inputValidation.errorBorder",
        "inputValidation.errorBackground",
        "list.errorForeground", # foreground colors for filenames AND tab titles when error
        "minimap.errorHighlight",
        "minimapGutter.deletedBackground",

    ],
    Color.solarRed0.alpha(0.75): [
        "editorWarning.foreground",
        "editorError.foreground",
    ],
    Color.solarRed1: [
        "errorForeground",
    ],
    Color.solarOrange0: [
        "activityWarningBadge.background",
        "inputValidation.warningBorder",
        "inputValidation.warningBackground",
        "list.warningForeground",
    ],
    Color.solarOrange0.alpha(0.75): [
        "minimap.warningHighlight",
    ],
    Color.solarYellow0: [
        "editorGutter.modifiedBackground",
    ],
    Color.solarYellow0.alpha(0.75): [
        "minimapGutter.modifiedBackground",
    ],
}
_SHINE_ELEMENTS = {
    Color.shine0: [
        "descriptionForeground", # Eg. extension descriptions in search
        "editor.foreground",
        "foreground",
        "icon.foreground",
        "sideBar.foreground",
        "sideBarTitle.foreground",
        "sideBarSectionHeader.foreground",
        "terminal.foreground",
    ],
    Color.shine1: [
    ],
    Color.shine2: [
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
        "list.activeSelectionForeground",
        "list.activeSelectionIconForeground",
        "list.inactiveSelectionForeground",
        "list.inactiveSelectionIconForeground",
    ],
    Color.shine5: [
    ],
    Color.shine6: [
    ],
}
_TWILIGHT_ELEMENTS = {
    Color.twilight0: [
        "tab.inactiveBackground",
        "activityBarBadge.foreground",
        "activityErrorBadge.foreground",
        "activityWarningBadge.foreground",
        "badge.foreground",
        "checkbox.background",
        "dropdown.background",
        "editorGroupHeader.tabsBackground",
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
        "breadcrumb.background",
        "dropdown.listBackground",
        "editor.background",
        "sideBarTitle.background",
        "tab.activeBackground",
        "tab.hoverBackground",
    ],
    Color.twilight2: [
        "list.activeSelectionBackground",
        "list.hoverBackground",
        "list.inactiveSelectionBackground",
        "panel.background",
        "sideBarSectionHeader.border",
        "sideBySideEditor.horizontalBorder",
        "sideBySideEditor.verticalBorder",
        "tab.border",
    ],
    Color.twilight3: [
        "checkbox.border",
        "dropdown.border",
        "editorGroup.border", # border between editor groups
        # "editorGroupHeader.border",
        # "editorGroupHeader.tabsBorder",
        "input.border",
        "sideBar.border",
        "editorWidget.background",
        "textBlockQuote.background",
    ],
    Color.twilight4: [
        "scrollbarSlider.background",
"listFilterWidget.background",
    ],
    Color.twilight5: [
        "activityBar.inactiveForeground",
    ],
    Color.twilight6: [
        "disabledForeground",
        "input.placeholderForeground",
        "scrollbar.shadow",
        "tab.inactiveForeground",
    ],
}

# Opacity controls - only the alpha level is considered, not the color
_OPACITY_CONTROLS = {
    Color.twilight0.alpha(0): [
        "list.focusOutline",
    ],
    Color.twilight0.alpha(0.5): [
        "minimap.foregroundOpacity",
    ],
}

UI_COLORs = {
    **_CERULEAN_ELEMENTS,
    **_SAPPHIRE_ELEMENTS,
    **_CEDAR_ELEMENTS,
    **_SPRUCE_ELEMENTS,
    **_SOLAR_ELEMENTS,
    **_SHINE_ELEMENTS,
    **_TWILIGHT_ELEMENTS,
    **_OPACITY_CONTROLS,

    "red": [
        # "editorActionList.background",
        # "editorActionList.foreground",
        # "editorActionList.focusForeground",
        # "editorActionList.focusBackground",


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
