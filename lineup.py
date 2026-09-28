"""Print three sequences with their lengths and GC fractions."""
SEQUENCES = ["ATGGCCTGGTAA", "GATTACA", "ATGCATGCAT"]
for dna in SEQUENCES:
    gc = (dna.count("G") + dna.count("C")) / len(dna)
    print(f"{dna:<14}{len(dna):>4}{gc:8.2f}")
