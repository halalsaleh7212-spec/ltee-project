# Reproduce report template

A classmate can copy this into an issue after testing a clean clone using
only the repository documentation. An automated agent or CI run must be
identified as such and does not count as the classmate exchange.

- Reviewer:
- Repository URL and exact commit:
- Operating system, processor, and Pixi version:
- Date and elapsed time:

## Documentation

Could you identify the question, data source and license, setup commands,
and expected outputs without asking the author? Record anything unclear.

## Execution

Record the commands actually run and full error messages. Did the locked
installation, downloads/checksums, workflow, report rendering, and GitHub
checks succeed? Were any undocumented changes needed?

## Results

Record the observed numbers and how you compared them. For this LTEE
project, `pixi run compare-workflows` should report identical VCF records:
25 / 775 / 10 for SRR2584863 / SRR2584866 / SRR2589044.

## Reuse and improvement

Could you find the licenses and citation? Name the single most useful
improvement, and record whether the author subsequently fixed it.

Adapted from the course's [reproduce-report template](https://khanlab.bio/cbio7501-f26/assessment/reproduce-report-template.html),
CC BY 4.0. Do not mark any check successful without performing it.
