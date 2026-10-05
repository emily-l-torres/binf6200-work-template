"""Tools for DNA sequences."""


def gc_fraction(sequence):
    """
    Work out the fraction of a DNA sequence that is G or C.

    @param sequence: a DNA sequence, such as "ATGC"
    @return: the GC fraction, from 0.0 to 1.0
    """
    if len(sequence) == 0:
        raise ValueError("an empty sequence has no GC fraction")
    sequence = sequence.upper()
    gc_count = sequence.count("G") + sequence.count("C")
    return gc_count / len(sequence)


def count_stop_codons(sequence: str) -> int:
    """
    Count the stop codons (TAA, TAG, TGA) in the first reading frame.

    @param sequence: a DNA sequence, such as "ATGTAA"
    @type sequence: str
    @return: the number of in-frame stop codons
    @rtype: int
    """
    sequence = sequence.upper()
    count = 0
    for position in range(0, len(sequence) - 2, 3):
        codon = sequence[position : position + 3]
        if codon in ("TAA", "TAG", "TGA"):
            count += 1
    return count


def main():
    """Print the GC fraction of one sequence."""
    print(f"GC fraction of ATGGCCTGGTAA: {gc_fraction('ATGGCCTGGTAA'):.2f}")


if __name__ == "__main__":
    main()
