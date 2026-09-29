"""Split a DNA sequence into codons, three bases at a time."""
SEQUENCE = "ATGGCCTGGTAA"
STOP_CODONS = ["TAA", "TAG", "TGA"]
for start in range(0, len(SEQUENCE), 3):
    codon = SEQUENCE[start:start + 3]
    if codon == "ATG":
        print(f"{start:>3} {codon} start")
    elif codon in STOP_CODONS:
        print(f"{start:>3} {codon} stop")
    else:
        print(f"{start:>3} {codon}")
