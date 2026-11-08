"""The participant journey: left to right, one column per step.

Builds one SVG from content/journey/journey.json. A thick blue line runs through
every step; dashed where the step is planned. Red dotted lines leave the journey
between two steps and end in a ring, as on the region chart. Arcs above the line
are people skipping steps or coming back. Under each step, four lanes: what you
do, where, who is with you, and what people told us, quoted from the pod's
statements (content/map/statements.json). Add a column or a quote to the JSON
and rebuild.
"""
import json

INK, PAPER, BLUE, RED = "#0b3536", "#e5e7de", "#0098d8", "#f54123"
FONT = "Inter, system-ui, sans-serif"
LM, LABW, COLW, GAP = 56, 190, 274, 22
LINE_Y = 700
DIA_Y, DIA_H = 352, 66   # centre and half-height of the diverge/converge strip
LANES = [("do", "You", 900), ("where", "Where", 1080), ("with", "With you", 1200), ("told", "What People Told Us", 1330)]
FS, LH, TFS = 15.118, 21, 21.993
BOTTOM = 1630
W = LM + LABW + 10 * (COLW + GAP) - GAP + LM
H = 1840


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


def svg(d):
    cols = d["columns"]
    idx = {c["id"]: i for i, c in enumerate(cols)}
    x0 = lambda i: LM + LABW + i * (COLW + GAP)
    cx = lambda i: x0(i) + 18
    o = []
    # the Cycle, shaded
    cyc = [i for i, c in enumerate(cols) if c.get("cycle")]
    a, b = x0(cyc[0]) - GAP / 2, x0(cyc[-1]) + COLW + GAP / 2
    o.append(f'<rect x="{a}" y="{LINE_Y - 40}" width="{b - a}" height="{BOTTOM - LINE_Y + 40}" fill="{INK}" fill-opacity=".06"/>'
             f'<text x="{a + 14}" y="{BOTTOM - 18}" font-size="13.745" font-weight="700" letter-spacing="1" fill="{INK}">THE CYCLE</text>')
    # bands: Learn, Build, Share
    for name, s, e in d["bands"]:
        bx, ex = x0(idx[s]), x0(idx[e]) + COLW
        o.append(f'<rect x="{bx}" y="212" width="{ex - bx}" height="6" fill="{INK}"/>'
                 f'<text x="{bx}" y="200" font-size="15.118" font-weight="700" letter-spacing="1" fill="{INK}">{esc(name).upper()}</text>')
    # diverge and converge: where the group opens up and where it narrows
    sh = d.get("shape")
    if sh:
        at = lambda spec: cx(idx[spec[0]]) + spec[1]
        P, Hh, cy = 5, DIA_H, DIA_Y
        def lens(x1, x2, h1, h2, hm, dashed, fill):
            xm = (x1 + x2) / 2
            path = (f'M{x1},{cy - h1} Q{xm},{cy - hm * 2 + (h1 + h2) / 2} {x2},{cy - h2} '
                    f'L{x2},{cy + h2} Q{xm},{cy + hm * 2 - (h1 + h2) / 2} {x1},{cy + h1} Z')
            dash = ' stroke-dasharray="10 8"' if dashed else ""
            return (f'<path d="{path}" fill="{fill}" fill-opacity="{0 if dashed else .16}" stroke="{INK}" '
                    f'stroke-width="{2 if dashed else 3}"{dash}/>')
        o.append(f'<text x="{LM}" y="{cy + 5}" font-size="13.745" font-weight="700" letter-spacing="1" fill="{INK}">DIVERGE,</text>'
                 f'<text x="{LM}" y="{cy + 25}" font-size="13.745" font-weight="700" letter-spacing="1" fill="{INK}">CONVERGE</text>')
        # in: many ways narrowing to the Cycle; out: fanning wide again
        fi = sh["in"]
        o.append(lens(at(fi["from"]), at(fi["to"]), Hh * .9, P, Hh * .55, True, INK))
        o.append(f'<text x="{(at(fi["from"]) + at(fi["to"])) / 2}" y="{cy + 5}" text-anchor="middle" font-size="{FS}" '
                 f'font-style="italic" fill="{INK}">{esc(fi["label"])}</text>')
        fo = sh["out"]
        o.append(lens(at(fo["from"]), at(fo["to"]), P, Hh * .9, Hh * .55, True, INK))
        o.append(f'<text x="{(at(fo["from"]) + at(fo["to"])) / 2 + 20}" y="{cy + 5}" text-anchor="middle" font-size="{FS}" '
                 f'font-style="italic" fill="{INK}">{esc(fo["label"])}</text>')
        for dm in sh["diamonds"]:
            x1, x2 = at(dm["from"]), at(dm["to"])
            o.append(lens(x1, x2, P, P, Hh, False, BLUE))
            lines = dm["open"]
            for k, line in enumerate(lines):
                o.append(f'<text x="{(x1 + x2) / 2}" y="{cy + 5 + (k - (len(lines) - 1) / 2) * 19}" text-anchor="middle" '
                         f'font-size="13.745" fill="{INK}">{esc(line)}</text>')
            o.append(f'<line x1="{x2}" y1="{cy - Hh - 14}" x2="{x2}" y2="{cy + Hh + 14}" stroke="{INK}" stroke-width="2"/>'
                     f'<text x="{x2}" y="{cy - Hh - 24}" text-anchor="middle" font-size="13.745" font-weight="700" '
                     f'letter-spacing=".5" fill="{INK}">{esc(dm["close"]).upper()}</text>')
    # arcs above the line: skips and returns
    for k, ar in enumerate(d["arcs"]):
        i, j = idx[ar["from"]], idx[ar["to"]]
        top = LINE_Y - 230 + ar["lane"] * 46
        sx, ex = cx(i) + (34 if j > i else -34), cx(j) + (-40 if j > i else 150)
        r = 20
        dx = 1 if ex > sx else -1
        path = (f'M{sx},{LINE_Y - 22} V{top + r} Q{sx},{top} {sx + dx * r},{top} H{ex - dx * r} '
                f'Q{ex},{top} {ex},{top + r} V{LINE_Y - 40}')
        o.append(f'<path d="{path}" fill="none" stroke="{BLUE}" stroke-width="5"/>'
                 f'<path d="M{ex - 11},{LINE_Y - 44} L{ex},{LINE_Y - 24} L{ex + 11},{LINE_Y - 44} Z" fill="{BLUE}"/>')
        lx = (sx + ex) / 2
        tw = len(ar["label"]) * FS * 0.55 + 20
        o.append(f'<rect x="{lx - tw / 2}" y="{top - 15}" width="{tw}" height="30" fill="{PAPER}"/>'
                 f'<text x="{lx}" y="{top + 5.5}" text-anchor="middle" font-size="{FS}" font-weight="600" fill="{BLUE}">{esc(ar["label"])}</text>')
    # the journey line
    for i in range(len(cols) - 1):
        planned = cols[i].get("planned") or cols[i + 1].get("planned")
        dash = ' stroke-dasharray="20 12"' if planned else ""
        o.append(f'<line x1="{cx(i)}" y1="{LINE_Y}" x2="{cx(i + 1)}" y2="{LINE_Y}" stroke="{BLUE}" stroke-width="10"{dash}/>')
    # leaks between two steps
    for s, e, label in d["leaks"]:
        mx = x0(idx[e]) - GAP / 2
        o.append(f'<line x1="{mx}" y1="{LINE_Y + 8}" x2="{mx}" y2="{LINE_Y + 108}" stroke="{RED}" stroke-width="7" '
                 f'stroke-dasharray="2 12" stroke-linecap="round"/>'
                 f'<circle cx="{mx}" cy="{LINE_Y + 130}" r="13" fill="{PAPER}" stroke="{RED}" stroke-width="6"/>'
                 f'<text x="{mx + 24}" y="{LINE_Y + 135.5}" font-size="{FS}" font-weight="600" fill="{RED}">{esc(label)}</text>')
    # stations and titles
    for i, c in enumerate(cols):
        x = cx(i)
        if c.get("planned"):
            o.append(f'<circle cx="{x}" cy="{LINE_Y}" r="18" fill="{PAPER}" stroke="{BLUE}" stroke-width="6" stroke-dasharray="8 6"/>')
        else:
            o.append(f'<circle cx="{x}" cy="{LINE_Y}" r="18" fill="{PAPER}" stroke="{INK}" stroke-width="6"/>')
        o.append(f'<text x="{x0(i)}" y="{LINE_Y - 64}" font-size="13.745" font-weight="700" fill="{INK}" letter-spacing=".5">'
                 f'{i + 1:02d}{("  " + esc(c["sub"]).upper()) if c.get("sub") else ""}{"  PLANNED" if c.get("planned") else ""}</text>')
    # lane rules and lane names
    for key, name, y in LANES:
        o.append(f'<line x1="{LM}" y1="{y - 34}" x2="{W - LM}" y2="{y - 34}" stroke="{INK}" stroke-width="1" stroke-opacity=".35"/>'
                 f'<text x="{LM}" y="{y}" font-size="13.745" font-weight="700" letter-spacing="1" fill="{INK}">{esc(name).upper()}</text>')
    o.append(f'<text x="{LM}" y="{LINE_Y - 64}" font-size="13.745" font-weight="700" letter-spacing="1" fill="{INK}">STEP</text>')
    # cells
    for i, c in enumerate(cols):
        x = x0(i)
        ty = LINE_Y - 30 + 0
        # title sits under the step number, above the line? no: under the line, beside leaks
        tl = wrap(c["title"], 20)
        for k, line in enumerate(tl):
            o.append(f'<text x="{x}" y="{LINE_Y - 64 + 30 + k * 26}" font-size="{TFS}" font-weight="700" fill="{INK}">{esc(line)}</text>') if False else None
        for key, name, y in LANES:
            if key == "told":
                yy = y
                for v, q in c.get("told", []):
                    o.append(f'<rect x="{x}" y="{yy - 15}" width="20" height="20" fill="{INK if v == "A" else PAPER}" stroke="{INK}" stroke-width="2"/>'
                             f'<text x="{x + 10}" y="{yy}" text-anchor="middle" font-size="12" font-weight="700" fill="{PAPER if v == "A" else INK}">{v}</text>')
                    for k, line in enumerate(wrap(f"“{q}”", 28)):
                        o.append(f'<text x="{x + 30}" y="{yy + k * LH}" font-size="{FS}" fill="{INK}">{esc(line)}</text>')
                    yy += LH * len(wrap(f"“{q}”", 28)) + 18
                if c.get("gap") or not c.get("told"):
                    o.append(f'<text x="{x}" y="{yy}" font-size="{FS}" font-style="italic" fill="{INK}" fill-opacity=".7">'
                             f'{esc(c.get("gap", "Nothing heard yet"))}</text>')
                continue
            yy = y
            for para in c.get(key, []):
                for line in wrap(para, 31):
                    o.append(f'<text x="{x}" y="{yy}" font-size="{FS}" fill="{INK}">{esc(line)}</text>')
                    yy += LH
            if key == "do" and c.get("plan"):
                yy += 6
                for line in wrap("Planned: " + c["plan"][0], 31):
                    o.append(f'<text x="{x}" y="{yy}" font-size="{FS}" font-style="italic" fill="{INK}">{esc(line)}</text>')
                    yy += LH
    # titles under the line, left of the leak rings
    for i, c in enumerate(cols):
        for k, line in enumerate(wrap(c["title"], 19)):
            o.append(f'<text x="{x0(i)}" y="{LINE_Y + 60 + k * 27}" font-size="{TFS}" font-weight="700" fill="{INK}">{esc(line)}</text>')
    # heading and key
    head = (f'<text x="{LM}" y="92" font-size="43.987" font-weight="700" fill="{INK}">{esc(d["title"])}</text>'
            f'<text x="{LM}" y="140" font-size="19.244" fill="{INK}">{esc(d["subtitle"])}</text>')
    ky = H - 96
    key = [f'<text x="{LM}" y="{ky - 30}" font-size="15.118" font-weight="700" fill="{INK}">How to Read It</text>',
           f'<line x1="{LM}" y1="{ky}" x2="{LM + 90}" y2="{ky}" stroke="{BLUE}" stroke-width="10"/>'
           f'<text x="{LM + 106}" y="{ky + 5.5}" font-size="{FS}" fill="{INK}">The journey</text>',
           f'<line x1="{LM + 300}" y1="{ky}" x2="{LM + 390}" y2="{ky}" stroke="{BLUE}" stroke-width="10" stroke-dasharray="20 12"/>'
           f'<text x="{LM + 406}" y="{ky + 5.5}" font-size="{FS}" fill="{INK}">Planned, not running yet</text>',
           f'<line x1="{LM + 680}" y1="{ky}" x2="{LM + 770}" y2="{ky}" stroke="{RED}" stroke-width="7" stroke-dasharray="2 12" stroke-linecap="round"/>'
           f'<text x="{LM + 786}" y="{ky + 5.5}" font-size="{FS}" fill="{INK}">Where people leave</text>',
           f'<line x1="{LM + 1010}" y1="{ky}" x2="{LM + 1100}" y2="{ky}" stroke="{BLUE}" stroke-width="5"/>'
           f'<text x="{LM + 1116}" y="{ky + 5.5}" font-size="{FS}" fill="{INK}">Skipping ahead, or coming back</text>']
    key.append(f'<path d="M{LM + 1420},{ky} Q{LM + 1465},{ky - 30} {LM + 1510},{ky} Q{LM + 1465},{ky + 30} {LM + 1420},{ky} Z" '
               f'fill="{BLUE}" fill-opacity=".16" stroke="{INK}" stroke-width="3"/>'
               f'<text x="{LM + 1526}" y="{ky + 5.5}" font-size="{FS}" fill="{INK}">Opens up, then narrows to a choice</text>')
    vx = LM + 1880
    for v, name in d["voices"]:
        key.append(f'<rect x="{vx}" y="{ky - 12}" width="20" height="20" fill="{INK if v == "A" else PAPER}" stroke="{INK}" stroke-width="2"/>'
                   f'<text x="{vx + 10}" y="{ky + 3}" text-anchor="middle" font-size="12" font-weight="700" fill="{PAPER if v == "A" else INK}">{v}</text>'
                   f'<text x="{vx + 32}" y="{ky + 5.5}" font-size="{FS}" fill="{INK}">{esc(name)}</text>')
        vx += 320
    body = head + "".join(o) + "".join(key)
    return (f'<svg class="jmap" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" role="img" '
            f'aria-label="{esc(d["title"])}" font-family="{FONT}"><rect width="{W}" height="{H}" fill="{PAPER}"/>{body}</svg>'), W, H
