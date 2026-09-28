"""Check whether a DNA sequence could be a complete gene."""
sequence = input("DNA sequence: ")
length = len(sequence)
last_codon = sequence[-3:]

if length > 0 and length % 3 == 0:
    print(f"{length} bases: a whole number of codons")
else:
    print(f"{length} bases: not a whole number of codons")

if not sequence.startswith("ATG"):
    print("No start codon: a gene begins with ATG")

if last_codon in ["TAA", "TAG", "TGA"]:
    print(f"Ends with the stop codon {last_codon}")
else:
    print(f"No stop codon at the end: {last_codon}")
