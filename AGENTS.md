# Project guidance

## Purpose

This repository is the GitHub Pages project site for DubiousLatchkey. Project-specific pages live under `_projects/`, and embedded repositories are managed as Git submodules.

## Submodules

- `spindafy/` and `swshRaidMap/` are registered in `.gitmodules`.
- When an embedded repository is updated upstream, fetch and check out the intended commit in that submodule, then verify the parent repository records the new gitlink.
- Preserve unrelated parent-repository changes and do not rewrite submodule history.

## Development

- Keep the parent checkout clean before changing a submodule pointer.
- Use the existing project content and Jekyll structure when updating the site.

## Social previews

- Project Open Graph images are actual browser screenshots in assets/images/social/, cropped to 1200 x 630 JPEGs under 5 MB.
- Each _projects/ page declares its screenshot and a concise description in front matter. The Projects tab uses portfolio.jpg; social_preview_image in _config.yml supplies the site-wide fallback.
- Refresh screenshots after major page changes. Capture the published page with embedded thumbnails fully loaded, then resize to 1200 pixels wide and crop from the top to 630 pixels tall.
- Verify generated og:image URLs and image dimensions after building. After deployment, use LinkedIn Post Inspector to refresh cached link previews; existing Featured cards may need to be re-added.
