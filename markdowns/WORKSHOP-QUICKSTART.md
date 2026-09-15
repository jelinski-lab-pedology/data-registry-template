# Workshop quick start

## Goal
By the end of the session, each project should have a cloned copy of this template and at least one dataset concept/release registered correctly.

## The five core components
1. **Packages** (`registry/registry--packages.csv`) — one row per dataset release/snapshot.
2. **Dictionary** (`registry/registry--dictionary.csv`) — one row per standardized registry field. Do not casually add/delete/reorder registry columns.
3. **Parties** (`registry/registry--parties.csv`) — one row per person or organization.
4. **Party roles** (`registry/registry--party-roles.csv`) — who did what for which dataset/release.
5. **Glossary + vocabularies** — the glossary defines shared language for humans; vocabulary CSVs define allowed machine values.

## Register one dataset
1. Decide whether this is a genuinely new **dataset concept** or another **release** of an existing dataset.
2. Mint IDs: `python scripts/mint_ids.py dataset my-dataset` or `python scripts/mint_ids.py release my-dataset <dataset_id> --ingest 2026-09-15`.
3. Create `data/<ds_iid>/<release_slug>/raw/` and place an unchanged copy of the delivered files there.
4. Run `python scripts/manifest.py data/<ds_iid>/<release_slug>/raw`. Paste the resulting integrity fields into packages.
5. Complete the packages row. Use source-provided wording for title/citation when available; document uncertainty instead of guessing.
6. Add people/organizations to parties once. Add their dataset/release-specific contributions to party-roles.
7. Run `python scripts/validate_registry.py`.

## Nulls
- blank = not yet assessed / not yet entered;
- `nap` = not applicable;
- `unk` = applicable but unknown after review;
- `none` appears only in the dictionary to mean a field may never be null.
Do not use `NA`, `N/A`, `NULL`, `None`, or `-9999` in registry tables.

## Lists in cells
When a registry field intentionally stores multiple values, use a pipe with **no padding**: `soil|hydrology|geospatial`. Never use comma-separated pseudo-lists.

## Naming
- CSV columns: `snake_case`.
- Human-readable internal identifiers (`*_iid`): lowercase `kebab-case`, immutable, never reused.
- UUID fields (`*_id`): opaque stable identifiers.
- File components: lowercase kebab-case; use `--` only to separate semantic filename/slug components (for example `my-dataset--ing20260915--r001`).
- Paths recorded in registry metadata are relative to the project root and use POSIX `/` separators.

## Glossary workflow
Copy `glossary/term-template.md` to `glossary/terms/<term-iid>.md`, edit one concept only, then run `python scripts/build_glossary.py`. Commit the term card, rebuilt `glossary.csv`, and `glossary--compiled.md` together.
