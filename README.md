# Jelinski Lab standardized data-registry starter

This repository is a project template for registering, preserving, documenting, and attributing heterogeneous research datasets before harmonization. It is designed so multiple lab projects can use the same dataset-level registry structure while keeping project-specific scientific schemas separate.

Start with `docs/WORKSHOP-QUICKSTART.md`, then read `docs/ARCHITECTURE.md` and `docs/REGISTRY-FIELD-GUIDE.md`.

## First commands
```bash
python scripts/build_glossary.py
python scripts/validate_registry.py
python scripts/mint_ids.py dataset example-dataset
```

## Canonical rules
1. Registry CSVs are authoritative machine-readable records.
2. Do not edit raw acquired files.
3. One dataset concept may have many releases.
4. Every acquired release gets a SHA-256 manifest.
5. IDs and IIDs are immutable and never reused.
6. Registry columns are standardized by the dictionary.
7. Controlled values are vocabularies, not ad hoc spelling variants.
8. People and organizations are registered separately from their roles.
9. Glossary term cards are shared across projects and compiled automatically.
10. Run validation before merging registry changes.
