# Packages: datasets and releases

`registry--packages.csv` is the central dataset-level inventory.

## Row meaning

One row represents **one acquired release or snapshot of one dataset concept**.

This means that repeated releases of the same dataset produce repeated rows with the same:

- `dataset_id`;
- `ds_iid`;

but different:

- `release_id`;
- `release_slug`;
- release-specific dates, source details, processing notes, and integrity fields.

## Field reference

| Field | Required | Type/domain | Meaning |
| --- | --- | --- | --- |
| dataset_id | yes | string / UUIDv4 | Stable opaque identifier for the dataset concept. Copied unchanged to every release row for that dataset. |
| ds_iid | yes | string / IID | Stable human-readable dataset identifier in lowercase kebab-case. Immutable and never reused. |
| release_id | conditional | string / UUIDv7 | Opaque identifier for a specific acquired release or snapshot. Required for a registered release. |
| release_slug | conditional | string / pattern | Human-readable release identifier: `{ds_iid}--ingYYYYMMDD--rNNN`. |
| title | yes | free text | Human-readable title for this dataset release. Prefer source-provided wording when available. |
| abstract | yes | free text | Concise description of the content and scope of the release. |
| purpose | no | free text | Why the source dataset was created or why it is being incorporated into the project. |
| source_org | yes | free text | Organization primarily responsible for the source delivery or source system. |
| source_citation | yes | free text | Citation or provenance statement describing the source of this release. |
| landing_page_url | no | URL/text | Public or internal landing page for the source dataset when one exists. |
| doi | no | identifier/text | DOI associated with the source dataset or release, if applicable. |
| eml_package_id | no | identifier/text | EML package identifier when the source uses Ecological Metadata Language. |
| repo_scope | no | free text / controlled later | Repository or archive system in which the source object is registered. |
| repo_identifier | no | free text | Identifier assigned by the source repository or archive. |
| repo_revision | no | free text | Revision/version identifier used by the source repository. |
| coverage_start | conditional | date/datetime | Beginning of the temporal coverage represented by the data, when applicable. |
| coverage_end | conditional | date/datetime | End of temporal coverage represented by the data, when applicable. |
| published_date | no | date | Date the source release was published, when known. |
| ingest_date | conditional | date | Date this release entered the local registry/workflow. Drives the readable release slug. |
| geo_description | conditional | free text | Human-readable spatial coverage description. |
| west | no | float | Western longitude/bounding coordinate when a bounding box is useful. |
| east | no | float | Eastern longitude/bounding coordinate. |
| south | no | float | Southern latitude/bounding coordinate. |
| north | no | float | Northern latitude/bounding coordinate. |
| spatial_reference | no | free text | Spatial reference system or coordinate reference description when applicable. |
| content_domains | conditional | vocab / multivalue | High-level content categories governed by `vocab/content-domains.csv`. Multiple values use an unpadded pipe. |
| license | conditional | free text | Formal license governing reuse, if stated. |
| intellectual_rights | conditional | free text | Rights, restrictions, data-sharing conditions, or intellectual-property notes not captured by `license`. |
| methods_summary | conditional | free text | Brief summary of how the source data were collected or generated. |
| processing_summary | conditional | free text | Brief summary of transformations already applied before or during ingest. |
| upstream_release_ids | no | multivalue IDs | Release IDs that are direct ancestors or upstream inputs. Do not use merely to indicate thematic similarity. |
| file_manifest_path | conditional | project-relative path | Path to the release manifest. Use a project-relative POSIX path. |
| manifest_sha256 | conditional | SHA-256 hex | SHA-256 digest of the manifest file itself. |
| file_count | conditional | integer | Number of files represented by the manifest. |
| total_bytes | conditional | integer | Total byte size of all files represented by the manifest. |
| release_status | yes | vocab | Lifecycle/registration status governed by `vocab/release-status.csv`. |
| notes | no | free text | Curator notes, caveats, unresolved issues, and contextual information that do not fit another field. |

## Dataset-level vs. release-level metadata

Some package fields describe the stable conceptual dataset; others may vary by release.

In practice, the packages table intentionally stores both in one release-grained table because a self-contained release row is easier to archive, export, validate, and interpret than a heavily normalized metadata database.

When a value is stable across releases, copy it consistently. When a later release changes scope, rights, source system, processing, or coverage, record the release-specific truth rather than forcing consistency.

## Creating a new dataset concept

Create a new `dataset_id` and `ds_iid` when the source represents a genuinely distinct conceptual dataset.

Do **not** create a new dataset merely because:

- you downloaded it again;
- a new annual release appeared;
- the file format changed;
- the source repository issued a new revision;
- additional files were added to a later snapshot.

Those situations generally indicate a new release of the existing dataset.

## Creating a new release

A new release is appropriate when the actual acquired content has changed or a new source snapshot must be distinguished from the prior one.

Examples:

- annual or periodic source updates;
- a collaborator sends a corrected delivery;
- the source repository republishes a new version;
- you intentionally preserve a later database export;
- the same named resource is acquired at a different time and differs in content.

## Provenance fields

`source_org`, `source_citation`, repository fields, URLs, and identifiers should reflect the source evidence.

Prefer:

1. a source-provided citation;
2. repository metadata;
3. accompanying documentation;
4. a curator-written provenance statement when no formal citation exists.

Do not make a citation look more formal than the evidence supports.

## Temporal coverage vs. acquisition time

Do not confuse:

- `coverage_start` / `coverage_end` — when the observations or represented phenomena occurred;
- `published_date` — when the source release was published;
- `ingest_date` — when this release entered the local workflow.

These dates can be very different.

## Geographic coverage

Use `geo_description` for a human-readable description.

The bounding fields are optional. They are most useful when a simple rectangular extent is meaningful and the coordinates can be supported by the source or a reproducible calculation.

Do not invent a bounding box from a vague place name merely to fill four fields.

## Rights

`license` records a formal license when one exists.

`intellectual_rights` captures broader restrictions or conditions such as:

- redistribution limitations;
- attribution requirements;
- agreements with collaborators;
- source-agency conditions;
- uncertainty about rights.

If rights are unclear, document that uncertainty.

## Methods and processing

`methods_summary` describes how the source data were produced.

`processing_summary` describes what happened to the data before or during acquisition/ingest.

This distinction is useful because a dataset may have been collected with one method, exported through another system, cleaned by a source collaborator, and then locally extracted without altering the original release.

## Lineage

Use `upstream_release_ids` only for actual lineage relationships.

A prior release is not automatically an upstream ancestor. For example, two independent exports from the same external database may overlap without one being derived from the other.

Document ambiguous lineage in `notes`.

## Integrity fields

The four integrity fields are normally script-generated:

- `file_manifest_path`;
- `manifest_sha256`;
- `file_count`;
- `total_bytes`.

Do not hand-calculate them when the manifest script is available.

## Release status

`release_status` is controlled by `vocab/release-status.csv`.

The status vocabulary should express the local registration/curation workflow. A status such as `registered` should have a precise definition—for example, required metadata completed, raw release preserved, manifest generated, and required relationships validated.

## Notes are important

The `notes` field is not a dumping ground, but it is intentionally flexible.

Use it for information that would otherwise be lost, such as:

- partial supersession;
- scope caveats;
- promises of follow-on deliveries that never arrived;
- conflicting dates;
- naming mismatches between source systems;
- unresolved rights questions;
- known limitations that should be revisited during harmonization.
