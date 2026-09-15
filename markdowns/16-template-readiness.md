# Template readiness and remaining implementation work

This chapter tracks the gap between the intended registry standard documented in this book and the current files that have evolved from AKSDB/JLDR prototypes.

It should be reviewed before the template repository is tagged as a stable release.

## Architecture decisions already made

The intended standard is now:

- no numeric prefixes on top-level directories;
- `registry/`, `vocab/`, `data/`, `scripts/`, `docs/`;
- glossary moved to a separate repository;
- five canonical registry CSV artifacts;
- one common vocabulary schema;
- dictionary as the field-level specification for everything in `registry/`.

## Reported/created changes

These have been discussed or created during the registry design process:

- [x] Remove numeric prefixes from registry/vocab directories.
- [x] Rename `table-iid.csv` to `registry-table-iid.csv`.
- [x] Create `registry--vocab-schema.csv` as a header-only schema file.
- [x] Define a rich common vocabulary structure.
- [x] Create draft CRediT role vocabulary.
- [x] Create draft CRediT contribution-degree vocabulary.
- [x] Decide to maintain the glossary in a separate repository.
- [x] Decide that one party-role row should represent one role assertion.

::: {.callout-note}
Items marked complete above reflect design decisions and generated artifacts from the workshop preparation. Confirm that the corresponding files have actually been committed to the local repository before treating them as implemented.
:::

## Registry/dictionary updates still needed

- [ ] Merge the 16 vocabulary-schema dictionary rows into the canonical `registry--dictionary.csv`.
- [ ] Change their `table_iid` from legacy `vocab` to `vocab-schema`.
- [ ] Update the dictionary's `table_iid` vocab reference to `registry-table-iid.csv`.
- [ ] Ensure `registry-table-iid.csv` contains exactly the canonical registry artifact identifiers:
  - `packages`
  - `parties`
  - `party-roles`
  - `dictionary`
  - `vocab-schema`
- [ ] Normalize `null_values` / `null_tokens` to the chosen canonical field name `null_tokens`.

## Identifier naming cleanup still needed

The prototype files contain naming drift. The intended v1 convention is:

```text
ds_id_uuidv4        -> dataset_id
release_id_uuidv7   -> release_id
party_uuidv4        -> party_id
party_slug/party_id -> party_iid where the value is a readable IID
eml_packageId       -> eml_package_id
```

Before v1:

- [ ] Update physical CSV headers.
- [ ] Update dictionary rows.
- [ ] Update scripts.
- [ ] Migrate existing registry records deliberately.
- [ ] Update validation.
- [ ] Document the schema migration.

## Parties updates still needed

- [ ] Remove `role_default` from `registry--parties.csv`.
- [ ] Remove `role_default` from the dictionary.
- [ ] Confirm person/organization requiredness rules.
- [ ] Confirm privacy guidance for email fields.

## Party-role redesign still needed

Replace the legacy role table with the target schema:

```text
role_assignment_id
dataset_id
release_id
party_id
role_schema
role_code
contribution_degree
role_basis
role_source
notes
```

Then:

- [ ] Update dictionary rows.
- [ ] Migrate any existing role rows.
- [ ] Add UUID minting for `role_assignment_id`.
- [ ] Update validator foreign-key checks.
- [ ] Implement dataset-level vs. release-level role semantics.
- [ ] Decide and create `role-basis.csv` if adopted.

## CRediT integration still needed

- [ ] Add `credit-roles.csv` to `vocab/`.
- [ ] Add `credit-contribution-degree.csv` to `vocab/`.
- [ ] Ensure `role-schema.csv` contains `credit`.
- [ ] Link the role schema to the correct role vocabulary in validation/configuration.
- [ ] Validate `role_code` conditionally.
- [ ] Validate degree only when appropriate.
- [ ] Preserve canonical CRediT labels/definitions and source URLs.
- [ ] Confirm whether the registry will support DataCite and EML role vocabularies immediately or later.

## File naming cleanup

The final convention should be applied consistently.

Recommended:

```text
registry/
    registry--packages.csv
    registry--parties.csv
    registry--party-roles.csv
    registry--dictionary.csv
    registry--vocab-schema.csv

vocab/
    registry-table-iid.csv
    content-domains.csv
    release-status.csv
    role-schema.csv
    credit-roles.csv
    credit-contribution-degree.csv
```

- [ ] Remove legacy `vocab--` filename prefixes if that is the final decision.
- [ ] Update every `vocab_ref` in the dictionary accordingly.
- [ ] Update scripts that assume old filenames.

## Script updates

- [ ] Remove old numbered-directory assumptions.
- [ ] Update path-resolution code to the final tree.
- [ ] Update `mint_ids.py` field names.
- [ ] Update `validate_registry.py` for the final headers.
- [ ] Add validation for all vocab files against `registry--vocab-schema.csv`.
- [ ] Add conditional role-vocabulary validation.
- [ ] Ensure manifest paths are emitted project-relative rather than absolute.
- [ ] Add manifest verification mode if the lightweight template script does not yet have it.

## Documentation synchronization

Once the CSVs are migrated:

- [ ] Compare every documentation field table against the actual dictionary.
- [ ] Run a documentation link check.
- [ ] Render the Quarto book.
- [ ] Tag the registry template version used by the documentation.

## Definition of “ready for lab use”

The template is ready for broader lab adoption when:

1. the five registry artifacts exist with final headers;
2. the dictionary defines every one of those headers;
3. all core vocabularies conform to `registry--vocab-schema.csv`;
4. CRediT roles are wired into party-role validation;
5. the generic validator passes on a clean template;
6. at least one real dataset has been registered end to end;
7. another lab member can complete a registration using the documentation without relying on undocumented oral instructions.
