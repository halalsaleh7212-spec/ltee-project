# Decision log

- Earlier lesson practice note (fictional collaborators): compare minimum read depths
  2 and 10; the example discussion contrasted 5 and 10. The dated entries below
  record the actual analysis decisions for this project.

- 2026-11-23: retain minimum depth 2 for comparison with the original shell workflow. Report sensitivity at depths 2, 5, 10, and 15. Counts for the 5,000 / 15,000 / 50,000 generation clones are respectively 10 / 25 / 775 at depth 2 and 1 / 4 / 123 at depth 15. The late clone has the most calls at every tested threshold; exact counts depend on filtering.

- 2026-11-23: keep BWA `-K 10000000`. Removing it with four cores preserved the 775 variant count for SRR2584866 but changed variant records. Restoring it reproduced all three trusted VCFs exactly.
