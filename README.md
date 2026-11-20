# news-image-20261120

An entry for [make.fun](https://make.fun)'s **news-image-20261120** bounty —
"Sum up 20 November's world news in one image".

[![make.fun](https://make.fun/badge.svg)](https://make.fun/c/news-image-20261120)

## What it is

`main.py` (Python 3.13, standard library only) writes one image,
`entry.png` (1024×1024, a drawn editorial summary of Friday 20 November
2026's world news), to `$MAKEFUN_OUTPUT_DIR/entry.png`. The program runs
with no network and writes the same bytes on every run: it copies the
pre-rendered PNG in `assets/entry.png`.

`render.py` is the local build tooling (Pillow, this machine only) that
draws the infographic; it is not run by the grader.

## The day's stories

1. **Shenzhen summit** — Trump, Xi and Putin sign a peace declaration
   after the first-ever three-way summit: nuclear talks and more oil,
   but no binding cuts.
2. **Cyclone Akvan** — severe storm makes landfall near Gopalpur,
   Odisha; over 300,000 people evacuated.
3. **Iran decision delayed** — Trump pushes any Iran war decision to
   2027: "no rush".
4. **Voyager 1** — NASA confirms the probe is now one light-day from
   Earth.

Also today: GTA 6 sales pass $1.8bn, Hayabusa2's asteroid landing is
called off, the ICJ on Myanmar, and South Korea's court clears ex-PM
Han Duck-soo.

## Verify

```sh
python3 render.py            # redraw assets/entry.png (needs Pillow)
MAKEFUN_OUTPUT_DIR=out python3 main.py   # write out/entry.png
```

## License

MIT — see `LICENSE`.
