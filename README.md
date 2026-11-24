# LTEE variant calling

Variant calling on three *Escherichia coli* clones from population Ara-3 of
Richard Lenski's Long-Term Evolution Experiment (LTEE), sampled at 5,000,
15,000, and 50,000 generations. We ask how variant counts change across these
clones and how sensitive the answer is to the minimum read-depth filter.

Author: Hala Alsaleh. This teaching project follows the
[CBIO7501 lessons](https://khanlab.bio/cbio7501-f26/) and adapts the analysis
steps from [Data Carpentry: Wrangling Genomics](https://datacarpentry.github.io/wrangling-genomics/04-variant_calling.html).

## Publication

The source study is Tenaillon et al. (2016), *Tempo and mode of genome evolution
in a 50,000-generation experiment*, **Nature** 536:165–170,
[doi:10.1038/nature18959](https://doi.org/10.1038/nature18959).
This repository is a teaching reanalysis using subsampled reads; the counts
are not an exhaustive inventory of mutations in each genome.

## Reproduce the results

Install [Pixi](https://pixi.prefix.dev/latest/) and Git. Use macOS or Linux;
on Windows, run the pipeline inside WSL2. Internet access is needed for the
initial software installation and data download.

```bash
git clone https://github.com/halalsaleh7212-spec/ltee-project.git
cd ltee-project
pixi install --locked
pixi run reproduce
```

Run commands from the project root. `reproduce` downloads and verifies the
raw data, runs Snakemake, and renders the Quarto report as HTML and PDF.
Software versions are pinned in `pixi.lock`. GitHub's
[Reproduce check](https://github.com/halalsaleh7212-spec/ltee-project/actions/workflows/reproduce.yml)
validates the citation, rebuilds the analysis, and checks the two workflow
implementations on a clean Linux machine.

Other useful commands:

```bash
pixi run run-nextflow          # the same analysis in Nextflow
pixi run compare-workflows     # compare Nextflow with Snakemake
pixi run compare-to-shell      # compare Snakemake with the shell pipeline
pixi task list
```

Nextflow publishes copies under `results/nextflow/`. To reuse task results
and create an execution report:

```bash
pixi run -e pipeline nextflow run workflow/nextflow/main.nf \
  -params-file config/config.yaml -resume \
  -with-report results/nextflow/execution-report.html
```

Keep `work/` and `.nextflow/` to retain Nextflow's cache. See
[Nextflow validation](docs/nextflow-validation.md) and
[container instructions](docs/containers.md) for details.

## Hardware

Measured on 2026-11-25 on an Apple M4 Pro with 48 GiB RAM: the installed
software environments occupied approximately 3.7 GiB, raw data 332 MiB,
and a fresh Snakemake result set 100 MiB. Using four cores, the complete
Snakemake workflow took 26.29 seconds with 443 MiB maximum resident set size
reported by macOS `time -l`. These are measurements, not minimum RAM requirements;
installation, downloading, and report rendering were excluded from the timed run.

Allow at least 6 GiB for project files, plus space for the package cache and
any Docker images. Extra workflow runs and saved shell-script results use
additional disk. See [measurement details](docs/resources.md).

## Repository contents

- [Project structure](docs/structure.md): folders and which files are regenerated.
- [Workflow diagram](docs/rulegraph.svg): dependencies between Snakemake rules.
- [Shared settings](config/config.yaml) and [sample sheet](metadata/samples.tsv).
- [Software versions](docs/software-versions.txt): explicit pipeline packages
  and builds on macOS ARM64; `pixi.lock` records all dependencies per platform.
- [Analysis decisions](docs/decisions.md) and [report source](reports/ltee-report.qmd).

## Expected outputs

| Path | Contents |
| --- | --- |
| `reports/ltee-report.html` and `.pdf` | Read quality, variants, depth sensitivity, and software versions |
| `results/qc/multiqc/multiqc_report.html` | Combined read-quality report |
| `results/vcf/` | Final variant records for each sample |
| `results/sensitivity/` | Variant files at the configured depths (2, 5, 10, 15) |
| `results/stats/` | Alignment and variant statistics |
| `results/nextflow/` | Equivalent outputs from Nextflow |
| `results/shell-script/` | Shell-pipeline outputs used for comparison |

At the default minimum depth of 2, expect **10** variants for SRR2589044,
**25** for SRR2584863, and **775** for SRR2584866. `compare-workflows` must
report identical variant records; it ignores run-specific VCF headers.
Generated results and rendered reports are excluded from Git.

## Data

The read subset is the Data Carpentry Genomics Curriculum Example Data,
[figshare version 3](https://doi.org/10.6084/m9.figshare.7726454.v3), file
`sub.tar.gz`. The original sequencing runs are in NCBI BioProject PRJNA295606.
The reference is *E. coli* B strain REL606, GenBank CP000819.1, assembly
GCA_000017985.1. Source URLs and provider checksums are in
[metadata/sources.tsv](metadata/sources.tsv), with local SHA-256 checksums in
[metadata/checksums.sha256](metadata/checksums.sha256).
Raw data is downloaded by code and kept read-only.

## Citation

See [CITATION.cff](CITATION.cff), or use GitHub's **Cite this repository** button.
Cite the original study and data source when using their material.

## Licenses

Code is distributed under [MIT](LICENSE). Original report text and figures
are available under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
The figshare read subset is provided under CC0; external data retains its
provider's terms. Adapted Data Carpentry material retains its CC BY 4.0
attribution. Third-party software and the linked Contributor Covenant keep
their own licenses.

## Contact and contributions

For questions or problems, open a
[GitHub issue](https://github.com/halalsaleh7212-spec/ltee-project/issues).
Read [CONTRIBUTING.md](CONTRIBUTING.md) before proposing changes and follow
[CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md). That file gives the private contact
for conduct reports.
