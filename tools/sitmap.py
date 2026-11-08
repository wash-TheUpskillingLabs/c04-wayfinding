"""The problem situation map: five questions, every statement, who said it.

Builds one SVG from content/map/statements.json in the manner of Dorst's
problem situation maps (Frame Innovation, 2015): five circles for WHAT, WHO,
WHERE, WHY and HOW SOLVED, drawn as Metro lines. Themes are stations. A theme
that answers two questions is an interchange: it sits in the overlap of the
two circles, on both lines, and nothing else is allowed into that overlap.

Nothing here is typed by hand into the picture: add a statement to the JSON
and rebuild. Layout is greedy: stations spiral out from the centre of their
region, largest first; statements spiral around their station and are never
allowed to overlap one another or leave their region.
"""
import json, math, os, re, html

W, H = 2440, 1900
GOLD = math.radians(137.508)

# WHAT across the top, the symptom; the four other questions in an arc below it, each
# overlapping it and its neighbours in the chain WHO, WHY, HOW, WHERE, left to right.
# Radii and distances are sized by how many statements each region holds.
CIRCLES = {
    "what":  dict(cx=1260, cy=700, r=605, word="WHAT", line="red"),
    "who":   dict(cx=554, cy=844, r=410, word="WHO", line="ink"),
    "why":   dict(cx=955, cy=1303, r=504, word="WHY", line="ink"),
    "how":   dict(cx=1593, cy=1328, r=488, word="HOW SOLVED", line="blue"),
    "where": dict(cx=1946, cy=840, r=420, word="WHERE", line="ink"),
}
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

def dist_box(c, x, y, w, h):
    """Distance from the circle's centre to the nearest point of the box."""
    nx = min(max(c["cx"], x), x + w); ny = min(max(c["cy"], y), y + h)
    return math.hypot(nx - c["cx"], ny - c["cy"])

def within(c, x, y, w, h, pad):
    R = c["r"] - pad
    return all((px - c["cx"]) ** 2 + (py - c["cy"]) ** 2 <= R * R
               for px, py in ((x, y), (x + w, y), (x, y + h), (x + w, y + h)))

def in_region(members, x, y, w, h, pad=9, strict=True):
    """Clear of every line. strict: wholly inside every member circle (the overlap itself,
    where an interchange station goes). Loose: inside at least one member, so a shared
    theme's statements fan out from the station into either circle. Never inside a
    circle that is not a member."""
    ins = [within(CIRCLES[q], x, y, w, h, pad) for q in members]
    if not (all(ins) if strict else any(ins)): return False
    for q, c in CIRCLES.items():
        if q in members:
            if not ins[list(members).index(q)] and dist_box(c, x, y, w, h) < c["r"] + pad: return False
        elif dist_box(c, x, y, w, h) < c["r"] + pad:
            return False
    return True

def hits(boxes, x, y, w, h, gap=2):
    for bx, by, bw, bh in boxes:
        if x < bx + bw + gap and x + w + gap > bx and y < by + bh + gap and y + h + gap > by: return True
    return False

def place_near(members, boxes, ox, oy, w, h, start=0, step=3.5, strict=True):
    """First free spot on a spiral around (ox, oy), inside the region."""
    members = list(members)
    for k in range(start, 90000):
        d = step * math.sqrt(k)
        a = k * GOLD
        x = ox + d * math.cos(a) - w / 2
        y = oy + d * math.sin(a) - h / 2
        if in_region(members, x, y, w, h, strict=strict) and not hits(boxes, x, y, w, h):
            return x, y
    return None

def region_centre(members):
    """Where a region's stations start spiralling from: the centroid of the part of the
    paper that is inside every member circle and outside every other, or, for a single
    circle, the part of it that faces away from everything it overlaps."""
    members = set(members)
    cs = [CIRCLES[q] for q in members]
    if len(cs) >= 2:
        xs = ys = n = 0
        x0, x1 = max(c["cx"] - c["r"] for c in cs), min(c["cx"] + c["r"] for c in cs)
        y0, y1 = max(c["cy"] - c["r"] for c in cs), min(c["cy"] + c["r"] for c in cs)
        for i in range(60):
            for j in range(60):
                x, y = x0 + (x1 - x0) * (i + .5) / 60, y0 + (y1 - y0) * (j + .5) / 60
                ins = {q for q, c in CIRCLES.items() if (x - c["cx"]) ** 2 + (y - c["cy"]) ** 2 < c["r"] ** 2}
                if ins == members: xs += x; ys += y; n += 1
        if n: return xs / n, ys / n
        a = cs[0]; return a["cx"], a["cy"]
    c = cs[0]
    vx = vy = 0.0
    for q2, c2 in CIRCLES.items():
        if c2 is c: continue
        d = math.hypot(c2["cx"] - c["cx"], c2["cy"] - c["cy"])
        if d < c["r"] + c2["r"]:
            vx += (c2["cx"] - c["cx"]) / d; vy += (c2["cy"] - c["cy"]) / d
    n = math.hypot(vx, vy)
    if n == 0: return c["cx"], c["cy"]
    return c["cx"] - vx / n * c["r"] * .45, c["cy"] - vy / n * c["r"] * .45

