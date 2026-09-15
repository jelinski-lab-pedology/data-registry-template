# Jelinski Pedology Group Data Registry

A shared, machine-readable registry standard for documenting datasets used across Jelinski Pedology Group research projects.

The registry is designed to make dataset identity, provenance, releases, rights, integrity, controlled terms, and contributor roles explicit **before** source data are harmonized, analyzed, or transformed.

The project is intentionally lightweight: the system of record is a set of version-controlled CSV files, controlled vocabularies, and reproducible command-line tools. Human-readable documentation is maintained as a Quarto book.

> **Core principle:** register the dataset you actually received, preserve its raw bytes, document where it came from and what it contains, record who contributed and how, and keep uncertainty visible rather than filling gaps with guesses.

---

## What this repository contains

The registry standard is organized around five canonical CSV artifacts:

```text
registry/
├── registry--packages.csv
├── registry--parties.csv
├── registry--party-roles.csv
├── registry--dictionary.csv
└── registry--vocab-schema.csv
```

Controlled vocabularies live separately:

```text
vocab/
├── registry-table-iid.csv
├── content-domains.csv
├── release-status.csv
├── role-schema.csv
├── credit-roles.csv
├── credit-contribution-degree.csv
└── ...
```

The project also includes:

```text
data/           acquired dataset releases and derived artifacts
scripts/        identifier, manifest, validation, and utility scripts
markdowns/      Quarto handbook source
docs/           rendered HTML handbook for GitHub Pages
```

The shared lab data-management glossary is maintained in a **separate repository** so terminology can evolve once and be reused across projects.

---

## The five registry files

### `registry--packages.csv`

One row represents **one acquired release or snapshot of one dataset concept**.

The packages table records:

- stable dataset identity;
- release identity;
- title, abstract, and purpose;
- source organization and citation;
- repository identifiers and URLs;
- temporal and spatial coverage;
- rights and licensing;
- methods and processing summaries;
- lineage;
- manifest/integrity information;
- release status;
- curator notes.

A conceptual dataset may therefore appear in multiple rows when multiple releases have been acquired.

---

### `registry--parties.csv`

One row represents one person or organization that needs a stable identity in the registry.

The parties table answers:

> **Who is this?**

Identity is kept separate from contribution roles so that the same person or organization can participate differently across datasets and releases.

---

### `registry--party-roles.csv`

One row represents one contributor-role assertion:

> **Party X performed Role Y for Dataset/Release Z.**

The intended design is relational:

```text
one row = one party × one dataset/release scope × one role
```

Multiple contributor roles should not be packed into one pipe-delimited cell.

CRediT is supported as the primary standardized contributor-role taxonomy, with controlled terms maintained in `vocab/credit-roles.csv`.

---

### `registry--dictionary.csv`

The dictionary is the field-level specification for the registry itself.

It defines:

- table;
- field/column name;
- display label;
- column order;
- requiredness;
- storage type;
- value-domain type;
- inline allowed values;
- vocabulary reference;
- null semantics;
- field definition;
- implementation notes.

The dictionary is intended to define **every standardized CSV in `registry/`**, including itself.

---

### `registry--vocab-schema.csv`

This is an intentionally **empty, header-only CSV** defining the standard physical structure required for every controlled vocabulary in `vocab/`.

Vocabulary columns include:

```text
concept_iid
term_code
pref_label
alt_labels
definition
broader_id
status
created
modified
scope_note
related_ids
exact_match_ids
close_match_ids
replaced_by
source
note
```

The meaning of those fields is defined in `registry--dictionary.csv`.

---

## Repository architecture

A typical project using the registry follows this pattern:

```text
.
├── README.md
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
│   └── credit-contribution-degree.csv
├── data/
│   └── <ds_iid>/
│       └── <release_slug>/
│           ├── raw/
│           ├── extracted/
│           ├── reference/
│           └── <release_slug>.sha256
├── scripts/
├── markdowns/
│   ├── _quarto.yml
│   ├── index.md
│   └── 01-...md
└── docs/
    └── rendered Quarto site
```

---

## Identity model

The registry distinguishes the **dataset concept** from individual **releases**.

### Dataset identity

A dataset concept has:

```text
dataset_id    opaque stable UUID
ds_iid        readable immutable internal identifier
```

Example:

