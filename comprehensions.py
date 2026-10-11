"""Build a list, a set and a dictionary in one line each."""
from collections import Counter

from pdb_tools import read_entry_ids

MANY_CHAINS = 50


def main() -> None:
    """Pick out the entries with many chains, three ways."""
    counts = Counter(read_entry_ids("data/pdb_protein.fasta"))
    # A list comprehension: square brackets
    big = [entry_id for entry_id, chains in counts.items() if chains >= MANY_CHAINS]
    print(big)
    # A set comprehension: curly brackets, one of each
    first_digits = {entry_id[0] for entry_id in counts}
    print(sorted(first_digits))
    # A dictionary comprehension: curly brackets, a key and a value
    big_counts = {entry_id: chains for entry_id, chains in counts.items() if chains >= MANY_CHAINS}
    print(big_counts)


if __name__ == "__main__":
    main()
