"""Print the lengths of the first five sequences in a FASTA file."""
FASTA_PATH = "data/pdb_protein.fasta"
shown = 0
with open(FASTA_PATH, encoding="utf-8") as handle:
    for line in handle:
        line = line.rstrip()
        if line.startswith(">"):
            continue
        print(len(line))
        shown += 1
        if shown == 5:
            break
