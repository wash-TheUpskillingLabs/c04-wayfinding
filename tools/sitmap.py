"""The problem situation map: five questions, every statement, who said it.

Builds one SVG from content/map/statements.json in the manner of Dorst's
problem situation maps (Frame Innovation, 2015): five circles for WHAT, WHO,
WHERE, WHY and HOW SOLVED; inside each, the themes sized by how many
statements they hold, and every statement in small type with a mark for who
said it. The darker the ground, the more was said there.

Nothing here is typed by hand into the picture: add a statement to the JSON
and rebuild. Layout is greedy: themes spiral out from the centre of their
circle, largest first; statements spiral around their theme and are never
allowed to overlap one another or leave the circle.
"""
import json, math, os, re, html

W, H = 2440, 1760
K = 1.43  # scale of the circle plan below
GOLD = math.radians(137.508)

# Where each circle sits. The question's word runs along its upper-left arc.
CIRCLES = {
    "what": dict(cx=400, cy=720, r=340, word="WHAT", line="red"),
    "who": dict(cx=590, cy=240, r=246, word="WHO", line="ink"),
    "where": dict(cx=835, cy=945, r=250, word="WHERE", line="ink"),
    "why": dict(cx=1120, cy=325, r=352, word="WHY", line="ink"),
    "how": dict(cx=1340, cy=850, r=330, word="HOW SOLVED", line="blue"),
}
for _c in CIRCLES.values():
    _c["cx"] = round(_c["cx"] * K); _c["cy"] = round(_c["cy"] * K + 20); _c["r"] = round(_c["r"] * K)
INK, PAPER, BLUE, RED = "#0b3536", "#e5e7de", "#0098d8", "#f54123"
LINE = {"ink": INK, "red": RED, "blue": BLUE}
LINE_W = 8      # every question is drawn as a Metro line
VOICES = [("A", "alumni"), ("O", "organizers"), ("P", "problem owner"), ("S", "steering committee"), ("X", "other programs")]
VOICE_NAME = dict(VOICES)

FS = 9.2           # statement type size
LH = 11.2          # statement line height
WRAP = 30          # characters per line before wrapping
GLYPH = 11         # width taken by the voice mark

def tw(text, fs, bold=False):
    """Rough Inter width: average advance ≈ .5em (.56 bold)."""
    return len(text) * fs * (.56 if bold else .5)

def wrap(text, n=WRAP):
    words, lines, cur = text.split(), [], ""
    for w in words:
        if cur and len(cur) + 1 + len(w) > n:
            lines.append(cur); cur = w
        else:
            cur = f"{cur} {w}" if cur else w
    if cur: lines.append(cur)
    return lines

def crosses(c, x, y, w, h, band):
    """Does the box touch this circle's line (its rim, widened by band)?"""
    nx = min(max(c["cx"], x), x + w); ny = min(max(c["cy"], y), y + h)
    near = math.hypot(nx - c["cx"], ny - c["cy"])
    far = max(math.hypot(px - c["cx"], py - c["cy"]) for px, py in ((x, y), (x + w, y), (x, y + h), (x + w, y + h)))
    return near < c["r"] + band and far > c["r"] - band

def inside(c, x, y, w, h, pad=9):
    """Inside its own line, and clear of every other line, so no stroke runs through type."""
    R = c["r"] - pad
    for px, py in ((x, y), (x + w, y), (x, y + h), (x + w, y + h)):
        if (px - c["cx"]) ** 2 + (py - c["cy"]) ** 2 > R * R: return False
    for c2 in CIRCLES.values():
        if c2 is not c and crosses(c2, x, y, w, h, pad): return False
    return True

def hits(boxes, x, y, w, h, gap=2):
    for bx, by, bw, bh in boxes:
        if x < bx + bw + gap and x + w + gap > bx and y < by + bh + gap and y + h + gap > by: return True
    return False

