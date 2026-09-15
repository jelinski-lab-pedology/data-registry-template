# Parties: people and organizations

`registry--parties.csv` gives stable identities to the people and organizations referenced elsewhere in the registry.

## Why parties are separate

A person's identity is not the same thing as their contribution.

For example, a person may be:

- a field investigator for one dataset;
- a curator for another;
- an author or data manager for a third;
- a supervisor at the dataset level but not involved in a particular release.

The parties table therefore answers:

> Who is this?

The party-roles table answers:

> What did this party do, for which dataset or release?

## Target field reference

| Field | Required | Type/domain | Meaning |
| --- | --- | --- | --- |
| party_id | yes | string / UUIDv4 | Stable opaque identifier for a person or organization. |
| party_iid | yes | string / IID | Stable human-readable identifier in lowercase kebab-case; immutable and never reused. |
| type | yes | enum | Whether the party is a `person` or `organization`. |
| given_name | conditional | free text | Given name for a person. |
| middle_name | no | free text | Middle name or initials for a person. |
| surname | conditional | free text | Surname/family name for a person. |
| org_name | conditional | free text | Official or preferred organization name when the party is an organization. |
| email | no | free text | Contact email when appropriate to record and share. |
| orcid | no | ORCID pattern | ORCID identifier for a person when available. |
| organization | no | free text | Primary affiliation or organization for a person, when useful. |
| notes | no | free text | Identity clarification, alternate forms, affiliation caveats, or other curation notes. |

::: {.callout-note}
The intended v1 schema removes `role_default`. Roles should not be treated as intrinsic properties of a party; context-specific contribution belongs in `registry--party-roles.csv`.
:::

## Person records

For a person:

- `type=person`;
- use the person's preferred or documented name form;
- record ORCID when known and appropriate;
- use `organization` for affiliation if useful;
- use notes to document ambiguous identity, name variants, or uncertain affiliation.

Do not fabricate middle names, email addresses, ORCIDs, or institutional affiliations.

## Organization records

For an organization:

- `type=organization`;
- populate `org_name`;
- leave person-name fields not applicable according to the registry null convention;
- create a stable `party_id` and `party_iid` just as for a person.

Organizations may themselves have roles in relation to datasets.

## `party_id` and `party_iid`

`party_id` is the stable opaque identifier used for relationships.

`party_iid` is the readable immutable identifier.

Good IIDs are:

- lowercase;
- short but recognizable;
- kebab-case;
- stable even if a person's affiliation changes.

Examples:

```text
njelinski
clping
alaska-center-conservation-science
usda-nrcs
```

An IID is not intended to store a person's current job title or organization.

## Duplicate prevention

Before creating a party, search existing party records.

The same person should not receive separate identities merely because:

- their name is rendered differently in different publications;
- one source uses initials and another uses the full name;
- their affiliation changes;
- one source includes an ORCID and another does not.

If two records may represent the same person but the evidence is uncertain, keep the uncertainty visible rather than merging aggressively.

## Privacy and appropriateness

The registry should contain only contact/identity information that is appropriate for the research context.

An email address is optional. Public persistent identifiers such as ORCID are generally preferable for long-term identity resolution when available.
