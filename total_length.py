"""Any number of arguments: *args, and its keyword cousin **kwargs."""


def total_length(*sequences):
    """
    Add up the lengths of any number of sequences.

    @param sequences: as many sequences as you like, separated by commas
    @return: their combined length
    """
    total = 0
    for sequence in sequences:
        total += len(sequence)
    return total


def show_details(name, **details):
    """
    Print a name and whatever named details come with it.

    @param name: a sequence's name
    @param details: any keyword arguments, such as chain="A"
    @return: nothing
    """
    print(name, details)


print(total_length("ATGC"))
print(total_length("ATGC", "GATTACA", "GG"))
show_details("101M", chain="A", organism="sperm whale")
