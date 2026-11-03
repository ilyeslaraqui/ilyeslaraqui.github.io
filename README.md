# ilyeslaraqui.github.io

Personal engineering portfolio, published with GitHub Pages.

## Layout

- `index.html`, `projects/*.html` — the pages. **Generated**: edit the source, not these files.
- `_src/build_site.py` — all page text and the list of projects (`PROJECTS`). Folders starting with `_` are not published.
- `_src/svg/` — diagrams and charts embedded in the pages.
- `img/` — photos and figures.
- `style.css` — colours, fonts and layout.

## Updating

1. Edit `_src/build_site.py` (or add images to `img/`).
2. Run `python3 _src/build_site.py`. It rewrites the pages and deletes the page of any project you removed.
3. Commit and push. The live site updates within a couple of minutes.
