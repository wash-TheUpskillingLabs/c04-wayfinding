"""The region chart: a flow network in the sign system.

Boxes are the parts of the region; labelled arrows are what passes between them. Four kinds of
flow, each drawn its own way so one can be followed at a time:

  people           blue, heavy
  work and code    ink, heavy
  knowledge        ink, light
  money, support   blue, light
  leaks            red, ending in a stop (where people leave)

Dashed means planned: not running yet. Data lives in content/flow/flow.json.
"""
import json, math

INK, PAPER, BLUE, RED = "#0b3536", "#e5e7de", "#0098d8", "#f54123"
W, H = 2700, 1920
FONT = "Inter, system-ui, sans-serif"
TITLE_FS, BODY_FS, LABEL_FS = 21.993, 15.118, 15.118
PAD, TITLE_LH, BODY_LH = 22, 30, 22
STYLE = {
    "people":    (BLUE, 7),
    "work":      (INK, 7),
    "knowledge": (INK, 3),
    "support":   (BLUE, 3),
    "leak":      (RED, 7),
}
NAMES = [("people", "People"), ("work", "Work and code"), ("knowledge", "Knowledge"),
         ("support", "Money and support")]
PAR = 30  # gap between parallel arrows


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def load(path):
    with open(path) as f:
        return json.load(f)


def box(n):
    h = PAD * 2 + TITLE_LH + BODY_LH * len(n.get("body", [])) + (6 if n.get("body") else 0)
    return n["x"] - n["w"] / 2, n["y"] - h / 2, n["w"], h


def anchor(spec, boxes, end=False):
    """'node:side:offset' -> a point on that side of the box; [x, y] passes through."""
    if not isinstance(spec, str):
        return tuple(spec), None
    k, side, off = spec.split(":")
    x, y, w, h = boxes[k]
    off, g = float(off), (8 if end else 0)
    cx, cy = x + w / 2, y + h / 2
    return {"t": ((cx + off, y - g), (0, -1)), "b": ((cx + off, y + h + g), (0, 1)),
            "l": ((x - g, cy + off), (-1, 0)), "r": ((x + w + g, cy + off), (1, 0))}[side]


def route(pts, r=24):
    """A polyline with rounded corners."""
    d = f"M{pts[0][0]:.1f},{pts[0][1]:.1f}"
    for i in range(1, len(pts) - 1):
        (ax, ay), (bx, by), (cx, cy) = pts[i - 1], pts[i], pts[i + 1]
        l1, l2 = math.hypot(bx - ax, by - ay), math.hypot(cx - bx, cy - by)
        rr = min(r, l1 / 2, l2 / 2)
        p = (bx - (bx - ax) / l1 * rr, by - (by - ay) / l1 * rr)
        q = (bx + (cx - bx) / l2 * rr, by + (cy - by) / l2 * rr)
        d += f" L{p[0]:.1f},{p[1]:.1f} Q{bx:.1f},{by:.1f} {q[0]:.1f},{q[1]:.1f}"
    d += f" L{pts[-1][0]:.1f},{pts[-1][1]:.1f}"
    return d


