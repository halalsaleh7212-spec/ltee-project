# Resource measurements

Measured 2026-11-25 on macOS ARM64, Apple M4 Pro (14 logical CPUs, 48 GiB RAM).
The Snakemake run was limited to four cores.

| Item | Measurement |
| --- | ---: |
| Default Pixi environment | 1.1 GiB |
| Pipeline Pixi environment | 2.6 GiB |
| Raw data | 332 MiB |
| Processed reference | 12 MiB |
| Fresh Snakemake outputs | 100 MiB |
| Existing results including shell/Nextflow copies and experiments | 1.1 GiB |
| Existing Nextflow task cache before the extra practice exercises | 866 MiB |
| Full Snakemake elapsed time | 26.29 seconds |
| Maximum resident set size reported by `time -l` | 464,207,872 bytes (443 MiB) |

Disk usage was measured with `du -sh`; environment totals exclude the separate
Pixi package-download cache and Docker images, and may count shared files more
than once. The populated results/cache figures depend on previous runs.

For timing, workflow/config/sample files were copied to an empty practice
folder and the existing read-only raw data was linked in. A fresh full
Snakemake run completed 49 jobs using the locked pipeline environment:

```bash
/usr/bin/time -l snakemake --cores 4
```

The run excluded installation, downloading, and Quarto rendering. macOS's
maximum-RSS value is the tool-reported statistic, not a measured sum of all
concurrent processes or a recommended minimum system RAM. Resource needs can
change with sample count, read coverage, tool versions, and thread settings.
