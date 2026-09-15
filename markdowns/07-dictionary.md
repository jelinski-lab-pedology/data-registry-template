# The registry dictionary

`registry--dictionary.csv` is the normative field-level specification for the standardized registry.

It answers:

- What columns exist?
- In what order?
- Are they required?
- What physical type is expected?
- How are values constrained?
- Which vocabulary governs a controlled field?
- What does the field mean?

## The dictionary should define everything in `registry/`

The intended standard has dictionary sections for:

```text
packages
parties
party-roles
dictionary
vocab-schema
```

The value of `table_iid` is governed by:

```text
vocab/registry-table-iid.csv
```

This creates a direct one-to-one mapping between standardized registry artifacts and dictionary table identifiers.

## Dictionary field reference

| Field | Required | Type/domain | Meaning |
| --- | --- | --- | --- |
| table_iid | yes | vocab | Canonical registry table/artifact identifier. Governed by `vocab/registry-table-iid.csv`. |
| column_iid | yes | pattern | Exact machine-readable column name as it appears in the CSV header. |
| column_label | yes | free text | Human-readable label for the column. |
| ordinal | yes | integer | One-based column position in the physical CSV. |
| required | yes | enum | Requirement state such as `yes`, `no`, or `conditional`. |
| storage_type | yes | enum | Expected physical/storage type, e.g. string, integer, float, datetime. |
| value_domain_type | yes | enum | How legal values are constrained: `free_text`, `enum`, `vocab`, `range`, or `pattern`. |
| allowed_values | conditional | free text | Inline values, regular expression, or range expression when the constraint is stored directly. |
| vocab_ref | conditional | path/filename | Vocabulary file used when `value_domain_type=vocab`. |
| null_tokens | yes | free text | Allowed null semantics for the field. Registry convention distinguishes blank, `nap`, `unk`, and dictionary-only `none`. |
| description | yes | free text | Normative definition of the field and how it should be interpreted. |
| notes | no | free text | Additional implementation guidance, examples, or caveats. |

## Self-description

The dictionary is self-describing.

Rows where:

```text
table_iid = dictionary
```

define the columns of `registry--dictionary.csv` itself.

This is intentionally recursive: the same mechanism used to define `packages` also defines the dictionary.

## `value_domain_type`

The value-domain type tells validators and curators how to interpret constraints.

### `free_text`

Human-readable prose is permitted.

Use this only when a field genuinely needs unconstrained text.

### `enum`

A small finite list is stored directly in `allowed_values`.

Example:

```text
person|organization
```

### `vocab`

The legal values come from a maintained vocabulary file referenced in `vocab_ref`.

Example:

```text
vocab_ref = release-status.csv
```

### `pattern`

The value must match a defined syntax, usually represented as a regular expression or documented pattern.

Useful for:

- UUID formatting;
- dates;
- IIDs;
- SHA-256 strings;
- release slugs.

### `range`

The value must fall within a numeric or ordinal range.

## Inline lists

When multiple allowed values are encoded in one dictionary cell, use an **unpadded pipe**:

```text
yes|no|conditional
```

not:

```text
yes | no | conditional
```

This convention is also used for intentionally multivalued registry cells where the schema allows them.

## Null semantics

The registry distinguishes several states.

### blank

Not yet assessed, not yet entered, or temporarily unresolved during drafting.

Blank should generally disappear from fields that are required before registration is complete.

### `nap`

Not applicable.

Example: a DOI field for a locally created dataset that has never had a DOI.

### `unk`

Applicable, but unknown after review.

Example: publication date known to exist but not recoverable from available documentation.

### `none`

Used in the dictionary to mean that a field is not permitted to be null.

Do not use ad hoc null strings such as:

```text
NA
N/A
NULL
None
-9999
```

## Changing the dictionary

Changing the dictionary changes the registry standard.

Therefore:

1. propose the change;
2. explain why it is needed;
3. update the dictionary;
4. update the physical CSV header/template;
5. update relevant vocabularies;
6. update validation;
7. migrate existing rows if necessary;
8. document the schema change;
9. review before merge.

A dictionary change should never be treated as a casual spreadsheet edit.

## `registry--vocab-schema.csv`

The vocabulary schema is a standardized registry artifact and should therefore be represented in the dictionary under:

```text
table_iid = vocab-schema
```

The 16 vocabulary-field definition rows belong inside the main dictionary. A separate `dictionary--vocab-fields.csv` is useful only as a development fragment and should not be the canonical source once those rows have been merged.
