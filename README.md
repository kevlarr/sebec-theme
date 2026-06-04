# Sebec Theme (WIP)

Originally inspired by more minimal themes like Nord, Zenburned, and Verdandi,
Sebec represents the search for a balanced theme where there is just enough variation in font
and UI styling for code (and the overall editor) to be easily scannable at a glance, but not so
much that it becomes distracting, jarring, or tiring.
Where light mode is equally as legible as dark, relying on the same palette, background variations,
and highlighting choices to reduce the cognitive impact when switching between modes.


<figure style="margin: 2rem 0">
<img src="./design/stacked-themes.png"/>
<figcaption style="text-align: center"><i>Light and dark modes share the same color palette and highlighting strategies</i></figcaption>
</figure>

Rather than trying to assign a wide range of colors across as many token categories as possible,
which in many themes tends (for me, at least) to impede visual processing rather than enable it,
Sebec aims to apply a more narrow range of colors to where it matters most - to distinguish the
most important semantic categories and modes of reading, and to downplay the elements that matter least.

Warmer, brighter yellows and reds are avoided except for diagnostics, and even purple and green are pushed
toward blue and cyan - separate enough to be distinct, but close enough for the eye to transition smoothly.

> *Signal over noise, more with less, that sort of thing.*

And at the UI layer, variations in background color should make it obvious which elements
deserve attention - a widget opening even in the periphery should bring the eye toward it.

Application support currently includes:

- **Editors:** VS Code
- **Terminals:** iTerm2, Windows Terminal

> *Interestingly enough, through a lot of iteration and evolution, the theme has unintentionally ended up
> bearing some surprising similarities to the default Neovim light and dark themes. Go figure!*

## Development

**Theme development should be easy.** At least, it should be easier than having hex color values
strewn all over the place.
(What does `#3b80c4` mean and how does it relate to `#6299d0`?
I don't know either, and I don't want to update the same code across different theme files
whenever those shades of blue change - especially when some apps use RGB over hex.)

That's why Sebec uses a series of generators to ultimately create the application themes:

- `poetry run update-colors <SVG file>` writes `color.py` to store all hex values as named
  colors on an enum, eg. `blue0` or `purple2`
- `poetry run generate` reads the `theme.yml` file which maps named colors to application
  theme settings and then generates the various application packages or theme files

The overall workflow looks like:

1. Define or adjust color swatches in the Affinity Designer palette file
2. Export the artboard (with named color layers) to SVG
3. Run `update-colors` on that SVG
4. Update `theme.yml`; map style objects (eg. `{ light: blue1 italic, dark: blue2 italic }`)
  to keys, using anchors and aliases whenever possible to maintain consistency in styles
5. Run `generate` for the series of Pydantic models to do their work and export all of the
  different application theme packages or files into `package/`

(First run `poetry install` to add the necessary scripts.)

## Testing the VS Code theme

Until the VS Code theme is published, it is most easily tested by launching through VS Code.
Open `package/vscode` in a **new** VS Code instance, after which selecting the `launch.json`
file and pressing `F5` will open another instance with the theme activated.

In other words:
- Clone this repo: `git clone git@github.com:kevlarr/sebec-theme.git`
- Navigate to the vscode package: `cd sebec-theme/package/vscode`
- Open vscode in the directory: `code .`
- Once vscode is open, press `F5` - this opens another vscode instance with the theme active
- Switch between `Dawn` and `Dusk` themes
