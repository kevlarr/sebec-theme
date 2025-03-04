"""UI Colors

See: https://code.visualstudio.com/api/references/theme-color#editor-groups-tabs

NOTE: Any terminal colors that are assiged here and are duplicative of those defined
in `sebec.shared` will be overridden.
"""

from sebec.vstheme.base import Color


# TODO: editor colors

_CERULEAN_ELEMENTS = {
    Color.Cerulean1: [
        "inputValidation.infoBorder",
        "inputValidation.infoBackground",
        "minimap.infoHighlight",
        "textLink.foreground",
        # "tab.activeBorder",
        "tab.selectedBorderTop",
        "activityBar.activeBorder",
        "activityBar.foreground",
    ],
    Color.Cerulean2: [
        "textLink.activeForeground",
    ],
    Color.Cerulean3: [
        "tab.activeForeground",
    ],
}
_SAPPHIRE_ELEMENTS = {
    Color.Sapphire0: [
        "button.background",
        "inputOption.hoverBackground",
        "scrollbarSlider.hoverBackground",
        "selection.background",
        "textBlockQuote.border",
        "toolbar.hoverBackground", # eg. hovering over icons in panels/widgets

        "tree.indentGuidesStroke",
        "tree.inactiveIndentGuidesStroke",
    ],
    Color.Sapphire1: [
        # "toolbar.hoverOutline", # eg. hovering over "..." icons, etc. in panels
    ],
    Color.Sapphire2: [
        # "editorGroup.border",
        "button.hoverBackground",
        "inputOption.activeBackground",
        "scrollbarSlider.activeBackground",
    ],
    Color.Sapphire3: [
        "editorGutter.foldingControlForeground",
    ],
}
_CEDAR_ELEMENTS = {
}
_SPRUCE_ELEMENTS = {
    Color.Spruce1.alpha(0.5): [
        "minimap.findMatchHighlight",
    ],
    Color.Spruce1: [
        "activityBarBadge.background",
        "badge.background",
        "editorGutter.addedBackground",
        "minimapGutter.addedBackground",
        "progressBar.background",
    ],
    Color.Spruce2: [
    ],
    Color.Spruce3: [
    ],
}
_SOLAR_ELEMENTS = {
    Color.SolarPurple0: [
        "focusBorder",
        "minimap.selectionHighlight",
        "toolbar.activeBackground", # Eg. the "..." icons when opened or other buttons when clicked
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
_SHINE_ELEMENTS = {
    Color.Shine1: [
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
}
_TWILIGHT_ELEMENTS = {
    Color.Twilight0: [
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
    Color.Twilight1: [
        "activityBar.background",
        "breadcrumb.background",
        "dropdown.listBackground",
        "editor.background",
        "sideBarTitle.background",
        "tab.activeBackground",
        "tab.hoverBackground",
    ],
    Color.Twilight2: [
        "panel.background",
        "list.activeSelectionBackground",
        "list.hoverBackground",
        "list.inactiveSelectionBackground",
        "sideBarSectionHeader.border",
        "sideBySideEditor.horizontalBorder",
        "sideBySideEditor.verticalBorder",
        "tab.border",
    ],
    Color.Twilight3: [
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
    Color.Twilight4: [
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
}

# Opacity controls - only the alpha level is considered, not the color
_OPACITY_CONTROLS = {
    Color.Twilight0.alpha(0): [
        "list.focusOutline",
    ],
    Color.Twilight0.alpha(0.5): [
        "minimap.foregroundOpacity",
    ],
}

UI_COLORS = {
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
