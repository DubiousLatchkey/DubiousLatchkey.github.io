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
