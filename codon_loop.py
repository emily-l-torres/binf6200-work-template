# Print each codon in a short reading frame, then again with its position.
codons = ["ATG", "GCC", "TGG", "TAA"]
for codon in codons:
    print(codon)
for position, codon in enumerate(codons):
    print(position, codon)