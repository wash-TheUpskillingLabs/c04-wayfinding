#!/usr/bin/env python3
"""Build the Wayfinding site from content/ into static HTML.

    python3 tools/build.py

Edit the words in content/. Each section is one file; the comment at its top
names it (id, title, short label, pictogram, tile colour).
A blog post is a folder in content/blog/ with post.json and its sections.

The script owns the sign system, so every page follows the same rules:

  Arrows say where a link goes, and nothing else.
    ↓  further down this page      →  another page on this site
    ↗  leaves this site            ↑  back to the top      ←  back
  Every arrow on a link is chosen here from the link's target, never by hand.
  Pictograms name a section and are never arrows. A sign that does nothing
  never looks like a control: interactive things always carry a text label.
  Every page shows where you are: the You are here bar names the section and
  opens every stop. Otherwise the page stays quiet (ma): space, not rules,
  separates sections.
"""
import html, json, os, re, sys
from datetime import date
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sitmap, flow

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
C = os.path.join(ROOT, "content")
REPO = "https://github.com/wash-TheUpskillingLabs/c04-wayfinding"

# Measured left side bearings of Inter's capitals, in em, for optical alignment.
LSB = {**dict.fromkeys("PFBLEHRDNMIK", .057), **dict.fromkeys("WAYVX", .023), "T": .032,
       **dict.fromkeys("OQCG", .04), "S": .035, "U": .05, "J": .03, "Z": .03}

ICONS = {
    # arrows: direction only
    "a-d": '<path d="M12 3v16M6 13l6 6 6-6"/>',
    "a-r": '<path d="M3 12h16M13 6l6 6-6 6"/>',
    "a-ur": '<path d="M6 18L17 7M8 6h10v10"/>',
    "a-u": '<path d="M12 21V5M6 11l6-6 6 6"/>',
    "a-l": '<path d="M21 12H5M11 6l-6 6 6 6"/>',
    # disclosure: opens or closes something here. Not an arrow, never a link.
    "chev": '<path d="M6 9l6 6 6-6"/>',
    "chev-l": '<path d="M15 6l-6 6 6 6"/>',
    "chev-r": '<path d="M9 6l6 6-6 6"/>',
    # pictograms: what a section is about
    "info": '<path d="M12 10v10M9 20h6M10 10h2M12 4v2"/>',
    "ppl": '<path d="M8 3v4M3 21v-6a5 5 0 0 1 10 0v6M17 6v3M14 21v-5a3.5 3.5 0 0 1 7 0v5"/>',
    "post": '<path d="M12 22V2M12 5h7l3 3-3 3h-7M12 13H5l-3 3 3 3h7"/>',
    "eye": '<path d="M2 12s4-7 10-7 10 7 10 7-4 7-10 7S2 12 2 12z"/><path d="M12 9.5a2.5 2.5 0 1 0 0 5 2.5 2.5 0 0 0 0-5z"/>',
    "speech": '<path d="M3 4h18v12H10l-5 4v-4H3z"/>',
    "flag": '<path d="M5 22V3M5 4h14l-3 4.5L19 13H5"/>',
    "note": '<path d="M5 3h10l4 4v14H5zM9 11h6M9 15h6"/>',
    "flask": '<path d="M9 3h6M10 3v6L4 20h16L14 9V3M7 15h10"/>',
    "pin": '<path d="M12 22s-7-7-7-12a7 7 0 0 1 14 0c0 5-7 12-7 12z"/><path d="M12 8v4"/>',
    "cliff": '<path d="M2 6h9v14h11"/>',
    "calendar": '<path d="M3 5h18v16H3zM3 10h18M8 2v5M16 2v5"/>',
    "link": '<path d="M9 7a5 5 0 1 0 0 10M15 7a5 5 0 1 1 0 10M8 12h8"/>',
    "one": '<path d="M12 3v4M7 21v-6a5 5 0 0 1 10 0v6"/>',
    "compass": '<path d="M12 2a10 10 0 1 0 0 20 10 10 0 0 0 0-20z"/><path d="M15.5 8.5l-2 5-5 2 2-5z"/>',
    "tool": '<path d="M14.5 6.5a4 4 0 0 0 5 5L21 13l-8 8-3-3 8-8-1.5-1.5a4 4 0 0 1-5-5L13 2z"/><path d="M3 21l6-6"/>',
    "question": '<path d="M8.5 8.5a3.5 3.5 0 1 1 5 3.2c-1 .5-1.5 1.2-1.5 2.3v1M12 19v2"/>',
}

