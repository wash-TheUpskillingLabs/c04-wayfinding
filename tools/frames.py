"""Frames built from the five needs, drawn on the same Metro lines (Dorst's step 6).

Every frame is an analogy, a place or system people already know. Each is a row, grouped by the candidate paradox it moves. The five needs from the themes map
run down the page in the same colours and order. A station marks a need the frame builds on; the two
needs a frame lets a person have at once are filled and joined, the way a Metro map joins the platforms of an
interchange. To the right: where the way of working is done well, and which side of the paradox
gives. Data: content/frames/frames.json, with the needs from content/themes/themes.json; reasoning
and sources in research/frames.md.
"""
import html
import themes as T

INK, PAPER, COLOURS, FONT = T.INK, T.PAPER, T.COLOURS, T.FONT
FS, TFS, HFS = T.FS, T.TFS, T.HFS
W = T.W
LM, NW, LS, RH, GH = 56, 340, 112, 52, 70
TOP = 300
LW = 8
X0 = LM + NW + 60                 # first need line
CD = X0 + 4 * LS + 84             # "Done well at" column
CG = CD + 500                     # "What gives" column
CHAR = FS * .52                   # rough width of one character of Inter at FS


def esc(s):
    return html.escape(s, quote=True)


def wrap(text, width):
    n = int(width / CHAR)
    lines, cur = [], ""
    for w_ in text.split():
        if cur and len(cur) + 1 + len(w_) > n:
            lines.append(cur); cur = w_
        else:
            cur = f"{cur} {w_}" if cur else w_
    return lines + [cur]


def counts(fd, td):
    """How many frames build on each need, and how many field players reach for it."""
    fr = {t["id"]: 0 for t in td["themes"]}
    for g in fd["groups"]:
        for f in g["frames"]:
            for k in f["t"]:
                fr[k] += 1
    field, _, nf, _ = T.counts(td)
    return fr, field, nf


