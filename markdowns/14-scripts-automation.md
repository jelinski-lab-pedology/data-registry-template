# Scripts and automation

The registry standard is intentionally usable without a database server. Small command-line tools provide repeatable operations around CSV files and filesystem releases.

## Core generic tools

### `mint_ids.py`

Purpose:

- mint dataset IDs/IIDs;
- mint release IDs/slugs;
- mint party IDs/IIDs.

Typical use:

```bash
python scripts/mint_ids.py dataset kenai-wetlands
python scripts/mint_ids.py release kenai-wetlands <dataset-id> --ingest 2026-09-15 --rev 1
python scripts/mint_ids.py party jane-smith
```

IDs should be minted by the tool rather than typed manually.

### `manifest.py`

Purpose:

- walk a frozen raw release;
- compute SHA-256 for each file;
- produce a deterministic manifest;
- report manifest hash, file count, and bytes.

The full production version should record project-relative paths and support verification.

### `validate_registry.py`

Purpose:

- compare CSV headers to the dictionary;
- enforce required fields;
- validate enums and vocabularies;
- check foreign keys;
- enforce path and identifier conventions;
- eventually implement conditional role-schema validation.

Validation should be run before registry changes are merged.

## Optional/source-specific tools

The AKSDB work produced several useful utilities that should be treated as optional tooling rather than mandatory parts of the registry standard.

### `inventory.py`

Profiles fields in extracted CSVs and creates a machine-generated field inventory with type inference and quality flags.

Useful when a project must harmonize large heterogeneous tabular deliveries.

### `extract_mdb.py`

Reproducibly extracts Microsoft Access `.mdb`/`.accdb` deliveries with `mdbtools`, capturing source tables and schema.

Useful only for projects that receive Access databases.

### `extract_props.py`

Recovers Access field descriptions, properties, and query definitions that are not exposed by basic table export.

### `convert_map.py`

Converts legacy wide mapping workbooks into a normalized long-format mapping table.

## Core vs. optional philosophy

The lab standard should avoid requiring every project to inherit the full complexity of the most complicated project.

A good boundary is:

```text
core:
    identity
    packages
    parties
    roles
    vocabularies
    manifests
    validation

optional:
    field inventories
    database extraction
    source-schema capture
    harmonization maps
    scientific schema validation
```

## Running scripts from anywhere

A mature template should include shared path-resolution logic so tools can locate the project root regardless of the current working directory.

Registry paths should always be written relative to the project root.

## Reproducibility

If a manual transformation is repeated more than once, strongly consider turning it into a script.

Examples:

- extracting tables;
- renaming columns;
- fixing encodings;
- creating manifests;
- generating inventories;
- validating vocabularies;
- compiling reports.

The objective is not to automate every judgment. It is to automate repeatable operations so human attention can focus on judgment.
