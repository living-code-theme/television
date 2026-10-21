<!-- living-code-readme:1 -->
# 📺 Living Code for Television

**Calm slate. Living color.** Living Code for Television: complete native TOML palettes for search results, matches, previews, selections and mode indicators.

[Installation](#installation) · [Flavors](#flavors) · [Configuration](#configuration) · [All ports](https://github.com/living-code-theme)

## Previews

Real application screenshots have not been captured yet.

## Installation

```sh
git clone https://github.com/living-code-theme/television.git
cd television
```

```sh
mkdir -p "${XDG_CONFIG_HOME:-$HOME/.config}/television/themes"
cp themes/*.toml "${XDG_CONFIG_HOME:-$HOME/.config}/television/themes/"
```

Merge this into the existing `config.toml` in your Television config directory:

```toml
[ui]
theme = "living-code-night"
```

Restart `tv`. If you configured a different config directory, put `themes/` beside that `config.toml`.

## Flavors

Expand a flavor for its full-size preview and activation instructions.

<details data-lc-flavor="night">
<summary><strong>Night</strong> · Dark · full palette</summary>

A real application capture is not available yet.

Set `theme = "living-code-night"` in the existing `[ui]` table and restart `tv`.

</details>

<details data-lc-flavor="frost">
<summary><strong>Frost</strong> · Dark · softer chroma</summary>

A real application capture is not available yet.

Set `theme = "living-code-frost"` in the existing `[ui]` table and restart `tv`.

</details>

<details data-lc-flavor="paper">
<summary><strong>Paper</strong> · Light · near-white slate</summary>

A real application capture is not available yet.

Set `theme = "living-code-paper"` in the existing `[ui]` table and restart `tv`.

</details>

<details data-lc-flavor="signal">
<summary><strong>Signal</strong> · Dark · teal accent</summary>

A real application capture is not available yet.

Set `theme = "living-code-signal"` in the existing `[ui]` table and restart `tv`.

</details>

## Configuration

A theme file has flat color keys; `[ui]` belongs only in `config.toml`. Existing `[ui.theme_overrides]` entries override the installed palette, so remove conflicting values if the colors do not match. The port sets both foreground and background on selected results and every mode badge.

## Compatibility

Targets Television’s documented flat TOML custom-theme API and all required fields in its `Theme` struct. The `send_to_channel_mode_fg` fallback in newer documentation is not needed by the pinned contract. Truecolor is recommended. Tests check the full required field set, native parsing, semantic colors and selected-row contrast.

## Contributing

Found a problem? [Open an issue](https://github.com/living-code-theme/television/issues/new/choose) with the app version, the flavor and a screenshot. Want Living Code somewhere else? [Request a port](https://github.com/living-code-theme/core/issues/new?template=port-request.yml).

Pull requests are welcome. Keep this README, `port.json` and `images/` in sync, and use real screenshots of the app, never mockups.

🦎 **One chameleon, many habitats.** Part of [Living Code](https://github.com/living-code-theme).

## License

[MIT](LICENSE) © Elliot Luque
