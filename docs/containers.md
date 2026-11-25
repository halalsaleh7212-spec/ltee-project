# Containers

The recipes in `containers/Dockerfile` and `containers/apptainer.def` build
software environments from `pixi.toml` and `pixi.lock`. Run build commands
from the repository root.

## v1.0.0 release image

A new `pipeline` image was built on 2026-11-25 for `linux/amd64`. Its
Dockerfile, `pixi.toml`, and `pixi.lock` match commit
`e1099019374144c92c4f78e51c86af9796c974e2`. The environment lives at
`/opt/project/.pixi/envs/pipeline`; its entrypoint activates that environment.
Invoke tools such as `snakemake`, `nextflow`, `python`, and `quarto` directly
inside the image. The production image does not include the Pixi executable
or this project's source/data, which must be mounted separately.

| Item | Value |
| --- | --- |
| Image tag | `ltee-project:1.0.0` |
| Image ID reported by Docker | `sha256:82b590f63bbe7e84130696b11fbffa809554001a1048c7529cc70520c1f0eca2` |
| Platform | `linux/amd64` |
| Published archive | `ltee-project_1.0.0_linux-amd64.tar.gz` |
| Archive bytes | 1,162,925,003 |
| Archive SHA-256 | `c490e81aca71da8010819c73cfaa02bb72ee0dc88d802909542e727fe45fc5ff` |

The archive passed gzip integrity and Docker manifest/tag checks. It was
prepared with `docker save` and gzip, and is kept outside Git. The previous
`0.1.0` image and archive were retained. The release provenance file records
the input hashes and distinguishes the working-tree snapshot used for testing
from the matching committed build specification.

### Companion download and saved-image use