def place_near(c, boxes, ox, oy, w, h, start=0, step=3.5):
    """First free spot on a spiral around (ox, oy), inside the circle."""
    for k in range(start, 22000):
        d = step * math.sqrt(k)
        a = k * GOLD
        x = ox + d * math.cos(a) - w / 2
        y = oy + d * math.sin(a) - h / 2
        if inside(c, x, y, w, h) and not hits(boxes, x, y, w, h):
            return x, y
    return None

def build(statements):
    byq = {}
    for s in statements: byq.setdefault(s["q"], {}).setdefault(s["theme"], []).append(s)
    boxes, heat, labels, items = [], [], [], []
    counts = {}
    for q, c in CIRCLES.items():
        themes = sorted(byq.get(q, {}).items(), key=lambda kv: -len(kv[1]))
        counts[q] = sum(len(v) for _, v in themes)
        n = max(1, len(themes))
        centres = []
        # pass 1: every theme's label, largest first, on a sunflower from the centre
        for i, (theme, ss) in enumerate(themes):
            cnt = len(ss)
            rr = c["r"] * .68 * math.sqrt((i + .5) / n)
            ang = i * GOLD + (0.9 if q in ("what", "how") else 2.3)
            tx, ty = c["cx"] + rr * math.cos(ang), c["cy"] + rr * math.sin(ang)
            fs = min(34, 12 + 1.9 * cnt)
            tl = wrap(theme, 24 if len(theme) > 26 else 40)
            w = max(tw(l, fs, True) for l in tl) + fs * .95 + 6
            h = fs * 1.05 * len(tl)
            pos = place_near(c, boxes, tx, ty, w, h, 0, 8)
            if pos is None: pos = (tx - w / 2, ty - h / 2)
            x, y = pos
            boxes.append((x, y, w, h))
            cxl, cyl = x + w / 2, y + h / 2
            labels.append((x, y, tl, fs, q))
            heat.append((cxl, cyl, 44 + 9 * cnt, min(.34, .09 + .024 * cnt)))
            centres.append((cxl, cyl))
        # pass 2: statements, round robin so each theme keeps its nearest ground
        most = max((len(ss) for _, ss in themes), default=0)
        for k in range(most):
            for i, (theme, ss) in enumerate(themes):
                if k >= len(ss): continue
                s = ss[k]
                cxl, cyl = centres[i]
                lines = wrap(s["text"])
                sw = GLYPH + max(tw(l, FS) for l in lines)
                sh = LH * len(lines)
                p = place_near(c, boxes, cxl, cyl, sw, sh, 1)
                if p is None: continue
                sx, sy = p
                boxes.append((sx, sy, sw, sh))
                items.append((sx, sy, lines, s["by"], s["src"], s["text"]))
    return boxes, heat, labels, items, counts

def word_angle(q):
    """Where on the rim the question's sign goes: the angle facing the most open paper,
    away from the other lines, the key in the top-left corner and the poster's edges."""
    c = CIRCLES[q]; R = c["r"] + 60
    best, best_score = 0.0, -1e9
    for i in range(360):
        a = math.radians(i)
        x, y = c["cx"] + R * math.cos(a), c["cy"] + R * math.sin(a)
        score = min(x - 40, W - 40 - x, y - 40, H - 70 - y)
        if x < 520 and y < 520: score = min(score, -100)
        for q2, c2 in CIRCLES.items():
            if q2 == q: continue
            score = min(score, math.hypot(x - c2["cx"], y - c2["cy"]) - c2["r"])
        if score > best_score: best, best_score = a, score
    return best

def esc(t): return html.escape(t, quote=True)

