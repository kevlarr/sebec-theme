
from pydantic import BaseModel, ConfigDict


class Base(BaseModel):
    model_config = ConfigDict(extra="forbid")


class ColorStyle(Base):
    foreground: str
    alpha: float | None = None

    def __str__(self) -> str:
        """Returns a string representation of the color with alpha level, if present."""
        if self.alpha is not None:
            return f"{self.foreground}{int(self.alpha * 255):02x}"
        return str(self.foreground)
