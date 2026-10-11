"""Add up the chains in the entries with many chains, two ways."""
from collections import Counter

from pdb_tools import read_entry_ids

MANY_CHAINS = 50


def main() -> None:
    """Total the big entries' chains with a list, then with a generator expression."""
    counts = Counter(read_entry_ids("data/pdb_protein.fasta"))
    # A list comprehension inside sum(): the whole list is built, then added up
    print(sum([chains for chains in counts.values() if chains >= MANY_CHAINS]))
    # A generator expression: no square brackets, so sum() gets one value at a time
    print(sum(chains for chains in counts.values() if chains >= MANY_CHAINS))


if __name__ == "__main__":
    main()
