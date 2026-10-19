"""Load every chain in pdb_protein.fasta into a pandas DataFrame, and describe it."""
from pdb_tools import load_chains

PDB_PATH = "data/pdb_protein.fasta"


def main() -> None:
    """Load the table, then look at its size, its first rows and its lengths."""
    chains = load_chains(PDB_PATH)
    print(chains.shape)
    print(chains.head(3))
    print(chains["length"].describe())


if __name__ == "__main__":
    main()