The companion was published on 2026-11-25 with DOI
[10.5281/zenodo.24533491](https://doi.org/10.5281/zenodo.24533491).
Its public metadata, eight file names, byte sizes and provider MD5 checksums
match the verified upload package. The record supplements source-code DOI
[10.5281/zenodo.24533293](https://doi.org/10.5281/zenodo.24533293).

The [companion record](https://zenodo.org/records/24533491) contains
these eight files together:

- `ltee-project_1.0.0_linux-amd64.tar.gz`
- `ltee-project_1.0.0_container-provenance.json`
- `ltee-report.html`
- `ltee-report.pdf`
- `multiqc_report.html`
- `validation-evidence.zip`
- `README.txt`
- `SHA256SUMS`

Download all eight files into one folder. `SHA256SUMS` covers each of the
other seven files. From that download folder, verify them before loading:

```bash
shasum -a256 -c SHA256SUMS
docker load -i ltee-project_1.0.0_linux-amd64.tar.gz
```

On Linux, `sha256sum -c SHA256SUMS` is an alternative checksum command.
The image archive's verified SHA-256 is recorded in the table
above. Docker accepts the gzip-compressed archive directly.

Run the saved environment against a checkout of the corresponding source
release. The image supplies the pipeline tools but contains neither the
project source nor its input data:

```bash
git clone --branch v1.0.0 https://github.com/halalsaleh7212-spec/ltee-project.git
cd ltee-project
docker run --rm --platform linux/amd64 \
  --mount "type=bind,source=$PWD,target=/work" -w /work \
  ltee-project:1.0.0 bash -c 'python scripts/download_data.py &&
    snakemake --cores 2 &&
    nextflow run workflow/nextflow/main.nf -params-file config/config.yaml &&
    python scripts/compare_vcfs.py results/vcf results/nextflow/vcf'
```

The supplied HTML/PDF reports were rendered successfully on the host. They
are not evidence that rendering completed inside the archived image under
Mac amd64 emulation. The native Linux rebuild checks and archived-image
limitation are documented below. Open the companion's `multiqc_report.html`
directly when viewing the PDF's quality report.

The companion's license statement distinguishes original project code
(MIT), original report text/figures (CC BY 4.0), the read subset (CC0), and
third-party software, data and MultiQC components under their own terms.
No blanket MIT or CC BY 4.0 license is applied to the complete container.

### Build without including old archives

Only three files are needed in the build context. From the repository root:

```bash
container_build_context=$(mktemp -d)
cp containers/Dockerfile pixi.toml pixi.lock "$container_build_context/"
docker build --platform linux/amd64 --build-arg ENV_NAME=pipeline \
  -t ltee-project:1.0.0 "$container_build_context"
```

The root `.dockerignore` also excludes saved image archives when building
with the full repository as context. Build outputs and archived images can
consume several GiB; the new image is displayed as 4.98 GB by `docker image ls`.

### Workflow and report validation

In a separate source snapshot, with the original raw data and trusted VCFs
mounted read-only, the archived image completed all 49 Snakemake jobs and all
32 Nextflow tasks. Both workflows produced identical variant records, also
matching the trusted results: SRR2584863 25, SRR2584866 775, SRR2589044 10.
The trusted host VCF files were unchanged.

Quarto rendering in that image did **not** complete under Docker Desktop's
amd64 emulation on the Apple Silicon host. A minimal plotting example
reproduced a stall in NumPy 2.5.4 scalar float floor division during Matplotlib
tick calculation. The isolated report run was stopped; packages and source
were not changed. The separately rendered host HTML/PDF reports are not
claimed as evidence that rendering passed inside this emulated image.

Native Linux container validation **passed on 2026-11-25** at commit
`2abdb89957b58f3a2476a1012d32b56324c053de`, in both the
[pull-request run](https://github.com/halalsaleh7212-spec/ltee-project/actions/runs/45496326076/job/138807692874)
and the
[branch-push run](https://github.com/halalsaleh7212-spec/ltee-project/actions/runs/45496313679/job/138807647162).
Each `container-reproduce` job built the locked pipeline image on a native
amd64 Linux runner, completed both workflows, checked exact variant-record
agreement and the expected 25/775/10 counts, rendered HTML and PDF, and checked
that committed files were unchanged. The `container-results` artifacts retain
logs, results, image inspection metadata, and reports for seven days. The
parallel direct Pixi reproduction jobs also passed; all four checks are
recorded in [release validation](release-validation.md).

These checks built fresh images from the same Dockerfile, `pixi.toml`, and
`pixi.lock` as the prepared archive. They did not load or certify the exact
archived image ID above. Base-image tags and build metadata can produce a
different image ID even with the same locked environment. Native Linux
success validates the build specification and its report workflow; the
archived image's Mac-emulation rendering limitation remains recorded above.

## Historical Lesson 08 Docker validation

The record below preserves the image and commands used for the Lesson 08
exercise. The saved `0.1.0` image is a snapshot of the environment at that
time, before the later Snakemake and Nextflow additions. Its image ID and
archive do not certify that it contains the current lockfile or the current
workflow tools. Rebuild the image from the current files when testing the
current environment.

The historical shell command shown below writes to `results/`. For a new
shell-script comparison against Snakemake, give it a separate output folder:
`bash scripts/run_variant_calling.sh 2 results/shell-script`.

The LTEE variant-calling workflow was successfully executed
using Docker Desktop on an Apple Silicon Mac.

### Container configuration

- Image: `ltee-project:0.1.0`
- Platform: `linux/amd64`
- Environment: `pipeline`
- Package specification: `pixi.toml` and `pixi.lock`
- Image ID: `sha256:8cb802126f71acfca6a0a46cc8f33d0725e9a91cc7b95712a7de36207f58aee1`

### Build command

```bash
docker build --platform linux/amd64 -f containers/Dockerfile \
  --build-arg ENV_NAME=pipeline -t ltee-project:0.1.0 .
```

### Execute the pipeline

```bash
docker run --rm --platform linux/amd64 \
  -v "$PWD":/work -w /work \
  ltee-project:0.1.0 \
  bash scripts/run_variant_calling.sh
```

### Verified results

| Sample | Variant count |
|---|---:|
| SRR2584863 | 25 |
| SRR2584866 | 775 |
| SRR2589044 | 10 |

All three samples produced the expected variant counts.

### Container archive

The image was exported to
`containers/ltee-project_0.1.0.tar.gz` using `docker save`.
The archive is excluded from Git using `.gitignore`.