def ic(name, cls=""):
    return f'<svg class="i{(" " + cls) if cls else ""}" aria-hidden="true"><use href="#{name}"/></svg>'

def arrow_for(href):
    """The one rule: an arrow says where its link goes."""
    if href.startswith(("http://", "https://", "mailto:")): return "a-ur", "ur"
    if href.startswith("#"): return "a-d", "down"
    return "a-r", ""

def lsb(text):
    t = re.sub(r"<[^>]+>", "", text).strip()
    return f' style="--lsb:{LSB.get(t[:1], .05)}em"'

def sprite():
    syms = "".join(f'<symbol id="{k}" viewBox="0 0 24 24">{v}</symbol>' for k, v in ICONS.items())
    return f'<svg width="0" height="0" style="position:absolute" aria-hidden="true">{syms}</svg>\n'

def read_section(path):
    raw = open(path, encoding="utf-8").read()
    m = re.match(r"<!--\n(.*?)\n-->\n", raw, re.S)
    meta = dict(line.split(": ", 1) if ": " in line else (line.rstrip(":"), "") for line in m.group(1).splitlines())
    return {**meta, "body": raw[m.end():].strip()}

def sections(folder):
    return [read_section(os.path.join(folder, f)) for f in sorted(os.listdir(folder)) if re.match(r"\d\d-.*\.html$", f)]

def fix_links(body):
    """Re-sign every button and call-to-action from its target."""
    def btn(m):
        attrs, label = m.group(1), m.group(2)
        href = re.search(r'href="([^"]+)"', attrs).group(1)
        a, cls = arrow_for(href)
        ext = ' rel="noopener"' if a == "a-ur" and "rel=" not in attrs else ""
        return f'<a{attrs}{ext}><span class="t">{label}</span><span class="tile blue">{ic(a, cls)}</span></a>'
    return re.sub(r'<a( class="btn[^"]*" href="[^"]+")><span class="t">(.*?)</span><span class="tile blue">.*?</span></a>', btn, body)

# ---------- page parts ----------

def head(title, desc, path):
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{html.escape(desc)}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:opsz,wght@14..32,400..800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/wayfinding.css">
<link rel="alternate" type="application/atom+xml" title="Wayfinding blog" href="/blog/feed.xml">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
{sprite()}'''

def sitenav(current):
    items = [("/", "The pod"), ("/about/", "About"), ("/blog/", "Blog")]
    out = []
    for href, label in items:
        cur = current == href or (href == "/blog/" and current.startswith("/blog/"))
        aria = ' aria-current="page"' if current == href else (' aria-current="true"' if cur else "")
        out.append(f'<a href="{href}"{aria}><span class="dot" aria-hidden="true"></span><span class="t">{label}</span></a>')
    out.append(f'<a href="{REPO}" rel="noopener"><span class="t">GitHub</span>{ic("a-ur", "ur")}</a>')
    return f'<nav class="sitenav" aria-label="Site">{"".join(out)}</nav>'

def signhead(current):
    return f'''  <div class="grid">
    <div class="signhead">
      <a class="wordmark" href="/"><span class="tile blue" aria-hidden="true">{ic("post")}</span><span><span class="t wordmark-t wm">Wayfinding</span><span class="t t-small sub">A Research Pod of Build Cycle C04, The Upskilling Labs of Greater Washington</span></span></a>
      {sitenav(current)}
    </div>
  </div>
