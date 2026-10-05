"""A function can read a global name, but assigning to it makes a local one."""

STOP_CODONS = ("TAA", "TAG", "TGA")

def count_stops(codons):
    """Count the stop codons in a list of codons."""
    stops = 0
    for codon in codons:
        if codon in STOP_CODONS:
            stops += 1
    return stops


print(count_stops(["ATG", "TAA"]))
