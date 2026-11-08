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
# Line colours, for maps only: they say which line is which, like the Metro. Never text, never red.
GREEN, VIOLET, SILVER = "#00a160", "#7b4fa0", "#9aa3a6"
FONT = "Inter, system-ui, sans-serif"
LM, LABW, COLW, GAP = 56, 190, 274, 22
LINE_Y = 580
STEP_Y = LINE_Y - 128          # step numbers
TITLE_Y = LINE_Y + 142         # step titles
RING_Y = LINE_Y + 214          # leak rings
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


def route(pts, r=14):
    """A polyline with rounded corners, for 45- and 90-degree Metro turns."""
    import math
    pts = [p for i, p in enumerate(pts) if i == 0 or p != pts[i - 1]]
    d = f"M{pts[0][0]:.1f},{pts[0][1]:.1f}"
    for i in range(1, len(pts) - 1):
        (ax, ay), (bx, by), (qx, qy) = pts[i - 1], pts[i], pts[i + 1]
        l1, l2 = math.hypot(bx - ax, by - ay), math.hypot(qx - bx, qy - by)
        if l1 == 0 or l2 == 0:
            continue
        rr = min(r, l1 / 2, l2 / 2)
        p1 = (bx - (bx - ax) / l1 * rr, by - (by - ay) / l1 * rr)
        p2 = (bx + (qx - bx) / l2 * rr, by + (qy - by) / l2 * rr)
        d += f" L{p1[0]:.1f},{p1[1]:.1f} Q{bx:.1f},{by:.1f} {p2[0]:.1f},{p2[1]:.1f}"
    d += f" L{pts[-1][0]:.1f},{pts[-1][1]:.1f}"
    return d


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

    # The journey line, drawn like the Metro. Where proposals are open, several lines
    # share one track as a bundle. At a vote, some lines end (a terminus bar) and the
    # chosen ones peel off at 45 degrees as pods, then projects. Every turn is 45 or 90
    # degrees with a rounded corner. How many lines there are is decided in the Cycle,
    # so the map draws a few and puts a vertical ellipsis where there may be more.
    lines = []
    LW = 8                      # line width inside the Cycle and on the branches
    def poly(pts, w=LW, dash="", col=BLUE):
        lines.append(f'<path d="{route(pts, 14)}" fill="none" stroke="{col}" stroke-width="{w}"{dash} '
                     f'stroke-linejoin="round"/>')
    def end(x, y, col=BLUE):    # terminus: this proposal stops at the vote
        lines.append(f'<line x1="{x}" y1="{y - 11}" x2="{x}" y2="{y + 11}" stroke="{col}" stroke-width="{LW}"/>')
    def dots(x, y):
        lines.append("".join(f'<circle cx="{x}" cy="{y + k * 12}" r="3.5" fill="{INK}"/>' for k in (-1, 0, 1)))
    def label(x, y, text):
        front.append(small(x, y + 5, text, weight=600))
    def chose(x, text):
        front.append(f'<line x1="{x}" y1="{LINE_Y - 110}" x2="{x}" y2="{LINE_Y + 110}" stroke="{INK}" '
                     f'stroke-width="1.5" stroke-dasharray="3 5"/>' + small(x, LINE_Y - 116, text, weight=700, caps=True))
    caps = []                   # interchanges: a pill across every line it serves

    # trunk between steps, outside the Cycle
    cyc_ids = [i for i, c in enumerate(cols) if c.get("cycle")]
    for i in range(len(cols) - 1):
        if i in cyc_ids and i + 1 in cyc_ids:
            continue
        planned = cols[i].get("planned") or cols[i + 1].get("planned")
        poly([(cx(i), LINE_Y), (cx(i + 1), LINE_Y)], 10, ' stroke-dasharray="20 12"' if planned else "")

    Y = LINE_Y
    # many ways in: separate lines that join the trunk at the first step
    fi = sh["in"]
    tx = cx(idx[fi["to"]])
    n = len(fi["ways"])
    sx0 = LM + 30
    for k, way in enumerate(fi["ways"]):
        o = (k - (n - 1) / 2) * 30
        poly([(sx0, Y + o), (tx - 20 - abs(o), Y + o), (tx - 20, Y), (tx, Y)])
        front.append(small(sx0, Y + o - 10, way, "start"))

    J, P, T, S = cx(idx["join"]), cx(idx["pod"]), cx(idx["team"]), cx(idx["show"])
    pr, pd, pj = sh["problem"], sh["pods"], sh["projects"]
    G = pd["gap"]                                  # distance between pods
    pods = [Y - G, Y, Y + G]                       # one above yours, yours, one below (and maybe more)
    # problem proposals share one track from the moment you join
    B = [-18, -6, 6, 18]
    fate = {-18: Y - G, -6: Y, 6: None, 18: Y + G}  # Vote 1: three go on as pods, one ends
    hue = {-18: GREEN, -6: BLUE, 6: SILVER, 18: VIOLET}
    podhue = {Y - G: GREEN, Y: BLUE, Y + G: VIOLET}
    for o in B:
        pts = [(J, Y), (J + 20, Y), (J + 20 + abs(o), Y + o), (P + 18, Y + o)]
        if fate[o] is None:
            poly(pts[:-1] + [(P - 30, Y + o)], col=hue[o])
            end(P - 30, Y + o, hue[o])
            continue
        dy = fate[o] - (Y + o)
        pts += [(P + 18 + abs(dy), fate[o]), (P + 18 + G + 10, fate[o])]
        poly(pts, col=hue[o])
    caps.append((P, Y - 18, Y + 18, True))
    label((J + P) / 2, Y - 44, pr["label"])
    front.append(small((J + P) / 2, Y + 50, pr["note"], italic=True))

    # inside each pod: proposals open into a bundle and merge back at a choice
    x = P + 18 + G + 10
    sp = 12
    for st in pd["stages"]:
        ex = at(st["to"]) if isinstance(st["to"], list) else P + st["to"]
        last = isinstance(st["to"], list)
        for c in pods:
            for o in (-sp, 0, sp):
                pts = [(x, c), (x + 14, c), (x + 14 + abs(o), c + o)]
                if not last:
                    pts += [(ex - 14 - abs(o), c + o), (ex - 14, c), (ex + 1, c)]
                    poly(pts, col=podhue[c])
                elif o == 0:
                    poly(pts + [(ex - 30, c)], col=podhue[c])   # Vote 2: the middle proposal ends here
                    end(ex - 30, c, podhue[c])
                else:
                    poly(pts + [(ex + 30, c + o)], col=podhue[c])
            if last:
                caps.append((ex, c - sp, c + sp, c == Y))
        label((x + ex) / 2, Y - G / 2, st["label"])
        if st.get("close"):
            chose(ex, st["close"])
        x = ex
    # projects build side by side, then all meet at the showcase
    projs = [(c + o, podhue[c]) for c in pods for o in (-sp, sp)]
    m = len(projs)
    for q, col in sorted(projs, key=lambda t: t[1] == BLUE):
        dy = abs(Y - q)
        poly([(x + 30, q), (S - 24 - dy, q), (S - 24, Y), (S, Y)], col=col)
    label((x + S - 60) / 2, Y - G / 2, pj["label"])
    # the dots: there may be more pods, and more projects in each, than drawn
    for dx_ in (P + 18 + G + 60, (P + 250 + P + 460) / 2, (x + S - 90) / 2):
        dots(dx_, Y + G / 2)
    dots((x + S - 90) / 2 + 60, Y)
    poly([(S, Y), (cx(idx["after"]), Y)], 10)

    # many ways out: the line splits into wherever people take it
    fo = sh["out"]
    ox = cx(idx[fo["from"]])
    mo = fo["n"]
    for k in range(mo):
        o = (k - (mo - 1) / 2) * 30
        poly([(ox, Y), (ox + 40, Y), (ox + 40 + abs(o), Y + o), (W - LM - 18, Y + o)])
        lines.append(f'<path d="M{W - LM - 20},{Y + o - 10} L{W - LM},{Y + o} L{W - LM - 20},{Y + o + 10} Z" fill="{BLUE}"/>')
    front.append(small(ox + 90, Y - (mo - 1) / 2 * 30 - 16, fo["label"], "start", 600))

    # arcs above: skips and returns
    for ar in d["arcs"]:
        i, j = idx[ar["from"]], idx[ar["to"]]
        top = 290 + ar["lane"] * 46
        sxa = cx(i) + (34 if j > i else -34)
        exa = cx(j) + ar.get("dx", -40 if j > i else 150)
        land = LINE_Y - (150 if ar.get("onto") == "top" else 40)
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
        y0 = LINE_Y + (120 if cols[idx[e]].get("cycle") or cols[idx[s]].get("cycle") else 8)
        front.append(f'<line x1="{mx}" y1="{y0}" x2="{mx}" y2="{RING_Y - 22}" stroke="{RED}" stroke-width="7" '
                     f'stroke-dasharray="2 12" stroke-linecap="round"/>'
                     f'<circle cx="{mx}" cy="{RING_Y}" r="13" fill="{PAPER}" stroke="{RED}" stroke-width="6"/>'
                     f'<text x="{mx + 24}" y="{RING_Y + 5.5}" font-size="{FS}" font-weight="600" fill="{INK}">{esc(label)}</text>')

    # stations, step numbers and titles
    for px_, t, bm, _ in caps:
        front.append(f'<rect x="{px_ - 16}" y="{t - 16}" width="32" height="{bm - t + 32}" rx="16" fill="{PAPER}" '
                     f'stroke="{INK}" stroke-width="5"/>')
    capx = {round(c[0]) for c in caps}
    for i, c in enumerate(cols):
        x = cx(i)
        if round(x) in capx:
            pass
        elif c.get("planned"):
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
           f'<text x="{LM + 106}" y="{ky + 5.5}" font-size="{FS}" fill="{INK}">The Journey</text>',
           f'<line x1="{LM}" y1="{ky + 44}" x2="{LM + 26}" y2="{ky + 44}" stroke="{GREEN}" stroke-width="8"/>'
           f'<line x1="{LM + 32}" y1="{ky + 44}" x2="{LM + 58}" y2="{ky + 44}" stroke="{BLUE}" stroke-width="8"/>'
           f'<line x1="{LM + 64}" y1="{ky + 44}" x2="{LM + 90}" y2="{ky + 44}" stroke="{VIOLET}" stroke-width="8"/>'
           f'<text x="{LM + 106}" y="{ky + 49.5}" font-size="{FS}" fill="{INK}">Each Pod Has Its Own Line; Blue Is Yours</text>'
           f'<line x1="{LM + 500}" y1="{ky + 44}" x2="{LM + 590}" y2="{ky + 44}" stroke="{SILVER}" stroke-width="8"/>'
           f'<text x="{LM + 606}" y="{ky + 49.5}" font-size="{FS}" fill="{INK}">A Proposal Not Chosen</text>',
           f'<line x1="{LM + 270}" y1="{ky}" x2="{LM + 360}" y2="{ky}" stroke="{BLUE}" stroke-width="10" stroke-dasharray="20 12"/>'
           f'<text x="{LM + 376}" y="{ky + 5.5}" font-size="{FS}" fill="{INK}">Planned, Not Running Yet</text>',
           f'<path d="M{LM + 640},{ky - 10} H{LM + 730} M{LM + 640},{ky + 2} H{LM + 700}" stroke="{BLUE}" stroke-width="8"/>'
           f'<line x1="{LM + 700}" y1="{ky - 9}" x2="{LM + 700}" y2="{ky + 13}" stroke="{BLUE}" stroke-width="8"/>'
           f'<text x="{LM + 746}" y="{ky + 5.5}" font-size="{FS}" fill="{INK}">Proposals Share a Track; Some End at a Vote</text>',
           ''.join(f'<circle cx="{LM + 1120}" cy="{ky + k * 12}" r="3.5" fill="{INK}"/>' for k in (-1, 0, 1)) +
           f'<text x="{LM + 1140}" y="{ky + 5.5}" font-size="{FS}" fill="{INK}">There May Be More, or Fewer</text>',
           f'<rect x="{LM + 1386}" y="{ky - 24}" width="28" height="48" rx="14" fill="{PAPER}" stroke="{INK}" stroke-width="5"/>'
           f'<text x="{LM + 1428}" y="{ky + 5.5}" font-size="{FS}" fill="{INK}">A Vote</text>',
           f'<line x1="{LM + 1560}" y1="{ky}" x2="{LM + 1650}" y2="{ky}" stroke="{RED}" stroke-width="7" stroke-dasharray="2 12" stroke-linecap="round"/>'
           f'<text x="{LM + 1666}" y="{ky + 5.5}" font-size="{FS}" fill="{INK}">Where People Leave</text>',
           f'<line x1="{LM + 1870}" y1="{ky}" x2="{LM + 1960}" y2="{ky}" stroke="{BLUE}" stroke-width="5"/>'
           f'<text x="{LM + 1976}" y="{ky + 5.5}" font-size="{FS}" fill="{INK}">Skipping Ahead or Coming Back</text>']
    vx = LM + 2290
    for v, name in d["voices"]:
        key.append(f'<rect x="{vx}" y="{ky - 12}" width="20" height="20" fill="{INK if v == "A" else PAPER}" stroke="{INK}" stroke-width="2"/>'
                   f'<text x="{vx + 10}" y="{ky + 3}" text-anchor="middle" font-size="12" font-weight="700" fill="{PAPER if v == "A" else INK}">{v}</text>'
                   f'<text x="{vx + 32}" y="{ky + 5.5}" font-size="{FS}" fill="{INK}">{esc(name)}</text>')
        vx += 320
    body = head + "".join(back) + "".join(lines) + "".join(front) + "".join(key)
    return (f'<svg class="jmap" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" role="img" '
            f'aria-label="{esc(d["title"])}" font-family="{FONT}"><rect width="{W}" height="{H}" fill="{PAPER}"/>{body}</svg>'), W, H
