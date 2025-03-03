"""Utility classes for defining semantic & textmate tokens.

https://macromates.com/manual/en/language_grammars#naming_conventions
https://code.visualstudio.com/api/language-extensions/semantic-highlight-guide
https://code.visualstudio.com/api/language-extensions/semantic-highlight-guide#semantic-token-scope-map
"""

__all__ = ["SemanticToken", "TextmateToken"]


class SemanticToken:
    token_type: str
    token_lang: str | None
    token_mods: list[str] | None

    def __init__(self, tt: str, *mods: str, lang: str | None = None):
        self.token_type = tt
        self.token_mods = mods
        self.token_lang = lang

    def serialize(self) -> str:
        """Returns a string representing the semantic token selector."""
        selector = self.token_type
        if mods := self.token_mods:
            selector += f".{'.'.join(mods)}"
        if lang := self.token_lang:
            selector += f":{lang}"
        return selector


class TextmateToken:
    name: str | None
    scope: str | list[str]

    def __init__(self, *scopes: str, name: str | None = None):
        self.name = name
        self.scope = scopes

    def serialize(self) -> dict:
        """Returns a dict with the scope and name of the token, if present."""
        if self.name:
            return {"scope": self.scope, "name": self.name}
        return {"scope": self.scope}
