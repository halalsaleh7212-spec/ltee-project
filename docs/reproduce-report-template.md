## Reproduce report

- **Repository and commit:** <!-- URL and `git rev-parse --short HEAD` -->
- **My computer:** <!-- OS, chip, Pixi version (`pixi --version`) -->
- **Date and time spent:** <!-- minutes from clone to result -->

## 1. Could I find out what the project is and how to run it?

- [ ] The README says what the project is about
- [ ] The README gives the command(s) to reproduce
- [ ] The README says what output to expect
- [ ] The data source is given with an identifier and a license

Notes:

## 2. Did it run?

- [ ] `pixi install --locked` worked (the lock file matches the manifest)
- [ ] The data downloaded and the checksums passed
- [ ] `pixi run reproduce` (or the documented command) finished without errors
- [ ] The *Reproduce* GitHub Action of the repository is green

Commands I ran, and any error message (paste it in full):

```
```

## 3. Did I get the same results?

- [ ] The numbers / figures match what the README or report says
- [ ] I compared them how? <!-- e.g. compare_vcfs.py, checksums, by eye -->

Differences I found:

Notes for this project: at minimum depth 2, expected final variants are
10, 25 and 775 for SRR2589044, SRR2584863 and SRR2584866 respectively.
`pixi run compare-workflows` compares complete final VCF records between
Snakemake and Nextflow.

## 4. Could I reuse it?

- [ ] There is a LICENSE, and I understand what I may do
- [ ] There is a valid `CITATION.cff`

## 5. The one change that would help most

<!-- Be specific and kind: "Add the --cores value to the README", not "unclear". -->
Source: [CBIO7501 reproduce-report template](https://khanlab.bio/cbio7501-f26/assessment/reproduce-report-template.html), CC BY 4.0.
