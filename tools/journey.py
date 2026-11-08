"""The participant journey: one map, left to right, one column per step.

Builds one SVG from content/journey/journey.json. The thick blue line is one
person's way through The Labs. Around it, the shape of the work: many ways in;
inside the Cycle, proposals open up and choices narrow them, and the Cycle
branches into pods and then projects; after it, many ways out. The blue line
runs straight through the middle of that shape, so you can see your own path
and every path beside it.

Red dotted lines leave between two steps and end in a ring, as on the region
chart. Arcs above are people skipping ahead or coming back. Under each step,
four lanes: what you do, where, who is with you, and what people told us,
quoted from the pod's statements (content/map/statements.json). Add a column, a
branch or a quote to the JSON and rebuild.
"""
import json

INK, PAPER, BLUE, RED = "#0b3536", "#e5e7de", "#0098d8", "#f54123"
FONT = "Inter, system-ui, sans-serif"
LM, LABW, COLW, GAP = 56, 190, 274, 22
LINE_Y = 580
STEP_Y = LINE_Y - 128          # step numbers
TITLE_Y = LINE_Y + 122         # step titles
RING_Y = LINE_Y + 196          # leak rings
LANES = [("do", "You", 850), ("where", "Where", 1030), ("with", "With you", 1150), ("told", "What People Told Us", 1280)]
FS, LH, TFS, SFS = 15.118, 21, 21.993, 13.745
BOTTOM = 1580
H = 1790


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def wrap(text, n):
    out, line = [], ""
    for w in text.split():
        if line and len(line) + 1 + len(w) > n:
            out.append(line)
            line = w
        else:
            line = f"{line} {w}".strip()
    return out + ([line] if line else [])


def load(path):
    with open(path) as f:
        return json.load(f)


def lens(x1, x2, y, h, h1=4, h2=4):
    """A shape that opens from x1 and closes at x2: proposals, then a choice."""
    xm = (x1 + x2) / 2
    path = (f'M{x1},{y - h1} Q{xm},{y - h * 2 + (h1 + h2) / 2} {x2},{y - h2} '
            f'L{x2},{y + h2} Q{xm},{y + h * 2 - (h1 + h2) / 2} {x1},{y + h1} Z')
    return (f'<path d="{path}" fill="{PAPER}" stroke="{INK}" '
            f'stroke-width="{2.5 if h > 10 else 1.5}"/>')


def bend(x1, y1, x2, y2, w=2.5, color=INK):
    xm = (x1 + x2) / 2
    return f'<path d="M{x1},{y1} C{xm},{y1} {xm},{y2} {x2},{y2}" fill="none" stroke="{color}" stroke-width="{w}"/>'


def small(x, y, text, anchor="middle", weight=400, italic=False, caps=False, fill=INK):
    t = esc(text).upper() if caps else esc(text)
    return (f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-size="{SFS}" font-weight="{weight}" '
            f'{"font-style=\"italic\" " if italic else ""}{"letter-spacing=\".5\" " if caps else ""}fill="{fill}">{t}</text>')


