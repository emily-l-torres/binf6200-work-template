"""A function that prints its answer, and what that costs."""


def gc_fraction(sequence):
    """Print the GC fraction of a DNA sequence."""
    gc_count = sequence.count("G") + sequence.count("C")
    return gc_count / len(sequence)


FRACTION = gc_fraction("ATGC")
print(FRACTION)
print(FRACTION * 100)
