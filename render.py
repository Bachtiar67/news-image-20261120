#!/usr/bin/env python3
"""Draw the 20 November 2026 world-news summary image (1024x1024 PNG).

Local build tooling only: the graded entrypoint (main.py) copies the
rendered asset byte-for-byte. Requires Pillow on this machine.
"""
import os
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                   "assets", "entry.png")

SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

NAVY = (15, 35, 64)
GOLD = (217, 164, 65)
INK = (18, 24, 34)
GREY = (84, 94, 108)
BG = (238, 241, 245)
WHITE = (255, 255, 255)
RED = (176, 58, 46)
TEAL = (14, 124, 123)
BLUE = (31, 78, 121)
PURPLE = (91, 58, 142)

img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)

f_title = ImageFont.truetype(SERIF_B, 50)
f_date = ImageFont.truetype(SANS_B, 24)
f_stand = ImageFont.truetype(SANS, 20)
f_tag = ImageFont.truetype(SANS_B, 18)
f_head = ImageFont.truetype(SANS_B, 26)
f_cap = ImageFont.truetype(SANS, 18)
f_strip = ImageFont.truetype(SANS, 18)
f_foot = ImageFont.truetype(SANS, 15)


def centre(text, font, y, fill, cx=W // 2):
    w = d.textlength(text, font=font)
    d.text((cx - w / 2, y), text, font=font, fill=fill)


def wrap(text, font, max_w):
    lines, cur = [], ""
    for word in text.split():
        trial = (cur + " " + word).strip()
        if d.textlength(trial, font=font) <= max_w:
            cur = trial
        else:
            lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


# ---------------- masthead ----------------
d.rectangle([0, 0, W, 148], fill=NAVY)
d.rectangle([0, 148, W, 152], fill=GOLD)
centre("THE WORLD TODAY", f_title, 14, WHITE)
centre("FRIDAY, 20 NOVEMBER 2026", f_date, 74, GOLD)
centre("Four stories that defined the day \u2014 from Shenzhen to deep space",
       f_stand, 108, (200, 210, 225))


# ---------------- illustration helpers ----------------
def draw_flags(x, y, w, h):
    """Three national flags (China, Russia, USA) above a skyline."""
    d.rectangle([x, y, x + w, y + h], fill=(176, 196, 222))
    # skyline
    base = y + h
    for bx, bw, bh in [(0, 60, 46), (70, 44, 66), (124, 70, 38),
                       (204, 52, 58), (266, 46, 40), (322, 58, 68),
                       (390, 70, 44)]:
        d.rectangle([x + bx, base - bh, x + bx + bw, base], fill=(38, 52, 74))
    fw, fh, gap = 132, 74, 22
    fx = x + (w - (3 * fw + 2 * gap)) // 2
    fy = y + 8
    # China
    d.rectangle([fx, fy, fx + fw, fy + fh], fill=(222, 41, 16))
    d.ellipse([fx + 12, fy + 12, fx + 30, fy + 30], fill=(255, 222, 0))
    for sx, sy in [(44, 12), (56, 20), (56, 34), (44, 42)]:
        d.ellipse([fx + sx, fy + sy, fx + sx + 7, fy + sy + 7],
                  fill=(255, 222, 0))
    # Russia
    rx = fx + fw + gap
    d.rectangle([rx, fy, rx + fw, fy + fh // 3 + 2], fill=WHITE)
    d.rectangle([rx, fy + fh // 3, rx + fw, fy + 2 * fh // 3 + 2],
                fill=(0, 57, 166))
    d.rectangle([rx, fy + 2 * fh // 3, rx + fw, fy + fh], fill=(213, 0, 50))
    # USA
    ux = rx + fw + gap
    for i in range(7):
        col = (179, 25, 66) if i % 2 == 0 else WHITE
        d.rectangle([ux, fy + i * fh // 7, ux + fw, fy + (i + 1) * fh // 7 + 1],
                    fill=col)
    d.rectangle([ux, fy, ux + fw // 2, fy + fh // 2 + 4], fill=(10, 49, 97))
    for sx in range(5):
        for sy in range(3):
            d.ellipse([ux + 6 + sx * 12, fy + 5 + sy * 11,
                       ux + 11 + sx * 12, fy + 10 + sy * 11], fill=WHITE)


def draw_cyclone(x, y, w, h):
    """Spiral storm over a coastline, with a warning triangle."""
    d.rectangle([x, y, x + w, y + h], fill=(207, 226, 240))
    cx, cy = x + w // 2 - 30, y + h // 2 - 6
    for r in range(15, 66, 13):
        d.arc([cx - r, cy - r, cx + r, cy + r], start=20, end=300,
              fill=(14, 124, 123), width=7)
    d.ellipse([cx - 13, cy - 13, cx + 13, cy + 13], fill=(240, 244, 248))
    # rain streaks
    for rx in range(x + 12, x + w - 40, 26):
        d.line([rx, y + 8, rx - 8, y + 34], fill=(90, 130, 170), width=3)
    # coastline
    d.polygon([(x, y + h), (x + w, y + h), (x + w, y + h - 26),
               (x + 200, y + h - 44), (x, y + h - 30)], fill=(122, 158, 92))
    d.polygon([(x, y + h - 30), (x + 200, y + h - 44), (x + w, y + h - 26),
               (x + w, y + h - 8), (x, y + h - 8)], fill=(46, 110, 160))
    # warning triangle
    tx, ty = x + w - 78, y + 10
    d.polygon([(tx + 26, ty), (tx + 52, ty + 46), (tx, ty + 46)],
              fill=(240, 180, 0))
    d.rectangle([tx + 23, ty + 14, tx + 29, ty + 34], fill=(20, 20, 20))
    d.ellipse([tx + 22, ty + 38, tx + 30, ty + 45], fill=(20, 20, 20))


def draw_calendar(x, y, w, h):
    """A wall calendar page marked 2027, beside a clock."""
    d.rectangle([x, y, x + w, y + h], fill=(226, 232, 240))
    # calendar page
    px, py, pw, ph = x + 30, y + 12, 250, 128
    d.rounded_rectangle([px, py, px + pw, py + ph], radius=8, fill=WHITE)
    d.rounded_rectangle([px, py, px + pw, py + 34], radius=8, fill=RED)
    d.rectangle([px, py + 20, px + pw, py + 34], fill=RED)
    centre("JANUARY", f_tag, py + 6, WHITE, cx=px + pw // 2)
    d.text((px + 26, py + 46), "2027", font=ImageFont.truetype(SANS_B, 46),
           fill=INK)
    d.text((px + 176, py + 58), "\u2713", font=ImageFont.truetype(SANS_B, 44),
           fill=(34, 139, 34))
    d.text((px + 24, py + 102), "Decision delayed", font=f_cap, fill=GREY)
    # clock
    ccx, ccy, cr = x + w - 78, y + 66, 44
    d.ellipse([ccx - cr, ccy - cr, ccx + cr, ccy + cr], fill=WHITE,
              outline=INK, width=4)
    d.line([ccx, ccy, ccx, ccy - 26], fill=INK, width=4)
    d.line([ccx, ccy, ccx + 20, ccy + 8], fill=INK, width=4)
    d.ellipse([ccx - 4, ccy - 4, ccx + 4, ccy + 4], fill=INK)


def draw_voyager(x, y, w, h):
    """A probe with a dish beaming home, Earth a small blue dot."""
    d.rectangle([x, y, x + w, y + h], fill=(10, 16, 34))
    for sx, sy, sr in [(30, 20, 2), (90, 44, 1), (150, 14, 2), (210, 52, 1),
                       (280, 22, 2), (340, 46, 1), (400, 16, 2), (60, 90, 1),
                       (430, 96, 2), (120, 110, 1), (330, 118, 1)]:
        d.ellipse([x + sx, y + sy, x + sx + sr * 2, y + sy + sr * 2],
                  fill=WHITE)
    # signal arcs from Earth to probe
    ex, ey = x + 52, y + h - 34
    for r in (18, 34, 50):
        d.arc([ex - r, ey - r, ex + r, ey + r], start=270, end=20,
              fill=(120, 200, 255), width=3)
    d.ellipse([ex - 16, ey - 16, ex + 16, ey + 16], fill=(40, 110, 220))
    d.ellipse([ex - 6, ey - 8, ex + 6, ey + 2], fill=(60, 180, 90))
    # probe: dish (wide gold ellipse) + body + boom
    px, py = x + w - 170, y + 34
    d.ellipse([px, py, px + 88, py + 44], fill=(217, 164, 65),
              outline=(170, 120, 40), width=2)
    d.ellipse([px + 30, py + 14, px + 58, py + 30], fill=(240, 196, 90))
    d.rectangle([px + 10, py + 52, px + 78, py + 66], fill=(200, 200, 210))
    d.line([px + 44, py + 66, px + 44, py + 92], fill=(200, 200, 210), width=4)
    d.line([px + 88, py + 22, px + 150, py + 8], fill=(180, 180, 190), width=3)
    d.ellipse([px + 146, py + 4, px + 154, py + 12], fill=(255, 80, 80))
    d.text((x + 118, y + h - 26), "1 light-day from Earth",
           font=ImageFont.truetype(SANS_B, 16), fill=(150, 200, 255))


# ---------------- story grid ----------------
STORIES = [
    dict(tag="SHENZHEN SUMMIT", colour=RED,
         head=["TRUMP, XI & PUTIN SIGN", "PEACE DECLARATION"],
         cap=("First three-way summit ends with a pledge on nuclear "
              "talks and more oil \u2014 but no binding cuts, and no "
              "end to the wars in Ukraine or Iran."),
         art=draw_flags),
    dict(tag="INDIA", colour=TEAL,
         head=["CYCLONE AKVAN HITS", "ODISHA COAST"],
         cap=("Severe storm makes landfall near Gopalpur with "
              "100 km/h winds. Over 300,000 people evacuated; "
              "423 rescue teams deployed."),
         art=draw_cyclone),
    dict(tag="WASHINGTON", colour=BLUE,
         head=["TRUMP PUTS IRAN WAR", "DECISION OFF TO 2027"],
         cap=("President says there is \u2018no rush\u2019 and he will "
              "\u2018see what happens\u2019 after 1 January, pushing "
              "any decision on Iran into next year."),
         art=draw_calendar),
    dict(tag="SPACE", colour=PURPLE,
         head=["VOYAGER 1 REACHES ONE", "LIGHT-DAY FROM EARTH"],
         cap=("NASA confirms the probe is now a light-day away "
              "\u2014 the farthest human-made object ever, still "
              "phoning home after 49 years."),
         art=draw_voyager),
]

CELL_W, CELL_H, GAP, MX = 500, 336, 8, 8
TOP = 160
for i, s in enumerate(STORIES):
    cx = MX + (i % 2) * (CELL_W + GAP)
    cy = TOP + (i // 2) * (CELL_H + GAP)
    d.rectangle([cx, cy, cx + CELL_W, cy + CELL_H], fill=WHITE,
                outline=(200, 208, 218), width=1)
    d.rectangle([cx, cy, cx + CELL_W, cy + 30], fill=s["colour"])
    d.text((cx + 12, cy + 5), s["tag"], font=f_tag, fill=WHITE)
    hy = cy + 40
    for line in s["head"]:
        d.text((cx + 12, hy), line, font=f_head, fill=INK)
        hy += 30
    s["art"](cx + 12, cy + 108, CELL_W - 24, 128)
    cap_lines = wrap(s["cap"], f_cap, CELL_W - 24)
    ty = cy + 244
    for line in cap_lines[:4]:
        d.text((cx + 12, ty), line, font=f_cap, fill=(52, 60, 72))
        ty += 22

# ---------------- also today strip ----------------
sy = TOP + 2 * CELL_H + GAP + 8
d.rectangle([MX, sy, W - MX, sy + 84], fill=(255, 250, 235),
            outline=(220, 200, 140), width=1)
d.text((MX + 12, sy + 6), "ALSO TODAY", font=f_tag, fill=(146, 96, 12))
strip = ("GTA 6 sales pass $1.8bn  \u00b7  Hayabusa2 engine fault ends its "
         "asteroid landing  \u00b7  ICJ: Myanmar likely sought to destroy "
         "the Rohingya  \u00b7  South Korea court clears ex-PM Han Duck-soo")
for j, line in enumerate(wrap(strip, f_strip, W - 2 * MX - 24)):
    d.text((MX + 12, sy + 30 + j * 22), line, font=f_strip, fill=(52, 60, 72))

# ---------------- footer ----------------
fy = sy + 84 + 10
d.line([MX, fy, W - MX, fy], fill=(180, 188, 198), width=1)
centre("Sources: Reuters, CNN, Le Monde, The Times, The Hindu, IMD  \u00b7  "
       "Drawn summary of the day's news", f_foot, fy + 8, GREY)

os.makedirs(os.path.dirname(OUT), exist_ok=True)
img.save(OUT, format="PNG")
print("wrote", OUT, img.size, os.path.getsize(OUT), "bytes")