'''

def herebar():
    return f'''<nav class="herebar" aria-label="You are here">
  <div class="here-row">
    <a class="here-mark" href="/"><span class="tile blue" aria-hidden="true">{ic("post")}</span><span class="t">Wayfinding</span></a>
    <button class="here-toggle" type="button" aria-expanded="false" aria-controls="stops"><span class="tile red" aria-hidden="true">{ic("pin")}</span><span class="t t-small lbl">You are here</span><span class="t t-small name" id="here-name"></span><span class="t t-small more">All stops</span>{ic("chev", "chev")}</button>
  </div>
  <ol class="dots" id="here-dots"></ol>
  <div class="stops" id="stops" hidden><ol class="mline stops-line" id="stops-list"></ol></div>
</nav>
'''

def section(s, nxt):
    tile = f' {s["tile"]}' if s.get("tile") else ""
    body = fix_links(s["body"])
    # Ma: no per-section "next stop". The page reads in order, and the
    # You are here bar names where you are and opens every stop.
    body = "\n".join("      " + line for line in body.splitlines())
    full = " full" if s.get("full") else ""
    return f'''  <section class="sec grid{full}" aria-labelledby="{s["id"]}">
    <div class="sign"><span class="tile{tile}" aria-hidden="true">{ic(s["icon"])}</span><h2 id="{s["id"]}"{lsb(s["title"])}>{s["title"]}</h2></div>
    <div class="flow">
{body}
    </div>
  </section>
'''

def footer():
    legend = [("a-d", "Further down this page"), ("a-r", "Another page on this site"), ("a-ur", "Leaves this site"), ("a-u", "Back to the top")]
    lis = "".join(f'<li>{ic(i)}<span class="t t-small">{t}</span></li>' for i, t in legend)
    lis += '<li><span class="here-dot" aria-hidden="true"></span><span class="t t-small">You are here</span></li>'
    return f'''<footer>
  <div class="grid">
    <a class="totop" href="#top"><span class="tile blue" aria-hidden="true">{ic("a-u")}</span><span class="t t-small">Back to the top</span></a>
    <div class="flow t-small">
      <p class="legend-title">How to read the signs</p>
      <ul class="legend">{lis}</ul>
      <p>A Research Pod of <a href="https://github.com/wash-TheUpskillingLabs/c04" rel="noopener">Build Cycle C04</a>, The Upskilling Labs of Greater Washington.</p>
      <p>This site is a prototype we’re building as we use it. Licensed CC BY 4.0: share it, adapt it, credit us.</p>
      <p>Set in Inter. Palette: Swiss Style Color Picker, scheme 14, by Fabian Burghardt.</p>
    </div>
  </div>
