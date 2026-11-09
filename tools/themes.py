"""The field's themes, drawn as Metro lines (Dorst's step 5).

Each theme is a human need, named the way a person would feel it, and drawn as a line running down
the page; each organization in the field is a row, with a station on every line whose need it
reaches for. A player on several lines is an interchange, the places frames
come from (step 6). The three voices inside The Labs sit at the top, so you can read across to see
which themes they share with the field. Data: content/themes/themes.json, one line of evidence per
station, so anyone can disagree with a mark and say why.
"""
import html, json

INK, PAPER, BLUE, RED = "#0b3536", "#e5e7de", "#0098d8", "#f54123"
# Five line colours from the Swiss palette (schemes 3, 10, 11, 14). Checked like the journey map's:
# every pair at least 19.6 CAM02-UCS apart under protanopia, deuteranopia and tritanopia, in this
# order. Blue is direction, so Coherence (where I am, what comes next) is blue.
COLOURS = {"yellow": "#e6c700", "blue": BLUE, "navy": "#08327d", "silver": "#a5a6a9", "green": "#007500"}
FONT = "Inter, system-ui, sans-serif"
FS, TFS, HFS = 15.118, 32, 15.118
LM, NW, LS, RH, GH = 56, 372, 124, 32, 58      # margin, name column, line spacing, row, group header
PANEL = NW + 60 + 4 * LS + 60
GUT = 88
W = LM + 2 * PANEL + GUT + LM
TOP = 318                                     # first group header
LW = 8
SPLIT = {"Mattering": ("", "Mattering"), "Coherence": ("", "Coherence"), "Support": ("", "Support"),
         "Belonging": ("", "Belonging"), "Becoming": ("", "Becoming")}


def esc(s):
    return html.escape(s, quote=True)


