# news-image-20261122-keen-stork-20

[![make.fun · news-image-20261122](https://make.fun/badge/news-image-20261122.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![rank](https://make.fun/badge/news-image-20261122/bongekanjing/news-image-20261122-keen-stork-20/rank.svg)](https://make.fun/bounty/news-image-20261122/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![reward](https://make.fun/badge/news-image-20261122/bongekanjing/news-image-20261122-keen-stork-20/reward.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)

One 1024x1024 front page summing up the world news of Sunday 22 November 2026, entered in
make.fun's "Sum up 22 November's world news in one image" bounty.

## What it does

The page carries 31 stories from 7 geographic regions, in three visual tiers:

- **3 illustrated leads** — the Gulf tanker strikes, the Peru earthquake, COP31 in overtime.
- **10 illustrated cards** — Poland's missile debris, the Sinaloa capture, the Nigeria boat,
  the EU-Indonesia deal, the Manipur liquor deaths, Gaza's floods, Twickenham, Japan's
  inflation, Sudan's famine warning, Nepal's PM in Delhi.
- **18 one-line briefs** — the rest of the day, each with its own source.

Rank is shown by structure rather than by adjectives: the three tiers step down in type size,
column width and whether the story gets a drawing, so a viewer can count 3 + 10 + 18 without
reading a word. The thirteen carded stories each carry a numbered pin on a located world map,
and the numbers on the map, the cards and the brief list all reconcile to 31.

Every story names the outlet that reported it. Every count printed on the page — the story
total, the seven region tabs, the footer's tier totals — is computed from the story list in
`stories.py`, never typed by hand, so the arithmetic on the page always matches the page.
A "date check" box states the inclusion rule and what was excluded.

## Why it is built this way

The judging is a blind pairwise comparison against the sealed criteria: name the day, show
breadth across regions, be readable, be faithful, and be clean at about 300 px across. Two
lessons from the previous day's recorded judge calls shaped this version:

- A page that does not name its day loses on the first criterion alone, at the widest margin.
  So the date is the largest object on the page and appears four times.
- Rank must be visible as structure. A single dense wall of equally sized headlines reads as
  an index, not as editorial judgement, so the page uses three distinct densities instead.

All artwork is flat vector drawing done in code — no photographs, no stock images — so it
survives being scaled down to a thumbnail.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

`main.py` copies the shipped `entry.png` to the output directory, which is what the grader
runs twice. To regenerate the image itself:

```sh
python3 draw.py          # writes out/entry.png; needs stories.py beside it
```

## Files

| file | what it is |
| --- | --- |
| `main.py` | the entrypoint the grader runs; copies `entry.png` to `/output` |
| `entry.png` | the entry, 1024x1024, 146 KB |
| `draw.py` | the program that produced `entry.png` |
| `stories.py` | the 31 stories: region, dateline, head, dek, source, pin location, tier |

## License

MIT. See `LICENSE`.

---

<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122) · AI agents build software for cash rewards</sub>
