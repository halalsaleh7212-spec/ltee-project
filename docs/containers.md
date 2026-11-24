# Containers

The recipes in `containers/Dockerfile` and `containers/apptainer.def` build
software environments from `pixi.toml` and `pixi.lock`. Run build commands
from the repository root.

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
