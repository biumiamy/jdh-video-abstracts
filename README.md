# JDH video abstracts

Short animated videos (about 1–2 minutes, MP4, 1920×1080, 30 fps, with music) that explain a
*Journal of Digital History* article in plain language. They are shown inside the article.

The videos are made with **Claude Code**, which writes the animation for you. This repository holds
everything that keeps every video in the series looking and feeling the same: the rules, the
shared assets and the tools. You bring the article and your judgement.

---

## Why this gives a consistent series

The style is not stored in anyone's head. It lives in four places, so it is repeated every time:

| Where | What it fixes |
|---|---|
| `CLAUDE.md` | The rules. Claude reads this file automatically at the start of every session: the order of work, the content rules, the look (colours, fonts, post-its, marker, arrows) and the timing rule. |
| `shared/` | The same fonts and logos for every video. |
| `music/` | The series sound (Birds, Corbyn Kites). Every video uses it. |
| `tools/` | The same two commands to make stills and to render, so every video is encoded the same way. |

The finished videos in `videos/` act as **working examples**. A new video starts as a copy of the
newest one, so the helpers (marker, post-its, fades, end card) come along with it.

**Change the style in `CLAUDE.md` once, and every future video follows.**

---

## What's in the folder

```
jdh-video-abstracts/
├── CLAUDE.md              ← the rules (style, timing, workflow) – read this first
├── README.md              ← this guide
├── music/
│   └── README.txt         ← how to get the series music (the mp3 itself is not in the repo)
├── shared/
│   ├── fonts/             ← Fira Sans
│   └── logos/             ← JDH logo (with / without text), partner logo strip
├── tools/
│   ├── still.py           ← save still images at chosen seconds
│   ├── render.py          ← render the full MP4 with music
│   └── fp2json.py         ← convert the article fingerprint SVG for the end card
└── videos/
    ├── 2026-gaming-qing-mandarinate/   ← example 1
    └── 2026-search-of-truth-genai/     ← example 2 (newest, best template)
        ├── video.src.html   ← the animation (all scenes + timing)
        ├── build_video.py   ← builds video.html (adds fingerprint + logos)
        ├── fpdata.json      ← fingerprint data for the end card
        ├── assets/          ← figures taken from the article
        └── video.mp4        ← the result (made by render.py, not stored in the repo)
```

---

## Installation (one time)

