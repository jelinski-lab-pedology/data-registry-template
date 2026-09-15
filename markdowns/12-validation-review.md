# Validation and review

Registry quality depends on both machine validation and human review.

Neither is sufficient alone.

## Machine validation

The validator should eventually check at least:

### Structure

- exact header order against the dictionary;
- no missing or extra columns;
- UTF-8 encoding;
- expected CSV dialect;
- no duplicated primary identifiers.

### Requiredness

- required fields populated;
- illegal null tokens rejected;
- conditional fields checked where machine rules are possible.

### Patterns and types

- UUID validity;
- IID syntax;
- release-slug syntax;
- ISO date formatting;
- SHA-256 length/characters;
- integers/floats parsed correctly.

### Controlled values

- enum values belong to the inline allowed list;
- vocabulary values exist as active or historically valid `term_code` values;
- registry table identifiers exist in `registry-table-iid.csv`.

### Referential integrity

- party-role `dataset_id` exists;
- release-specific role `release_id` exists and belongs to the stated dataset;
- `party_id` exists;
- `broader_id`, `related_ids`, and `replaced_by` refer to valid concepts where applicable.

### File integrity

- manifest path exists;
- recorded manifest path follows convention;
- manifest hash matches;
- optional full manifest verification passes;
- paths are project-relative, not absolute.

## Conditional role validation

Party roles require richer validation because the legal `role_code` depends on `role_schema`.

Example:

```text
role_schema=credit
```

should trigger validation against:

```text
vocab/credit-roles.csv
```

and, if populated, contribution degree should be checked against:

```text
vocab/credit-contribution-degree.csv
```

This is a planned enhancement to the generic validator.

## Human review

Human review must consider things a validator cannot reliably determine.

### Identity review

- Is this really a new dataset?
- Is the party already registered under another name?
- Does this release overlap but not descend from an earlier release?

### Provenance review

- Is the source organization correct?
- Is the citation faithful to the source?
- Did a collaborator provide files that originated elsewhere?

### Rights review

- Is the stated license actually attached to this dataset?
- Are there redistribution restrictions?
- Does an agency permission apply only to certain subsets?

### Contributor review

- Is the CRediT role supported by evidence?
- Is the role dataset-level or release-specific?
- Are field collectors and curators being made visible rather than erased?

### Scientific review

- Does the abstract accurately describe what is in the files?
- Are spatial and temporal coverage statements defensible?
- Is the processing summary technically accurate?

## Suggested review checklist

Before changing `release_status` to a completed/registered state:

- [ ] Dataset vs. release decision reviewed.
- [ ] Required IDs minted by the project script.
- [ ] Raw acquisition preserved unchanged.
- [ ] Manifest generated.
- [ ] Required package fields reviewed.
- [ ] Source citation/provenance reviewed.
- [ ] Rights reviewed.
- [ ] Parties deduplicated.
- [ ] Party roles supported by evidence.
- [ ] Controlled values validated.
- [ ] Paths are portable/project-relative.
- [ ] Uncertainties documented.
- [ ] Validator passes.
- [ ] Another person or a deliberate second-pass review has inspected the entry.

## Errors vs. warnings

Validators should distinguish:

### Errors

Conditions that violate the registry standard.

Examples:

- missing required ID;
- invalid controlled value;
- broken foreign key;
- malformed release slug;
- header inconsistent with dictionary.

### Warnings

Conditions that may be valid but deserve attention.

Examples:

- a release has no DOI;
- a rights field is `unk`;
- a party lacks ORCID;
- temporal coverage is absent because the dataset is timeless/reference-only;
- a release has no public landing page.

Do not turn every incomplete metadata field into an error; that encourages invented values.