```text
dataset_id = <uuid>
ds_iid     = nrcs-nasis-ak
```

These remain stable across releases.

### Release identity

Each frozen acquisition receives:

```text
release_id
release_slug
```

Recommended release-slug pattern:

```text
{ds_iid}--ingYYYYMMDD--rNNN
```

Example:

```text
nrcs-nasis-ak--ing20260915--r003
```

A new download, corrected collaborator delivery, annual update, repository revision, or other materially distinct acquisition normally receives a new release identity while retaining the same dataset identity.

---

## Raw data and integrity

Files placed under:

```text
data/<ds_iid>/<release_slug>/raw/
```

should be treated as immutable source acquisitions.

Do not clean, rename, overwrite, or silently alter raw source files after registration.

Derived material belongs in directories such as:

```text
extracted/
reference/
```

Each release should receive a deterministic SHA-256 manifest. The packages registry stores:

```text
file_manifest_path
manifest_sha256
file_count
total_bytes
```

This allows later verification that a copy of a source release is byte-for-byte identical to the registered version.

A manifest verifies **file identity**, not scientific correctness or provenance. Those require separate review.

---

## Controlled vocabularies

Registry fields with defined legal values should use either:

- a small inline enum in the dictionary; or
- a maintained vocabulary in `vocab/`.

Vocabulary files use the common schema represented by `registry--vocab-schema.csv`.

Examples include:

```text
release-status.csv
content-domains.csv
role-schema.csv
credit-roles.csv
credit-contribution-degree.csv
```

Machine-readable values are stored using `term_code`.

Human-readable labels and definitions live in the vocabulary.

For intentional multivalue cells, use an **unpadded pipe**:

```text
soil|hydrology|geospatial
```

not:

```text
soil | hydrology | geospatial
```

---

## Null values

The registry distinguishes different kinds of missing information.

```text
blank   not yet assessed / not yet entered during drafting
nap     not applicable
unk     applicable, but unknown after review
none    dictionary instruction meaning null is not permitted
```

Avoid ad hoc values such as:

```text
NA
N/A
NULL
None
-9999
```

Uncertainty should remain explicit rather than being replaced with a plausible guess.

---

## CRediT contributor roles

