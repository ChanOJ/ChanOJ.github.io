# ChanOJ.github.io

GitHub Pages index of my historical websites, each kept in its own repository and
served from bunny.net. The page is `index.html`, rendered from [`sites.json`](sites.json).

## Adding a site

Add an entry to `sites.json` (`title`, `year`, `description`, `url`, `repo`, `image`) in a
pull request with a screenshot in `shots/` (480 px wide JPEG), keeping the list in alphabetical order by title. Merging to `main`
publishes it.

## Preview

```bash
python3 -m http.server 3412
```
