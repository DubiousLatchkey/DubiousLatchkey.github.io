# Project guidance

## Purpose

This repository is the GitHub Pages project site for DubiousLatchkey. Project-specific pages live under `_projects/`.

## Standalone projects

- spindafy and swshRaidMap are independently hosted and were removed as submodules. Do not restore submodule checkout or copy steps in the Pages workflow.
- Local leftover checkouts of those projects may still exist; preserve them and do not commit them into the portfolio.

## Development

- Preserve unrelated local changes when updating the site.
- Use the existing project content and Jekyll structure when updating the site.

## Social previews

- Project Open Graph images are actual browser screenshots in assets/images/social/, cropped to 1200 x 630 JPEGs under 5 MB.
- Each _projects/ page declares its screenshot and a concise description in front matter. The Projects tab uses portfolio.jpg; social_preview_image in _config.yml supplies the site-wide fallback.
- Refresh screenshots after major page changes. Capture the published page with embedded thumbnails fully loaded, then resize to 1200 pixels wide and crop from the top to 630 pixels tall.
- Verify generated og:image URLs and image dimensions after building. After deployment, use LinkedIn Post Inspector to refresh cached link previews; existing Featured cards may need to be re-added.
