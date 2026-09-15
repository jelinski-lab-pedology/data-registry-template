# Vocabulary schema update

All vocabulary CSVs now use the same 16-column schema:

concept_iid, term_code, pref_label, alt_labels, definition, broader_id,
status, created, modified, scope_note, related_ids, exact_match_ids,
close_match_ids, replaced_by, source, note

Key design rules:
- `concept_iid` is globally unique within the registry system and follows
  `{vocab_iid}--{term_code}`.
- `term_code` is the machine-readable value stored in governed fields.
- Multivalued metadata fields use an unpadded pipe (`a|b|c`).
- External standards retain their canonical labels/definitions in the vocabulary;
  local machine-readable term codes do not replace the canonical wording.
- `dictionary--vocab-fields.csv` contains the 16 dictionary rows that define the
  shared vocabulary artifact schema.
- `vocab--table-iid.csv` now includes `vocab`, making the dictionary able to
  identify vocabulary files as a standard artifact type.
- `jldr--dictionary--vocab-updated.csv` is the existing JLDR dictionary with the
  vocab schema aligned, `null_values` normalized to `null_tokens`, and the current
  vocab references wired to the standardized filenames.
