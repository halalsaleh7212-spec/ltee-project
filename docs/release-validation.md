# Lesson 12 release readiness

Status: release preparation in progress; no Zenodo DOI has been issued for
this project. A classmate's reproduce report is still pending.

## Independent automated clone check

On 2026-11-25, a new clone of commit
`c9aea8b0236e51461d073c04960e51b9751df9dd` started without project data,
results, or environments. The host Pixi package-download cache could be
reused. Only the README commands were needed.

| Command | Result | Elapsed seconds |
| --- | --- | ---: |
| `pixi install --locked` | Passed | 3.575 |
| `pixi exec cffconvert --validate -i CITATION.cff` | Passed | 0.199 |
| `pixi run reproduce` | Passed; 49 Snakemake jobs and HTML/PDF reports | 157.578 |
| `pixi run compare-workflows` | Passed; 32 Nextflow tasks | 27.023 |
| `git status --porcelain` | Empty | 0.021 |

Seven raw files downloaded, passed provider MD5 and local SHA-256 checks,
and were made read-only. Final records matched exactly: 25 variants for
SRR2584863, 775 for SRR2584866, and 10 for SRR2589044.

The instructor's `assessment/check_capstone.py` passed 19 of 20 automatic
checks. Only the project-release DOI was missing. That script reports
structural evidence; it does not grade scientific interpretation or replace
peer review. The merged base also passed GitHub's Reproduce check.

The supplied ORCID was then added to `CITATION.cff`; schema validation
passed again. Nextflow lint also completed with no errors. These later
metadata checks do not change the workflow results above.

## Missing-file exercise

Two disposable clones demonstrated the lesson's untracked-helper failure.
`scripts/settings.py` existed only in the first clone, and Git marked it
untracked. A new clone did not contain it and `ls` failed as expected.
Only the disposable exercise folders were removed afterward.

## Before submission

- Complete the real classmate exchange and address any findings; use the
  [reproduce-report template](reproduce-report-template.md).
- The current container image is saved and checksum-verified; both container
  workflows match the trusted VCFs. Native Linux container report validation
  is pending because plotting stalled under Mac emulation. See
  [container validation](containers.md). Host-rendered HTML/PDF reports are ready.
- Practise Zenodo archiving in its sandbox, then enable the public LTEE
  repository in the real Zenodo account before publishing the release.
- Set the actual release date in `CITATION.cff`, publish the tested `v1.0.0`
  revision, verify the archive, then add its real DOI and badge.
- Recheck the released version and submit the repository URL and DOI.

Source: [CBIO7501 Lesson 12](https://khanlab.bio/cbio7501-f26/pages/12-putting-it-together.html).
