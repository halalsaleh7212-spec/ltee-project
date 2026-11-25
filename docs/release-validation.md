# Lesson 12 release validation

The tested source release, production Zenodo code archive and companion
container/report archive were published on **2026-11-25**. Manual Zenodo
Sandbox practice was also completed.
The classmate exchange remains pending.

## Published source archive

| Item | Verified value |
| --- | --- |
| GitHub release | [v1.0.0](https://github.com/halalsaleh7212-spec/ltee-project/releases/tag/v1.0.0) |
| Release commit | `96d49a805881da112a8f704d1f3ac91902938fe7` |
| Real version DOI | [10.5281/zenodo.24533293](https://doi.org/10.5281/zenodo.24533293) |
| Public Zenodo record | [24533293](https://zenodo.org/records/24533293) |
| Record title and version | LTEE variant calling; `v1.0.0` |
| Creator and ORCID | Hala Alsaleh; [0009-0005-6882-748X](https://orcid.org/0009-0005-6882-748X) |
| Access and source-code license | Open; MIT |
| ZIP size | 183,603 bytes |
| Provider MD5 | `7a1fd533f0b410d90081347cc654a9f0` |
| Verified SHA-256 | `5c234fb4890686712f193c7bf7fdd606eceadfb4e09280c10253daa684774b0f` |

Verification used public HTTP endpoints without account cookies. The public
record metadata, publication date, source-repository link, license and ORCID
were checked. The source ZIP was downloaded from the record, its size and
provider checksum verified, and each archived file compared with Git's blob
content at the release commit: **all 53 tracked files matched**, with no
missing, additional or changed files.

The annotated Git tag object `2becc87cdc42726266dea00dc796db92f04e8d45`
points to the release commit above. This explains the `2becc87` suffix in the
ZIP's top-level folder. The release is public, not a draft or prerelease.
Its source archive is a fixed snapshot; adding the issued DOI to the current
README and citation metadata does not rewrite that released snapshot.

## Published companion archive

The [companion record](https://zenodo.org/records/24533491), version `1.0.0`,
was published on 2026-11-25 with DOI
[10.5281/zenodo.24533491](https://doi.org/10.5281/zenodo.24533491).
It contains the saved `linux/amd64` image, provenance JSON, HTML/PDF analysis
reports, MultiQC report, validation evidence ZIP, README and checksum manifest.

Public API verification confirmed publication and open access, Hala Alsaleh's
name and ORCID, the license statement, and the `IsSupplementTo` relation to
software DOI `10.5281/zenodo.24533293`. All **eight file names, byte sizes and
provider MD5 checksums** matched the local upload manifest, totaling
**1,167,193,033 bytes**. Download verification and saved-image use are documented
in [container instructions](containers.md).

The record preserves the component licenses: original report text, figures
and documentation are CC BY 4.0; original code is MIT; bundled dependencies
and third-party material retain their individual licenses. The uploaded
`SHA256SUMS` covers the other seven files. The saved-image validation and
native Linux CI rebuilds have separate provenance in the archive.

## Completed Sandbox practice

The manually uploaded report practice record was published on 2026-11-25:
[Zenodo Sandbox record 648835](https://sandbox.zenodo.org/records/648835),
version `practice-1`. The public metadata identifies Hala Alsaleh and the
same ORCID, with a CC BY 4.0 report license.

Its identifier **10.5072/zenodo.648835 is a test DOI**, not the production
project DOI and not the identifier to submit or cite for this release.
The practice record is explicitly labelled as a test record and links back
to the repository. The production source DOI is listed separately above.

## Clean-clone reproduction check

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

At that pre-release commit, the instructor's `assessment/check_capstone.py`
passed 19 of 20 structural checks. Only the project-release DOI was missing. The merged base also
passed GitHub's Reproduce check.

The supplied ORCID was then added to `CITATION.cff`; schema validation
passed again. Nextflow lint also completed with no errors.

After the published source DOI was added, citation validation, local document
links and all 20 course structure checks passed.

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
committed files did not change. The container jobs built the
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

## Missing-file exercise

Two disposable clones demonstrated the lesson's untracked-helper failure.
`scripts/settings.py` existed only in the first clone, and Git marked it
untracked. A new clone did not contain it and `ls` failed as expected.
Only the disposable exercise folders were removed afterward.

## Remaining submission work

- Complete the independent classmate exchange, retain the resulting report,
  and address any findings; use the
  [reproduce-report template](reproduce-report-template.md).
- Preserve the saved container archive and its provenance. Its workflows
  match the trusted VCFs; native Linux CI rebuilt the same specification and
  passed both workflows and HTML/PDF rendering. The archived image and CI
  rebuilds remain distinct in [container validation](containers.md).
- Submit the repository URL and the real production DOI after completing
  the required peer check. Do not substitute the Sandbox test DOI.

Source: [CBIO7501 Lesson 12](https://khanlab.bio/cbio7501-f26/pages/12-putting-it-together.html).
