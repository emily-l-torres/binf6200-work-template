"""Positional, keyword and default arguments."""


def describe(name, sequence, decimals=2):
    """
    Describe a sequence by its name and GC fraction.

    @param name: the sequence's name
    @param sequence: a DNA sequence
    @param decimals: how many decimal places to round to; 2 if you leave it out
    @return: one line of text
    """
    fraction = (sequence.count("G") + sequence.count("C")) / len(sequence)
    return f"{name}: {round(fraction, decimals)}"


print(describe("seq2", "GATTACA"))
print(describe("seq2", "GATTACA", 4))
print(describe(sequence="GATTACA", name="seq2"))
print(describe("seq2", "GATTACA", decimals=1))
