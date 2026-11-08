"""How the region fits together, as one chart in the Wayfinding sign system.

Rows, one above the other: how the region is organised, the Cycle's dates, a
person's route, and, dashed, what is planned: where people gather, and the commons
of OLOS, modules and kits. Each row is a sequence of steps. Where the same thing
appears in two rows (a pod, the vote, the showcase) the steps share a column and a
connector between them says what passes across. Red marks where people stop.

Everything is read from content/flow/flow.json; edit that and rebuild.
"""
import json, math, html

INK, PAPER, BLUE, RED = "#0b3536", "#e5e7de", "#0098d8", "#f54123"
LINE = {"ink": INK, "blue": BLUE, "red": RED}
LINE_W = 8

W = 2600
LEFT, COL = 440, 138          # first column's x, and the step between columns
LANE_Y0, LANE_DY = 500, 384   # first line's y, and the step between lines
TOP = 24                      # 4px grid: everything lands on multiples of 4
FS, LH = 13.745, 20           # station text: the site's t-small, on a 20px rhythm
NAME_FS = 16.494              # station names: the site's body size
WRAP = 15
DASH = '22 14'       # a planned line, like a Metro line under construction

def esc(t): return html.escape(t, quote=True)

def wrap(text, n=WRAP):
    words, lines, cur = text.split(), [], ""
    for w in words:
        if cur and len(cur) + 1 + len(w) > n: lines.append(cur); cur = w
        else: cur = f"{cur} {w}" if cur else w
    if cur: lines.append(cur)
    return lines

def load(path):
    return json.load(open(path, encoding="utf-8"))

