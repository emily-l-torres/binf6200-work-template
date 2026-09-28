"""Count the sequences in a FASTA file by counting its header lines."""
FASTA_PATH = "data/pdb_protein.fasta"
count = 0  # before the loop: start at zero
with open(FASTA_PATH, encoding="utf-8") as handle:
    for line in handle:
        if line.startswith(">"):
            count += 1  # inside the loop: one more header
print(f"{count:,} sequences")  # after the loop: the total
