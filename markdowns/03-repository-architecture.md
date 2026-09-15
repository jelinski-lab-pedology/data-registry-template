# Repository architecture

## Recommended project tree

The lab-wide template uses descriptive directories without numeric prefixes:

```text
project/
├── README.md
├── project.toml                  # optional project marker/configuration
├── registry/
│   ├── registry--packages.csv
│   ├── registry--parties.csv
│   ├── registry--party-roles.csv
│   ├── registry--dictionary.csv
│   └── registry--vocab-schema.csv
├── vocab/
│   ├── registry-table-iid.csv
│   ├── content-domains.csv
│   ├── release-status.csv
│   ├── role-schema.csv
│   ├── credit-roles.csv
│   ├── credit-contribution-degree.csv
│   └── ...
├── data/
│   └── <ds_iid>/
│       └── <release_slug>/
│           ├── raw/
│           ├── extracted/
│           ├── reference/
│           └── <release_slug>.sha256
├── scripts/
│   ├── mint_ids.py
│   ├── manifest.py
│   ├── validate_registry.py
│   └── ...
└── docs/
    ├── index.md
    ├── 01-overview.md
    └── ...
```

The lab glossary lives in a **separate repository** and is not part of this project tree.

## `registry/`

The `registry/` directory contains the standardized tables that define and populate the project registry.

A useful rule is:

> Every standardized CSV in `registry/` must be defined by `registry--dictionary.csv`.

The five canonical registry artifacts are:

### `registry--packages.csv`

Dataset- and release-level descriptive metadata, provenance, coverage, rights, processing, integrity, and status.

### `registry--parties.csv`

Stable identities for people and organizations referenced by the registry.

### `registry--party-roles.csv`

Relationships between parties and datasets/releases. One row should represent one role assertion.

### `registry--dictionary.csv`

Field-level specification for all standardized registry tables, including itself and the vocabulary schema.

### `registry--vocab-schema.csv`

An intentionally empty, header-only CSV that physically represents the common schema all vocabulary files must follow.

It is not a vocabulary. It is a standardized registry artifact whose columns are defined in the dictionary.

## `vocab/`

The `vocab/` directory contains controlled value sets used by registry fields.

All files in this directory should conform to the header in `registry--vocab-schema.csv`.

Examples include:

- `registry-table-iid.csv`;
- `content-domains.csv`;
- `release-status.csv`;
- `role-schema.csv`;
- `credit-roles.csv`;
- `credit-contribution-degree.csv`.

A vocabulary's filename is descriptive; the standardized structure comes from the vocab schema.

## `data/`

The `data/` directory contains acquired releases and derived material.

```text
data/<ds_iid>/<release_slug>/
```

creates a direct mapping between registry identities and filesystem locations.

A release directory may contain:

- `raw/` — unchanged acquired files;
- `extracted/` — machine-generated exports from source containers or databases;
- `reference/` — documentation supplied with the release or curated reference material;
- curation tables or inventories;
- a manifest beside the directories it describes.

Projects may add additional derived directories, but raw acquisitions should remain immutable.

## `scripts/`

Core scripts implement repeatable registry operations.

The shared standard should keep only genuinely generic tools here. Highly source-specific tooling can live in project repositories or an optional utilities area.

Core examples:

- mint dataset, release, and party identifiers;
- create and verify manifests;
- validate registry CSVs against the dictionary;
- validate foreign keys and vocabularies.

## `docs/`

The `docs/` directory contains this Quarto-ready handbook.

The documentation explains the standard, but does not replace the machine-readable registry.

## Separate glossary repository

The shared lab glossary is maintained independently because it has a different lifecycle from project registries.

Projects can link to the glossary repository in documentation without copying all glossary content into each registry. This avoids divergent definitions and allows terms to evolve through one shared Git history.

## Dependency model

The architecture can be summarized as:

```text
registry--dictionary.csv
        │
        ├── defines registry--packages.csv
        ├── defines registry--parties.csv
        ├── defines registry--party-roles.csv
        ├── defines itself
        └── defines registry--vocab-schema.csv
                              │
                              └── constrains every CSV in vocab/
```

Project-specific scientific data structures sit outside this core and can build on it without changing the shared registry standard.
