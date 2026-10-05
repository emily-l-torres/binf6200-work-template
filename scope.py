"""A name made inside a function stays inside it."""


def gc_fraction(sequence):
    """Return the GC fraction of a DNA sequence."""
    gc_count = sequence.count("G") + sequence.count("C")
    return gc_count / len(sequence)


print(gc_fraction("ATGC"))
print(gc_count)