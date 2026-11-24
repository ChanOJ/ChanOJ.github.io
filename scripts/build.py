#!/usr/bin/env python3
"""Render the site list of sites.json into index.html (static HTML, no JavaScript).

Usage: python3 scripts/build.py          rewrite index.html
       python3 scripts/build.py --check  exit 1 if index.html is out of date
"""
import html
import json
import re
import sys
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parent.parent
START, END = "<!-- sites:start -->", "<!-- sites:end -->"
DATE = re.compile(r"\d{4}(-\d{2}(-\d{2})?)?")
CONTRIBUTION = {"cod": "code", "gfx": "graphics", "hst": "hosting"}
LINK = 'target="_blank" rel="noopener noreferrer"'


def card(s):
    e = html.escape
    for t in s.get("contribution", []):
        if t not in CONTRIBUTION:
            sys.exit(f'{s["title"]}: unknown contribution "{t}"')
    host = urlparse(s["url"]).netloc
    out = [
        "    <li>",
        '      <div class="text">',
        f'        <h2><a href="{e(s["url"])}" {LINK}>{e(s["title"])}</a></h2>',
        f'        <p>{e(s["description"])}</p>',
        f'        <p class="changes">{e(s["changes"])}</p>',
        f'        <p class="contribution">My contribution: {e(", ".join(CONTRIBUTION[t] for t in s["contribution"]))}</p>',
        f'        <p class="meta">{e(host)} · <a href="{e(s["repo"])}" {LINK}>Source on GitHub</a></p>',
        "      </div>",
    ]
    if s.get("image"):
        out += [
            f'      <a href="{e(s["url"])}" tabindex="-1" {LINK}>',
            f'        <img class="shot" src="{e(s["image"])}" alt="Screenshot of {e(s["title"])}" width="800" height="600" loading="lazy">',
            "      </a>",
        ]
    out.append("    </li>")
    return "\n".join(out)


def render():
    sites = json.loads((ROOT / "sites.json").read_text(encoding="utf-8"))
    for s in sites:
        if not DATE.fullmatch(s.get("date", "")):
            sys.exit(f'{s.get("title")}: "date" must be YYYY, YYYY-MM or YYYY-MM-DD')
    # "date" strings sort chronologically; a less precise date comes before a more precise one
    # of the same period (1999 before 1999-09).
    sites.sort(key=lambda s: (s["date"], s["title"].casefold()))
    page = (ROOT / "index.html").read_text(encoding="utf-8")
    body = "\n".join(card(s) for s in sites)
    new, n = re.subn(
        re.escape(START) + r".*?" + re.escape(END),
        lambda _: f"{START}\n{body}\n    {END}",
        page,
        flags=re.S,
    )
    if n != 1:
        sys.exit(f"index.html must contain exactly one {START} ... {END} block")
    return page, new


page, new = render()
if "--check" in sys.argv:
    if page != new:
        sys.exit("index.html is out of date: run python3 scripts/build.py")
    print("index.html is up to date")
else:
    (ROOT / "index.html").write_text(new, encoding="utf-8")
    print("index.html updated")
