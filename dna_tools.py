"""Tools for DNA sequences."""


def gc_fraction(sequence):
    """
    Work out the fraction of a DNA sequence that is G or C.

    @param sequence: a DNA sequence, such as "ATGC"
    @return: the GC fraction, from 0.0 to 1.0
    """
    gc_count = sequence.count("G") + sequence.count("C")
    return gc_count / len(sequence)


def main():
    """Print the GC fraction of one sequence."""
    print(f"GC fraction of ATGGCCTGGTAA: {gc_fraction('ATGGCCTGGTAA'):.2f}")


if __name__ == "__main__":
    main()
