# reports

Quarto documents (`.qmd`) that turn results into a report: text, code,
figures and tables in one file. Render with `pixi run quarto render reports/<file>.qmd`.
The rendered HTML is not committed; it can always be rebuilt.

## LTEE report (lesson 07)

`pixi run report` verifies/downloads the raw data and renders
`ltee-report.qmd` to self-contained HTML and a PDF using Typst.
The report covers input-read quality; variant results are a later exercise.

To use a different number of reads for summaries without editing the source:

```bash
pixi run quarto render reports/ltee-report.qmd -P max_reads:2000
```

The default is 10,000 reads per file. Read counts always use the entire file.
`pixi run reproduce` includes the report alongside QC and variant calling.
GitHub Actions retains the HTML and PDF in its `results` artifact for 7 days.
Generated reports are not committed; the QMD, bibliography, helper and locked
software environment are the reproducible source.

Local checks completed for lesson 07: default and parameterized renders,
HTML and Typst PDF output, a first-document Word export, and notebook rendering
with figure alt text. The deliberately broken report failed with the expected
`NameError` for an undefined `samples` variable and was removed afterwards.