</footer>
<script src="/assets/wayfinding.js" defer></script>
</body>
</html>
'''

def nice_date(iso):
    d = date.fromisoformat(iso)
    return f'{d.strftime("%b")} {d.day}, {d.year}'

# ---------- pages ----------

def posts():
    root = os.path.join(C, "blog")
    out = []
    for slug in sorted(os.listdir(root)):
        meta = json.load(open(os.path.join(root, slug, "post.json"), encoding="utf-8"))
        out.append({**meta, "slug": slug, "secs": sections(os.path.join(root, slug))})
    # Newest first; "rank" in post.json breaks a tie between posts of the same day (higher first).
    return sorted(out, key=lambda p: (p["date"], p.get("rank", 0)), reverse=True)

def post_list(ps):
    lis = "".join(f'''
  <li><time class="t t-small num" datetime="{p["date"]}">{nice_date(p["date"])}</time><p class="t-h3"><a href="/blog/{p["slug"]}/">{p["title"]}</a></p><p class="t-body">{p["dek"]}</p></li>''' for p in ps)
    return f'<ul class="rows posts">{lis}\n</ul>'

def post_carousel(ps):
    """Blog post cards in a row that scrolls sideways and snaps. Works with no script;
    the script reveals Previous and Next."""
    cards = []
    for p in ps:
        if p.get("cover"):
            cover = f'<img class="card-cover" src="{p["cover"]}" alt="" loading="lazy">'
        else:
            cover = f'<span class="card-cover card-icon" aria-hidden="true">{ic(p.get("icon", "note"))}</span>'
        cards.append(f'''  <li><a class="card" href="/blog/{p["slug"]}/">{cover}<span class="card-body"><time class="t t-small num" datetime="{p["date"]}">{nice_date(p["date"])}</time><span class="t t-h3 card-title">{p["title"]}</span><span class="t t-small card-dek">{p["dek"]}</span><span class="card-read"><span class="t t-small">Read the post</span>{ic("a-r")}</span></span></a></li>''')
    nav = f'<div class="carousel-nav" hidden><button type="button" class="cbtn cprev">{ic("chev-l")}<span class="t">Previous</span></button><button type="button" class="cbtn cnext"><span class="t">Next</span>{ic("chev-r")}</button><a class="all" href="/blog/"><span class="t">All posts</span>{ic("a-r")}</a></div>'
    return f'<div class="carousel" role="region" aria-roledescription="carousel" aria-label="Blog posts">\n<ul class="cards">\n' + "\n".join(cards) + f'\n</ul>\n{nav}\n</div>'

def build_home(ps):
    secs = sections(os.path.join(C, "home"))
    for s in secs: s["body"] = s["body"].replace("{{latest_posts}}", post_list(ps[:3])).replace("{{post_carousel}}", post_carousel(ps))
    h1 = "People don’t get lost in the room. They get lost on the way to the next one."
    page = head("Wayfinding", "Wayfinding: a Research Pod in Build Cycle C04, The Upskilling Labs of Greater Washington. How do people find their way between the parts of The Labs, and what do they need to see to choose the route that fits them?", "/")
    page += herebar() + f'''<header class="cover" id="top">
{signhead("/")}  <div class="grid hero">
    <h1{lsb(h1)}>{h1}</h1>
    <p class="t-lead sub">We’re rebuilding how The Labs gets people from their first workshop to whatever comes next.</p>
    <div class="ctas">
      <a class="btn light" href="#ways"><span class="t">Find your way in</span><span class="tile blue">{ic("a-d", "down")}</span></a>
    </div>
  </div>
</header>

<main id="main">
'''
    page += "".join(section(s, secs[i + 1] if i + 1 < len(secs) else None) for i, s in enumerate(secs))
    page += "</main>\n\n" + footer()
    return page

def build_post(p, mapb=None):
    secs = p["secs"]
    if mapb:
        for sec in secs: sec["body"] = sec["body"].replace("{{map}}", mapb[0]).replace("{{total}}", str(mapb[1])).replace("{{flow}}", mapb[2])
    page = head(f'{p["title"]} | Wayfinding', p["dek"], f'/blog/{p["slug"]}/')
    words = sum(len(re.sub(r"<[^>]+>", " ", s["body"]).split()) for s in secs if s["id"] != "sources")
    mins = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"][min(9, max(0, round(words / 230) - 1))]
    page += herebar() + f'''<header class="cover short" id="top">
{signhead(f'/blog/{p["slug"]}/')}  <div class="grid hero">
    <a class="back" href="/blog/">{ic("a-l")}<span class="t t-small">All posts</span></a>
    <h1{lsb(p["title"])}>{p["title"]}</h1>
    <p class="t-lead dek">{p["dek"]}</p>
    <p class="t-small byline">{p["byline"]}, <time datetime="{p["date"]}">{nice_date(p["date"])}</time>. A {mins}-minute read.</p>
  </div>
</header>

