"""A generator runs only when it's asked for a value, and only once."""
from residue_total import iter_sequences


def main() -> None:
    """Ask a generator for values one at a time, then all at once, twice."""
    sequences = iter_sequences("data/seven_chains.fasta")
    print(type(sequences))
    print(len(next(sequences)))
    print(sum(len(sequence) for sequence in sequences))
    print(sum(len(sequence) for sequence in sequences))


if __name__ == "__main__":
    main()