def load(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def href(d, p):
    return p.get("link") or (d["src"] + p["file"])


def counts(d):
    field, inside = {t["id"]: 0 for t in d["themes"]}, {t["id"]: 0 for t in d["themes"]}
    nf = ni = 0
    for g in d["groups"]:
        for p in g["players"]:
            if g.get("inside"):
                ni += 1
            else:
                nf += 1
            for t in p["t"]:
                (inside if g.get("inside") else field)[t] += 1
    return field, inside, nf, ni


def panels(d):
    """Inside, libraries, agencies and coordinators on the left; programs, networks, funders right."""
    gs = d["groups"]
    return [gs[:4], gs[4:]]


def panel_height(groups):
    return sum(GH + RH * len(g["players"]) for g in groups)


def svg(d):
    themes = d["themes"]
    field, inside, nf, ni = counts(d)
    ph = max(panel_height(p) for p in panels(d))
    ky = TOP + ph + 70
    H = ky + 340
    out = [f'<svg class="tmap" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" role="img" '
           f'aria-label="Five human needs running through the field, drawn as Metro lines, with a station for each organization that reaches for a need. The table below lists every station and its evidence." '
           f'font-family="{FONT}"><rect width="{W}" height="{H}" fill="{PAPER}"/>']
    t = out.append
    t(f'<text x="{LM}" y="{LM + 26}" font-size="{TFS}" font-weight="700" fill="{INK}">Five Human Needs Running Through the Field</text>')
    t(f'<text x="{LM}" y="{LM + 64}" font-size="{FS}" fill="{INK}">Under everything {nf} organizations around The Labs do, and what {["no","one","two","three","four","five"][ni] if ni < 6 else ni} voices inside it told us, is a person who needs something. '
      f'Each line is one of those needs, named for the research behind it. Each station is an organization reaching for it.</text>')
    t(f'<text x="{LM}" y="{LM + 90}" font-size="{FS}" font-style="italic" fill="{INK}">Dorst’s step 5, Themes. Field from desk research logged Nov 6; '
      f'needs read {esc(d["asof"])}. Hover a station for its evidence; every station is in the table below.</text>')
    for pi, groups in enumerate(panels(d)):
        px = LM + pi * (PANEL + GUT)
        x0 = px + NW + 60
        xs = [x0 + i * LS for i in range(len(themes))]
        bottom = TOP + panel_height(groups) - 6
        # theme names over their lines
        for x, th in zip(xs, themes):
            a, b = SPLIT.get(th["name"], (th["name"], ""))
            t(f'<text x="{x}" y="{TOP - 82}" text-anchor="middle" font-size="{HFS}" font-weight="700" fill="{INK}">{esc(a)}</text>'
              f'<text x="{x}" y="{TOP - 62}" text-anchor="middle" font-size="{HFS}" font-weight="700" fill="{INK}">{esc(b)}</text>')
        # row guides first, under everything
        y = TOP
        rows = []
        for g in groups:
            y += GH
            for p in g["players"]:
                rows.append((y + RH / 2, p, g))
                y += RH
        for cy, p, g in rows:
            if p["t"]:
                t(f'<line x1="{px + NW - 8}" y1="{cy}" x2="{xs[-1]}" y2="{cy}" stroke="{INK}" stroke-width="1" stroke-dasharray="1 5"/>')
        # the lines
        for x, th in zip(xs, themes):
            t(f'<line x1="{x}" y1="{TOP - 40}" x2="{x}" y2="{bottom}" stroke="{COLOURS[th["colour"]]}" stroke-width="{LW}" stroke-linecap="butt"/>'
              f'<rect x="{x - 11}" y="{bottom}" width="22" height="{LW}" fill="{COLOURS[th["colour"]]}"/>')
        # group headers
        y = TOP
        for g in groups:
            t(f'<line x1="{px}" y1="{y + 12}" x2="{px + NW - 8}" y2="{y + 12}" stroke="{INK}" stroke-width="2"/>'
              f'<text x="{px}" y="{y + 40}" font-size="{FS}" font-weight="700" fill="{INK}" letter-spacing=".06em">{esc(g["name"].upper())}</text>')
            y += GH + RH * len(g["players"])
        # rows: name, then a station on each line the player carries
        for cy, p, g in rows:
            bold = ' font-weight="700"' if g.get("inside") else ""
            t(f'<a href="{esc(href(d, p))}"><text x="{px}" y="{cy + 5.3}" font-size="{FS}"{bold} fill="{INK}">{esc(p["name"])}</text></a>')
            if not p["t"]:
                t(f'<text x="{px + len(p["name"]) * FS * .52 + 16}" y="{cy + 5.3}" font-size="{FS}" font-style="italic" fill="{INK}">no theme in what we found</text>')
            for x, th in zip(xs, themes):
                if th["id"] in p["t"]:
                    t(f'<circle cx="{x}" cy="{cy}" r="9" fill="{PAPER}" stroke="{INK}" stroke-width="4">'
                      f'<title>{esc(p["name"])}, {esc(th["name"])}: {esc(p["t"][th["id"]])}</title></circle>')
    # key: each need in a person's own words, what it feels like without it, and how many reach for it
    t(f'<line x1="{LM}" y1="{ky - 34}" x2="{W - LM}" y2="{ky - 34}" stroke="{INK}" stroke-width="2"/>')
    kw = (W - 2 * LM) / len(themes)

    def wrap(text, n=44):
        lines, cur = [], ""
        for w_ in text.split():
            if cur and len(cur) + 1 + len(w_) > n:
                lines.append(cur); cur = w_
            else:
                cur = f"{cur} {w_}" if cur else w_
        return lines + [cur]
    for i, th in enumerate(themes):
        x = LM + i * kw
        t(f'<line x1="{x}" y1="{ky}" x2="{x + 40}" y2="{ky}" stroke="{COLOURS[th["colour"]]}" stroke-width="{LW}"/>'
          f'<text x="{x + 54}" y="{ky + 5.3}" font-size="{FS}" font-weight="700" fill="{INK}">{esc(th["name"])}</text>')
        y = ky + 36
        for ln in wrap(f"“{th['is']}”"):
            t(f'<text x="{x}" y="{y}" font-size="{FS}" fill="{INK}">{esc(ln)}</text>'); y += 22
        y += 6
        for j, ln in enumerate(wrap(f"Without it: {th['without']}.")):
            t(f'<text x="{x}" y="{y}" font-size="{FS}" fill="{INK}">' + (f'<tspan font-weight="700">Without it:</tspan>{esc(ln[11:])}' if j == 0 else esc(ln)) + '</text>'); y += 22
        y += 6
        for j, ln in enumerate(wrap(f"Rooted in: {th['roots']}.")):
            t(f'<text x="{x}" y="{y}" font-size="{FS}" fill="{INK}">' + (f'<tspan font-weight="700">Rooted in:</tspan>{esc(ln[10:])}' if j == 0 else esc(ln)) + '</text>'); y += 22
        y += 6
        t(f'<text x="{x}" y="{y}" font-size="{FS}" fill="{INK}">{field[th["id"]]} of {nf} reach for it; {inside[th["id"]]} of {ni} inside</text>')
    sy = ky + 294
    t(f'<circle cx="{LM + 9}" cy="{sy}" r="9" fill="{PAPER}" stroke="{INK}" stroke-width="4"/>'
      f'<text x="{LM + 30}" y="{sy + 5.3}" font-size="{FS}" fill="{INK}">This organization reaches for the need, by what it says it wants, has tried, or how it sees the problem</text>'
      f'<text x="{LM + 900}" y="{sy + 5.3}" font-size="{FS}" font-weight="700" fill="{INK}">Bold:</text>'
      f'<text x="{LM + 948}" y="{sy + 5.3}" font-size="{FS}" fill="{INK}">a voice inside The Labs (alumni survey, organizers’ record, the problem owner)</text>')
    t("</svg>")
    return "".join(out), W, H


def table(d):
    """Every station as a row, for screen readers and for reading."""
    names = {th["id"]: th["name"] for th in d["themes"]}
    rows = []
    for g in d["groups"]:
        for p in g["players"]:
            marks = list(p["t"].items()) or [("", "No theme in what we found; the file is thin.")]
            for i, (k, v) in enumerate(marks):
                who = f'<a href="{esc(href(d, p))}">{esc(p["name"])}</a>' if i == 0 else ""
                cells = (esc(g["name"]) if i == 0 else "", who, esc(names.get(k, "")), esc(v))
                rows.append("<tr>" + "".join(f'<td><span class="t t-small">{c}</span></td>' for c in cells) + "</tr>")
    head = "".join(f'<th><span class="t t-small">{h}</span></th>' for h in ("Group", "Organization", "Need", "Evidence, from its file"))
    return f'<table class="pm-table"><thead><tr>{head}</tr></thead><tbody>{"".join(rows)}</tbody></table>'
