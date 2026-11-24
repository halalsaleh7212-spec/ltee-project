# Contributing

Suggestions, bug reports, and improvements to this LTEE research project are
welcome. Please use the following process so that changes remain reproducible.

## Propose a change

Open an [issue](https://github.com/halalsaleh7212-spec/ltee-project/issues)
before making a larger change. Describe the problem or idea and the expected
result. For a bug report, include your operating system, the command you ran,
and the relevant error message; remove any passwords, tokens, or private data.

## Make and check your changes

1. Fork the repository, clone your fork, and create a branch for your change.
2. Make small, focused changes and use clear commit messages.
3. From the project root, install the locked environment and reproduce the
   analysis:

   ```bash
   pixi install --locked
   pixi run reproduce
   ```

4. When changing the variant-calling workflow, also run:

   ```bash
   pixi run compare-to-shell
   pixi run compare-workflows
   ```

   Explain any intentional differences in the results in your pull request.

## Keep the project reproducible

- Keep raw data out of Git. Use `scripts/download_data.py` through
  `pixi run download` to obtain and verify the files in `data/raw/`.
- Keep generated results, local environments, and workflow caches out of Git
  according to `.gitignore`.
- Commit `pixi.toml` and `pixi.lock` together when changing dependencies.
- Record analysis decisions in `docs/decisions.md` and update documentation
  when commands or expected outputs change.

## Community conduct

Follow [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) in issues, pull requests,
and discussions. Use its private reporting contact for conduct concerns.

## Submit a pull request

Push your branch to your fork and open a pull request against this repository's
`main` branch. Explain what changed, why, and which checks you ran; link any
related issue. The GitHub **Reproduce** check must pass before merging.

Adapted from [CBIO7501, Lesson 11: Contributing and conduct](https://khanlab.bio/cbio7501-f26/pages/11-documentation.html#contributing-and-conduct).