def svg(d):
    cols = d["columns"]
    idx = {c["id"]: i for i, c in enumerate(cols)}
    cw = [c.get("w", COLW) for c in cols]
    starts = [LM + LABW + sum(cw[:i]) + i * GAP for i in range(len(cols))]
    x0 = lambda i: starts[i]
    cx = lambda i: x0(i) + 18
    W = starts[-1] + cw[-1] + LM
    sh = d["shape"]
    at = lambda spec: cx(idx[spec[0]]) + spec[1]
    back, front = [], []     # the shape sits behind the line; stations and labels in front

    # the Cycle, shaded
    cyc = [i for i, c in enumerate(cols) if c.get("cycle")]
    a, b = x0(cyc[0]) - GAP / 2, x0(cyc[-1]) + cw[cyc[-1]] + GAP / 2
    back.append(f'<rect x="{a}" y="{LINE_Y - 150}" width="{b - a}" height="{BOTTOM - LINE_Y + 150}" rx="4" fill="none" '
                f'stroke="{INK}" stroke-width="3"/>'
                f'<rect x="{a}" y="{BOTTOM - 40}" width="132" height="40" fill="{INK}"/>'
                + small(a + 16, BOTTOM - 14, "The Cycle", "start", 700, caps=True, fill=PAPER))
    # bands: Learn, Build, Share
    for name, s, e in d["bands"]:
        bx, ex = x0(idx[s]), x0(idx[e]) + cw[idx[e]]
        back.append(f'<rect x="{bx}" y="212" width="{ex - bx}" height="6" fill="{INK}"/>'
                    f'<text x="{bx}" y="200" font-size="15.118" font-weight="700" letter-spacing="1" fill="{INK}">{esc(name).upper()}</text>')

    # many ways in: the places people hear of us, all running into one line
    fi = sh["in"]
    tx = cx(idx[fi["to"]])
    sx0 = LM + 30
    n = len(fi["ways"])
    for k, way in enumerate(fi["ways"]):
        y = LINE_Y + (k - (n - 1) / 2) * 36
        back.append(f'<line x1="{sx0}" y1="{y}" x2="{sx0 + 60}" y2="{y}" stroke="{INK}" stroke-width="1.5"/>'
                    + bend(sx0 + 60, y, tx - 4, LINE_Y, 1.5))
        front.append(small(sx0, y - 7, way, "start"))

    # the Cycle: problem proposals open, Vote 1 closes them into pods
    pr = sh["problem"]
    px1, px2 = at(pr["from"]), at(pr["to"])
    back.append(lens(px1, px2, LINE_Y, pr["h"]))
    for k, line in enumerate(pr["label"]):
        front.append(small((px1 + px2) / 2, LINE_Y - 40 + k * 18, line))
    # each pod runs its own paradox, frame and project proposals
    pd = sh["pods"]
    npods, gap, br = pd["n"], pd["gap"], pd["branch"]
    ys = [LINE_Y + (k - (npods - 1) / 2) * gap for k in range(npods)]
    for y in ys:
        if y != LINE_Y:
            back.append(bend(px2, LINE_Y, px2 + br, y))
    sx = px2 + br
    back.append(f'<line x1="{px2}" y1="{LINE_Y}" x2="{sx}" y2="{LINE_Y}" stroke="{INK}" stroke-width="2.5"/>')
    for st in pd["stages"]:
        ex = at(st["to"]) if isinstance(st["to"], list) else px2 + st["to"]
        for y in ys:
            back.append(lens(sx, ex, y, pd["h"]))
        front.append(small((sx + ex) / 2, ys[0] + 5, st["label"]))
        if st.get("close"):
            front.append(f'<line x1="{ex}" y1="{LINE_Y - 108}" x2="{ex}" y2="{LINE_Y + 100}" stroke="{INK}" '
                         f'stroke-width="1.5" stroke-dasharray="3 5"/>' + small(ex, LINE_Y - 116, st["close"], weight=700, caps=True))
        sx = ex
    # Vote 2: each pod splits into projects, which build and meet at the showcase
    pj = sh["projects"]
    xs = at(pj["to"])
    for y, k in zip(ys, pj["counts"]):
        pys = [y + (j - (k - 1) / 2) * pj["gap"] for j in range(k)]
        for py in pys:
            back.append(bend(sx, y, sx + br, py, 1.5) if py != y else
                        f'<line x1="{sx}" y1="{y}" x2="{sx + br}" y2="{y}" stroke="{INK}" stroke-width="1.5"/>')
            back.append(lens(sx + br, xs - br, py, 6))
            back.append(bend(xs - br, py, xs, LINE_Y, 1.5))
    front.append(small((sx + xs) / 2, ys[0] - 34, pj["label"]))

    # many ways out: from after, the work fans into wherever people take it
    fo = sh["out"]
    ox = cx(idx[fo["from"]]) + 24
    m = fo["n"]
    for k in range(m):
        y = LINE_Y + (k - (m - 1) / 2) * 34
        back.append(bend(ox, LINE_Y, ox + 150, y, 1.5) + f'<line x1="{ox + 150}" y1="{y}" x2="{W - LM - 14}" y2="{y}" '
                    f'stroke="{INK}" stroke-width="1.5"/><path d="M{W - LM - 14},{y - 5} L{W - LM},{y} L{W - LM - 14},{y + 5} Z" fill="{INK}"/>')
    front.append(small(ox + 160, LINE_Y - (m - 1) / 2 * 34 - 14, fo["label"], "start", italic=True))

    # the journey line: one person's path, straight through the middle of it all
    lines = []
    for i in range(len(cols) - 1):
        planned = cols[i].get("planned") or cols[i + 1].get("planned")
        dash = ' stroke-dasharray="20 12"' if planned else ""
        lines.append(f'<line x1="{cx(i)}" y1="{LINE_Y}" x2="{cx(i + 1)}" y2="{LINE_Y}" stroke="{BLUE}" stroke-width="10"{dash}/>')

    # arcs above: skips and returns
    for ar in d["arcs"]:
        i, j = idx[ar["from"]], idx[ar["to"]]
        top = 290 + ar["lane"] * 46
        sxa = cx(i) + (34 if j > i else -34)
        exa = cx(j) + ar.get("dx", -40 if j > i else 150)
        land = LINE_Y - (110 if ar.get("onto") == "top" else 40)
        r, dx = 20, (1 if exa > sxa else -1)
        path = (f'M{sxa},{LINE_Y - 22} V{top + r} Q{sxa},{top} {sxa + dx * r},{top} H{exa - dx * r} '
                f'Q{exa},{top} {exa},{top + r} V{land}')
        front.append(f'<path d="{path}" fill="none" stroke="{BLUE}" stroke-width="5"/>'
                     f'<path d="M{exa - 11},{land - 4} L{exa},{land + 16} L{exa + 11},{land - 4} Z" fill="{BLUE}"/>')
        lx = (sxa + exa) / 2
        tw = len(ar["label"]) * FS * 0.55 + 20
        front.append(f'<rect x="{lx - tw / 2}" y="{top - 15}" width="{tw}" height="30" fill="{PAPER}"/>'
                     f'<text x="{lx}" y="{top + 5.5}" text-anchor="middle" font-size="{FS}" font-weight="600" fill="{INK}">{esc(ar["label"])}</text>')

    # leaks between two steps; inside the Cycle they drop from the bottom of the shape
    for s, e, label in d["leaks"]:
        mx = x0(idx[e]) - GAP / 2
        y0 = LINE_Y + (102 if cols[idx[e]].get("cycle") or cols[idx[s]].get("cycle") else 8)
        front.append(f'<line x1="{mx}" y1="{y0}" x2="{mx}" y2="{RING_Y - 22}" stroke="{RED}" stroke-width="7" '
                     f'stroke-dasharray="2 12" stroke-linecap="round"/>'
                     f'<circle cx="{mx}" cy="{RING_Y}" r="13" fill="{PAPER}" stroke="{RED}" stroke-width="6"/>'
                     f'<text x="{mx + 24}" y="{RING_Y + 5.5}" font-size="{FS}" font-weight="600" fill="{INK}">{esc(label)}</text>')

    # stations, step numbers and titles
    for i, c in enumerate(cols):
        x = cx(i)
        if c.get("planned"):
            front.append(f'<circle cx="{x}" cy="{LINE_Y}" r="18" fill="{PAPER}" stroke="{BLUE}" stroke-width="6" stroke-dasharray="8 6"/>')
        else:
            front.append(f'<circle cx="{x}" cy="{LINE_Y}" r="18" fill="{PAPER}" stroke="{INK}" stroke-width="6"/>')
        tag = f'{i + 1:02d}' + (f'  {c["sub"]}' if c.get("sub") else "") + ("  planned" if c.get("planned") else "")
        front.append(small(x0(i), STEP_Y, tag, "start", 700, caps=True))
        for k, line in enumerate(wrap(c["title"], 19)):
            front.append(f'<text x="{x0(i)}" y="{TITLE_Y + k * 27}" font-size="{TFS}" font-weight="700" fill="{INK}">{esc(line)}</text>')
    front.append(small(LM, STEP_Y, "Step", "start", 700, caps=True))

    # lanes
    for key, name, y in LANES:
        front.append(f'<line x1="{LM}" y1="{y - 34}" x2="{W - LM}" y2="{y - 34}" stroke="{INK}" stroke-width="1" stroke-opacity=".35"/>'
                     + small(LM, y, name, "start", 700, caps=True))
    for i, c in enumerate(cols):
        x = x0(i)
        for key, name, y in LANES:
            yy = y
            if key == "told":
                for v, q in c.get("told", []):
                    ql = wrap(f"“{q}”", int(cw[i] / 9.6))
                    front.append(f'<rect x="{x}" y="{yy - 15}" width="20" height="20" fill="{INK if v == "A" else PAPER}" stroke="{INK}" stroke-width="2"/>'
                                 f'<text x="{x + 10}" y="{yy}" text-anchor="middle" font-size="12" font-weight="700" fill="{PAPER if v == "A" else INK}">{v}</text>')
                    for k, line in enumerate(ql):
                        front.append(f'<text x="{x + 30}" y="{yy + k * LH}" font-size="{FS}" fill="{INK}">{esc(line)}</text>')
                    yy += LH * len(ql) + 18
                if c.get("gap") or not c.get("told"):
                    front.append(f'<text x="{x}" y="{yy}" font-size="{FS}" font-style="italic" fill="{INK}">'
                                 f'{esc(c.get("gap", "Nothing Heard Yet"))}</text>')
                continue
            for para in c.get(key, []):
                for line in wrap(para, int(cw[i] / 8.8)):
                    front.append(f'<text x="{x}" y="{yy}" font-size="{FS}" fill="{INK}">{esc(line)}</text>')
                    yy += LH
            if key == "do" and c.get("plan"):
                yy += 6
                for line in wrap("Planned: " + c["plan"][0], int(cw[i] / 8.8)):
                    front.append(f'<text x="{x}" y="{yy}" font-size="{FS}" font-style="italic" fill="{INK}">{esc(line)}</text>')
                    yy += LH
    if sh.get("note"):
        front.append(small(a + 150, BOTTOM - 14, sh["note"], "start", italic=True))

    # heading and key
    head = (f'<text x="{LM}" y="92" font-size="43.987" font-weight="700" fill="{INK}">{esc(d["title"])}</text>'
            f'<text x="{LM}" y="140" font-size="19.244" fill="{INK}">{esc(d["subtitle"])}</text>')
    ky = H - 96
    key = [f'<text x="{LM}" y="{ky - 30}" font-size="15.118" font-weight="700" fill="{INK}">How to Read It</text>',
           f'<line x1="{LM}" y1="{ky}" x2="{LM + 90}" y2="{ky}" stroke="{BLUE}" stroke-width="10"/>'
           f'<text x="{LM + 106}" y="{ky + 5.5}" font-size="{FS}" fill="{INK}">Your Path</text>',
           f'<line x1="{LM + 270}" y1="{ky}" x2="{LM + 360}" y2="{ky}" stroke="{BLUE}" stroke-width="10" stroke-dasharray="20 12"/>'
           f'<text x="{LM + 376}" y="{ky + 5.5}" font-size="{FS}" fill="{INK}">Planned, Not Running Yet</text>',
           lens(LM + 640, LM + 730, ky, 18) +
           f'<text x="{LM + 746}" y="{ky + 5.5}" font-size="{FS}" fill="{INK}">Proposals Open, a Choice Narrows Them</text>',
           f'<line x1="{LM + 1110}" y1="{ky}" x2="{LM + 1200}" y2="{ky}" stroke="{INK}" stroke-width="1.5"/>'
           f'<text x="{LM + 1216}" y="{ky + 5.5}" font-size="{FS}" fill="{INK}">Other People’s Paths</text>',
           f'<line x1="{LM + 1440}" y1="{ky}" x2="{LM + 1530}" y2="{ky}" stroke="{RED}" stroke-width="7" stroke-dasharray="2 12" stroke-linecap="round"/>'
           f'<text x="{LM + 1546}" y="{ky + 5.5}" font-size="{FS}" fill="{INK}">Where People Leave</text>',
           f'<line x1="{LM + 1760}" y1="{ky}" x2="{LM + 1850}" y2="{ky}" stroke="{BLUE}" stroke-width="5"/>'
           f'<text x="{LM + 1866}" y="{ky + 5.5}" font-size="{FS}" fill="{INK}">Skipping Ahead or Coming Back</text>']
    vx = LM + 2160
    for v, name in d["voices"]:
        key.append(f'<rect x="{vx}" y="{ky - 12}" width="20" height="20" fill="{INK if v == "A" else PAPER}" stroke="{INK}" stroke-width="2"/>'
                   f'<text x="{vx + 10}" y="{ky + 3}" text-anchor="middle" font-size="12" font-weight="700" fill="{PAPER if v == "A" else INK}">{v}</text>'
                   f'<text x="{vx + 32}" y="{ky + 5.5}" font-size="{FS}" fill="{INK}">{esc(name)}</text>')
        vx += 320
    body = head + "".join(back) + "".join(lines) + "".join(front) + "".join(key)
    return (f'<svg class="jmap" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" role="img" '
            f'aria-label="{esc(d["title"])}" font-family="{FONT}"><rect width="{W}" height="{H}" fill="{PAPER}"/>{body}</svg>'), W, H
