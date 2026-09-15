# Identifiers, releases, paths, and manifests

This chapter describes the identity and integrity conventions that make the registry reproducible.

## Two kinds of identifiers

### Opaque IDs

Opaque `*_id` fields are primarily for machine relationships.

The target conventions are:

```text
dataset_id        UUIDv4
party_id          UUIDv4
role_assignment_id UUIDv4
release_id        UUIDv7
```

UUID versions are implementation choices documented by the standard; the UUID type does not belong in the column name.

### Human-readable IIDs

Human-readable immutable identifiers use the `_iid` suffix.

Examples:

```text
ds_iid     = blm-aim
party_iid  = njelinski
```

IIDs use lowercase kebab-case and should remain stable.

## Why both?

Opaque IDs are robust relationship keys.

Readable IIDs are easier for humans to navigate, type, search, and recognize.

The registry intentionally uses both rather than forcing one identifier to do both jobs.

## Release slugs

A release slug combines:

- dataset IID;
- ingest date;
- release sequence.

Pattern:

```text
{ds_iid}--ing{YYYYMMDD}--r{NNN}
```

Example:

```text
blm-aim--ing20260914--r003
```

The double dash separates semantic components. Internal word separators use a single hyphen.

## Release sequence

`r001`, `r002`, etc. are local release counters.

They are not intended to reproduce a source repository's version numbering. Source versions belong in the relevant repository/version fields.

## UUIDv7 release IDs

UUIDv7 provides a time-sortable identifier.

The current minting approach embeds the delivery/ingest day in the UUIDv7 timestamp. The readable release slug remains the authoritative human sequence, especially when multiple releases are registered on the same day.

## Project-relative paths

Paths recorded in registry metadata should be:

- relative to the project root;
- POSIX-style with `/`;
- independent of a particular user's workstation.

Good:

```text
data/blm-aim/blm-aim--ing20260914--r003/blm-aim--ing20260914--r003.sha256
```

Bad:

```text
/Users/nic/Desktop/project/data/...
C:\Users\someone\project\data\...
```

Absolute local paths make a registry non-portable.

## Raw release layout

Recommended layout:

```text
data/
└── blm-aim/
    └── blm-aim--ing20260914--r003/
        ├── raw/
        ├── extracted/
        ├── reference/
        └── blm-aim--ing20260914--r003.sha256
```

## SHA-256 manifest

The manifest contains one deterministic line per included file:

```text
<sha256>  <relative/path/inside/raw>
```

The entries are sorted by path.

A cryptographic hash changes when file content changes, making the manifest a strong way to detect whether a supposedly identical release has been altered.

## What the integrity fields mean

### `file_manifest_path`

Where the manifest is located, relative to the project root.

### `manifest_sha256`

SHA-256 digest of the manifest itself.

If two parties have the same manifest digest, the manifest contents are byte-for-byte identical.

### `file_count`

Number of files represented.

### `total_bytes`

Combined byte size of the represented files.

## What a manifest does not prove

A manifest proves byte identity, not scientific correctness.

It does not establish that:

- the source was authoritative;
- the files are complete;
- the observations are accurate;
- the license is correct;
- the extraction was scientifically appropriate.

Those questions require provenance and review.

## Verify before transforming

When possible:

1. acquire the release;
2. freeze it under `raw/`;
3. create the manifest;
4. register integrity metadata;
5. only then begin extraction or transformation.

This sequence preserves a defensible baseline.
