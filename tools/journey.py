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
# Line colours, for maps only: they say which line is which, like the Metro's Green, Yellow and
# Silver lines. Never text, never red. All from the Swiss Style Color Picker: green and yellow from
# scheme 11 (its red, yellow, green, blue is the Metro's own set), silver from scheme 3. Checked by
# colour science (research/journey-map-colour.md, tools/colourcheck.py): every pair of lines stays
# at least 19 CAM02-UCS units apart under protanopia, deuteranopia and tritanopia.
GREEN, YELLOW, SILVER = "#007500", "#e6c700", "#a5a6a9"   # pod A, pod C, a proposal not chosen
# Each pod is a colour family. Its paradoxes branch in shades of it: one keeps the pod's colour,
# the other takes a darker or lighter shade, again from the Swiss palette (light green scheme 8,
# navy scheme 10, ochre scheme 7). Frames and projects keep their paradox's shade, so a project
# can be traced back to the paradox it came from. Order on the map puts light beside dark, so
# lines that run side by side stay at least 15 CAM02-UCS apart for every kind of colour vision.
GREEN_LT, NAVY, OCHRE = "#3dbd5d", "#08327d", "#c7943e"
CASE = 0     # no casing: like the Metro, lines are flat colour (research/journey-map-colour.md)
FONT = "Inter, system-ui, sans-serif"
LM, LABW, COLW, GAP = 56, 190, 274, 22
LINE_Y = 650
STEP_Y = LINE_Y - 198          # step numbers
TITLE_Y = LINE_Y + 216         # step titles
RING_Y = LINE_Y + 288          # leak rings
LANES = [("do", "You", 994), ("where", "Where", 1174), ("with", "With you", 1294), ("told", "What People Told Us", 1424)]
FS, LH, TFS, SFS = 15.118, 21, 21.993, 13.745
BOTTOM = 1724
H = 1934


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
    back.append(f'<rect x="{a}" y="{LINE_Y - 220}" width="{b - a}" height="{BOTTOM - LINE_Y + 220}" rx="4" fill="none" '
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
    lines, casings = [], []     # casings are drawn first, under every line, so they only show at outer edges
    LW = 8                      # line width inside the Cycle and on the branches
    def poly(pts, w=LW, dash="", col=BLUE):
        d_ = route(pts, 14)
        casings.append(f'<path d="{d_}" fill="none" stroke="{INK}" stroke-width="{w + 2 * CASE}"{dash} stroke-linejoin="round"/>')
        lines.append(f'<path d="{d_}" fill="none" stroke="{col}" stroke-width="{w}"{dash} '
                     f'stroke-linejoin="round"/>')
    def end(x, y, col=BLUE):    # terminus: this proposal stops at the vote
        casings.append(f'<rect x="{x - LW / 2 - CASE}" y="{y - 11 - CASE}" width="{LW + 2 * CASE}" height="{22 + 2 * CASE}" fill="{INK}"/>')
        lines.append(f'<line x1="{x}" y1="{y - 11}" x2="{x}" y2="{y + 11}" stroke="{col}" stroke-width="{LW}"/>')
    def dots(x, y):
        lines.append("".join(f'<circle cx="{x}" cy="{y + k * 12}" r="3.5" fill="{INK}"/>' for k in (-1, 0, 1)))
    def label(x, y, text):
        front.append(small(x, y + 5, text, weight=600))
    def chose(x, text):
        front.append(f'<line x1="{x}" y1="{LINE_Y - 180}" x2="{x}" y2="{LINE_Y + 180}" stroke="{INK}" '
                     f'stroke-width="1.5" stroke-dasharray="3 5"/>' + small(x, LINE_Y - 186, text, weight=700, caps=True))
    caps = []                   # interchanges: a pill across every line it serves

    # trunk between steps, outside the Cycle
    cyc_ids = [i for i, c in enumerate(cols) if c.get("cycle")]
    loop_exit = {i: x0(i) + cw[i] - 40 for i, c in enumerate(cols) if c.get("loop")}
    for i in range(len(cols) - 1):
        if i in cyc_ids and i + 1 in cyc_ids:
            continue
        planned = cols[i].get("planned") or cols[i + 1].get("planned")
        poly([(loop_exit.get(i, cx(i)), LINE_Y), (cx(i + 1), LINE_Y)], 10, ' stroke-dasharray="20 12"' if planned else "")

    # Before the Cycle there is no set order: sessions are a loop you can join anywhere and
    # go round as often as you like. Its stations run Learn, Build, Share, the upskiller's own
    # spiral, so the order is a suggestion you can see, not a rule. Under it, a planned record
    # stamps each session, so the path makes sense looking back.
    for i, c in enumerate(cols):
        lp = c.get("loop")
        if not lp:
            continue
        lx1, lx2 = cx(i), loop_exit[i]
        top, bot, r = LINE_Y - lp["h"], LINE_Y + lp["h"], lp["h"]
        lines.append(f'<path d="M{lx1},{LINE_Y} V{top + r} Q{lx1},{top} {lx1 + r},{top} H{lx2 - r} Q{lx2},{top} {lx2},{top + r} '
                     f'V{bot - r} Q{lx2},{bot} {lx2 - r},{bot} H{lx1 + r} Q{lx1},{bot} {lx1},{bot - r} Z" fill="none" '
                     f'stroke="{BLUE}" stroke-width="10"/>')
        casings.append(lines[-1].replace(f'stroke="{BLUE}" stroke-width="10"', f'stroke="{INK}" stroke-width="{10 + 2 * CASE}"'))
        # the way round: arrowheads on the loop, clockwise
        for ax, ay, dx_ in ((lx1 + (lx2 - lx1) * .5, top, 1), (lx1 + (lx2 - lx1) * .5, bot, -1)):
            lines.append(f'<path d="M{ax - 9 * dx_},{ay - 9} L{ax + 7 * dx_},{ay} L{ax - 9 * dx_},{ay + 9} Z" fill="{PAPER}"/>')
        n = len(lp["stations"])
        for k, st in enumerate(lp["stations"]):
            sx_, sy = st["at"]
            px_, py = lx1 + (lx2 - lx1) * sx_, (top if sy == "top" else bot)
            front.append(f'<circle cx="{px_}" cy="{py}" r="12" fill="{PAPER}" stroke="{INK}" stroke-width="5"/>')
            if sy == "top":     # above the line, outside the loop
                front.append(small(px_, py - 22, st["name"], weight=700) + small(px_, py - 39, st["kind"], caps=True))
            else:               # above the line, inside the loop
                front.append(small(px_, py - 22, st["name"], weight=700) + small(px_, py - 39, st["kind"], caps=True))
        front.append(small((lx1 + lx2) / 2, LINE_Y - 14, lp["inside"][0], italic=True)
                     + small((lx1 + lx2) / 2, LINE_Y + 3, lp["inside"][1], italic=True))
        # your record, planned: a stamp for every session
        ry, rx1 = TITLE_Y + 40, lx1 + 300
        lines.append(f'<line x1="{rx1}" y1="{ry}" x2="{lx2}" y2="{ry}" stroke="{INK}" stroke-width="3" stroke-dasharray="10 8"/>')
        for k in range(6):
            sxk = rx1 + 20 + k * (lx2 - rx1 - 40) / 5
            front.append(f'<rect x="{sxk - 7}" y="{ry - 7}" width="14" height="14" rx="2" fill="{PAPER}" stroke="{INK}" stroke-width="2.5"/>')
        front.append(small(lx2, ry + 28, lp["record"], "end", 700))

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
    hue = {-18: GREEN, -6: BLUE, 6: SILVER, 18: YELLOW}
    podhue = {Y - G: GREEN, Y: BLUE, Y + G: YELLOW}
    for o in B:
        pts = [(J, Y), (J + 20, Y), (J + 20 + abs(o), Y + o), (P + 18, Y + o)]
        if fate[o] is None:
            poly(pts[:-1] + [(P - 30, Y + o)], col=hue[o])
            end(P - 30, Y + o, hue[o])
            continue
        dy = fate[o] - (Y + o)
        pts += [(P + 18 + abs(dy), fate[o]), (P + 18 + G + 56, fate[o])]
        poly(pts, col=hue[o])
    caps.append((P, Y - 18, Y + 18, True))
    label((J + P) / 2, Y - 44, pr["label"])
    front.append(small((J + P) / 2, Y + 50, pr["note"], italic=True))

    # inside each pod: proposals open into a bundle and merge back at a choice
    x = P + 18 + G + 56
    # each pod is a named line: a disc with a letter, so lines read without colour (WMATA's service discs)
    for c, letter in zip(pods, pd["letters"]):
        dxc = P + 18 + G + 26
        front.append(f'<circle cx="{dxc}" cy="{c}" r="17" fill="{PAPER}" stroke="{podhue[c]}" stroke-width="6"/>'
                     f'<text x="{dxc}" y="{c + 5}" text-anchor="middle" font-size="{SFS}" font-weight="700" fill="{INK}">{letter}</text>')
    # Inside each pod the line opens and closes twice, then meets Vote 2. Paradox proposals
    # merge in sensemaking into a few paradoxes; under each paradox, frame proposals merge
    # into a few frames; at Vote 2 each frame is offered as a project, and the ones people
    # register for go on to build. Merging is drawn as Metro lines joining one track (no
    # terminus): nothing is cut, ideas combine. A vote is a terminus bar: a line ends there.
    # Counts are illustrative; the dots say there may be more or fewer.
    PARA = [(-36, -27), (-18, -27), (18, 27), (36, 27)]                # proposal -> paradox
    FRAME = {-27: [(-43, -35), (-27, -35), (-11, -19)],                # under each paradox:
             27: [(11, 19), (27, 35), (43, 35)]}                        # proposal -> frame
    ENDS = 19                                                          # the frame no one registered for
    def track(pts):
        out = []
        for pt in pts:
            if not out or pt != out[-1]:
                out.append(pt)
        return out
    e1, e2 = (P + st["to"] for st in pd["stages"][:2])
    T2 = at(pd["stages"][2]["to"])
    frames = sorted({g for fs in FRAME.values() for _, g in fs})
    shades = {Y - G: (GREEN, GREEN_LT), Y: (NAVY, BLUE), Y + G: (YELLOW, OCHRE)}   # upper, lower paradox
    def shade(c, off):
        return shades[c][0 if off < 0 else 1]
    for c, letter in sorted(zip(pods, pd["letters"]), key=lambda t: t[0] == Y):   # your pod drawn last
        for o, t in PARA:     # in hindsight, each proposal takes the shade of the paradox it merges into
            poly(track([(x + 14, c), (x + 14 + abs(o), c + o), (e1 - 14 - abs(o - t), c + o),
                        (e1 - 14, c + t), (e1 + 1, c + t)]), col=shade(c, t))
        poly([(x - 2, c), (x + 16, c)], col=podhue[c])                 # the pod's own colour up to the split
        for p_, fs in FRAME.items():
            for f, g in fs:
                poly(track([(e1, c + p_), (e1 + 34, c + p_), (e1 + 34 + abs(f - p_), c + f),
                            (e2 - 14 - abs(f - g), c + f), (e2 - 14, c + g), (e2 + 1, c + g)]), col=shade(c, p_))
            # each paradox is named, like a branch of a Paris RER line (C1, C2): letter and number, not just shade
            front.append(f'<circle cx="{e1 + 15}" cy="{c + p_}" r="13" fill="{PAPER}" stroke="{shade(c, p_)}" stroke-width="4"/>'
                         f'<text x="{e1 + 15}" y="{c + p_ + 4}" text-anchor="middle" font-size="11" font-weight="700" '
                         f'fill="{INK}">{letter}{1 if p_ < 0 else 2}</text>')
        for g in frames:
            if g == ENDS:
                poly([(e2, c + g), (T2 - 30, c + g)], col=shade(c, g))
                end(T2 - 30, c + g, shade(c, g))
            else:
                poly([(e2, c + g), (T2 + 30, c + g)], col=shade(c, g))
        caps.append((T2, c + frames[0], c + frames[-1], c == Y))
    for st, (sx_, ex_) in zip(pd["stages"], ((x, e1), (e1, e2), (e2, T2))):
        label((sx_ + ex_) / 2, Y - G / 2, st["label"])
        if st.get("close"):
            chose(ex_, st["close"])
    x = T2
    # projects build side by side, then all meet at the showcase
    projs = [(c + g, shade(c, g), c == Y) for c in pods for g in frames if g != ENDS]
    for q, col, _ in sorted(projs, key=lambda t: t[2]):
        dy = abs(Y - q)
        poly([(x + 30, q), (S - 24 - dy, q), (S - 24, Y), (S, Y)], col=col)
    label((x + S - 60) / 2, Y - G / 2, pj["label"])
    # the dots: there may be more pods, and more paradoxes, frames and projects, than drawn
    for dx_ in (P + 18 + G + 26, (x + e1) / 2 - 30, (e1 + e2) / 2, (e2 + T2) / 2, (x + S - 90) / 2):
        dots(dx_, Y + G / 2)
    poly([(S, Y), (cx(idx["after"]), Y)], 10)

    # many ways out: the line splits, and each way out is named for where it ends, like a Metro line
    fo = sh["out"]
    ox = cx(idx[fo["from"]])
    mo = fo["n"]
    for k in range(mo):
        o = (k - (mo - 1) / 2) * 36
        poly([(ox, Y), (ox + 40, Y), (ox + 40 + abs(o), Y + o), (W - LM - 18, Y + o)])
        lines.append(f'<path d="M{W - LM - 20},{Y + o - 10} L{W - LM},{Y + o} L{W - LM - 20},{Y + o + 10} Z" fill="{BLUE}"/>')
    for k, name in enumerate(fo.get("ends", [])):
        o = (k - (mo - 1) / 2) * 36
        front.append(small(W - LM - 26, Y + o - 9, name, "end", 600))
    front.append(small(ox + 40, Y - (mo - 1) / 2 * 36 - 34, fo["label"], "start", 700, caps=True))

    # arcs above: skips and returns
    for ar in d["arcs"]:
        i, j = idx[ar["from"]], idx[ar["to"]]
        top = 290 + ar["lane"] * 46
        sxa = cx(i) + (34 if j > i else -34)
        exa = cx(j) + ar.get("dx", -40 if j > i else 150)
        land = LINE_Y - (220 if ar.get("onto") == "top" else 40)
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
    for lk in d["leaks"]:
        if isinstance(lk, dict):        # from a point, e.g. the bottom of the session loop
            mx, y0, label = at(lk["at"]), LINE_Y + lk["dy"], lk["label"]
        else:
            s, e, label = lk
            mx = x0(idx[e]) - GAP / 2
            y0 = LINE_Y + (190 if cols[idx[e]].get("cycle") or cols[idx[s]].get("cycle") else 8)
        front.append(f'<line x1="{mx}" y1="{y0}" x2="{mx}" y2="{RING_Y - 22}" stroke="{RED}" stroke-width="7" '
                     f'stroke-dasharray="2 12" stroke-linecap="round"/>'
                     f'<circle cx="{mx}" cy="{RING_Y}" r="13" fill="{PAPER}" stroke="{RED}" stroke-width="6"/>'
                     f'<text x="{mx + 24}" y="{RING_Y + 5.5}" font-size="{FS}" font-weight="600" fill="{INK}">{esc(label)}</text>')

    # stations, step numbers and titles
    for px_, t, bm, _ in caps:
        front.append(f'<rect x="{px_ - 16}" y="{t - 16}" width="32" height="{bm - t + 32}" rx="16" fill="{PAPER}" '
                     f'stroke="{INK}" stroke-width="5"/>')
    capx = {round(c[0]) for c in caps}
    spans = {}
    for px_, t, bm, _ in caps:
        r = spans.setdefault(round(px_), [t, bm])
        r[0], r[1] = min(r[0], t), max(r[1], bm)
    for i, c in enumerate(cols):
        x = cx(i)
        if c.get("loop"):
            hh = c["loop"]["h"]
            ring = (f'<rect x="{x - 30}" y="{LINE_Y - hh - 30}" width="{loop_exit[i] - x + 60}" height="{2 * hh + 60}" '
                    f'rx="{hh + 30}" fill="none" stroke="{RED}" stroke-width="6"/>')
        elif round(x) in spans:
            t, bm = spans[round(x)]
            ring = (f'<rect x="{x - 26}" y="{t - 26}" width="52" height="{bm - t + 52}" rx="26" fill="none" '
                    f'stroke="{RED}" stroke-width="6"/>')
        else:
            ring = f'<circle cx="{x}" cy="{LINE_Y}" r="29" fill="none" stroke="{RED}" stroke-width="6"/>'
        front.append(f'<g class="yah yah-{i}" display="none">{ring}</g>')
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
    lm = d.get("landmarks", [])
    if lm:
        LY = LINE_Y - 242
        front.append(small(LM, LY, "Landmarks", "start", 700, caps=True))
        for l in lm:
            lx = at(l["at"])
            flag = (f'<path d="M{lx},{LY + 6} V{LY - 16} H{lx + 14} L{lx + 10},{LY - 11} L{lx + 14},{LY - 6} H{lx + 2}" '
                    f'fill="{INK}" stroke="{INK}" stroke-width="2" stroke-linejoin="round"/>')
            front.append(flag + small(lx + 20, LY, l["name"], "start", 700)
                         + (small(lx + 20, LY + 18, l["when"], "start", italic=True) if l.get("when") else ""))

    # lanes
    for key, name, y in LANES:
        front.append(f'<line x1="{LM}" y1="{y - 34}" x2="{W - LM}" y2="{y - 34}" stroke="{INK}" stroke-width="1" stroke-opacity=".35"/>'
                     + small(LM, y, name, "start", 700, caps=True))
    for i, c in enumerate(cols):
        x = x0(i)
        front.append(f'<g class="lt c{i}">')
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
        front.append('</g>')
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
           f'<line x1="{LM + 64}" y1="{ky + 44}" x2="{LM + 90}" y2="{ky + 44}" stroke="{YELLOW}" stroke-width="8"/>'
           f'<text x="{LM + 106}" y="{ky + 49.5}" font-size="{FS}" fill="{INK}">Each Pod Has Its Own Colour; Blue Is Yours</text>'
           f'<line x1="{LM + 500}" y1="{ky + 44}" x2="{LM + 590}" y2="{ky + 44}" stroke="{SILVER}" stroke-width="8"/>'
           f'<text x="{LM + 606}" y="{ky + 49.5}" font-size="{FS}" fill="{INK}">A Proposal Not Chosen</text>',
           f'<circle cx="{LM + 900}" cy="{ky + 44}" r="14" fill="{PAPER}" stroke="{GREEN}" stroke-width="5"/>'
           f'<text x="{LM + 900}" y="{ky + 49}" text-anchor="middle" font-size="{SFS}" font-weight="700" fill="{INK}">A</text>'
           f'<text x="{LM + 928}" y="{ky + 49.5}" font-size="{FS}" fill="{INK}">A Pod’s Line, by Letter as Well as Colour</text>'
           f'<text x="{LM + 1386}" y="{ky + 49.5}" font-size="{FS}" font-style="italic" fill="{INK}">Not to scale: steps are evenly spaced, not by time.</text>'
           f'<path d="M{LM + 1870},{ky + 32} H{LM + 1900} L{LM + 1912},{ky + 44} H{LM + 1960} M{LM + 1870},{ky + 56} H{LM + 1900} L{LM + 1912},{ky + 44}" '
           f'fill="none" stroke="{BLUE}" stroke-width="8" stroke-linejoin="round"/>'
           f'<text x="{LM + 1976}" y="{ky + 49.5}" font-size="{FS}" fill="{INK}">Lines Merge in Sensemaking: No Vote, Nothing Cut</text>'
           f'<path d="M{LM + 2440},{ky + 44} H{LM + 2462} L{LM + 2474},{ky + 32} H{LM + 2530}" fill="none" stroke="{GREEN}" stroke-width="8" stroke-linejoin="round"/>'
           f'<path d="M{LM + 2462},{ky + 44} L{LM + 2474},{ky + 56} H{LM + 2530}" fill="none" stroke="{GREEN_LT}" stroke-width="8" stroke-linejoin="round"/>'
           f'<text x="{LM + 2546}" y="{ky + 49.5}" font-size="{FS}" fill="{INK}">A Pod’s Paradoxes, A1 and A2, Branch in Shades of Its Colour; Projects Keep Their Shade</text>',
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
    body = head + "".join(back) + "".join(casings if CASE else []) + "".join(lines) + "".join(front) + "".join(key)
    return (f'<svg class="jmap" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" role="img" '
            f'aria-label="{esc(d["title"])}" font-family="{FONT}"><rect width="{W}" height="{H}" fill="{PAPER}"/>{body}</svg>'), W, H
