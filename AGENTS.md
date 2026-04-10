# Repository Guidelines

## Project Structure & Module Organization
This repository stores standalone RPM packaging units. Each package lives in its own top-level directory and usually contains a single `.spec` file plus any supporting assets.

Examples:
- `mesa-git/mesa.spec`
- `zed/zed.spec`
- `cachyos-default-kernel/cachyos-default-kernel.spec`
- `cachyos-default-kernel/99-default`

Automation lives in `.github/workflows/`. The root `README.md` is brief; package-specific behavior should be clear from the spec and nearby assets.

## Build, Test, and Development Commands
Use RPM tooling against the individual spec you are editing.

- `rpmspec -P mesa-git/mesa.spec`
  Expands macros and catches basic spec syntax issues.
- `rpmbuild -bs mesa-git/mesa.spec`
  Builds a source RPM to validate sources, patches, and metadata.
- `rpmbuild -ba zed/zed.spec`
  Runs a full build for a package.
- `mock --rebuild *.src.rpm`
  Optional clean-room rebuild if `mock` is available.

If a package pulls live sources, verify URLs, tags, and checks before updating version fields.

## Coding Style & Naming Conventions
Keep spec formatting consistent with existing files:
- Use aligned `Name:`, `Version:`, `Release:` style fields.
- Prefer four-space indentation inside `%prep`, `%build`, and `%install`.
- Name package directories after the package source, and keep the spec filename predictable, usually `<package>.spec`.
- Add changelog entries only when that spec already maintains them manually.

Avoid broad refactors. This repo favors minimal, targeted spec updates.

## Testing Guidelines
There is no centralized test framework. Validation is package-specific:
- Run `rpmspec -P` before committing.
- Prefer `rpmbuild -bs` for quick checks.
- Use `rpmbuild -ba` when changing patches, file lists, subpackages, or build flags.

When you cannot build locally, note that explicitly in the change summary.

## Commit & Pull Request Guidelines
Follow the commit style already used in history:
- `chore(mesa-git): update to commit 564b061`
- `feat(cachyos-default-kernel): add default CachyOS kernel hook package`

Use Conventional Commit prefixes like `feat(...)` and `chore(...)`. Keep scope equal to the package directory name. PRs should state:
- what package changed
- what upstream version/commit was adopted
- whether the spec was syntax-checked or fully built
