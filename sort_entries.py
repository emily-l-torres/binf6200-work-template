"""Sort PDB entries by how many chains they have."""
from collections import Counter
from operator import itemgetter

from pdb_tools import read_entry_ids


def main() -> None:
    """Sort the entries by chain count, most first, two ways."""
    counts = Counter(read_entry_ids("data/pdb_protein.fasta"))
    by_lambda = sorted(counts.items(), key=lambda pair: pair[1], reverse=True)
    print(by_lambda[:5])
    by_itemgetter = sorted(counts.items(), key=itemgetter(1), reverse=True)
    print(by_lambda == by_itemgetter)


if __name__ == "__main__":
    main()
