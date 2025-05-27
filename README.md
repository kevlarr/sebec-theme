# Twilight Lake

Twilight Lake is a cross-application, dual color theme
originally derived from [Nord](https://www.nordtheme.com/) (in particular the Polar Night and Aurora swatches)
with an extended palette inspired by the shifting colors of twilight
on a forested lake.

Application support currently includes:

- iTerm2
- VS Code
- Windows Terminal

**Note:** This theme is still very much a work in progress, and language
support in VS Code is still very preliminary.

## Background

The main goals for this project include:

1. Finding the perfect balance in token stylization

    a. Using enough colorization & style rules to aid visual processing but
     prevent them from becoming overly distracting

    b. Having consistent color & style rules across both light & dark themes to
    reduce the cognitive impact of switching modes

2. Leveraging a greater range of background colors

    a. Increasing the range of UI element background colors improves the visual
    separation of elements and attention to overlay elements

3. Reducing the maintenance burden of custom themes

    a. Themes for supported applications should all be generated automatically
    from a single, easy to read configuration

    b. Updating palette colors should not require manually changing hex or rgb values
    in any application theme file

## Palette

The palette is comprised of:

- **Sky**: Two 8-color ranges meant for use as the primary background & foreground colors
    - **Dawn** and **Dusk**: Inspired by the colors of the sky as it brightens before sunset and fades after sunset

- **Lake**: Three 4-color ranges meant for use as the primary accent & token colors
    - **Sapphire** and **Cerulean**: Inspired by the reflections of the sky on the water,
    these are intended to be the predominant shades used for token colorization
    - **Evergreen**: Inspired by the deep, warm greens of spruce, cedar, and pines that surround the lake, this range is intended to offer extra separation
    from the blues above while still not contrasting too much

- **Solar**: Four 3-color ranges meant for use as secondary accents

![Palette colors](./design/palette.svg)

## Development

Run `poetry install` to add the necessary scripts.

The various theme files are generated via `poetry run generate`,
which will update their files stored in `package/`.

After updating the Affinity Designer palette, re-export the `palette.svg` file
from the artboard and then run `poetry run update-colors` to update the `Color` enum itself.

### Testing the VS Code theme

Open `package/vscode` in a **new** VS Code instance, after which selecting the `launch.json`
file and pressing `F5` will open another instance with the theme activated.
