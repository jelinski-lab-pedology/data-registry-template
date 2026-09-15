# Registering a dataset

This chapter is the standard end-to-end workflow.

## Before you begin

Gather everything that came with the dataset:

- raw files;
- README files;
- metadata exports;
- database dictionaries;
- source URLs;
- citations;
- emails or handoff notes that contain provenance;
- licenses or data-use conditions;
- documentation naming contributors or organizations.

Do not start by filling cells from memory.

## Step 1: decide whether this is a new dataset or a new release

Ask:

> Does this acquisition represent a new conceptual data resource, or another snapshot/version of a dataset already registered?

If new, mint a new dataset identity.

If it is another release, reuse the existing `dataset_id` and `ds_iid`.

When uncertain, document the uncertainty before minting duplicate concepts.

## Step 2: mint identifiers

For a new dataset:

```bash
python scripts/mint_ids.py dataset my-dataset
```

For a release:

```bash
python scripts/mint_ids.py release   my-dataset   <existing-dataset-id>   --ingest 2026-09-15   --rev 1
```

For a new party:

```bash
python scripts/mint_ids.py party jane-smith
```

Do not ask an LLM to invent UUIDs in prose when the project script is available.

## Step 3: create the release directory

Create:

```text
data/<ds_iid>/<release_slug>/raw/
```

Place an unchanged copy of the acquired release in `raw/`.

Preserve source filenames unless there is a compelling archival reason to wrap the delivery in another container. Renaming raw files can make later source comparison harder.

## Step 4: generate the manifest

Run the project manifest tool.

For example:

```bash
python scripts/manifest.py   data/<ds_iid>/<release_slug>/raw
```

Record the generated integrity fields in the package row.

## Step 5: draft the packages row

Use source evidence to fill:

- description;
- provenance;
- source identifiers;
- dates;
- geographic coverage;
- rights;
- methods;
- processing;
- lineage;
- integrity;
- status.

Use the dictionary while drafting. Do not assume a field's meaning from its name alone.

## Step 6: register parties

Identify people and organizations that need stable references.

Before creating a new party, search `registry--parties.csv` for an existing record.

Add only identity information supported by evidence.

## Step 7: assign roles

For each contributor relationship:

1. determine dataset-level or release-level scope;
2. choose the role schema;
3. choose one valid role code;
4. create one role row;
5. optionally record degree and evidence.

Do not compress several roles into one cell.

## Step 8: run validation

Run:

```bash
python scripts/validate_registry.py
```

Fix machine-detectable errors before requesting human review.

## Step 9: review against the source

A second pass should verify:

- identity;
- release/dataset distinction;
- dates;
- provenance;
- rights;
- citations;
- contributors;
- uncertain values;
- manifest information.

## Step 10: commit the registration

Commit the registry changes, vocab changes if any, manifests, and any new scripts or documentation together when they represent one logical registration event.

A useful commit message is specific:

```text
Register BLM AIM release ing20260915 r003
```

## Registration is not harmonization

Do not delay registration until scientific cleaning is complete.

The registry should capture the acquisition **before** the messy work of schema harmonization begins. Later processing can be documented incrementally while preserving the original source context.
