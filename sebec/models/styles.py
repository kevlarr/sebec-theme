from enum import StrEnum

from .base import Base



class ThemeStyle(StrEnum):
    Light = "light"
    Dark = "dark"


class ThemeStyleNames(Base):
    light: str
    dark: str
