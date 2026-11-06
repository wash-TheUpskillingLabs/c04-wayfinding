#!/usr/bin/env python3
"""Build the Wayfinding site from content/ into static HTML.

    python3 tools/build.py

Edit the words in content/. Each section is one file; the comment at its top
names it (id, title, short label for route maps, pictogram, tile colour).
A blog post is a folder in content/blog/ with post.json and its sections.

The script owns the sign system, so every page follows the same rules:

  Arrows say where a link goes, and nothing else.
    ↓  further down this page      →  another page on this site
    ↗  leaves this site            ↑  back to the top      ←  back
  Every arrow on a link is chosen here from the link's target, never by hand.
  Pictograms name a section and are never arrows. A sign that does nothing
  never looks like a control: interactive things always carry a text label.
  Every page shows where you are (the You are here bar, which opens every
  stop) and the next stop at the end of each section.
"""
import html, json, os, re, sys
from datetime import date

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
    items = [("/", "The pod"), ("/blog/", "Blog")]
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

def linemap(secs, label="On this page"):
    lis = "".join(f'<li><a href="#{s["id"]}"><span class="stn" aria-hidden="true"></span><span class="t t-small">{s["short"]}</span></a></li>' for s in secs)
    return f'''    <nav class="linemap" aria-label="{label}">
      <p class="t t-small lm-title">{label}</p>
      <ol>{lis}</ol>
    </nav>
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
    if nxt:
        follow = f'<a class="next" href="#{nxt["id"]}"><span class="t t-small">Next stop</span><span class="t">{nxt["title"]}</span>{ic("a-d")}</a>'
    else:
        follow = f'<a class="next" href="#top"><span class="t t-small">End of the line</span><span class="t">Back to the top</span>{ic("a-u")}</a>'
    body = "\n".join("      " + line for line in (body + "\n" + follow).splitlines())
    return f'''  <section class="sec grid" aria-labelledby="{s["id"]}">
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
    return sorted(out, key=lambda p: p["date"], reverse=True)

def post_list(ps):
    lis = "".join(f'''
  <li><time class="t t-small num" datetime="{p["date"]}">{nice_date(p["date"])}</time><p class="t-h3"><a href="/blog/{p["slug"]}/">{p["title"]}</a></p><p class="t-body">{p["dek"]}</p></li>''' for p in ps)
    return f'<ul class="rows posts">{lis}\n</ul>'

def build_home(ps):
    secs = sections(os.path.join(C, "home"))
    for s in secs: s["body"] = s["body"].replace("{{latest_posts}}", post_list(ps[:3]))
    h1 = "People don’t get lost in the room. They get lost on the way to the next one."
    page = head("Wayfinding", "Wayfinding: a Research Pod in Build Cycle C04, The Upskilling Labs of Greater Washington. How do people find their way between the parts of The Labs, and what do they need to see to choose the route that fits them?", "/")
    page += herebar() + f'''<header class="cover" id="top">
{signhead("/")}  <div class="grid hero">
    <h1{lsb(h1)}>{h1}</h1>
    <p class="t-lead sub">We’re rebuilding how The Labs gets people from their first workshop to whatever comes next.</p>
    <div class="ctas">
      <a class="btn light" href="#ways"><span class="t">Find your way in</span><span class="tile blue">{ic("a-d", "down")}</span></a>
      <p class="t-small way-hint">Three ways in, from one minute to a few hours a week.</p>
    </div>
  </div>
</header>

<main id="main">
'''
    page += "".join(section(s, secs[i + 1] if i + 1 < len(secs) else None) for i, s in enumerate(secs))
    page += "</main>\n\n" + footer()
    return page

def build_post(p):
    secs = p["secs"]
    page = head(f'{p["title"]} | Wayfinding', p["dek"], f'/blog/{p["slug"]}/')
    words = sum(len(re.sub(r"<[^>]+>", " ", s["body"]).split()) for s in secs if s["id"] != "sources")
    mins = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"][min(9, max(0, round(words / 230) - 1))]
    page += herebar() + f'''<header class="cover short" id="top">
{signhead(f'/blog/{p["slug"]}/')}  <div class="grid hero">
    <a class="back" href="/blog/">{ic("a-l")}<span class="t t-small">All posts</span></a>
    <h1{lsb(p["title"])}>{p["title"]}</h1>
    <p class="t-lead dek">{p["dek"]}</p>
    <p class="t-small byline">{p["byline"]}, <time datetime="{p["date"]}">{nice_date(p["date"])}</time>. A {mins}-minute read.</p>
{linemap(secs, "In this post")}  </div>
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

def write(rel, text):
    path = os.path.join(ROOT, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    open(path, "w", encoding="utf-8").write(text)
    print("wrote", rel)

if __name__ == "__main__":
    ps = posts()
    write("index.html", build_home(ps))
    write("blog/index.html", build_blog(ps))
    for p in ps: write(f"blog/{p['slug']}/index.html", build_post(p))
    write("blog/feed.xml", build_feed(ps))
    write("404.html", build_404())
