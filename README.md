# ChanOJ.github.io

GitHub Pages index of my historical websites, each kept in its own repository and
served from bunny.net. The page is `index.html`, rendered from [`sites.json`](sites.json).

## Adding a site

Add an entry to `sites.json` (`title`, `year`, `description`, `changes`, `url`, `repo`, `image`) in a
pull request with a screenshot in `shots/` (800 px wide JPEG). Merging to `main`
publishes it. The page sorts the list by `year`, then by `title`, whatever the order in `sites.json`.

`changes` is a one-line summary of what was changed from the original site so that it works
today (or "Served as-is..." if nothing was). Take it from the "Changes from the original site"
section of the site's own README, and update it when that README changes.

Screenshots are 800×600 (4:3, so they stay sharp on retina screens), taken with an 800×600
viewport on the live site: the home page, the whole fake popup window for sites that have one
(Bomb, Made), or the first English page when the site is bilingual (Orange Juice 98).

Links on the page open in a new tab (`target="_blank"`, `rel="noopener noreferrer"`).

## Preview

```bash
python3 -m http.server 3412
```
