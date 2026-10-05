"""Type hints say what a function takes and gives back, and Python doesn't check them."""


def gc_percent(sequence: str) -> int:
    """
    Work out the percentage of a DNA sequence that is G or C.

    @param sequence: a DNA sequence
    @return: the GC percentage
    """
    return (sequence.count("G") + sequence.count("C")) / len(sequence) * 100


print(gc_percent("GATTACA"))
