"""Write the header of every chain A record to its own file."""
FASTA_PATH = "data/pdb_protein.fasta"
OUT_PATH = "data/chain_a_headers.txt"
kept = 0
with open(FASTA_PATH, encoding="utf-8") as fasta:
    with open(OUT_PATH, "w", encoding="utf-8") as out:
        for line in fasta:
            line = line.rstrip()
            if line.startswith(">") and ":A:" in line:
                print(line, file=out)
                kept += 1
print(f"Wrote {kept:,} headers to {OUT_PATH}")
