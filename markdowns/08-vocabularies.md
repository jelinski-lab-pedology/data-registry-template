# Controlled vocabularies

Controlled vocabularies make legal values explicit and reusable.

## Vocabulary architecture

Every vocabulary CSV in `vocab/` conforms to:

```text
registry/registry--vocab-schema.csv
```

That file contains a header only and no term rows.

Its fields are defined in:

```text
registry/registry--dictionary.csv
```

under:

```text
table_iid = vocab-schema
```

This creates one standardized vocabulary structure for the entire registry.

## Vocabulary field reference

| Field | Required | Type/domain | Meaning |
| --- | --- | --- | --- |
| concept_iid | yes | pattern | Stable identifier for the concept represented by the vocabulary row. Recommended form: `{vocab_iid}--{term_code}`. |
| term_code | yes | pattern | Machine-readable value used in governed registry/data fields. Lowercase kebab-case for local vocabularies. |
| pref_label | yes | free text | Preferred human-readable label. |
| alt_labels | no | multivalue text | Alternative labels, abbreviations, synonyms, or source-specific spellings separated by an unpadded pipe. |
| definition | yes | free text | Definition of the concept. Use canonical wording when adopting an external standard. |
| broader_id | no | concept ID | Immediate broader/parent concept for hierarchical vocabularies. |
| status | yes | enum | Concept lifecycle state, typically `active`, `proposed`, or `deprecated`. |
| created | yes | date | Date the vocabulary row was created, YYYY-MM-DD. |
| modified | yes | date | Date the vocabulary row was last substantively modified, YYYY-MM-DD. |
| scope_note | no | free text | Guidance on when or how the concept should be used. |
| related_ids | no | multivalue IDs | Related local concept identifiers that are associative rather than hierarchical/equivalent. |
| exact_match_ids | no | multivalue IDs/URIs | External identifiers judged to represent the same concept. |
| close_match_ids | no | multivalue IDs/URIs | External identifiers representing closely related but non-identical concepts. |
| replaced_by | conditional | concept ID | Preferred successor when a concept is deprecated. |
| source | yes | free text / citation / URL | Authoritative source for the term or definition. |
| note | no | free text | Curator comments that do not belong in the definition or scope note. |

## Why a common schema?

A vocabulary is more than a list of strings.

The common structure allows the registry to represent:

- stable concept identity;
- machine codes;
- human labels;
- synonyms;
- definitions;
- hierarchy;
- lifecycle state;
- external mappings;
- provenance.

That becomes especially valuable for large scientific classifications and externally maintained standards.

## `concept_iid` vs. `term_code`

These two fields serve different purposes.

### `term_code`

The machine-readable value stored in a governed field.

Example:

```text
data-curation
```

### `concept_iid`

A stable identifier for the vocabulary concept itself.

Recommended local form:

```text
credit-role--data-curation
```

A term code may be readable, but the concept ID makes relationships and mappings more explicit.

## Preferred and alternate labels

`pref_label` is the canonical display label.

`alt_labels` can contain synonyms, abbreviations, older labels, or source-specific variants.

Multiple alternative labels use an unpadded pipe:

```text
data management|research data curation
```

Alternative labels do not become additional legal term codes unless the vocabulary explicitly creates them as distinct concepts.

## Definitions and sources

For an externally maintained standard such as CRediT:

- preserve the canonical preferred label;
- preserve or accurately reproduce the canonical definition;
- cite the canonical source in `source`;
- keep local implementation details in `scope_note` or `note`.

Do not silently rewrite an external standard merely to fit local terminology.

## Hierarchy

`broader_id` allows a vocabulary to represent parent-child relationships.

This is useful for hierarchical concepts such as:

- soil taxonomy;
- geomorphic classifications;
- organizational hierarchies;
- method families.

A flat vocabulary simply leaves `broader_id` empty/not applicable.

## Lifecycle

Terms can evolve.

Use `status` to distinguish:

```text
proposed
active
deprecated
```

When a deprecated term has a direct successor, populate `replaced_by`.

Do not delete a published vocabulary term merely because it is no longer preferred; historical data may still contain its code.

## Mapping to external vocabularies

`exact_match_ids` and `close_match_ids` allow local concepts to be linked to external identifiers.

Use exact matches conservatively. "Looks similar" is not the same as semantic equivalence.

## Current core vocabularies

The registry currently anticipates at least:

```text
registry-table-iid.csv
content-domains.csv
release-status.csv
role-schema.csv
credit-roles.csv
credit-contribution-degree.csv
```

Additional vocabularies should be created only when a controlled field actually requires them.

## `registry-table-iid.csv`

This vocabulary defines the standardized registry table identifiers.

The intended terms are:

```text
packages
parties
party-roles
dictionary
vocab-schema
```

These correspond to the five canonical CSV artifacts in `registry/`.

## Creating a new vocabulary

1. Copy the header from `registry--vocab-schema.csv`.
2. Choose a descriptive kebab-case filename.
3. Define the legal `term_code` values.
4. Create stable `concept_iid` values.
5. Add preferred labels and definitions.
6. Record the source.
7. Add hierarchy/mappings only when supported.
8. Reference the vocabulary from the relevant dictionary row using `vocab_ref`.
9. Update validation if special conditional rules are required.
10. Review the vocabulary before it becomes authoritative.
