# Worked example

This example demonstrates the full reasoning process using a fictional dataset.

## Scenario

A collaborator sends a folder:

```text
peat-depth-survey-2026/
├── peat_depths.csv
├── site_notes.docx
└── README.txt
```

The README says:

- the data are from a 2026 Kenai Peninsula field campaign;
- Jane Smith led field data collection;
- Alex Lee developed the sampling design;
- the files are an updated delivery replacing a preliminary folder sent two months earlier;
- no DOI exists;
- redistribution is permitted within the collaborative project, but public release has not yet been approved.

A preliminary release is already registered under:

```text
dataset_id = 3e...
ds_iid     = kenai-peat-depths
```

## Step 1: dataset or release?

This is **not** a new dataset concept.

It is an updated release of `kenai-peat-depths`.

Reuse:

```text
dataset_id = 3e...
ds_iid     = kenai-peat-depths
```

Mint a new release.

## Step 2: mint the release

```bash
python scripts/mint_ids.py release   kenai-peat-depths   3e...   --ingest 2026-09-15   --rev 2
```

Suppose the tool returns:

```text
release_id   = <uuidv7>
release_slug = kenai-peat-depths--ing20260915--r002
```

## Step 3: preserve raw files

Create:

```text
data/kenai-peat-depths/kenai-peat-depths--ing20260915--r002/raw/
```

Copy the three supplied files into `raw/` unchanged.

## Step 4: generate manifest

Run:

```bash
python scripts/manifest.py   data/kenai-peat-depths/kenai-peat-depths--ing20260915--r002/raw
```

Record the generated:

- manifest path;
- manifest SHA-256;
- file count;
- total bytes.

## Step 5: package metadata

Potential values include:

```text
title:
Kenai Peninsula peat-depth field survey, 2026 updated delivery

purpose:
Updated field delivery for peat-depth modeling and targeted sampling analysis.

source_org:
<collaborator organization, if documented>

doi:
nap

coverage_start:
2026-...

coverage_end:
2026-...

intellectual_rights:
Collaborative-project redistribution permitted; public release not yet approved.

processing_summary:
Updated delivery superseding the preliminary 2026 handoff; no local transformations applied to raw files.

release_status:
<appropriate current workflow term>
```

Notice that the rights statement is preserved as a condition rather than incorrectly converting it into an open license.

## Step 6: parties

Search the existing parties table for Jane Smith and Alex Lee.

If absent, create new party IDs/IIDs.

Do not add job titles as permanent roles on their identity records.

## Step 7: roles

If using CRediT:

Jane's field contribution supports:

```text
role_schema = credit
role_code   = investigation
```

Alex's sampling-design contribution may support:

```text
role_schema = credit
role_code   = methodology
```

If the README explicitly indicates Jane led the investigation role and multiple investigators exist:

```text
contribution_degree = lead
```

If that ranking is not stated or needed, leave degree unassigned.

Create one row per role assertion.

## Step 8: role evidence

A defensible record might use:

```text
role_basis  = source-declared
role_source = data/kenai-peat-depths/.../raw/README.txt
```

This is preferable to assigning roles solely because a person's job title sounds compatible with a CRediT role.

## Step 9: review uncertainties

Questions for human review might include:

- Does the updated delivery fully supersede the preliminary release?
- What exact temporal coverage dates are present in the CSV?
- Should the dataset-level title remain stable across releases?
- Is the collaborator organization explicitly documented?
- Should rights be encoded as `license=nap` plus a detailed `intellectual_rights` statement?
- Is the preliminary release a direct upstream ancestor or merely an earlier snapshot?

These questions should be resolved explicitly rather than guessed.

## Step 10: validate and commit

Run validation, inspect the diff, and commit the registration.

The result is a release that can later be transformed and harmonized without losing the context of what originally entered the project.
