"""A default list is made once, and it remembers."""


def collect(gene, found=None):
    """
    Add a gene to a list of genes found so far.

    @param gene: a gene name
    @param found: the list to add it to; a new empty list if you leave it out, or so it seems
    @return: the list
    """
    if found is None:
        found = []
    found.append(gene)
    return found


print(collect("BRAF"))
print(collect("KRAS"))
print(collect("TP53"))