<main id="main">
'''
    page += "".join(section(s, secs[i + 1] if i + 1 < len(secs) else None) for i, s in enumerate(secs))
    page += "</main>\n\n" + footer()
    return page

def build_blog(ps):
    secs = [
        {"id": "posts", "title": "All posts", "short": "All posts", "icon": "note", "tile": "", "body": post_list(ps)},
        {"id": "subscribe", "title": "Get new posts", "short": "Subscribe", "icon": "eye", "tile": "blue",
         "body": f'<p>Add <a href="/blog/feed.xml">the feed</a> to any feed reader, or watch the pod’s repo on GitHub, where every post starts as a pull request.</p>\n<a class="btn" href="{REPO}"><span class="t">Follow on GitHub</span><span class="tile blue"></span></a>'},
    ]
    page = head("Blog | Wayfinding", "Notes from the Wayfinding pod as we work: what we read, who we talked to, what we built, and what broke.", "/blog/")
    page += herebar() + f'''<header class="cover short" id="top">
{signhead("/blog/")}  <div class="grid hero">
    <h1{lsb("Blog")}>Blog</h1>
    <p class="t-lead dek">Notes from the pod as we work: what we read, who we talked to, what we built, and what broke.</p>
  </div>
</header>

<main id="main">
'''
    page += "".join(section(s, secs[i + 1] if i + 1 < len(secs) else None) for i, s in enumerate(secs))
    page += "</main>\n\n" + footer()
    return page

def build_about(ps):
    secs = sections(os.path.join(C, "about"))
    page = head("About | Wayfinding", "About the Wayfinding pod: what we believe, where people get lost at The Labs, how we work and what we're building.", "/about/")
    page += herebar() + f'''<header class="cover short" id="top">
{signhead("/about/")}  <div class="grid hero">
    <h1{lsb("About")}>About the pod</h1>
    <p class="t-lead dek">Wayfinding is one of three Research Pods in Build Cycle C04. We study how people find their way between the parts of The Labs, and build what helps them choose the route that fits.</p>
  </div>
</header>

<main id="main">
'''
    page += "".join(section(s, secs[i + 1] if i + 1 < len(secs) else None) for i, s in enumerate(secs))
    page += "</main>\n\n" + footer()
    return page

def map_block():
    """The problem situation map for the blog post: the poster, its button, and every statement as a table."""
    sts = json.load(open(os.path.join(C, "map", "statements.json"), encoding="utf-8"))
    asof = date.today().strftime("%b %-d, %Y")
    pic, counts, _ = sitmap.svg(sts, asof, underlay="/assets/proto-labs-map.webp")
    write("map/problem-situation.svg", pic.replace('href="/assets/proto-labs-map.webp"', 'href="https://c04-wayfinding.vercel.app/assets/proto-labs-map.webp"'))
    total = len(sts)
    block = f'''<div class="sitmap-wrap">{pic}</div>
<a class="btn" href="/map/problem-situation.svg"><span class="t">Open the poster</span><span class="tile blue">{ic("a-r")}</span></a>
<details class="pm-details"><summary><span><span class="t">All {total} statements as a table</span></span>{ic("chev", "chev")}</summary>{sitmap.table(sts)}</details>'''
    return block, total

def flow_block():
    """The region chart for its blog post: the chart inline, and a link to the poster."""
    data = flow.load(os.path.join(C, "flow", "flow.json"))
    pic, w, h = flow.svg(data)
    write("flow/the-region.svg", pic)
    show = "".join(f'<button type="button" class="chip" data-show="{k}" aria-pressed="false">{n}</button>'
                   for k, n in [("all", "All")] + flow.NAMES)
    return f'''<div class="flow-show" hidden><span class="t t-small">Show</span>{show}</div>