def svg(data):
    nodes = {n["id"]: n for n in data["nodes"]}
    boxes = {k: box(n) for k, n in nodes.items()}
    outs = [tuple(o) for o in data.get("outs", [])]

    lines, labels, heads = [], [], []
    for f in data["flows"]:
        p0, _ = anchor(f["path"][0], boxes)
        mids = [tuple(p) for p in f["path"][1:-1]]
        pe, _ = anchor(f["path"][-1], boxes, end=True)
        pts = [p0] + mids + [pe]
        # straighten: a box-side anchor next to a via point shares its axis
        color, sw = STYLE[f["type"]]
        leak = f["type"] == "leak"
        if leak:  # stop short of the stop sign
            (ax, ay), (bx, by) = pts[-2], pts[-1]
            L = math.hypot(bx - ax, by - ay)
            pts[-1] = (bx - (bx - ax) / L * 26, by - (by - ay) / L * 26)
        dash = ' stroke-dasharray="18 12"' if f.get("planned") else ""
        if leak:
            dash = ' stroke-dasharray="2 12" stroke-linecap="round"'
        cls = f'fl f-{f["type"]}'
        tip = pts[-1]
        if not leak:  # pull the line back under the arrowhead
            (ax, ay), (bx, by) = pts[-2], pts[-1]
            L = math.hypot(bx - ax, by - ay)
            ux, uy = (bx - ax) / L, (by - ay) / L
            s = 12 + sw
            pts[-1] = (bx - ux * s, by - uy * s)
            p1 = (bx - ux * s * 1.5 - uy * s * 0.8, by - uy * s * 1.5 + ux * s * 0.8)
            p2 = (bx - ux * s * 1.5 + uy * s * 0.8, by - uy * s * 1.5 - ux * s * 0.8)
            heads.append(f'<path class="{cls}" d="M{p1[0]:.1f},{p1[1]:.1f} L{bx:.1f},{by:.1f} '
                         f'L{p2[0]:.1f},{p2[1]:.1f} Z" fill="{color}"/>')
        lines.append(f'<path class="{cls}" d="{route(pts)}" fill="none" stroke="{color}" stroke-width="{sw}"{dash}/>')
        # label: given, or the middle of the longest segment
        if "at" in f:
            lx, ly = f["at"]
        else:
            segs = list(zip(pts, pts[1:]))
            a, b = max(segs, key=lambda s: math.hypot(s[1][0] - s[0][0], s[1][1] - s[0][1]))
            lx, ly = (a[0] + b[0]) / 2, (a[1] + b[1]) / 2
        text = f["label"]
        tw = len(text) * LABEL_FS * 0.53 + 16
        anc = f.get("anchor", "middle")
        rx = {"middle": lx - tw / 2, "start": lx, "end": lx - tw}[anc]
        tx = {"middle": lx, "start": lx + 8, "end": lx - 8}[anc]
        lc = INK if f["type"] in ("work", "knowledge") else color
        weight = 600 if sw > 4 else 400
        labels.append(
            f'<g class="{cls}"><rect x="{rx:.1f}" y="{ly - 15:.1f}" width="{tw:.1f}" height="30" fill="{PAPER}"/>'
            f'<text x="{tx:.1f}" y="{ly + 5.5:.1f}" text-anchor="{anc}" font-size="{LABEL_FS}" '
            f'font-weight="{weight}" fill="{lc}">{esc(text)}</text></g>')

    stops = []
    for ox, oy in outs:
        stops.append(f'<g class="fl f-leak"><circle cx="{ox}" cy="{oy}" r="14" fill="{PAPER}" '
                     f'stroke="{RED}" stroke-width="6"/><text x="{ox}" y="{oy + 44}" text-anchor="middle" '
                     f'font-size="{LABEL_FS}" font-weight="600" fill="{INK}">Leaves</text></g>')

    blocks = []
    for k, n in nodes.items():
        x, y, w, h = boxes[k]
        kind = n.get("kind", "org")
        dash = ' stroke-dasharray="14 10"' if n.get("planned") else ""
        if kind == "org":
            fill, stroke, sw, tc = INK, INK, 3, PAPER
            if n.get("planned"):
                fill, tc = PAPER, INK
        elif kind == "people":
            fill, stroke, sw, tc = PAPER, BLUE, 6, INK
        else:
            fill, stroke, sw, tc = PAPER, INK, 3, INK
        out = [f'<rect x="{x:.1f}" y="{y:.1f}" width="{w}" height="{h:.1f}" fill="{fill}" stroke="{stroke}" '
               f'stroke-width="{sw}"{dash}/>']
        ty = y + PAD + 21
        out.append(f'<text x="{x + PAD:.1f}" y="{ty:.1f}" font-size="{TITLE_FS}" font-weight="700" fill="{tc}">'
                   f'{esc(n["title"])}</text>')
        ty += 8
        for line in n.get("body", []):
            ty += BODY_LH
            out.append(f'<text x="{x + PAD:.1f}" y="{ty:.1f}" font-size="{BODY_FS}" fill="{tc}">{esc(line)}</text>')
        if n.get("planned"):
            out.append(f'<text x="{x + w - PAD:.1f}" y="{y + h - PAD:.1f}" text-anchor="end" font-size="13.745" '
                       f'font-weight="600" fill="{tc}">Planned</text>')
        blocks.append(f'<g class="node">{"".join(out)}</g>')

    # the region and what it runs: one outline around all three
    c, r_, g = boxes["commons"], boxes["region"], boxes["gather"]
    top, mid = min(c[1], r_[1]) - 64, max(c[1] + c[3], r_[1] + r_[3]) + 20
    left, right, inner, bot = c[0] - 30, r_[0] + r_[2] + 30, max(c[0] + c[2], g[0] + g[2]) + 30, g[1] + g[3] + 30
    blocks.insert(0, f'<path d="M{left:.1f},{top:.1f} H{right:.1f} V{mid:.1f} H{inner:.1f} V{bot:.1f} H{left:.1f} Z" '
                     f'fill="none" stroke="{INK}" stroke-width="2"/><text x="{c[0] + c[2] / 2 + 96:.1f}" y="{top + 38:.1f}" '
                     f'font-size="15.118" font-weight="700" fill="{INK}">The region, and what it runs</text>')
    # national holds the regional association for now: one outline around both
    n_ = boxes["national"]
    otop, oleft, oright = n_[1] - 44, left - 26, right + 26
    blocks.insert(0, f'<path d="M{oleft:.1f},{otop:.1f} H{oright:.1f} V{mid + 14:.1f} H{inner + 14:.1f} V{bot + 14:.1f} '
                     f'H{oleft:.1f} Z" fill="none" stroke="{INK}" stroke-width="4"/><text x="{oleft + 16:.1f}" '
                     f'y="{otop + 30:.1f}" font-size="15.118" font-weight="700" fill="{INK}">The Upskilling Labs: '
                     f'national, and the region within it</text>')

    # heading and key
    head = [f'<text x="56" y="92" font-size="43.987" font-weight="700" fill="{INK}">{esc(data["title"])}</text>',
            f'<text x="56" y="140" font-size="19.244" fill="{INK}">{esc(data["subtitle"])}</text>']
    kx, ky = 56, H - 120
    key = [f'<text x="{kx}" y="{ky - 28}" font-size="15.118" font-weight="700" fill="{INK}">How to read it</text>']
    items = NAMES + [("leak", "Where people leave")]
    for i, (t, name) in enumerate(items):
        color, sw = STYLE[t]
        x = kx + i * 330
        dash = ' stroke-dasharray="2 12" stroke-linecap="round"' if t == "leak" else ""
        key.append(f'<line x1="{x}" y1="{ky}" x2="{x + 90}" y2="{ky}" stroke="{color}" stroke-width="{sw}"{dash}/>'
                   f'<text x="{x + 106}" y="{ky + 5.5}" font-size="15.118" fill="{INK}">{esc(name)}</text>')
    key.append(f'<line x1="{kx}" y1="{ky + 50}" x2="{kx + 90}" y2="{ky + 50}" stroke="{INK}" stroke-width="7" '
               f'stroke-dasharray="18 12"/><text x="{kx + 106}" y="{ky + 55.5}" font-size="15.118" fill="{INK}">'
               f'Dashed: planned, not running yet</text>')
    key.append(f'<rect x="{kx + 430}" y="{ky + 36}" width="40" height="28" fill="{INK}"/><text x="{kx + 486}" '
               f'y="{ky + 55.5}" font-size="15.118" fill="{INK}">Run by the region</text>')
    key.append(f'<rect x="{kx + 760}" y="{ky + 36}" width="40" height="28" fill="{PAPER}" stroke="{BLUE}" '
               f'stroke-width="6"/><text x="{kx + 816}" y="{ky + 55.5}" font-size="15.118" fill="{INK}">People</text>')
    key.append(f'<rect x="{kx + 990}" y="{ky + 36}" width="40" height="28" fill="{PAPER}" stroke="{INK}" '
               f'stroke-width="3"/><text x="{kx + 1046}" y="{ky + 55.5}" font-size="15.118" fill="{INK}">'
               f'Not run by the region</text>')

    body = "".join(head + blocks + lines + heads + stops + labels + key)
    out = (f'<svg class="fnet" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" role="img" '
           f'aria-label="{esc(data["title"])}" font-family="{FONT}"><rect width="{W}" height="{H}" fill="{PAPER}"/>'
           f'{body}</svg>')
    return out, W, H
