import enum


__all__ = ["Color"]


class Color(enum.StrEnum):
    # Muted light beige spectrum inspired by the faint light of dawn before the sun breaks
    sunrise0 = "#C2C0B7"
    sunrise1 = "#CBCAC2"
    sunrise2 = "#D7D5CC"
    sunrise3 = "#E0DFD6"
    sunrise4 = "#EAE8E1"
    sunrise5 = "#F0EFEA"
    sunrise6 = "#F6F6F3"

    # Muted dark blue spectrum inspired by the deepening sky at dusk after the sun sets
    twilight0 = "#15181E"
    twilight1 = "#1B1F27"
    twilight2 = "#212630"
    twilight3 = "#2E3440"
    twilight4 = "#3B4352"
    twilight5 = "#444D5E"
    twilight6 = "#4C566A"

    # Spectrum of soft whites resembling the shine of stars or the highlights on waves
    shine0 = "#ABB3C4"
    shine1 = "#B6BECE"
    shine2 = "#C0C8D8"
    shine3 = "#CCD3E0"
    shine4 = "#D9DEE8"
    shine5 = "#E5E9F0"
    shine6 = "#EDF0F5"

    # Brighter, warmer blues of the water reflecting the midday sky
    cerulean0 = "#4C9DB8"
    cerulean1 = "#69ADC4"
    cerulean2 = "#88BED0"

    # Darker, cooler blues of the water reflecting the dusk sky
    sapphire0 = "#405C82"
    sapphire1 = "#4A6A96"
    sapphire2 = "#5C7EAE"
    sapphire3 = "#819CC1"

    # Cooler greens of spruce
    spruce0 = "#5E9C87"
    spruce1 = "#76AD9B"
    spruce2 = "#8FBCAD"

    # Warmer greens of cedar
    cedar0 = "#7DA05A"
    cedar1 = "#91B073"
    cedar2 = "#A5BE8C"

    # Accent colors reminiscent of the rising and setting sun
    solarPurple0 = "#A3759C"
    solarPurple1 = "#B48EAE"
    solarRed0 = "#AE474F"
    solarRed1 = "#BF6169"
    solarOrange0 = "#C66F52"
    solarOrange1 = "#D08870"
    solarYellow0 = "#E5BB67"
    solarYellow1 = "#EBCB8B"

    def alpha(self, alpha: float) -> str:
        """
        Returns the color value with the alpha level appended to it,
        convered to hexadecimal.
        """
        alpha = max(0.0, min(1.0, alpha))  # Clamp alpha to [0.0, 1.0]
        return f"{self.value}{int(alpha * 255):02x}"