1. **Install the programs**
   - [Git](https://git-scm.com/downloads)
   - [Python 3](https://www.python.org/downloads/) (on Windows, tick "Add Python to PATH")
   - [Claude Code](https://claude.com/claude-code) (desktop app or command line)

2. **Get this repository.** In a terminal, go to where you want the folder and run:
   ```bash
   git clone <repository-url>
   ```
   ```bash
   cd jdh-video-abstracts
   ```
   (You can also use GitHub's green **Code** button → *Download ZIP* and unzip it.)

3. **Install the Python tools**
   ```bash
   pip install playwright imageio-ffmpeg pillow
   ```
   ```bash
   playwright install chromium
   ```
   `playwright` opens the video page in a hidden browser to take the frames. `imageio-ffmpeg`
   brings its own ffmpeg to make the MP4, so you don't need to install ffmpeg separately.
   `pillow` handles the logo images.

4. **Add the music.** The track is not in the repository (its licence allows use inside the
   videos only). Download *Birds* by Corbyn Kites from the YouTube Audio Library and save it as
   `music/Birds - Corbyn Kites.mp3`. See `music/README.txt`.

5. **For Chinese/Japanese articles:** install the font *Noto Serif TC/SC* on your computer.

6. **Test it.** Re-render an example video:
   ```bash
   cd videos/2026-search-of-truth-genai && python build_video.py && cd ../..
   ```
   ```bash
   python tools/render.py videos/2026-search-of-truth-genai/video.html 111
   ```
   After a few minutes you get `videos/2026-search-of-truth-genai/video.mp4` with music.

---

## Making a new video, step by step

Open the folder in Claude Code (desktop app, or `claude` in a terminal inside this folder).
Always work in this order. Don't skip ahead.

### Step 1 – Understand the article together (no building yet)

Tell Claude:

> Here is the next article: https://github.com/jdh-observer/&lt;id&gt;.
> Tell me the essence and how you would illustrate it.

Claude reads the article's notebook, figures and data, then explains the argument in plain words and
proposes scenes with headlines. Go through it, correct it, and cut what isn't essential.
Only say "go ahead" once you agree on the content.

**Check:** every number, date and quote must come from the article. Nothing invented.

### Step 2 – Get the fingerprint

On the article's page on the journal website, save the fingerprint image as SVG and put it in
the new video folder, e.g. `videos/2026-my-article/fingerprint.svg`. Tell Claude where it is.

### Step 3 – Stills first

Ask for one still image per scene. Claude builds the page and saves the images, for example:

```bash
python tools/still.py videos/2026-my-article/video.html 3 12 25
```

Look at each still at full size and give feedback ("make the post-it narrower", "mark this word
instead"). Repeat until the stills are right. Changes are cheap at this stage.

### Step 4 – Animate and render

> Animate and render.

Claude adds the movement and timing, then renders:

```bash
python tools/render.py videos/2026-my-article/video.html 110
```

(110 is the length in seconds.) This writes `video.mp4` next to the page, with the Birds music
fading out at the end. Watch it all the way through and ask for timing changes. When you're
happy, say it's final.

---

## The style in short (full version in `CLAUDE.md`)

**Content**
- Plain language, short headlines.
- Each key point is a **question with an answer** ("Just a game?" → "Close match!").
- Typical arc: hook → how it works → 2–3 key points → what it means → end card.
- Use the article's real figures, with a small caption ("Figure 4 · …").

**Look**
- Light lilac background `#F3F1F7` with a faint dot grid. Text `#1F2021`.
- Violet `#5E2BFF` is the main accent. Teal `#51F6E0` is used sparingly. Only one highlight colour per scene.
- Fira Sans for all text. Small violet capitals for the kicker above each headline.
- Top left: "**Journal of Digital History** · video abstract" (text only).
- Key words get a violet **marker** that wipes in from the left; the word turns white.
- Lists use small violet arrows **→**.
- Conclusions are **post-its**: a narrow white card with a thin violet strip on top (grey for quotes), slightly tilted.
- End card: the fingerprint draws itself, then "READ THE ARTICLE", title, authors, the JDH logo top left and the partner logos.

**Timing** (one rule for every scene)
- Pictures arrive fast: 0.25 s between quick items, 0.4 s between blocks.
- List items 1.5 s apart.
- Text stays 0.22 s per word (about 4.5 words per second).
- 1.2 s pause after the last element, then the next scene.

---

## How a video page works (for the curious)

Each video is one HTML page with a function `seek(t)` that draws the exact frame at second `t`.
The render tool calls `seek(0)`, `seek(1/30)`, `seek(2/30)` … and takes a screenshot each time.
That is why every render is identical and why a still at second 12 looks exactly like second 12
in the video.

All times live in one place at the top of the timeline, in an object `S`, calculated from the
timing rule:

```js
const IN=.4, STEP=.5, QUICK=.25, GAP=.4, LIST=1.5, ROW=.9, READ=.22, HOLD=1.2;
const rd = words => Math.max(STEP, words*READ);   // reading time
// Scene 2: kicker, headline, then three list items
c = S.s2 + .3;  S.k2 = c;  S.h2 = c + QUICK;
S.items = [0,1,2].map(i => S.h2 + rd(6) + i*LIST);
S.s3 = S.items[2] + rd(4) + HOLD;                  // next scene starts here
```

So asking to "make scene 2 slower" or "give the quote more time" changes one number, and
everything after it moves along automatically.

---

## Tips

- One video per folder in `videos/`, named `year-short-title`.
- Start from the newest example. Don't start from scratch.
- If you change a style rule (e.g. how post-its look), ask Claude to update `CLAUDE.md` too.
  Then the next video uses it automatically. Older videos only change if you ask for it.
- The music may be used inside the videos but must not be shared on its own.
