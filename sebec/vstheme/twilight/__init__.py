from sebec.vstheme.base import Theme, ThemeCategory
from .token_colors import SCOPE_SETTINGS
from .ui_colors import UI_COLORS


__all__ = ["Twilight"]


Twilight = Theme(
    name="sebec-twilight",
    category=ThemeCategory.dark,
    colors=UI_COLORS,
    scopes=SCOPE_SETTINGS,
)
