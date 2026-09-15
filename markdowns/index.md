# Lab Data Registry

The **Lab Data Registry** is a standardized, machine-readable system for documenting datasets that enter research projects in the lab. Its purpose is to make the identity, provenance, content, rights, integrity, and human contributions associated with a dataset explicit **before** the data are harmonized, analyzed, or transformed.

The registry is designed for projects that combine heterogeneous data from multiple sources. Each project can maintain its own populated registry while using the same shared structure, conventions, vocabularies, identifiers, and validation rules.

::: {.callout-important}
The registry CSV files are the **system of record**. This documentation explains the system, but rendered documentation is not authoritative metadata. When the documentation and the registry disagree, the registry specification and versioned schema must be reconciled explicitly.
:::

## What the registry contains

The core registry consists of five standardized CSV artifacts in `registry/`:

1. `registry--packages.csv` — one row per acquired dataset release or snapshot.
2. `registry--parties.csv` — one row per person or organization that must be referenced.
3. `registry--party-roles.csv` — one row per contributor-role assertion.
4. `registry--dictionary.csv` — the field-level specification for every standardized registry CSV.
5. `registry--vocab-schema.csv` — an empty header-only template that defines the physical structure required for controlled-vocabulary CSVs.

Controlled vocabularies live in `vocab/`. The lab glossary is maintained separately in its own repository.

## Start here

If you are new to the registry:

- Read [Overview](01-overview.md).
- Read [Design principles](02-design-principles.md).
- Review the [repository architecture](03-repository-architecture.md).
- Follow [Registering a dataset](10-registering-a-dataset.md).
- If you are using an LLM for the first pass, use the prompts in [LLM-assisted registration](11-llm-assisted-registration.md).
- Before merging changes, complete [Validation and review](12-validation-review.md).

## Core idea in one sentence

> Register the dataset you actually received, preserve its raw bytes, document what it is and where it came from, identify the people and organizations involved, record what they contributed, and make every controlled term and field definition explicit.

## Documentation scope

This book documents the **registry standard and workflow**. It does not define project-specific scientific schemas such as soil pedon/horizon tables, vegetation observations, laboratory tables, model outputs, or harmonized analysis products. Projects may document those with the same principles, but they remain project-specific.

The shared **data-management glossary** is intentionally outside this repository so it can evolve as a lab-wide resource used by multiple registry implementations.
