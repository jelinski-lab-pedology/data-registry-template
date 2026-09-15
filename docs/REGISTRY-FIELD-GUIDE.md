# Registry field guide

The canonical field specification is `registry/registry--dictionary.csv`. This guide explains how humans should think about the tables.

## Packages
A **dataset concept** is stable across time (`dataset_id`, `ds_iid`). A **release** is a particular acquired snapshot (`release_id`, `release_slug`). Therefore, multiple package rows may share `dataset_id` + `ds_iid` but must have distinct release identifiers. Reserve a concept before acquisition only when useful; otherwise create the concept at first acquisition.

Group the remaining package fields mentally into: **description** (title, abstract, purpose); **provenance/discovery** (source organization, citation, landing page, DOI/repository IDs); **coverage** (time and geography); **rights**; **methods/processing**; **lineage** (`upstream_release_ids`); **integrity** (manifest path/hash/count/bytes); and **curation state** (`release_status`).

## Parties and party roles
Register a person or organization once in `parties`. Do not encode a person's job in the identity row as the only record of contribution. Put context-specific contributions in `party-roles`; a single person can have several roles for a release. Prefer established role schemas such as CRediT, DataCite, or EML rather than inventing synonyms.

## Dictionary
The dictionary is self-describing: rows where `table_iid=dictionary` define the dictionary's own columns. A field is constrained by `storage_type` plus `value_domain_type`. Use `enum` for small inline lists, `vocab` for a maintained vocabulary file, `range` for numeric/ordinal bounds, `pattern` for regular-expression/format constraints, and `free_text` only where unconstrained prose is genuinely intended.

## Controlled vocabularies
Use a separate vocabulary file when values need definitions, synonyms, lifecycle state, hierarchy, or are numerous enough that an inline enum becomes difficult to maintain. The starter files intentionally use a compact vocabulary structure; projects can adopt the richer AKSDB concept vocabulary when needed.

## Glossary
The glossary is intentionally *not* another registry table. It is a shared knowledge layer maintained as term cards. Project repos may vendor a snapshot, use a Git submodule/subtree, or link to the shared glossary repository; the lab should designate one canonical source to prevent divergent definitions.
