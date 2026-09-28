"""Print each header in a small file."""
with open("data/three_fasta_headers.txt", encoding="utf-8") as handle:
    for line in handle:
        line = line.rstrip()
        print(line)
        