def svg(fd, td):
    needs = td["themes"]
    xs = {th["id"]: X0 + i * LS for i, th in enumerate(needs)}
    nfr = sum(len(g["frames"]) for g in fd["groups"])
    fr, field, nf = counts(fd, td)
    body = sum(GH + RH * len(g["frames"]) for g in fd["groups"])
    bottom = TOP + body - 6
    ky = bottom + 96
    H = ky + 250
    n0 = len(fd["groups"][0]["frames"])
    w0 = ["no frames", "one that holds", "two that hold", "three that hold"][n0] if n0 < 4 else f"{n0} that hold"
    out = [f'<svg class="fmap" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" role="img" '
           f'aria-label="{nfr} frames drawn on the five need lines: {w0} all five needs, then {nfr - n0} grouped by the paradox each one moves. A station marks a need the frame builds on; joined stations are the needs it lets a person have at once. The table below lists every station." '
           f'font-family="{FONT}"><rect width="{W}" height="{H}" fill="{PAPER}"/>']
    t = out.append
    title = fd.get("title") or f'{["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve"][nfr] if nfr < 13 else nfr} Frames Built From Five Human Needs'
    t(f'<text x="{LM}" y="{LM + 26}" font-size="{TFS}" font-weight="700" fill="{INK}">{esc(title)}</text>')
    t(f'<text x="{LM}" y="{LM + 64}" font-size="{FS}" fill="{INK}">Each row is a frame, an analogy: a place people already know where they get these needs at once, without being paid to be there. '
      f'{["", "The first holds", "The first two hold", "The first three hold"][n0] if n0 < 4 else f"The first {n0} hold"} all five; the rest are grouped by the paradox each moves.</text>')
    t(f'<text x="{LM}" y="{LM + 90}" font-size="{FS}" fill="{INK}">Dorst’s step 6, Frames. Built {esc(fd["asof"])} from the five needs on the field themes map. '
      f'Hover a station for how the frame builds on that need; every station is in the table below.</text>')
    # need names over their lines, and the two text columns' heads
    for th in needs:
        t(f'<text x="{xs[th["id"]]}" y="{TOP - 62}" text-anchor="middle" font-size="{HFS}" font-weight="700" fill="{INK}">{esc(th["name"])}</text>')
    t(f'<text x="{CD}" y="{TOP - 62}" font-size="{HFS}" font-weight="700" fill="{INK}">Done well at</text>'
      f'<text x="{CG}" y="{TOP - 62}" font-size="{HFS}" font-weight="700" fill="{INK}">What gives</text>')
    rows, y = [], TOP
    for g in fd["groups"]:
        y += GH
        for f in g["frames"]:
            rows.append((y + RH / 2, f))
            y += RH
    # row guides, under everything
    for cy, f in rows:
        t(f'<line x1="{LM + NW - 8}" y1="{cy}" x2="{CD - 24}" y2="{cy}" stroke="{INK}" stroke-width="1" stroke-dasharray="1 5"/>')
    # the need lines
    for th in needs:
        x, c = xs[th["id"]], COLOURS[th["colour"]]
        t(f'<line x1="{x}" y1="{TOP - 40}" x2="{x}" y2="{bottom}" stroke="{c}" stroke-width="{LW}" stroke-linecap="butt"/>'
          f'<rect x="{x - 11}" y="{bottom}" width="22" height="{LW}" fill="{c}"/>')
    # group headers: the paradox, and what pulls apart in it
    y = TOP
    for g in fd["groups"]:
        t(f'<line x1="{LM}" y1="{y + 12}" x2="{LM + NW - 8}" y2="{y + 12}" stroke="{INK}" stroke-width="2"/>'
          f'<line x1="{CD}" y1="{y + 12}" x2="{W - LM}" y2="{y + 12}" stroke="{INK}" stroke-width="2"/>'
          f'<text x="{LM}" y="{y + 40}" font-size="{FS}" font-weight="700" fill="{INK}" letter-spacing=".06em">{esc(g["name"].upper())}</text>'
          f'<text x="{CD}" y="{y + 40}" font-size="{FS}" fill="{INK}"><tspan font-weight="700">{esc(g.get("label", "Pulls apart:"))}</tspan> {esc(g["pulls"])}</text>')
        y += GH + RH * len(g["frames"])
    # rows: name, the interchange, stations, then the two text columns
    for cy, f in rows:
        t(f'<a href="{esc(fd["post"])}#{esc(f["id"])}"><text x="{LM}" y="{cy + 5.3}" font-size="{FS}" font-weight="700" fill="{INK}">{esc(f["name"])}</text></a>')
        held = sorted(xs[k] for k in f["holds"])
        a, b = held[0], held[-1]
        t(f'<line x1="{a}" y1="{cy}" x2="{b}" y2="{cy}" stroke="{PAPER}" stroke-width="16"/>'
          f'<line x1="{a}" y1="{cy}" x2="{b}" y2="{cy}" stroke="{INK}" stroke-width="6"/>')
        for th in needs:
            k = th["id"]
            if k in f["t"]:
                fill = INK if k in f["holds"] else PAPER
                t(f'<circle cx="{xs[k]}" cy="{cy}" r="9" fill="{fill}" stroke="{INK}" stroke-width="4">'
                  f'<title>{esc(f["name"])}, {esc(th["name"])}: {esc(f["t"][k])}</title></circle>')
        for x, text, width in ((CD, f["done"], CG - CD - 32), (CG, f["gives"], W - LM - CG)):
            ls = wrap(text, width)
            y0 = cy + 5.3 - 11 * (len(ls) - 1)
            for i, ln in enumerate(ls):
                t(f'<text x="{x}" y="{y0 + 22 * i}" font-size="{FS}" fill="{INK}">{esc(ln)}</text>')
    # key: each need in a person's words, and how often the field and these frames reach for it
    t(f'<line x1="{LM}" y1="{ky - 34}" x2="{W - LM}" y2="{ky - 34}" stroke="{INK}" stroke-width="2"/>')
    kw = (W - 2 * LM) / len(needs)
    for i, th in enumerate(needs):
        x = LM + i * kw
        t(f'<line x1="{x}" y1="{ky}" x2="{x + 40}" y2="{ky}" stroke="{COLOURS[th["colour"]]}" stroke-width="{LW}"/>'
          f'<text x="{x + 54}" y="{ky + 5.3}" font-size="{FS}" font-weight="700" fill="{INK}">{esc(th["name"])}</text>')
        y = ky + 36
        for ln in wrap(f"“{th['is']}”", kw - 40):
            t(f'<text x="{x}" y="{y}" font-size="{FS}" fill="{INK}">{esc(ln)}</text>'); y += 22
        t(f'<text x="{x}" y="{ky + 124}" font-size="{FS}" fill="{INK}">{fr[th["id"]]} of {nfr} frames; {field[th["id"]]} of {nf} in the field</text>')
    sy = ky + 194
    t(f'<circle cx="{LM + 9}" cy="{sy}" r="9" fill="{PAPER}" stroke="{INK}" stroke-width="4"/>'
      f'<text x="{LM + 30}" y="{sy + 5.3}" font-size="{FS}" fill="{INK}">The frame builds on this need</text>'
      f'<line x1="{LM + 420}" y1="{sy}" x2="{LM + 500}" y2="{sy}" stroke="{INK}" stroke-width="6"/>'
      f'<circle cx="{LM + 420}" cy="{sy}" r="9" fill="{INK}" stroke="{INK}" stroke-width="4"/>'
      f'<circle cx="{LM + 500}" cy="{sy}" r="9" fill="{INK}" stroke="{INK}" stroke-width="4"/>'
      f'<text x="{LM + 524}" y="{sy + 5.3}" font-size="{FS}" fill="{INK}">Joined: the needs the frame lets a person have at once, like the platforms of an interchange. An open station on the link is a need it also touches.</text>')
    t("</svg>")
    return "".join(out), W, H


def table(fd, td):
    """Every station as a row, for screen readers and for reading."""
    names = {th["id"]: th["name"] for th in td["themes"]}
    order = [th["id"] for th in td["themes"]]
    rows = []
    for g in fd["groups"]:
        for j, f in enumerate(g["frames"]):
            marks = sorted(f["t"].items(), key=lambda kv: order.index(kv[0]))
            for i, (k, v) in enumerate(marks):
                held = " (joined)" if k in f["holds"] else ""
                who = f'<a href="#{esc(f["id"])}">{esc(f["name"])}</a>' if i == 0 else ""
                cells = (esc(g["name"]) if i == 0 and j == 0 else "", who, esc(names[k]) + held, esc(v))
                rows.append("<tr>" + "".join(f'<td><span class="t t-small">{c}</span></td>' for c in cells) + "</tr>")
    head = "".join(f'<th><span class="t t-small">{h}</span></th>' for h in ("Paradox", "Frame", "Need", "How the frame builds on it"))
    return f'<table class="pm-table"><thead><tr>{head}</tr></thead><tbody>{"".join(rows)}</tbody></table>'
