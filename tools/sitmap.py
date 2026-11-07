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
    "what": dict(cx=400, cy=720, r=340, word="WHAT"),
    "who": dict(cx=600, cy=235, r=232, word="WHO"),
    "where": dict(cx=830, cy=920, r=205, word="WHERE"),
    "why": dict(cx=1120, cy=325, r=352, word="WHY"),
    "how": dict(cx=1340, cy=850, r=330, word="HOW SOLVED"),
}
for _c in CIRCLES.values():
    _c["cx"] = round(_c["cx"] * K); _c["cy"] = round(_c["cy"] * K + 20); _c["r"] = round(_c["r"] * K)
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

def inside(c, x, y, w, h, pad=10):
    R = c["r"] - pad
    for px, py in ((x, y), (x + w, y), (x, y + h), (x + w, y + h)):
        if (px - c["cx"]) ** 2 + (py - c["cy"]) ** 2 > R * R: return False
    return True

def hits(boxes, x, y, w, h, gap=3):
    for bx, by, bw, bh in boxes:
        if x < bx + bw + gap and x + w + gap > bx and y < by + bh + gap and y + h + gap > by: return True
    return False

def place_near(c, boxes, ox, oy, w, h, start=0, step=6.5):
    """First free spot on a spiral around (ox, oy), inside the circle."""
    for k in range(start, 6000):
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
            w = max(tw(l, fs, True) for l in tl) + 6
            h = fs * 1.05 * len(tl)
            pos = place_near(c, boxes, tx, ty, w, h, 0, 8)
            if pos is None: pos = (tx - w / 2, ty - h / 2)
            x, y = pos
            boxes.append((x, y, w, h))
            cxl, cyl = x + w / 2, y + h / 2
            labels.append((cxl, y, tl, fs))
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
                p = place_near(c, boxes, cxl, cyl, sw, sh, 1, 6.5)
                if p is None: continue
                sx, sy = p
                boxes.append((sx, sy, sw, sh))
                items.append((sx, sy, lines, s["by"], s["src"], s["text"]))
    return boxes, heat, labels, items, counts

def esc(t): return html.escape(t, quote=True)

