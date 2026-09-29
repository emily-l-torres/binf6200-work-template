"""Print the name and length of every sequence in a FASTA file."""
import sys

FASTA_PATH = "data/tiny.fasta"
name = ""
try:
    # 1. Open the file. If it isn't there, say so and stop.
    with open(FASTA_PATH, encoding="utf-8") as handle:
        # 2. For each line: take the newline off
        for line in handle:
            line = line.rstrip()
            # A header: remember the name, without the ">"
            if line.startswith(">"):
                name = line[1:]
            # Anything else is that record's sequence: report its length
            else:
                print(f"{name:<20}{len(line):>6}")
except FileNotFoundError:
    print(f"Error: cannot find {FASTA_PATH}", file=sys.stderr)
    sys.exit(1)