<div class="flow-wrap" data-show="all">{pic}</div>
<a class="btn" href="/flow/the-region.svg"><span class="t">Open the Chart</span><span class="tile blue">{ic("a-r")}</span></a>'''

def build_404():
    secs = [{"id": "routes", "title": "Ways back", "short": "Ways back", "icon": "post", "tile": "blue", "body": f'''<ul class="rows routes">
  <li><a class="route-link" href="/"><span class="t">The pod’s home page</span>{ic("a-r")}</a><span class="t t-small quiet">What we’re working on and how to join.</span></li>
  <li><a class="route-link" href="/blog/"><span class="t">The blog</span>{ic("a-r")}</a><span class="t t-small quiet">Everything we’ve written so far.</span></li>
  <li><a class="route-link" href="{REPO}/tree/main/research" rel="noopener"><span class="t">The research folder</span>{ic("a-ur")}</a><span class="t t-small quiet">On GitHub. Every source we’ve read.</span></li>
</ul>
<p>If a link on our site brought you here, that’s our mistake. <a href="{REPO}/issues/new?title=Broken%20link" rel="noopener">Tell us which one</a> and we’ll fix it.</p>'''}]
    page = head("Off the map | Wayfinding", "This page isn’t here. Here are the ways back.", "/404")
    page += f'''<header class="cover short" id="top">
{signhead("/404")}  <div class="grid hero">
    <h1{lsb("You")}>You’re off the map.</h1>
    <p class="t-lead dek">The page you asked for isn’t here. It may have moved, or the address has a typo. For a pod that studies getting lost, this is a little embarrassing.</p>
  </div>
</header>

<main id="main">
'''
    page += "".join(section(s, secs[i + 1] if i + 1 < len(secs) else None) for i, s in enumerate(secs))
    page += "</main>\n\n" + footer()
    return page

def build_feed(ps):
    entries = "".join(f'''
  <entry>
    <title>{html.escape(p["title"])}</title>
    <link href="/blog/{p["slug"]}/" />
    <id>tag:c04-wayfinding,{p["date"]}:{p["slug"]}</id>
    <updated>{p["date"]}T12:00:00-05:00</updated>
    <summary>{html.escape(p["dek"])}</summary>
  </entry>''' for p in ps)
    return f'''<?xml version="1.0" encoding="utf-8"?>
<feed xmlns="http://www.w3.org/2005/Atom">
  <title>Wayfinding blog</title>
  <subtitle>Notes from the Wayfinding pod, Build Cycle C04, The Upskilling Labs of Greater Washington.</subtitle>
  <link href="/blog/" />
  <link rel="self" href="/blog/feed.xml" />
  <id>tag:c04-wayfinding,2026:blog</id>
  <updated>{ps[0]["date"]}T12:00:00-05:00</updated>
  <author><name>The Wayfinding pod</name></author>{entries}
</feed>
'''

def themes_into(ps):
    """The field's themes (Dorst's step 5) for any post that asks for {{themes}}: the map, its poster, every station as a table."""
    import themes
    data = themes.load(os.path.join(C, "themes", "themes.json"))
    pic, w, h = themes.svg(data)
    write("themes/field-themes.svg", pic)
    n = sum(len(g["players"]) for g in data["groups"] if not g.get("inside"))
    block = f'''<div class="tmap-wrap">{pic}</div>
<a class="btn" href="/themes/field-themes.svg"><span class="t">Open the Poster</span><span class="tile blue">{ic("a-r")}</span></a>
<details class="pm-details"><summary><span><span class="t">All {n} Players, as a Table</span></span>{ic("chev", "chev")}</summary>{themes.table(data)}</details>'''
    for p in ps:
        for sec in p["secs"]:
            sec["body"] = sec["body"].replace("{{themes}}", block)


def write(rel, text):
    path = os.path.join(ROOT, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    open(path, "w", encoding="utf-8").write(text)
    print("wrote", rel)

if __name__ == "__main__":
    ps = posts()
    themes_into(ps)
    write("index.html", build_home(ps))
    write("about/index.html", build_about(ps))
    write("blog/index.html", build_blog(ps))
    mapb = map_block() + (flow_block(),)
    for p in ps: write(f"blog/{p['slug']}/index.html", build_post(p, mapb))
    write("blog/feed.xml", build_feed(ps))
    write("404.html", build_404())
