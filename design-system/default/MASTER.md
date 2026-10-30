# 随笔 · Design System

> Source of truth for the personal blog redesign. Page-specific notes may live in
> `design-system/default/pages/`; otherwise use these rules.

## Direction

- **Style:** Editorial grid with Swiss Modernism structure.
- **Mood:** Warm, literary, quiet, precise, personal.
- **Dials:** Variance 4/10, motion 3/10, density 4/10.
- **Principles:** strong typographic hierarchy, asymmetric composition, generous
  reading space, restrained decoration, subtle state motion.

## Color Tokens

### Light

| Role | Token | Value |
|---|---|---|
| Page | `--page` | `#f3eee5` |
| Soft page | `--page-soft` | `#eae2d6` |
| Surface | `--surface` | `#fbf8f1` |
| Raised surface | `--surface-raised` | `#fffdf8` |
| Primary text | `--ink` | `#172238` |
| Secondary text | `--ink-soft` | `#38475b` |
| Muted text | `--muted` | `#596372` |
| Border | `--border` | `#d4cabc` |
| Strong border | `--border-strong` | `#9e9180` |
| Accent | `--accent` | `#9a4526` |
| Accent hover | `--accent-hover` | `#7d351c` |
| Accent soft | `--accent-soft` | `#efd9cc` |
| Focus ring | `--focus` | `#0e7490` |

### Dark

| Role | Token | Value |
|---|---|---|
| Page | `--page` | `#10161b` |
| Soft page | `--page-soft` | `#151e25` |
| Surface | `--surface` | `#172129` |
| Raised surface | `--surface-raised` | `#1c2731` |
| Primary text | `--ink` | `#f2eee6` |
| Secondary text | `--ink-soft` | `#d3d7d6` |
| Muted text | `--muted` | `#aab4b8` |
| Border | `--border` | `#34424b` |
| Strong border | `--border-strong` | `#66747c` |
| Accent | `--accent` | `#e5a176` |
| Accent hover | `--accent-hover` | `#f1b48f` |
| Accent soft | `--accent-soft` | `#3b281f` |
| Focus ring | `--focus` | `#81d4ea` |

All primary, secondary, muted, accent, and CTA text combinations meet WCAG AA.

## Typography

- **Display:** Newsreader, then Noto Serif SC and Songti SC fallbacks.
- **Body/UI:** Public Sans, then PingFang SC and Microsoft YaHei fallbacks.
- **Technical labels:** SFMono-Regular, Cascadia Code, Consolas.
- **Hero:** 50–88px, line-height 0.99–1.08.
- **Section title:** 30–54px.
- **Article body:** 18–21px with 1.9–1.95 line-height.
- **Long-form measure:** 60–70 characters.

## Layout

- Content width: 1180px.
- Article width: 760px with a 170px reading-information rail.
- Breakpoints: 1080, 840, 680, 390px.
- Responsive proof points: 375, 768, 1024, 1440px.
- Header height: 78px desktop, 68px mobile.

## Components

- **Primary action:** terracotta pill, 48–50px high, white or dark text according
  to theme.
- **Secondary action:** underline or outlined neutral action; never competes with
  the primary CTA.
- **Article card:** semantic heading link, category chip, date, excerpt and author;
  the first card becomes a full-width editorial feature.
- **Inputs:** 50px minimum height, visible labels, persistent help text, 4px focus
  halo and error text connected by proximity.
- **Icons:** inline 1.4–1.7px stroke SVG only; decorative icons use `aria-hidden`.

## Motion

- Initial hero reveal: opacity and 14px vertical translation, 720–820ms.
- Micro-interactions: 180–260ms with `cubic-bezier(0.16, 1, 0.3, 1)`.
- Reading progress only animates `transform`.
- All non-essential motion is disabled under `prefers-reduced-motion`.

## Accessibility

- Visible skip link and 3px focus ring.
- Logical H1 → H2 → H3 hierarchy.
- Touch actions remain at least 40–50px high on mobile.
- Theme control exposes `aria-pressed` and an action-specific label.
- No horizontal scrolling at tested widths.
- No color-only meaning; category and status also use text.