def svg(data):
    lanes = data["lanes"]
    ncol = max(s["col"] for l in lanes for s in l["stations"]) + 1
    H = LANE_Y0 + sum(l.get("gap", LANE_DY) for l in lanes[1:]) + 260
    xs = lambda col: LEFT + col * COL
    ys, y = {}, LANE_Y0
    for i, l in enumerate(lanes):
        if i: y += l.get("gap", LANE_DY)
        ys[l["id"]] = y
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-labelledby="fl-title fl-desc" class="flow">',
         f'<title id="fl-title">{esc(data["title"])}</title>',
         '<desc id="fl-desc">Three lines: how the region is organised, the Cycle’s dates, and a person’s route through them. Stations that share a column are the same thing seen from two lines.</desc>',
         '<style>@import url("https://fonts.googleapis.com/css2?family=Inter:wght@400;700;800&amp;display=swap");'
         '.flow text{font-family:Inter,system-ui,sans-serif;font-feature-settings:"ss01","cv11"}.flow .num{font-variant-numeric:tabular-nums}</style>',
         f'<rect width="{W}" height="{H}" fill="{PAPER}"/>']
    # interchanges: a rail between stations that are the same thing on two lines. Each rail
    # segment carries an arrow for what passes across it, and says what that is.
    links = {}
    for l in lanes:
        for s in l["stations"]:
            if s.get("link"): links.setdefault(s["link"], []).append((xs(s["col"]), ys[l["id"]]))
    o.append('<g class="fl-rails">')
    for r in data.get("rails", []):
        a, b = r["between"]
        x = xs(next(s["col"] for l in lanes if l["id"] == a for s in l["stations"] if s.get("link") == r["link"]))
        ya, yb = ys[a], ys[b]
        col = RED if r.get("stop") else INK
        dash = ' stroke-dasharray="2 8"' if r.get("stop") else (' stroke-dasharray="8 8"' if r.get("planned") else "")
        y0, y1 = min(ya, yb), max(ya, yb)
        o.append(f'<line x1="{x}" y1="{y0}" x2="{x}" y2="{y1}" stroke="{col}" stroke-width="3"{dash} stroke-linecap="round"/>')
        # the arrow: on the rail, 48px short of the station it points at
        if r["dir"] == "up":
            ty = y0 + 44; o.append(f'<path d="M{x - 9},{ty + 10}l9,-10 9,10" stroke="{col}" stroke-width="3" fill="none" stroke-linecap="round" stroke-linejoin="round"/>')
        else:
            ty = y1 - 44; o.append(f'<path d="M{x - 9},{ty - 10}l9,10 9,-10" stroke="{col}" stroke-width="3" fill="none" stroke-linecap="round" stroke-linejoin="round"/>')
        # the label, beside the rail, midway between the lines
        nxt = min((v for v in ys.values() if v > y0), default=y1)
        ly = (y0 + nxt) / 2        # the middle of the first gap below the rail's top
        lines = wrap(r["label"], 18)
        rail_xs = {xs(s["col"]) for l in lanes for s in l["stations"] if s.get("link")}
        crowded = any(0 < ox - x < 170 for ox in rail_xs)
        left = r["side"] == "left" if r.get("side") else (x > W - 220 or crowded)
        for j, t in enumerate(lines):
            o.append(f'<text x="{x - 14 if left else x + 14}" y="{ly - LH * (len(lines) - 1) / 2 + LH * j + 5:.0f}"{" text-anchor=\"end\"" if left else ""} font-size="{FS}" font-weight="700" fill="{col}">{esc(t)}</text>')
    o.append('</g>')
    # the region and the two things it runs, bracketed as one block
    grp = [ys[l["id"]] for l in lanes if l.get("group") == "region"]
    if len(grp) > 1:
        o.append(f'<path d="M36,{min(grp) - 120}V{max(grp) + 60}" stroke="{INK}" stroke-width="4" fill="none" stroke-linecap="round"/>')
    # the lines
    for l in lanes:
        y = ys[l["id"]]; col = LINE[l["line"]]
        x0 = xs(l["stations"][0]["col"]); x1 = xs(l["stations"][-1]["col"])
        dash = f' stroke-dasharray="{DASH}"' if l.get("planned") else ""
        if l["end"] == "arrow":
            x1e = x1 + COL * .9
            o.append(f'<path d="M{x0},{y}H{x1e}" stroke="{col}" stroke-width="{LINE_W}" stroke-linecap="round" fill="none"/>')
            o.append(f'<path d="M{x1e - 14},{y - 12}l14,12-14,12" stroke="{col}" stroke-width="6" fill="none" stroke-linecap="round" stroke-linejoin="round"/>')
            if l.get("end_label"):
                for j, t in enumerate(wrap(l["end_label"], 18)):
                    o.append(f'<text x="{x1e + 6}" y="{y - 36 - LH * (1 - j)}" text-anchor="end" font-size="{FS}" font-weight="700" fill="{INK}">{esc(t)}</text>')
        else:
            o.append(f'<path d="M{x0},{y}H{x1}" stroke="{col}" stroke-width="{LINE_W}" stroke-linecap="butt" fill="none"{dash}/>')
            if l["end"] == "stop":
                o.append(f'<line x1="{x1}" y1="{y - 18}" x2="{x1}" y2="{y + 18}" stroke="{col}" stroke-width="{LINE_W}" stroke-linecap="round"/>')
        # the line's name at the left, and what the line gives and gets
        name_lines = wrap(l["name"], 24)
        ny = y - 60 - 28 * (len(name_lines) - 1)
        for j, t in enumerate(name_lines):
            o.append(f'<text x="56" y="{ny + 28 * j}" font-size="21.9919" font-weight="800" letter-spacing="-.01em" fill="{INK}">{esc(t)}</text>')
        if l.get("planned"):
            o.append(f'<rect x="56" y="{ny - 50}" width="76" height="24" rx="4" fill="none" stroke="{INK}" stroke-width="2" stroke-dasharray="4 3"/>')
            o.append(f'<text x="94" y="{ny - 33}" text-anchor="middle" font-size="{FS}" font-weight="800" fill="{INK}">Planned</text>')
        gy = y - 28
        for head, body in (("Gives", l.get("gives", "")), ("Gets", l.get("gets", ""))):
            o.append(f'<text x="56" y="{gy}" font-size="{FS}" font-weight="800" fill="{INK}">{head}</text>')
            for j, t in enumerate(wrap(body, 34)):
                o.append(f'<text x="112" y="{gy + LH * j}" font-size="{FS}" fill="{INK}">{esc(t)}</text>')
            gy += LH * len(wrap(body, 34)) + 8
    # stations
    for i, l in enumerate(lanes):
        y = ys[l["id"]]; col = LINE[l["line"]]
        for s in l["stations"]:
            x = xs(s["col"])
            ring = RED if s.get("stop") else col
            shared = s.get("link") and len(links[s["link"]]) > 1
            if shared:
                o.append(f'<circle cx="{x}" cy="{y}" r="15" fill="{PAPER}" stroke="{INK}" stroke-width="4"/>')
                o.append(f'<circle cx="{x}" cy="{y}" r="8" fill="none" stroke="{ring}" stroke-width="4"/>')
            else:
                o.append(f'<circle cx="{x}" cy="{y}" r="12" fill="{PAPER}" stroke="{ring}" stroke-width="5"/>')
            # name and note, stacked; neighbours alternate above and below the line so
            # they never touch. Text wears a paper halo where a rail passes behind it.
            halo = f' stroke="{PAPER}" stroke-width="6" paint-order="stroke" stroke-linejoin="round"' if shared else ""
            name = wrap(s["name"], WRAP); note = wrap(s.get("note", ""), 19)
            rows = []   # (text, size, weight, opacity, class)
            if s.get("date"): rows.append((s["date"], FS, 700, 1, ' class="num"'))
            rows += [(t, NAME_FS, 800, 1, "") for t in name]
            rows += [(t, FS, 400, .76, "") for t in note]
            side = l.get("labels", "alternate")
            below = side == "below" or (side == "alternate" and s["col"] % 2 == 0)
            ty = y + 44 if below else y - 28 - LH * (len(rows) - 1)
            for (t, fs, wt, op, cls) in rows:
                o.append(f'<text{cls} x="{x}" y="{ty:.0f}" text-anchor="middle" font-size="{fs}" font-weight="{wt}" fill="{INK}"{" fill-opacity=%.2f" % op if op < 1 else ""}{halo}>{esc(t)}</text>')
                ty += LH
    # title and key
    o.append(f'<text x="48" y="88" font-size="54.98" font-weight="800" letter-spacing="-.025em" fill="{INK}">{esc(data["title"])}</text>')
    if data.get("subtitle"):
        o.append(f'<text x="48" y="128" font-size="16.494" fill="{INK}">{esc(data["subtitle"])}</text>')
    ky = 172
    o.append(f'<text x="48" y="{ky}" font-size="{FS}" font-weight="800" fill="{INK}">How to read it</text>'); ky += 28
    for colr, name in ((INK, "The region, what it runs, and the Cycle’s dates"), (BLUE, "A person’s route")):
        o.append(f'<line x1="48" y1="{ky - 5}" x2="80" y2="{ky - 5}" stroke="{colr}" stroke-width="{LINE_W}"/>')
        o.append(f'<text x="92" y="{ky}" font-size="{FS}" fill="{INK}">{esc(name)}</text>'); ky += 24
    o.append(f'<circle cx="64" cy="{ky - 5}" r="7" fill="{PAPER}" stroke="{INK}" stroke-width="3"/><circle cx="64" cy="{ky - 5}" r="3" fill="none" stroke="{BLUE}" stroke-width="2.5"/>')
    o.append(f'<text x="92" y="{ky}" font-size="{FS}" fill="{INK}">The same step in two rows</text>'); ky += 24
    o.append(f'<line x1="64" y1="{ky - 14}" x2="64" y2="{ky + 2}" stroke="{INK}" stroke-width="3" stroke-linecap="round"/><path d="M58,{ky - 8}l6,-6 6,6" stroke="{INK}" stroke-width="3" fill="none" stroke-linecap="round" stroke-linejoin="round"/>')
    o.append(f'<text x="92" y="{ky}" font-size="{FS}" fill="{INK}">What passes between them, and which way</text>'); ky += 24
    o.append(f'<circle cx="64" cy="{ky - 5}" r="6" fill="{PAPER}" stroke="{RED}" stroke-width="3"/>')
    o.append(f'<text x="92" y="{ky}" font-size="{FS}" fill="{INK}">Where people stop</text>'); ky += 24
    o.append(f'<line x1="48" y1="{ky - 5}" x2="80" y2="{ky - 5}" stroke="{INK}" stroke-width="{LINE_W}" stroke-dasharray="10 6"/>')
    o.append(f'<text x="92" y="{ky}" font-size="{FS}" fill="{INK}">Planned: not running yet</text>')
    o.append(f'<text x="48" y="{H - 32}" font-size="{FS}" fill="{INK}">Built from content/flow/flow.json; edit it and rebuild. Wayfinding, a Research Pod of Build Cycle C04, The Upskilling Labs of Greater Washington.</text>')
    o.append('</svg>')
    return "\n".join(o), W, H