The registry uses the [CRediT Contributor Role Taxonomy](https://credit.niso.org/) for standardized research-contribution roles.

The canonical 14 CRediT roles are maintained in:

```text
vocab/credit-roles.csv
```

Optional contribution degree values are maintained in:

```text
vocab/credit-contribution-degree.csv
```

with:

```text
lead
equal
supporting
```

The intended party-role design is:

```text
role_assignment_id
dataset_id
release_id
party_id
role_schema
role_code
contribution_degree
role_basis
role_source
notes
```

A role should be assigned based on documented contribution, not merely a person's job title or position.

---

## Registering a dataset

A typical registration workflow is:

1. Gather the source files and documentation.
2. Determine whether the acquisition is a new dataset concept or a new release.
3. Mint required identifiers.
4. Create the release directory.
5. Preserve the source delivery unchanged under `raw/`.
6. Generate a manifest.
7. Draft a packages row.
8. Register any new people or organizations.
9. Add contributor-role assertions where supported.
10. Run validation.
11. Review against source evidence.
12. Commit the registration.

The detailed workflow is documented in the handbook.

---

## Using LLMs for a first pass

LLMs are encouraged as **curation assistants**.

They are useful for:

- reading heterogeneous metadata;
- extracting candidate values;
- comparing documentation to registry fields;
- identifying likely people and organizations;
- summarizing methods;
- identifying missing information;
- checking values against controlled vocabularies;
- preparing a review report.

They are **not** authoritative metadata sources.

When using ChatGPT, Claude, Gemini, Codex, Claude Code, or another LLM:

- provide the registry dictionary;
- provide relevant vocabularies;
- provide the source documentation;
- require evidence for important values;
- prohibit invented metadata;
- distinguish direct evidence from inference;
- preserve unresolved values as `unk`, `nap`, blank, or notes as appropriate;
- review all proposed edits before committing them.

Full copy/paste prompts for chat-based and in-repository workflows are included in:

```text
markdowns/11-llm-assisted-registration.md
```

---

## Command-line tools

Core generic scripts should support the registry workflow.

Typical tools include:

```text
mint_ids.py
manifest.py
validate_registry.py
```

Depending on the project, optional utilities may support:

- Access database extraction;
- field inventories;
- source-schema capture;
- harmonization maps;
- scientific schema validation.

Project-specific extraction or harmonization tools are intentionally kept separate from the minimal lab-wide registry standard.

---

## Documentation

Comprehensive documentation is maintained as a Quarto book under:

```text
markdowns/
```

The handbook includes chapters on:

1. overview;
2. design principles;
3. repository architecture;
4. packages;
5. parties;
6. contributor roles;
7. the registry dictionary;
8. controlled vocabularies;
9. identifiers and manifests;
10. dataset registration;
11. LLM-assisted registration;
12. validation and review;
13. governance and versioning;
14. scripts and automation;
15. a worked example;
16. template readiness.

### Render the handbook

The Quarto project file lives inside `markdowns/`.

Its output directory should be configured as:

```yaml
project:
  type: book
  output-dir: ../docs
```

From the repository root:

```bash
quarto render markdowns --to html
```

or from inside `markdowns/`:

```bash
quarto render --to html
```

Rendered GitHub Pages content is written to:

```text
./docs/
```

---

## Validation

Before committing a completed registration, validation should eventually check:

- exact registry headers;
- required fields;
- permitted null tokens;
- UUID and IID formats;
- release-slug syntax;
- dates;
- enums;
- vocabulary references;
- foreign-key relationships;
- project-relative paths;
- manifest metadata;
- duplicate identifiers;
- conditional contributor-role vocabularies.

Machine validation does not replace human review.

Human review should verify:

- dataset vs. release identity;
- provenance;
- citations;
- dates;
- rights;
- spatial/temporal coverage;
- contributor identity;
- contributor roles;
- scientific accuracy;
- unresolved uncertainty.

---

## File and field naming conventions

### Directories

Use descriptive lowercase names:

```text
registry/
vocab/
data/
scripts/
markdowns/
docs/
```

### Registry filenames

Registry artifacts use a registry namespace plus a semantic name:

```text
registry--packages.csv
registry--parties.csv
registry--party-roles.csv
registry--dictionary.csv
registry--vocab-schema.csv
```

### Vocabulary filenames

Use descriptive lowercase kebab-case:

```text
registry-table-iid.csv
release-status.csv
content-domains.csv
credit-roles.csv
```

### CSV fields

Use lowercase snake_case:

```text
dataset_id
release_slug
content_domains
role_schema
```

### Recorded paths

Use project-relative POSIX paths:

```text
data/nrcs-nasis-ak/nrcs-nasis-ak--ing20260915--r003/...
```

Do not store machine-specific absolute paths.

---

## Development status

This repository is currently in active development toward a stable **v1.0 registry standard**.

Important remaining work includes:

- final migration of legacy identifier field names;
- merging the standardized vocabulary-schema definitions into the canonical dictionary;
- completing the redesigned `party-roles` table;
- removing legacy `role_default` from parties;
- fully wiring CRediT roles into conditional validation;
- deciding whether to adopt a controlled `role-basis` vocabulary;
- updating scripts to the final unnumbered directory structure and filenames;
- testing the template with real end-to-end dataset registrations.

The detailed readiness checklist is maintained in:

```text
markdowns/16-template-readiness.md
```

Until v1.0 is tagged, treat schema changes as deliberate design changes that may require migration.

---

## Governance

The registry is intended to be shared across multiple lab projects.

Changes to **registry contents** and changes to the **registry standard** should be treated differently.

Adding a dataset row is routine registry work.

Changing a standardized column, identifier convention, vocabulary structure, or relationship model is a schema change and should be reviewed before adoption across projects.

Prefer:

1. small explicit changes;
2. version-controlled migrations;
3. deprecation rather than silent deletion;
4. stable identifiers;
5. documented sources;
6. validation before merge.

---

## Guiding principle

The registry is useful only if another researcher can later determine:

- what data entered the project;
- which exact release was used;
- where it came from;
- what rights and restrictions applied;
- what transformations occurred;
- who contributed;
- what controlled terms mean;
- which values remain uncertain;
- and whether the files being used today are the same ones that were originally registered.

The objective is not perfect metadata at the moment of acquisition.

The objective is a **reviewable, traceable, reproducible record that improves over time**.
