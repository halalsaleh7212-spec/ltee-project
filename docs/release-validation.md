# Lesson 12 release readiness

Status: release preparation in progress; no Zenodo DOI has been issued for
this project. A classmate's reproduce report is still pending.

The production Zenodo connection to GitHub was approved on 2026-11-25, and
archiving is enabled for the public `halalsaleh7212-spec/ltee-project`
repository. Sandbox archiving practice and publication of the tested release
are still pending. `CITATION.cff` is prepared with the intended release date
2026-11-25; confirm that date immediately before publication and update it if
publication occurs on a later date. This preparation does not establish that
the release or archive has been published.

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

## Native Linux checks

On 2026-11-25, all four GitHub checks at commit
`2abdb89957b58f3a2476a1012d32b56324c053de` completed successfully:

| Trigger | Check | Result |
| --- | --- | --- |
| Pull request | [Direct Pixi reproduction](https://github.com/halalsaleh7212-spec/ltee-project/actions/runs/45496326076/job/138807693237) | Passed |
| Pull request | [Container reproduction](https://github.com/halalsaleh7212-spec/ltee-project/actions/runs/45496326076/job/138807692874) | Passed |
| Branch push | [Direct Pixi reproduction](https://github.com/halalsaleh7212-spec/ltee-project/actions/runs/45496313679/job/138807647455) | Passed |
| Branch push | [Container reproduction](https://github.com/halalsaleh7212-spec/ltee-project/actions/runs/45496313679/job/138807647162) | Passed |

The direct jobs installed the locked environment, validated `CITATION.cff`,
ran `pixi run reproduce` and `pixi run compare-workflows`, and checked that
committed files did not change. The container jobs independently built the
pipeline environment on native amd64 Linux, downloaded the checksum-verified
inputs, completed Snakemake and Nextflow, compared exact variant records,
confirmed counts of 25/775/10, rendered HTML and PDF, and checked that committed
files did not change. Results and reports were saved as seven-day workflow
artifacts; the container artifacts also include build/run logs and image
inspection metadata.

The CI images were rebuilt from the same Dockerfile, manifest, and lockfile as
the saved release image. CI did not load the Mac-built archive or validate its
exact image ID. The successful native rendering and the earlier Mac-emulation
limitation are distinguished in [container validation](containers.md).
These automated checks do not replace the classmate reproduction exercise.

## Missing-file exercise

Two disposable clones demonstrated the lesson's untracked-helper failure.
`scripts/settings.py` existed only in the first clone, and Git marked it
untracked. A new clone did not contain it and `ls` failed as expected.
Only the disposable exercise folders were removed afterward.

## Before submission

- Complete the real classmate exchange and address any findings; use the
  [reproduce-report template](reproduce-report-template.md).
- Preserve the saved, checksum-verified container archive and its provenance
  for the release. Its workflows match the trusted VCFs; a fresh native Linux
  image built from the same specification also passed both workflows and
  HTML/PDF rendering. See [container validation](containers.md) for the
  distinction between the archived image and the CI rebuilds.
- Complete the manual Zenodo Sandbox archiving practice. Production
  repository archiving is already enabled.
- Confirm that `CITATION.cff` records the actual publication date, publish
  the tested `v1.0.0` revision, verify the resulting archive, then add its
  real DOI and badge.
- Recheck the released version and submit the repository URL and DOI.

Source: [CBIO7501 Lesson 12](https://khanlab.bio/cbio7501-f26/pages/12-putting-it-together.html).