def build(statements):
    """Returns the placed boxes, station labels, statements and per-question counts."""
    regions = {}
    for s in statements:
        key = frozenset(k for k in (s["q"], s.get("q2"), s.get("q3")) if k)
        regions.setdefault(key, {}).setdefault(s["theme"], []).append(s)
    boxes, labels, items = [], [], []
    counts = {q: 0 for q in CIRCLES}
    for s in statements:
        for k in (s["q"], s.get("q2"), s.get("q3")):
            if k: counts[k] += 1
    # overlaps first (they have the least room), then the single circles
    order = sorted(regions, key=lambda k: (-len(k), -sum(len(v) for v in regions[k].values())))
    placed_themes = []
    for key in order:
        themes = sorted(regions[key].items(), key=lambda kv: -len(kv[1]))
        ox, oy = region_centre(key)
        n = max(1, len(themes))
        centres = []
        reach = min(CIRCLES[q]["r"] for q in key) * {1: .55, 2: .4}.get(len(key), .25)
        for i, (theme, ss) in enumerate(themes):
            cnt = len(ss)
            rr = reach * math.sqrt((i + .5) / n)
            ang = i * GOLD + .9
            tx, ty = ox + rr * math.cos(ang), oy + rr * math.sin(ang)
            if len(key) == 1:
                fs = min(34, 12 + 1.9 * cnt)
                tl = wrap(theme, 24 if len(theme) > 26 else 40)
            else:   # an interchange: the overlap is tight, so the name stacks
                fs = min(24 if len(key) == 2 else 18, 12 + 1.4 * cnt)
                tl = wrap(theme, 15 if len(key) == 2 else 12)
            w = max(tw(l, fs, True) for l in tl) + fs * .95 + 6
            h = fs * 1.05 * len(tl)
            pos = place_near(key, boxes, tx, ty, w, h, 0, 8)
            if pos is None: pos = (tx - w / 2, ty - h / 2)
            x, y = pos
            boxes.append((x, y, w, h))
            labels.append((x, y, tl, fs, tuple(sorted(key, key=list(CIRCLES).index))))
            centres.append((x + w / 2, y + h / 2))
        placed_themes.append((key, themes, centres))
    # statements: a circle's own first, then the shared ones, which have two circles to
    # choose from. Within each pass, round robin across regions and themes so none starves.
    def pass_over(groups):
        queue = []
        for key, themes, centres in groups:
            for i, (theme, ss) in enumerate(themes):
                queue.append((key, centres[i], list(ss)))
        while queue:
            nxt = []
            for key, (cxl, cyl), ss in queue:
                s = ss.pop(0)
                lines = wrap(s["text"])
                sw = GLYPH + max(tw(l, FS) for l in lines)
                sh = LH * len(lines)
                p = place_near(key, boxes, cxl, cyl, sw, sh, 1, strict=False)
                if p is not None:
                    sx, sy = p
                    boxes.append((sx, sy, sw, sh))
                    items.append((sx, sy, lines, s["by"], s["src"], s["text"]))
                if ss: nxt.append((key, (cxl, cyl), ss))
            queue = nxt
    pass_over([t for t in placed_themes if len(t[0]) == 1])
    pass_over([t for t in placed_themes if len(t[0]) > 1])
    return boxes, None, labels, items, counts

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
    o.append(f'<desc id="pm-desc">{len(statements)} statements from alumni, organizers, the problem owner, the steering committee and other programs, sorted into what, who, where, why and how solved. Every statement is listed in the table that follows the map.</desc>')
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
    # themes as stations on their line; an interchange wears both lines' colours
    o.append(f'<g class="pm-stations" font-weight="800" fill="{INK}" letter-spacing="-.01em">')
    for x, y, tl, fs, key in labels:
        rr = fs * .3
        cx_, cy_ = x + rr + fs * .06, y + fs * .86 - fs * .36
        sw = max(2.5, fs * .13)
        if len(key) == 1:
            o.append(f'<circle cx="{cx_:.1f}" cy="{cy_:.1f}" r="{rr:.1f}" fill="{PAPER}" stroke="{LINE[CIRCLES[key[0]]["line"]]}" stroke-width="{sw:.1f}"/>')
        else:   # an interchange: one ring per line, outermost first
            step = sw * 1.4
            o.append(f'<circle cx="{cx_:.1f}" cy="{cy_:.1f}" r="{rr + sw:.1f}" fill="{PAPER}"/>')
            for n, q in enumerate(key):
                o.append(f'<circle cx="{cx_:.1f}" cy="{cy_:.1f}" r="{rr + sw - step * n:.1f}" fill="none" stroke="{LINE[CIRCLES[q]["line"]]}" stroke-width="{sw:.1f}"/>')
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
    o.append(f'<text x="48" y="188" font-size="16.494">{len(statements)} statements, as of {esc(asof)}. A theme in an overlap counts for each of its questions.</text>')
    o.append(f'<text x="48" y="236" font-size="13.745" font-weight="800">How to read the signs</text>')
    ky = 268
    for col, name in ((RED, "WHAT gets in the way: where people stop"), (INK, "WHO, WHERE and WHY"), (BLUE, "HOW SOLVED: only what worked elsewhere")):
        o.append(f'<line x1="48" y1="{ky-5}" x2="80" y2="{ky-5}" stroke="{col}" stroke-width="{LINE_W}"/>')
        o.append(f'<text x="92" y="{ky}" font-size="13.745">{esc(name)}</text>')
        ky += 24
    o.append(f'<circle cx="64" cy="{ky-5}" r="6" fill="{PAPER}" stroke="{INK}" stroke-width="3"/>')
    o.append(f'<text x="92" y="{ky}" font-size="13.745">A theme. The bigger the name, the more was said</text>')
    ky += 24
    o.append(f'<circle cx="64" cy="{ky-5}" r="8.5" fill="{PAPER}" stroke="{RED}" stroke-width="3"/><circle cx="64" cy="{ky-5}" r="4.5" fill="none" stroke="{INK}" stroke-width="3"/>')
    o.append(f'<text x="92" y="{ky}" font-size="13.745">An interchange: a theme that answers two or three questions, in their overlap</text>')
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
