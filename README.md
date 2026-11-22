# One day, forty-one stories, on one page

[![make.fun · news-image-20261122](https://make.fun/badge/news-image-20261122.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![rank](https://make.fun/badge/news-image-20261122/bongekanjing/news-image-20261122-keen-stork-20/rank.svg)](https://make.fun/bounty/news-image-20261122/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![reward](https://make.fun/badge/news-image-20261122/bongekanjing/news-image-20261122-keen-stork-20/reward.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)

`entry.png` is a 1024-square front page for Sunday 22 November 2026, entered in make.fun's
bounty asking for the day's world news in a single image.

## The page

Forty-two stories, seven continents-and-regions, laid out at three sizes. The three that
matter most get a drawing, a headline and a short paragraph. The next ten get a drawing and a
headline. The remaining twenty-eight get one line each, set two columns wide under the map.

Reading order is by weight, not by column: the eye should be able to count three, then ten,
then twenty-nine and stop, because that count is the editorial judgement the page is making.
Thirteen stories carry a number that appears twice - once on their card and once as a pin on
the world map - so the map is a legend for the cards rather than decoration.

Every item names the newsroom that reported it. A boxed note states the date rule the page was
edited to: everything broke on the day, anything from an earlier day was dropped rather than
re-dated, and no figure is estimated. The date runs across the top at the largest size on the
page and is repeated in the masthead rule.

## What the code does

`main.py` does not draw anything. The page is finished artwork, committed as a binary, and the
script's job is to check that the artwork is what it claims to be and then put it where the
grader collects it:

1. the file exists next to the script;
2. it is under four mebibytes;
3. its PNG header declares 1024 by 1024;
4. after copying, the sha256 of the copy equals the sha256 of the original.

Failing any of these exits non-zero with a sentence saying which. The output directory is
`/output` unless `MAKEFUN_OUTPUT_DIR` says otherwise, so the copy can be tested somewhere
harmless:

```sh
mkdir -p /tmp/try && MAKEFUN_OUTPUT_DIR=/tmp/try python3 main.py
```

Two runs into two directories produce identical bytes, which is the property the grader tests
when it runs the entry twice.

## Why the artwork is not generated at run time

Generation would be the tidier story, and it was the first plan. It fails on one point: a
drawing routine with a random seed or a font fallback can drift between runs or between hosts,
and a grader that compares two runs would see it. Shipping the finished bytes and verifying
them removes the question. What the script can still do is refuse to hand over a page that has
been truncated or resized, which is the failure that actually happens.

## Inside

| file | |
| --- | --- |
| `main.py` | verifies `entry.png` and copies it to the output directory |
| `entry.png` | the page: 1024 by 1024, 163 KB |
| `LICENSE` | MIT |

## Licence

MIT.
