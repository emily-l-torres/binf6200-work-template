"""Print the five PDB entries with the most chains."""
import collections

import pdb-tools


def main() -> None:
    """Count the chains in each entry, and print the five largest."""
    entry_ids = pdb_tools.read_entry_ids("data/pdb_protein.fasta")
    counts = collections.Counter(entry_ids)
    for entry_id, chains in counts.most_common(5):
        print(entry_id, chains)


if __name__ == "__main__":
    main()
