# Migration notes from current JLDR / AKSDB examples

The attached examples contain naming drift from ongoing design work. The lab-wide template resolves it as follows:

| Current/example name | Standard name | Rationale |
|---|---|---|
| `ds_id_uuidv4` / `dataset_id` | `dataset_id` | Type belongs in the dictionary, not the column name. |
| `release_id_uuidv7` / `release_id` | `release_id` | Same principle. |
| `party_uuidv4` | `party_id` | Consistent opaque-ID convention. |
| `party_slug` / `party_iid` / `party_id` used as a slug | `party_iid` | `_iid` consistently means human-readable immutable identifier. |
| `eml_packageId` | `eml_package_id` | All registry headers use snake_case. |
| spaced inline enums such as `yes | no` | `yes|no` | Pipe lists have no padding. |

Do not silently rewrite an established project registry. Treat migration as a versioned schema change and update scripts/validation at the same time.
