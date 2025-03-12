from pathlib import Path

from yaml import safe_load

from .theme import ThemeModel


def parse_yml(filepath: Path) -> ThemeModel:
    with open(filepath) as yml_file:
        content = safe_load(yml_file)
        return ThemeModel.model_validate(content)
