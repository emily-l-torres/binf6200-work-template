"""One function for the fraction of any bases, instead of one function per pair."""


def base_fraction(sequence, bases):
    """
    Work out the fraction of a DNA sequence made of the given bases.
    @param sequence: a DNA sequence
    @param bases: the bases to count, such as "GC"
    @return: the fraction, from 0.0 to 1.0
    """
    count = 0
    for base in bases:
        count += sequence.count(base)
    return count / len(sequence)


print(base_fraction("GATTACA", "GC"))
print(base_fraction("GATTACA", "AT"))
print(base_fraction("GATTACA", "AG"))
