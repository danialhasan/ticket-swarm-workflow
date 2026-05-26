# Mercury — Style Reference
> Mountain Top Command Center

**Theme:** dark

The deck should feel like a command center at twilight: dark, spacious, precise,
and focused. The canvas uses deep neutral surfaces while off-white text carries
the narrative. Mercury Blue is a restrained accent, not a decorative wash.

## Theater Adaptation

This is for a 1920x1080, 70-foot screen. The original Mercury reference includes
smaller web UI text, but this deck does not.

- Minimum visible text size: `24px`
- All explicit deck CSS `font-size` and `font:` declarations must stay `>=24px`
- Workbench mode must allow vertical scrolling while hiding horizontal overflow
- Run `node check-deck.mjs` after CSS changes

## Tokens — Colors

| Name | Value | Token | Role |
|------|-------|-------|------|
| Mercury Blue | `#5266eb` | `--color-mercury-blue` | Primary accent and rare indicator color |
| Ghost Blue | `#cdddff` | `--color-ghost-blue` | Soft blue grid/safe-area accents |
| Deep Space | `#171721` | `--color-deep-space` | Outermost page background |
| Midnight Slate | `#1e1e2a` | `--color-midnight-slate` | Slide canvas |
| Graphite | `#272735` | `--color-graphite` | Contained panels and interactive surfaces |
| Lead | `#70707d` | `--color-lead` | Borders and dividers |
| Starlight | `#ededf3` | `--color-starlight` | Primary text |
| Silver | `#c3c3cc` | `--color-silver` | Secondary text and footer copy |
| Pure White | `#ffffff` | `--color-pure-white` | Text on strong accent surfaces only |

## Typography

- Headline font: `arcadiaDisplay`, with Inter/Manrope fallbacks
- Body font: `arcadia`, with Inter/Manrope fallbacks
- Headline weight: light `360`
- Emphasis/small headings: `480`
- Tracking: subtle positive spacing
- Minimum projected/control text: `24px`

## Surfaces

- Slide canvas: Midnight Slate
- Workbench surround: Deep Space
- Panels: Graphite at partial opacity with Lead borders
- Proof groups: simple Lead top divider, transparent background
- HUD/notes/help: dark translucent panel with Lead border
- No heavy shadows or decorative gradients

## Layout Rules

- One idea per slide
- Keep the canvas sparse enough for the back row
- Use simple diagrams, proof strips, and flow rows
- Avoid dense dashboard layouts unless the slide is explicitly a product screenshot
- Keep projected content inside the 1920x1080 safe area

## Do

- Use Starlight for primary statements
- Use Silver for supporting copy
- Keep Mercury Blue rare and purposeful
- Use Lead for restrained structure
- Preserve the command-center feeling: quiet, expansive, technical

## Don't

- Do not introduce a broad saturated palette
- Do not drop below 24px visible text
- Do not add decorative gradients or heavy shadows
- Do not use large rounded white cards in this style
- Do not let controls or HUD elements clutter stage mode
