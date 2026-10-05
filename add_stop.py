"""A function can change a list you hand it."""


def add_stop(codons):
    """
    Add a stop codon to the end of a list of codons.

    @param codons: a list of codons
    @return: nothing; the list itself changes
    """
    codons.append("TAA")


gene = ["ATG", "GCC"]
add_stop(gene)
print(gene)
