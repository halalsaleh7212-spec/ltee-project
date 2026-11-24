# Nextflow lesson exercises

Completed on 2026-11-25 with Nextflow 26.10.7, following
[CBIO7501 Lesson 10](https://khanlab.bio/cbio7501-f26/pages/10-nextflow.html).
The main workflow and depth-filter tests are documented in
[nextflow-validation.md](nextflow-validation.md).

These additional exercises used separate disposable practice folders, copied
workflow/config/sample files, and links to the existing read-only raw data.
They did not replace the project's trusted results or main workflow cache.

| Exercise | Verified result |
| --- | --- |
| Uppercase toy, first run | Two tasks executed; both outputs correctly converted to uppercase |
| Toy with `-resume` | Both tasks came from cache |
| QC-only workflow | Three FASTQC tasks and one MULTIQC task executed |
| Full pipeline resumed after QC | 28 tasks executed, four QC tasks cached |
| Task inspection | A FASTQC task contained two staged read symlinks, its exact `.command.sh`, empty stderr, and exit code 0 |
| Launch from `workflow/nextflow/` | Failed with exit 1 because `metadata/samples.tsv` was not found relative to that folder |
| Return to project root and resume | All 32 tasks cached |
| Compare final variants | All three VCFs matched trusted records: 25 / 775 / 10 for SRR2584863 / SRR2584866 / SRR2589044 |
| Clean disposable run history and task cache | Removed 32 task folders; SHA-256 checks confirmed all 43 published files were unchanged |
| nf-core demo | Release 1.2.0 with `test,docker` completed all eight tasks successfully |

## What the exercises demonstrate

Processes describe commands; channels carry samples between them. A channel
created from the sample sheet launches one task per sample, while `collect()`
waits for all FastQC outputs before starting MultiQC. A plain reference input
produces a reusable value channel, so every sample can use the same reference.

Run names from `nextflow log` can be supplied to `-resume RUN_NAME` to select
a specific cache. In the QC-to-full exercise, replacing the practice QC-only
script with the complete workflow reused the same four QC tasks.

Relative sample and read paths are resolved from the launch directory.
Always run the real workflow from the repository root:

```bash
pixi run -e pipeline nextflow run workflow/nextflow/main.nf \
  -params-file config/config.yaml -resume
```

## Cleanup

Inspect before deleting a cache:

```bash
nextflow log
nextflow clean RUN_NAME -n
```

In the disposable exercise, `nextflow clean RUN_NAME -f` removed each practice
run. Shared task folders stayed until all exercise runs referencing them were
cleaned. Published results remained usable because the configuration uses
`workflow.output.mode = 'copy'`. The main project's cache was retained.

## Pinned community pipeline

With Docker running, the separate community-pipeline exercise used:

```bash
nextflow run nf-core/demo -r 1.2.0 -profile test,docker \
  --outdir results -with-report execution-report.html -with-trace trace.tsv
```

The trace recorded eight completed tasks, with no failures. This uses the
community pipeline's own test data and containers, not the LTEE input data.
The release is pinned so the demo's pipeline source is identifiable.
