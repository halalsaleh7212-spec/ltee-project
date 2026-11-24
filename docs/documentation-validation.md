# Documentation validation

Completed on 2026-11-25 for CBIO7501 Lesson 11.

- The README answers the seven reader questions: purpose, source publication,
  contents, hardware, reproduction commands, outputs, and contact.
- `CONTRIBUTING.md` describes issues, branches, reproduction checks, pull
  requests, and reproducibility conventions. `CODE_OF_CONDUCT.md` links the
  Contributor Covenant 3.0 and gives the maintainer's existing public email
  as the private reporting contact.
- `pixi exec cffconvert --validate -i CITATION.cff` passed schema 1.2.0.
- `cffconvert -f apalike` and `-f bibtex` successfully generated citations.
- The break-it exercise used a disposable copy with an ORCID missing its URL
  prefix. Validation rejected it with exit code 1. The real citation file
  remained valid and contains no unprovided ORCID or project DOI.
- The GitHub Reproduce workflow now validates the citation before rebuilding
  the analysis and comparing Snakemake with Nextflow.
- Software versions were exported using `pixi list -e pipeline --explicit`.
  The full lockfile remains the package/checksum record for each platform.
- The Snakemake rule graph was generated with `--rulegraph`, rendered with
  Graphviz, and visually inspected. Local documentation links were checked.
- Hardware and runtime measurements are recorded in `resources.md`; the
  benchmark completed all 49 Snakemake jobs from fresh processed/output folders.

## Finding a tool version

For the lesson question about which samtools version was used, consult
`../pixi.lock` and `software-versions.txt` at the same Git revision as the
analysis. The recorded version is samtools 1.25. The report additionally
prints the Python, pandas, and matplotlib versions used to render its figures.
