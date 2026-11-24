# Nextflow validation

Validated on 2026-11-24 on macOS ARM64 with Nextflow 26.10.7 and the software
recorded in `pixi.lock`. The workflow follows
[CBIO7501 lesson 10](https://khanlab.bio/cbio7501-f26/pages/10-nextflow.html).

## Equivalent results

`pixi run compare-workflows` completed successfully. All final VCF records
matched Snakemake exactly, ignoring run-specific VCF headers:

| Sample | Generation | Minimum depth 2 | Minimum depth 10 |
| --- | ---: | ---: | ---: |
| SRR2589044 | 5,000 | 10 | 5 |
| SRR2584863 | 15,000 | 25 | 16 |
| SRR2584866 | 50,000 | 775 | 415 |

All 12 depth-sensitivity VCFs also matched Snakemake record for record.
The run produced six FastQC HTML reports and a combined MultiQC report.
`nextflow lint workflow/nextflow/` reported no errors in either source file.

## Cache behaviour

Run from the project root:

```bash
pixi run -e pipeline nextflow run workflow/nextflow/main.nf \
  -params-file config/config.yaml -resume \
  -with-trace results/lesson10-resume.tsv \
  -with-report results/nextflow/execution-report.html
```

With unchanged inputs and settings, the trace contained 32 cached tasks and
no newly executed tasks.

```bash
pixi run -e pipeline nextflow run workflow/nextflow/main.nf \
  -params-file config/config.yaml --min_depth 10 -resume \
  -output-dir results/nextflow-d10 \
  -with-trace results/lesson10-depth10.tsv
```

Changing the minimum depth executed only three `FILTER_VARIANTS` tasks and
three `VARIANT_STATS` tasks. The remaining 26 tasks were cached. Depth-10
final records matched the corresponding Snakemake sensitivity records.
The shared configuration remains at minimum depth 2.

## Reproducing the check

Use `pixi run compare-workflows` to build and compare both implementations.
The GitHub Reproduce workflow runs this check after rendering the report.
Results and task caches are generated files and are excluded from Git.
Keep both `work/` and `.nextflow/` if you want to reuse the local task cache.
