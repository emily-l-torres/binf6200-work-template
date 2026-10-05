"""Return two values at once, as a tuple."""


def length_and_gc(sequence):
    """
    Measure a sequence.

    @param sequence: a DNA sequence
    @return: a tuple of its length and its GC fraction
    """
    fraction = (sequence.count("G") + sequence.count("C")) / len(sequence)
    return len(sequence), fraction


def main():
    """Measure one sequence, and unpack what comes back."""
    print(length_and_gc("GATTACA"))
    length, fraction = length_and_gc("GATTACA")
    print(length)
    print(f"{fraction:.2f}")


if __name__ == "__main__":
    main()
    