def svg(statements, asof, underlay=None):
    boxes, heat, labels, items, counts = build(statements)
    o = []
    o.append(f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-labelledby="pm-title pm-desc" class="sitmap">')
    o.append('<title id="pm-title">The problem situation: how people find their way between the parts of The Labs</title>')
    o.append(f'<desc id="pm-desc">{sum(counts.values())} statements from alumni, organizers, the problem owner, the steering committee and other programs, sorted into what, who, where, why and how solved. Every statement is listed in the table that follows the map.</desc>')
    o.append('<style>@import url("https://fonts.googleapis.com/css2?family=Inter:wght@400;700;800&amp;display=swap");.sitmap text{font-family:Inter,system-ui,sans-serif}</style>')
    o.append('<defs><radialGradient id="pm-heat"><stop offset="0" stop-color="#0b3536" stop-opacity="1"/><stop offset=".55" stop-color="#0b3536" stop-opacity=".35"/><stop offset="1" stop-color="#0b3536" stop-opacity="0"/></radialGradient>')
    for q, c in CIRCLES.items():
        # upper-left quarter arc, running from the left point up to the top
        o.append(f'<path id="pm-arc-{q}" d="M{c["cx"]-c["r"]-14},{c["cy"]} A{c["r"]+14},{c["r"]+14} 0 0 1 {c["cx"]},{c["cy"]-c["r"]-14}"/>')
    o.append('</defs>')
    o.append(f'<rect width="{W}" height="{H}" fill="#e5e7de"/>')
    if underlay:
        o.append(f'<image href="{underlay}" x="{W*0.28:.0f}" y="{-40}" width="{W*0.9:.0f}" height="{W*0.9*0.8273:.0f}" opacity=".09" preserveAspectRatio="xMidYMid slice" style="filter:grayscale(1)"/>')
    # heat under everything
    o.append('<g class="pm-heat">')
    for x, y, r, op in heat:
        o.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r:.0f}" fill="url(#pm-heat)" opacity="{op:.2f}"/>')
    o.append('</g>')
    # circles and their words
    for q, c in CIRCLES.items():
        o.append(f'<circle cx="{c["cx"]}" cy="{c["cy"]}" r="{c["r"]}" fill="none" stroke="#0b3536" stroke-opacity=".55" stroke-width="1.2"/>')
        o.append(f'<text class="pm-word" font-size="54" font-weight="800" fill="#0b3536" fill-opacity=".22" letter-spacing=".06em"><textPath href="#pm-arc-{q}" startOffset="8%">{c["word"]}</textPath></text>')
    # statements
    o.append(f'<g class="pm-items" font-size="{FS}" fill="#0b3536">')
    for x, y, lines, by, src, full in items:
        gx, gy = x + 4.5, y + LH * .62
        hollow = by == "X"
        o.append(f'<g class="pm-s" data-by="{by}"><title>{esc(full)} — {esc(VOICE_NAME[by])}, {esc(src)}</title>')
        if hollow:
            o.append(f'<circle cx="{gx:.1f}" cy="{gy:.1f}" r="3.6" fill="none" stroke="#0b3536" stroke-width=".9"/>')
        else:
            o.append(f'<circle cx="{gx:.1f}" cy="{gy:.1f}" r="3.8" fill="#0b3536"/>')
        o.append(f'<text x="{gx:.1f}" y="{gy+1.9:.1f}" text-anchor="middle" font-size="5.2" font-weight="700" fill="{"#0b3536" if hollow else "#e5e7de"}">{by}</text>')
        for j, l in enumerate(lines):
            o.append(f'<text x="{x+GLYPH:.1f}" y="{y+LH*(j+.85):.1f}">{esc(l)}</text>')
        o.append('</g>')
    o.append('</g>')
    # theme labels on top
    o.append('<g class="pm-labels" font-weight="700" fill="#0b3536">')
    for x, y, tl, fs in labels:
        for j, t in enumerate(tl):
            o.append(f'<text x="{x:.1f}" y="{y + fs*1.05*j + fs*.86:.1f}" text-anchor="middle" font-size="{fs:.1f}">{esc(t)}</text>')
    o.append('</g>')
    # title, legend, counts
    o.append('<g fill="#0b3536">')
    o.append(f'<text x="48" y="72" font-size="34" font-weight="700">The problem situation</text>')
    o.append(f'<text x="48" y="100" font-size="15">How people find their way between the parts of The Labs. {sum(counts.values())} statements, as of {esc(asof)}.</text>')
    o.append('<text x="48" y="140" font-size="11" font-weight="700">Who said it</text>')
    for i, (k, name) in enumerate(VOICES):
        yy = 162 + i * 20
        if k == "X":
            o.append(f'<circle cx="55" cy="{yy-4}" r="5.5" fill="none" stroke="#0b3536" stroke-width="1"/><text x="55" y="{yy-1}" text-anchor="middle" font-size="7" font-weight="700">X</text>')
        else:
            o.append(f'<circle cx="55" cy="{yy-4}" r="5.8" fill="#0b3536"/><text x="55" y="{yy-1}" text-anchor="middle" font-size="7" font-weight="700" fill="#e5e7de">{k}</text>')
        o.append(f'<text x="70" y="{yy}" font-size="11">{esc(name)}</text>')
    o.append(f'<text x="48" y="{162 + len(VOICES)*20 + 8}" font-size="11">Darker ground: more was said there. Larger words: a theme more people named.</text>')
    # footer: counts per question
    parts = " · ".join(f'{CIRCLES[q]["word"].title()} {counts.get(q, 0)}' for q in CIRCLES)
    o.append(f'<text x="48" y="{H-28}" font-size="11">{esc(parts)}. Built from content/map/statements.json; add a line and rebuild. Wayfinding, a Research Pod of Build Cycle C04, The Upskilling Labs of Greater Washington.</text>')
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
