# Governance and versioning

The registry is a shared standard. It therefore needs rules for change.

## Separate data changes from schema changes

Adding a new package row is a **data change**.

Adding a new column to `registry--packages.csv` is a **schema change**.

Those should not be treated as equivalent Git edits.

Schema changes require broader review because they affect every project using the standard.

## Proposed change workflow

For a schema change:

1. describe the problem;
2. explain why existing fields/vocabularies cannot represent it;
3. propose the smallest change;
4. update the dictionary;
5. update the relevant physical CSV header;
6. update vocabularies;
7. update validation;
8. document migration requirements;
9. test against existing project registries;
10. merge only after review.

## Preserve backward interpretability

Do not silently delete fields or vocabulary terms that have already been used.

If a concept is no longer preferred:

- deprecate it;
- keep its historical definition;
- point to a replacement when appropriate.

If a registry field must be renamed or removed, document the migration and consider a schema version boundary.

## Versioning the registry standard

The lab should tag releases of the template repository.

A practical pattern could be:

```text
v0.x   active design / workshop phase
v1.0   first stable registry standard
v1.x   backward-compatible additions/clarifications
v2.0   intentionally breaking schema changes
```

The exact versioning policy can be formalized later, but tagged states are valuable because project registries can say which template version they implement.

## Git workflow

A lightweight shared workflow is sufficient:

- create a branch for non-trivial schema/vocab changes;
- make changes in small logical commits;
- run validation;
- open a pull request;
- review both the machine-readable change and documentation;
- merge after agreement.

Routine package registrations may use a simpler process depending on the project.

## Vocabulary governance

A vocabulary change should distinguish:

### New concept

Add a new concept with a stable ID and source.

### Label refinement

If meaning is unchanged, update the preferred/alternate label and modification date carefully.

### Meaning change

Do not reuse an existing code for a different concept. Create a new concept and deprecate the old one if necessary.

### External standard update

Document which version/state of the external standard is being followed and preserve the source.

## Roles and attribution

Contributor metadata can be sensitive in a social sense even when not legally sensitive.

Do not assign CRediT roles merely to reward or rank people. Record documented contributions. CRediT itself is a contribution taxonomy and is not intended to define authorship.

## Auditability

Git history, manifests, stable identifiers, and source evidence together create an audit trail.

The goal is not bureaucracy. The goal is to ensure that a future researcher can reconstruct:

- what entered the project;
- when;
- from where;
- in what exact form;
- under what conditions;
- with whose contributions;
- and how the metadata evolved.
