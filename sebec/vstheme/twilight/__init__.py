from sebec.vstheme.base import Theme, ThemeCategory
from .token_colors import TOKEN_COLORS
from .ui_colors import UI_COLORs


__all__ = ["Twilight"]


Twilight = Theme(
    name="sebec-twilight",
    category=ThemeCategory.dark,
    colors=UI_COLORs,
    token_colors=TOKEN_COLORS,
)
