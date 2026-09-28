"""Report the count, average length, longest and shortest sequence in a FASTA file."""
FASTA_PATH = "data/pdb_protein.fasta"
count = 0
total_length = 0
longest = None
longest_header = ""
shortest = None
shortest_header = ""
header = ""
with open(FASTA_PATH, encoding="utf-8") as handle:
    for line in handle:
        line = line.rstrip()
        if line.startswith(">"):
            header = line
            continue
        length = len(line)
        count += 1
        total_length += length
        if longest is None or length > longest:
            longest = length
            longest_header = header
        if shortest is None or length < shortest:
            shortest = length
            shortest_header = header
print(f"{count:,} sequences")
print(f"Average length: {total_length / count:.2f}")
print(f"Longest:  {longest:>5} {longest_header}")
print(f"Shortest: {shortest:>5} {shortest_header}")
