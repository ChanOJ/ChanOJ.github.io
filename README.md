# ChanOJ.github.io

GitHub Pages index of my historical websites, each kept in its own repository and
served from bunny.net. The page is `index.html`, rendered from [`sites.json`](sites.json).

## Adding a site

Add an entry to `sites.json` (`title`, `year`, `description`, `changes`, `url`, `repo`, `image`) in a
pull request with a screenshot in `shots/` (800 px wide JPEG), then run
`python3 scripts/build.py`: it renders the list into `index.html` as static HTML (no JavaScript,
so search engines and link previews see it), sorted by `year` then `title`, whatever the order in
`sites.json`. Entries of the same year can carry an optional `date` (`YYYY-MM-DD`, the date of the
state of the site they show) to be listed in that order (undated entries of the year come first). The *Check: index.html* workflow fails if `index.html` is out of date. Merging to `main`
publishes it.

`changes` is a one-line summary of what was changed from the original site so that it works
today (or "Served as-is..." if nothing was). Take it from the "Changes from the original site"
section of the site's own README, and update it when that README changes.

Screenshots are 800×600 (4:3, so they stay sharp on retina screens), taken with an 800×600
viewport on the live site: the home page, the whole fake popup window for sites that have one
(Bomb, Made), or the first English page when the site is bilingual (Orange Juice 98).

Links on the page open in a new tab (`target="_blank"`, `rel="noopener noreferrer"`).

## SEO

`index.html` carries a title, description, canonical URL and Open Graph tags; `robots.txt`,
`sitemap.xml` and `favicon.svg` sit at the root. To submit the site, verify it in Google Search
Console and Bing Webmaster Tools (add the verification meta tag they give to the `<head>`, or
their verification file at the root) and submit `https://chanoj.github.io/sitemap.xml`.

## Preview

```bash
python3 -m http.server 3412
```
