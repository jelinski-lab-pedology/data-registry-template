# LLM-assisted first-pass registration

LLMs can dramatically reduce the time required to assemble a first-pass registry entry, especially when a release includes multiple documentation files. They should be used as **curation assistants**, not as authorities.

## Core rule

> Extract, infer cautiously, and flag uncertainty. Never fabricate missing metadata to make the row look complete.

An LLM-generated registry row is a draft until reviewed by a person.

## What an LLM should read first

Before analyzing a dataset, provide or direct the agent to:

1. `registry/registry--dictionary.csv`;
2. `registry/registry--packages.csv`;
3. `registry/registry--parties.csv`;
4. `registry/registry--party-roles.csv`;
5. `registry/registry--vocab-schema.csv`;
6. all relevant files in `vocab/`;
7. this documentation;
8. source documentation supplied with the dataset.

This prevents the model from inventing a parallel schema.

## Upload/chat prompt

Use this when working in ChatGPT, Claude, Gemini, or another chat interface where you are uploading the dataset documentation.

```text
I am registering a dataset using our lab's standardized data registry.

Attached are:
1. the source dataset files and/or documentation available to me;
2. registry--dictionary.csv;
3. the current packages, parties, and party-roles CSVs;
4. the relevant vocabularies.

Your job is to prepare a FIRST-PASS registration for human review.

Rules:
- Treat registry--dictionary.csv as authoritative for field meaning and constraints.
- Do not add, remove, rename, or reorder registry columns.
- Do not invent facts that are not supported by the source material.
- Distinguish explicitly among:
  (a) values directly supported by source evidence,
  (b) reasonable inferences,
  (c) unknown or unresolved values.
- Use our null semantics correctly: blank for not-yet-assessed during drafting,
  nap for not applicable, and unk for applicable but unknown after review.
- Use only legal vocabulary term_code values from the supplied vocab files.
- For intentional multivalue cells, use an unpadded pipe: a|b|c.
- Do not create a new dataset concept until you compare the acquisition with
  existing packages rows and determine whether it is a new dataset or a new release.
- Do not invent UUIDs. Tell me which identifiers need to be minted with the project script.
- Do not modify raw source files.
- Preserve source-provided citations, names, identifiers, dates, and rights language as faithfully as possible.
- Flag conflicting evidence rather than silently choosing one source.
- Search the existing parties table before proposing a new party.
- For contributor roles, propose one row per role assertion and use an existing role schema/vocabulary.

Return:
A. A short assessment: new dataset concept or new release, with reasoning.
B. A proposed packages row in exact CSV column order.
C. Proposed new parties, if any.
D. Proposed party-role assertions, if supported.
E. A list of unresolved questions / fields needing human review.
F. A source-evidence table showing where the most important values came from.
G. A list of any vocabulary terms or schema changes you think may be needed. Do not make those changes automatically.
```

## In-repository coding-agent prompt

Use this with Codex, Claude Code, or another agent operating inside the project directory.

```text
You are helping prepare a FIRST-PASS dataset registration in this repository.

Before making any changes:
1. Read the documentation under docs/.
2. Read registry/registry--dictionary.csv.
3. Read all existing registry CSVs.
4. Read registry/registry--vocab-schema.csv and all vocabularies in vocab/.
5. Inspect the source dataset delivery and all accompanying documentation.
6. Inspect the existing packages table to determine whether this is a new dataset
   concept or a new release of an existing dataset.

Rules:
- The registry dictionary is authoritative.
- Never alter files under data/**/raw/.
- Never silently modify registry schemas.
- Never invent metadata.
- Never invent IDs when a project script exists to mint them.
- Use project-relative POSIX paths in registry fields.
- Use legal vocabulary term_code values only.
- One party-role row represents one role assertion.
- Preserve uncertainty and conflicting evidence explicitly.
- Make the smallest set of changes necessary for this one registration.
- Do not "clean up" unrelated registry rows.

Workflow:
A. Produce a written plan and identify whether this is a new dataset or release.
B. Use scripts/mint_ids.py for IDs that genuinely need to be created.
C. Create the standard data/<ds_iid>/<release_slug>/raw/ structure if needed,
   but do not move/delete existing source material without explicit instruction.
D. Generate the manifest with the project manifest tool.
E. Draft/update the packages row.
F. Add parties only if they are not already registered.
G. Add one role row per supported role assertion.
H. Run the registry validator.
I. Show me a diff and a review report before considering the registration complete.

Review report must include:
- evidence used;
- inferred values;
- unresolved fields;
- validation results;
- any proposed vocabulary or schema changes;
- anything you deliberately left untouched.
```

## Review prompt

A second LLM pass can be useful if it is framed as adversarial review rather than rewriting.

```text
Review this proposed registry change against the source materials and the registry dictionary.

Do NOT improve prose merely for style.

Look specifically for:
- unsupported claims;
- invented dates, citations, rights, identifiers, coordinates, or organizations;
- confusion between dataset identity and release identity;
- invalid null tokens;
- invalid vocabulary values;
- multivalue cells using the wrong delimiter;
- contributor roles that are inferred without evidence;
- duplicate parties;
- inconsistent source names;
- lineage claims that are not actually derivational;
- absolute local file paths;
- manifest fields that appear hand-entered rather than script-generated;
- fields whose value conflicts with source documentation.

Return:
1. errors that must be corrected;
2. uncertainties needing human judgment;
3. machine-validation issues;
4. fields that appear well supported;
5. a concise recommendation: accept, revise, or reject the draft.
```

## Evidence discipline

A strong first-pass workflow should preserve a small evidence trail.

For important fields, the LLM should say where the value came from:

| Registry field | Proposed value | Evidence | Confidence |
|---|---|---|---|
| `source_org` | ... | source README | direct |
| `published_date` | ... | repository page | direct |
| `coverage_end` | ... | inferred from latest observation date | inferred |
| `license` | `unk` | no license found | unresolved |

This is especially helpful during workshop registration because it turns review into verification rather than reconstruction.

## What LLMs are good at here

LLMs are well suited to:

- reading heterogeneous documentation;
- consolidating repeated metadata;
- locating candidate citations;
- identifying names and organizations;
- summarizing methods;
- comparing a proposed row to the dictionary;
- spotting missing fields;
- generating review questions.

## What requires caution

LLMs commonly overreach by:

- filling plausible dates;
- treating a website as a formal citation;
- assuming an open website implies an open license;
- inferring organizational affiliation from context;
- confusing data publication date with observation dates;
- treating any earlier release as direct lineage;
- selecting contributor roles from job titles rather than documented contributions.

The prompt should explicitly discourage these behaviors.

## Final rule

An LLM can produce a useful first draft.

A human curator is responsible for deciding that a release is **registered**.