def sign_tile(q):
    """The question's name on an enamel sign, set just outside its line where the rim faces open paper."""
    c = CIRCLES[q]
    fs, cap = 32.9879, 24          # the site's h2: cap height 24
    w = tw(c["word"], fs, True) * 1.02 + 2 * 16
    h = cap + 2 * 14
    best = word_angle(q)
    ux, uy = math.cos(best), math.sin(best)
    reach = abs(w / 2 * ux) + abs(h / 2 * uy)
    d = c["r"] + LINE_W / 2 + 10 + reach
    x = min(max(c["cx"] + d * ux - w / 2, 24), W - 24 - w)
    y = min(max(c["cy"] + d * uy - h / 2, 24), H - 24 - h)
    fill = LINE[c["line"]]
    ink_text = c["line"] != "ink"     # like .tile.red and .tile.blue: ink on the signal colours
    return (f'<g class="pm-sign"><rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="4" fill="{fill}"/>'
            f'<text x="{x + w / 2:.1f}" y="{y + 14 + cap:.1f}" text-anchor="middle" font-size="{fs}" font-weight="800" '
            f'letter-spacing=".02em" fill="{INK if ink_text else PAPER}">{c["word"]}</text></g>')

def svg(statements, asof, underlay=None):
    """underlay is accepted for older callers and ignored: the sign system allows no decoration."""
    boxes, heat, labels, items, counts = build(statements)
    o = []
    o.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-labelledby="pm-title pm-desc" class="sitmap">')
    o.append('<title id="pm-title">The problem situation: how people find their way between the parts of The Labs</title>')
    o.append(f'<desc id="pm-desc">{sum(counts.values())} statements from alumni, organizers, the problem owner, the steering committee and other programs, sorted into what, who, where, why and how solved. Every statement is listed in the table that follows the map.</desc>')
    o.append('<style>@import url("https://fonts.googleapis.com/css2?family=Inter:wght@400;700;800&amp;display=swap");'
             '.sitmap text{font-family:Inter,system-ui,sans-serif;font-feature-settings:"ss01","cv11"}</style>')
    o.append(f'<rect width="{W}" height="{H}" fill="{PAPER}"/>')
    # the five lines
    o.append('<g class="pm-lines" fill="none">')
    for q, c in CIRCLES.items():
        o.append(f'<circle cx="{c["cx"]}" cy="{c["cy"]}" r="{c["r"]}" stroke="{LINE[c["line"]]}" stroke-width="{LINE_W}"/>')
    o.append('</g>')
    # statements
    o.append(f'<g class="pm-items" font-size="{FS}" fill="{INK}">')
    for x, y, lines, by, src, full in items:
        gx, gy = x + 4.5, y + LH * .62
        hollow = by == "X"
        o.append(f'<g class="pm-s" data-by="{by}"><title>{esc(full)} — {esc(VOICE_NAME[by])}, {esc(src)}</title>')
        if hollow:
            o.append(f'<circle cx="{gx:.1f}" cy="{gy:.1f}" r="3.5" fill="{PAPER}" stroke="{INK}" stroke-width="1"/>')
        else:
            o.append(f'<circle cx="{gx:.1f}" cy="{gy:.1f}" r="3.8" fill="{INK}"/>')
        o.append(f'<text x="{gx:.1f}" y="{gy+1.9:.1f}" text-anchor="middle" font-size="5.2" font-weight="800" fill="{INK if hollow else PAPER}">{by}</text>')
        for j, l in enumerate(lines):
            o.append(f'<text x="{x+GLYPH:.1f}" y="{y+LH*(j+.85):.1f}">{esc(l)}</text>')
        o.append('</g>')
    o.append('</g>')
    # themes as stations on their line
    o.append(f'<g class="pm-stations" font-weight="800" fill="{INK}" letter-spacing="-.01em">')
    for x, y, tl, fs, q in labels:
        rr = fs * .3
        o.append(f'<circle cx="{x + rr + fs*.06:.1f}" cy="{y + fs*.86 - fs*.36:.1f}" r="{rr:.1f}" fill="{PAPER}" stroke="{LINE[CIRCLES[q]["line"]]}" stroke-width="{max(2.5, fs*.13):.1f}"/>')
        for j, t in enumerate(tl):
            o.append(f'<text x="{x + fs*.95:.1f}" y="{y + fs*1.05*j + fs*.86:.1f}" font-size="{fs:.1f}">{esc(t)}</text>')
    o.append('</g>')
    # the question signs, outside their lines
    for q in CIRCLES:
        o.append(sign_tile(q))
    # title and key, set like the site: cap heights on whole pixels, 4px steps
    o.append(f'<g fill="{INK}">')
    o.append(f'<text x="48" y="88" font-size="54.98" font-weight="800" letter-spacing="-.025em">The problem</text>')
    o.append(f'<text x="48" y="148" font-size="54.98" font-weight="800" letter-spacing="-.025em">situation</text>')
    o.append(f'<text x="48" y="188" font-size="16.494">{sum(counts.values())} statements, as of {esc(asof)}.</text>')
    o.append(f'<text x="48" y="236" font-size="13.745" font-weight="800">How to read the signs</text>')
    ky = 268
    for col, name in ((RED, "WHAT gets in the way: where people stop"), (INK, "WHO, WHERE and WHY"), (BLUE, "HOW SOLVED: only what worked elsewhere")):
        o.append(f'<line x1="48" y1="{ky-5}" x2="80" y2="{ky-5}" stroke="{col}" stroke-width="{LINE_W}"/>')
        o.append(f'<text x="92" y="{ky}" font-size="13.745">{esc(name)}</text>')
        ky += 24
    o.append(f'<circle cx="64" cy="{ky-5}" r="6" fill="{PAPER}" stroke="{INK}" stroke-width="3"/>')
    o.append(f'<text x="92" y="{ky}" font-size="13.745">A theme. The bigger the name, the more was said</text>')
    ky += 32
    for k, name in VOICES:
        if k == "X":
            o.append(f'<circle cx="64" cy="{ky-5}" r="6.5" fill="{PAPER}" stroke="{INK}" stroke-width="1.4"/><text x="64" y="{ky-1.6}" text-anchor="middle" font-size="9" font-weight="800">X</text>')
        else:
            o.append(f'<circle cx="64" cy="{ky-5}" r="7" fill="{INK}"/><text x="64" y="{ky-1.6}" text-anchor="middle" font-size="9" font-weight="800" fill="{PAPER}">{k}</text>')
        o.append(f'<text x="92" y="{ky}" font-size="13.745">{esc(name)}</text>')
        ky += 24
    parts = " · ".join(f'{CIRCLES[q]["word"].title()} {counts.get(q, 0)}' for q in CIRCLES)
    for j, line in enumerate((parts + ".", "Built from content/map/statements.json; add a line and rebuild.",
                              "Wayfinding, a Research Pod of Build Cycle C04,", "The Upskilling Labs of Greater Washington.")):
        o.append(f'<text x="48" y="{H - 32 - 24 * (3 - j)}" font-size="13.745">{esc(line)}</text>')
    o.append('</g></svg>')
    return "\n".join(o), counts, items

def table(statements):
    """The same statements as a table, for screen readers and for reading."""
    order = list(CIRCLES)
    rows = []
    for q in order:
        ss = [s for s in statements if s["q"] == q]
        themes = {}
        for s in ss: themes.setdefault(s["theme"], []).append(s)
        for theme, items in sorted(themes.items(), key=lambda kv: -len(kv[1])):
            for s in items:
                cells = (CIRCLES[q]["word"].title(), theme, s["text"], VOICE_NAME[s["by"]], s["src"])
                rows.append("<tr>" + "".join(f'<td><span class="t t-small">{esc(c)}</span></td>' for c in cells) + "</tr>")
    return ('<table class="pm-table"><thead><tr><th><span class="t t-small">Question</span></th><th><span class="t t-small">Theme</span></th><th><span class="t t-small">Statement</span></th><th><span class="t t-small">Who</span></th><th><span class="t t-small">Source</span></th></tr></thead><tbody>'
            + "".join(rows) + '</tbody></table>')
