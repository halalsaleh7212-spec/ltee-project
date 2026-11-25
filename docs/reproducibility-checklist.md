# Reproducibility checklist

Copy this checklist for the next project. Record the date, exact commit and
evidence beside each item when using it.

## Before starting

- [ ] Define the question, repository, platforms and data-access plan.
- [ ] Record source identifiers, formats, storage, permissions and licenses.

For this project, use the [README](../README.md),
[folder guide](structure.md) and [source metadata](../metadata/sources.tsv).
The analysis uses subsampled public sequencing reads, not a complete inventory
of mutations. Retain the exact figshare version and reference accession.

## During the project

- [ ] Verify scripted downloads and preserve the raw input.
- [ ] Commit tools and lockfile together; track configuration and decisions.
- [ ] Generate results and reports with code; review small changes and run CI.

Keep shared settings in [config/config.yaml](../config/config.yaml) and
explanations in [decisions.md](decisions.md). Check equivalent Snakemake and
Nextflow variant records with `pixi run compare-workflows`. Keep generated
results and environments out of Git, while committing every required script.

## At submission

- [ ] Validate the documented procedure, citation and licenses from a fresh clone.
- [ ] Exchange with a classmate; record findings, discuss them and fix problems.
- [ ] Publish the appropriate release and link its evidence and artifacts.

Use the [README](../README.md) commands, then check `git status --short` and
current Reproduce checks. Validate citation syntax with
`pixi exec cffconvert --validate -i CITATION.cff`. The default depth should yield
10, 25 and 775 variants for SRR2589044, SRR2584863 and SRR2584866 respectively;
compare complete variant records, not just counts. Inspect HTML, PDF and MultiQC.

The classmate exchange remains pending. Use the
[peer report template](reproduce-report-template.md) to record actual commands,
timing, full errors and undocumented steps in an issue. The course prioritizes
the capstone exchange; LTEE can also be exchanged if time permits.

For LTEE submission, provide the GitHub repository and real release DOI.
Follow [release validation](release-validation.md) for current archive status;
a reserved DOI or Sandbox test DOI is not evidence of a published deposit.
Link the source data identifiers, released code, saved container and rendered
report, with checksums and provenance for archived files.

The code's MIT license does not relicense external data or container software.
Original report text and figures are CC BY 4.0; the figshare read subset is CC0.
The saved image supplies the software environment, with code and data mounted
separately. Preserve the precise verification limits in
[container documentation](containers.md) when describing that image.

## After publication

- [ ] Keep released environments; address issues through documented new versions.

Retain `pixi.lock`, the saved image, source checksums and release provenance.
Identify the affected release when correcting results; publish a new release
and version DOI rather than silently changing an archived analysis.

Phase structure adapted from [CBIO7501 Lesson 12](https://khanlab.bio/cbio7501-f26/pages/12-putting-it-together.html),
CC BY 4.0; project-specific guidance added here.
