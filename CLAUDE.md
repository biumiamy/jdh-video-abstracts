# JDH video abstracts — project instructions for Claude

Short animated videos (MP4, 1920×1080, 30 fps) that make Journal of Digital History articles
accessible. Shown inside the article; social media is secondary. Each video gets its own folder in `videos/`.

## How we work (always in this order)
1. **Understand the article together.** Read the article's GitHub repo (`article.ipynb`, figures in the
   notebook outputs and `media/`, tables, data). Explain the argument to Mirjam in plain words, scene by
   scene, and propose headlines/questions. Do not build anything before she agrees on the content.
2. **Stills first.** One still per scene at full size (`tools/still.py`). Get feedback, revise.
3. **Animate**, then render with `tools/render.py`. Show the full video; adjust timing on request.

## Content rules
- Every fact, number, date and quote comes from the article. Nothing invented. Paraphrase carefully
  (e.g. statutes are "official rules", not "the real world").
- Use the article's real figures, with a small source caption ("Figure 4 · …").
- Plain language, short headlines. Each key point is a question with an answer
  ("Just a game?" → "Close match!"). Kickers in violet capitals.
- Typical arc (adapt per article, don't force it): hook → how it works → 2–3 key points → what it means → end card.
  Visual motifs are article-specific (dice and a board were only for the Qing game article).

## Look (identical across the series)
- Background #F3F1F7 with a faint dot grid · text #1F2021 · greys #ADB5BD / #495057
- Accents: violet #5E2BFF (main), teal #51F6E0 (sparingly) · only one highlight colour per scene
- Fonts: Fira Sans (`shared/fonts`); Chinese/Japanese in Noto Serif TC/SC (install it locally)
- Top-left label (text only): "**Journal of Digital History** · video abstract". On the end card it is replaced by
  the JDH logo with text (`shared/logos/jdh-logo-text.svg`, 52 px high), without "video abstract"
- Highlight a key word with a marker that wipes left→right behind it (violet bar, word turns white)
- Lists use small violet arrows "→" (no round icons)
- Notes/conclusions as post-its: white card, thin violet strip on top (grey strip for quotes), slight tilt,
  narrow (3–4 lines). Long quotes: break into short lines, never full-width
- End card: the article's fingerprint (from the journal site, SVG) drawing itself, "READ THE ARTICLE",
  title, authors, "Journal of Digital History", logo row (`shared/logos`)

## Timing rule (one rule for every scene, seconds)
- Pictures arrive fast: 0.25 between quick items (dice, bars, markers); 0.4 between blocks
- List items (rules, results, rows): 1.5 apart (rows of a grid: 0.9)
- Text stays as long as it takes to read: 0.22 per word (≈4.5 words/s), never less than 0.5
- Fade-in 0.4 · 1.2 pause after the last element · then the next scene
- Charts build immediately after their headline number; no waiting
- Where possible, carry an object into the next scene (e.g. dice shrinking into the board)
- Music: ALWAYS `music/Birds - Corbyn Kites.mp3` (the series sound), starting at 0 s, fade out over the last ~3.5 s.
  Every rendered video must have this sound. Use another track only if Mirjam asks.

## Technical setup
- Each video = one HTML page with a global `seek(t)` function that draws the frame at time t
  (see `videos/2026-gaming-qing-mandarinate/build_video.py`: the schedule object `S` at the top of the
  timeline holds all times, computed from the timing rule).
- `python tools/still.py videos/<name>/video.html 3 12 25` → PNG stills
- `python tools/render.py videos/<name>/video.html <seconds>` → `videos/<name>/video.mp4` with the Birds music
- Needs: Python 3, `pip install playwright`, `playwright install chromium`, ffmpeg.
