def at_fraction(sequence): 
    """Return the fraction of a DNA sequence that is A or T.""" 
    return (sequence.count("A") + sequence.count("T")) / len(sequence)