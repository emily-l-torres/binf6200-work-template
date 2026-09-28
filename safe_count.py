"""Count the sequences in a FASTA file, and say so plainly when the file is missing."""
import sys

FASTA_PATH = "data/pdb_protein.fasta"
count = 0
try:
    with open(FASTA_PATH, encoding="utf-8") as handle:
        for line in handle:
            if line.startswith(">"):
                count += 1
except FileNotFoundError:
    print(f"Error: cannot find {FASTA_PATH}", file=sys.stderr)
    sys.exit(1)
print(f"{count:,} sequences")
