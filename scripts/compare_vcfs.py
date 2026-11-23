"""Compare variant records, ignoring VCF header lines."""
import sys
from pathlib import Path


def records(path):
    with path.open() as fh:
        return [line.rstrip("\n") for line in fh if not line.startswith("#")]


def main():
    if len(sys.argv) != 3:
        sys.exit("Usage: python scripts/compare_vcfs.py DIR1 DIR2")

    first, second = map(Path, sys.argv[1:])
    names = sorted(
        {p.name for p in first.glob("*_final_variants.vcf")}
        | {p.name for p in second.glob("*_final_variants.vcf")}
    )
    if not names:
        sys.exit("No final variant files found.")

    differences = 0
    for name in names:
        a, b = first / name, second / name
        if not a.exists() or not b.exists():
            print(f"{name}: missing in one directory")
            differences += 1
            continue

        left, right = records(a), records(b)
        if left == right:
            print(f"{name}: identical ({len(left)} variants)")
        else:
            print(f"{name}: DIFFERENT ({len(left)} vs {len(right)} variants)")
            differences += 1

    sys.exit(1 if differences else 0)


if __name__ == "__main__":
    main()
