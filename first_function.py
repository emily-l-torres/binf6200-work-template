"""Define a function once, then call it three times."""


def gc_fraction(sequence):
    """Return the fraction of a DNA sequence that is G or C."""
    gc_count = sequence.count("G") + sequence.count("C")
    return gc_count / len(sequence)


print(gc_fraction("ATGC"))
print(gc_fraction("GGCCGGCC"))
print(gc_fraction("GATTACA"))