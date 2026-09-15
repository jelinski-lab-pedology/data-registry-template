# Design principles

The registry is built around a small set of rules. These rules are more important than any individual filename.

## Machine-readable first

Registry CSVs and controlled vocabularies are authoritative machine-readable records. Human-readable documentation may be generated from them, but the rendered documentation is a presentation layer.

This means that a fact is not fully registered merely because it appears in a README or manuscript. Important provenance, identity, rights, status, and attribution information should be represented in the structured registry.

## Dataset identity is distinct from release identity

A dataset concept persists across multiple acquisitions or versions. A release represents one specific snapshot.

Stable dataset identity allows the registry to answer:

> Are these two deliveries versions of the same conceptual dataset?

Release identity allows the registry to answer:

> Are these the exact same bytes or the same specific source snapshot?

Both are necessary.

## Raw acquisitions are immutable

Files placed under a release `raw/` directory should not be edited in place.

If an Access database is exported to CSV, a spreadsheet is cleaned, a geodatabase is normalized, or a text encoding is repaired, that transformation should produce a derived artifact rather than silently altering the source acquisition.

The registry therefore separates **what arrived** from **what we subsequently did to it**.

## Integrity is explicit

Each acquired release should receive a deterministic SHA-256 manifest. The manifest provides a cryptographic fingerprint of the files included in the release.

The registry records:

- the manifest path;
- the SHA-256 of the manifest;
- the file count;
- total bytes.

This allows future users to verify whether a copy of the raw acquisition is exactly the version that was registered.

## Identifiers are stable

Opaque UUIDs and human-readable IIDs serve different purposes.

- `*_id` fields are stable opaque identifiers used for relationships.
- `*_iid` fields are human-readable immutable identifiers used for navigation and interpretation.
- release slugs are readable identifiers for specific acquisitions.

An identifier is never recycled for a different concept.

## People and organizations remain visible

Data integration can unintentionally erase the contributions of field crews, laboratory analysts, database maintainers, curators, and source organizations.

The registry therefore separates:

- **party identity** — who the person or organization is;
- **party role** — what that party did in relation to a dataset or release.

This supports richer attribution than placing a single "owner" or "contact" field on a dataset.

## Controlled values are explicit

If a field accepts a defined set of values, those values should not depend on memory or ad hoc spelling.

Small, stable sets may be stored as inline enums. Larger, reusable, hierarchical, externally standardized, or definition-bearing value sets should be represented as vocabulary CSVs.

## Uncertainty is documented, not hidden

A first-pass registry may contain unknowns. That is acceptable.

The correct response to missing evidence is to record the uncertainty using the registry's null semantics and notes—not to invent a plausible value.

This principle is especially important when LLMs are used to accelerate initial registration.

## Automation assists curation; it does not replace review

LLMs and scripts are encouraged for:

- extracting likely metadata from source documentation;
- profiling files;
- drafting package rows;
- suggesting contributors and roles;
- checking formats;
- generating manifests;
- validating controlled values.

However, the first-pass output must be reviewed by a person who can evaluate source evidence and project context.

## The system should fail visibly

Silent inconsistency is more dangerous than an explicit error.

Validation should detect malformed identifiers, invalid controlled values, orphaned foreign keys, bad paths, missing required fields, and schema drift. When a fact cannot be validated automatically, the documentation should say that human review is required.
