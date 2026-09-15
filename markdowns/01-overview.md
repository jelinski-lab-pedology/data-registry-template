# Overview

## Why a dataset registry?

Research projects often accumulate data in ways that are understandable at the moment of acquisition but difficult to reconstruct later. Files arrive by email, download, shared drive, collaborator handoff, API export, database extract, or legacy archive. Names change. A source may be downloaded more than once. A later release may partly overlap an earlier release. The people who collected or curated the data can disappear from the visible provenance chain once a consolidated dataset is created.

The Lab Data Registry is intended to prevent those problems by requiring a small amount of structured documentation at the point where data enter a project.

The registry answers four foundational questions:

1. **What did we receive?**
2. **Which exact release or snapshot did we use?**
3. **Where did it come from and what are the conditions on its use?**
4. **Who contributed to it, and in what role?**

A fifth component—the registry dictionary—makes the registry itself interpretable by defining the meaning and legal values of every standardized field.

## What is being registered?

The primary object is an **acquired dataset release**.

A dataset is a conceptual data resource that can persist through time. A release is a specific delivered, downloaded, exported, or frozen snapshot of that dataset.

For example, a statewide monitoring dataset downloaded in 2024 and downloaded again in 2026 may be the same dataset concept but two different releases. They should share a stable `dataset_id` and `ds_iid` while receiving distinct `release_id` and `release_slug` values.

This distinction is central to the registry.

## What the registry is not

The registry is not:

- a replacement for the raw data;
- a scientific data model for every project;
- a general-purpose database management system;
- a prose README that happens to list datasets;
- a publication bibliography;
- a substitute for repository metadata such as EML or DataCite;
- a guarantee that all metadata are correct merely because a row exists.

The registry is a structured local record that connects those resources and makes the acquisition and curation process auditable.

## Registry vs. scientific schema

The registry operates primarily at the **dataset/release level**.

A project-specific scientific schema describes the structure of the actual research data: for example pedons, horizons, soil samples, vegetation observations, laboratory results, rasters, or model predictions.

Those two concerns should not be conflated.

A project may use the registry to record an acquired geodatabase, then separately inventory hundreds of fields and map them into a harmonized soil schema. The registry records the acquired package and its provenance; the project schema records how scientific observations are represented.

## Registry vs. glossary

The registry dictionary defines fields such as `release_status`, `dataset_id`, or `source_citation`.

The separate lab glossary defines broader concepts such as *dataset*, *release*, *metadata*, *registry*, *schema*, and *controlled vocabulary*. The glossary is a human knowledge resource shared across projects; the registry is a machine-readable metadata system instantiated separately within each project.

## Intended users

The standard is designed for:

- graduate and undergraduate researchers;
- principal investigators;
- data curators;
- collaborators preparing datasets for integration;
- future lab members who were not present when the data were acquired;
- computational tools and LLMs that need an explicit, inspectable schema.

The system should be usable by a person editing CSV files directly, but structured enough to support validation and automation.
