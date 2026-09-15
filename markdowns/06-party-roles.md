# Party roles and contributor attribution

`registry--party-roles.csv` records the relationship between a party and a dataset or release.

## Fundamental row rule

> **One row = one party × one dataset/release scope × one role assertion.**

Do not store several roles in a pipe-delimited `role_code` cell.

If one contributor performed three CRediT roles, create three rows.

This makes role assertions independently searchable, attributable, reviewable, and citable.

## Target v1 schema

| Field | Required | Type/domain | Meaning |
| --- | --- | --- | --- |
| role_assignment_id | yes | string / UUIDv4 | Stable opaque identifier for this one role assertion. |
| dataset_id | yes | foreign key | Dataset concept to which the contribution applies. |
| release_id | no | foreign key | Specific release to which the contribution applies. Blank means the assertion applies at the dataset level. |
| party_id | yes | foreign key | Person or organization performing the role. |
| role_schema | yes | vocab | Role system being used, e.g. `credit`, `datacite`, `eml`, or a designated local schema. |
| role_code | yes | conditional vocab | Machine-readable role code valid under the selected `role_schema`. One row contains one role. |
| contribution_degree | no | conditional vocab | Optional degree such as CRediT `lead`, `equal`, or `supporting` when supported by the role schema. |
| role_basis | no | vocab / proposed | How the role was established, e.g. declared by source, publication, curator-assigned, or inferred. |
| role_source | no | free text / path / identifier | Citation, URL, file path, or note pointing to the evidence for the role assertion. |
| notes | no | free text | Additional context about the role assertion. |

::: {.callout-warning}
The current legacy party-role CSV and dictionary have not yet been migrated to this target schema. This chapter documents the recommended v1 design. Complete the migration before tagging the registry template as v1.0.
:::

## Dataset-level and release-level contributions

`dataset_id` is always required.

`release_id` is optional:

- blank `release_id` means the role applies to the dataset concept generally;
- populated `release_id` means the role applies specifically to that release.

This avoids a separate `role_scope` field while preserving an important distinction.

## Why IDs rather than readable slugs?

Foreign-key relationships should use stable opaque identifiers:

- `dataset_id`;
- `release_id`;
- `party_id`.

Readable IIDs and slugs are still available in the related tables and can be joined for display.

This avoids duplicating human-readable identifiers throughout relationship tables and reduces the chance that a spelling change breaks referential integrity.

## Role schemas

`role_schema` identifies the controlled role system being used.

Examples may include:

- `credit`;
- `datacite`;
- `eml`;
- a deliberately defined local role schema.

The legal `role_schema` values live in `vocab/role-schema.csv`.

`role_code` must then be validated against the vocabulary associated with that schema.

This is a **conditional vocabulary relationship**.

For example:

```text
role_schema = credit
role_code   = data-curation
```

means that `data-curation` must exist in `vocab/credit-roles.csv`.

## CRediT integration

CRediT is the Contributor Role Taxonomy standardized as ANSI/NISO Z39.104-2022. It defines 14 contributor roles and allows a contributor to hold multiple roles. When multiple contributors share a role, an optional degree of contribution may be specified as `lead`, `equal`, or `supporting`.

The registry should include:

```text
vocab/credit-roles.csv
vocab/credit-contribution-degree.csv
```

The canonical CRediT role vocabulary contains:

- Conceptualization
- Data curation
- Formal analysis
- Funding acquisition
- Investigation
- Methodology
- Project administration
- Resources
- Software
- Supervision
- Validation
- Visualization
- Writing – original draft
- Writing – review & editing

For external standards, preserve canonical preferred labels and definitions in the vocabulary while using a local machine-readable `term_code`.

Canonical references:

- <https://credit.niso.org/>
- <https://credit.niso.org/contributor-roles-defined/>
- <https://credit.niso.org/contributor-roles/>

## Contribution degree

For CRediT, `contribution_degree` may be:

```text
lead
equal
supporting
```

The field is optional. It should not be populated for a role schema that does not support the concept unless the local standard explicitly defines how to interpret it.

## Role evidence

A structured contributor system is much stronger if the source of a role assertion is visible.

The target design therefore includes:

- `role_basis` — how the role was established;
- `role_source` — evidence or reference.

A future `role-basis.csv` vocabulary might include values such as:

```text
source-declared
contributor-declared
publication
curator-assigned
inferred
```

The final terms should be reviewed before the vocabulary is adopted.

## Example

A contributor who led field collection and equally contributed to methodology would receive two rows:

```text
<uuid-1>,<dataset-id>,,<party-id>,credit,investigation,lead,publication,<doi>,...
<uuid-2>,<dataset-id>,,<party-id>,credit,methodology,equal,publication,<doi>,...
```

## What still needs to be implemented for CRediT

Before the template is complete:

1. Place `credit-roles.csv` in `vocab/`.
2. Place `credit-contribution-degree.csv` in `vocab/`.
3. Ensure `role-schema.csv` contains the `credit` term and identifies CRediT as the intended scheme.
4. Update the party-role section of `registry--dictionary.csv` to the target schema.
5. Remove `role_default` from the parties schema.
6. Update validation so `role_code` is checked against the vocabulary associated with `role_schema`.
7. Validate `contribution_degree` against the CRediT degree vocabulary when `role_schema=credit`.
8. Decide whether to adopt a `role-basis.csv` vocabulary.
