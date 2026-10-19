"""Keep the rows of a DataFrame that pass a test, and pick a value by its position."""
from pdb_tools import load_chains

PDB_PATH = "data/pdb_protein.fasta"
LONG = 2500


def main() -> None:
    """Find the chains longer than LONG residues, and the entry of the first one."""
    chains = load_chains(PDB_PATH)
    long_chains = chains[chains["length"] > LONG]
    print(len(long_chains))
    print(long_chains.head(3))
    print(long_chains.iloc[0, 0])


if __name__ == "__main__":
    main()
