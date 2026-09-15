# Standard lab dataset-registry architecture

## Design principles
- **Machine-readable first.** CSV/YAML/Markdown records are the system of record; rendered documentation is a presentation layer.
- **Dataset concept != release.** A stable dataset identity persists across snapshots; each acquired snapshot gets a release identity.
- **Raw means immutable.** Never edit files under a release `raw/`; transformations are scripted into derived locations.
- **Integrity is explicit.** Every acquired release gets a deterministic SHA-256 manifest.
- **People stay visible.** Party identity is separated from party roles, so original collectors, creators, curators, and contributors remain attributable.
- **Constraints are explicit.** Every standardized registry field is defined in the dictionary; controlled terms live in vocabularies.
- **Shared language is modular.** Glossary terms are independent Git-reviewable Markdown cards compiled into living artifacts.

## Recommended repository tree
```text
project/
├── data-registry.toml
├── README.md
├── registry/
│   ├── registry--packages.csv
│   ├── registry--dictionary.csv
│   ├── registry--parties.csv
│   └── registry--party-roles.csv
├── vocab/
│   ├── vocab--table-iid.csv
│   ├── vocab--release-status.csv
│   ├── vocab--content-domains.csv
│   └── vocab--role-schema.csv
├── scripts/
│   ├── mint_ids.py
│   ├── manifest.py
│   ├── validate_registry.py
│   └── build_glossary.py
├── data/
│   └── <ds_iid>/
│       └── <release_slug>/
│           ├── raw/
│           ├── extracted/
│           ├── reference/
│           └── <release_slug>.sha256
└── docs/
    ├── ARCHITECTURE.md
    ├── REGISTRY-FIELD-GUIDE.md
    └── WORKSHOP-QUICKSTART.md
```

## Registry component boundaries
**Packages** answers: What dataset/release is this? Where did it come from? What does it cover? What are its rights, methods, processing state, and exact raw bytes?

**Dictionary** answers: What does each standardized registry column mean? What type is it? Is it required? What values are legal?

**Parties** answers: Who are the people/organizations we need to refer to?

**Party roles** answers: What did each party do for a dataset or specific release?

**Vocabularies** answer: What machine values are permitted and what do they mean?

## What does *not* belong in the shared registry standard
Project-specific scientific schemas (e.g., pedon/horizon tables, vegetation tables, model outputs) should be documented in project-specific schema/dictionary files. They may reuse the same dictionary pattern, but they should not force every project to share scientific fields that are irrelevant to it.
