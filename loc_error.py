"""Ask a filtered table for a row label it doesn't have."""
from pdb_tools import load_chains

PDB_PATH = "data/pdb_protein.fasta"
LONG = 2500


def main() -> None:
    """Keep the chains longer than LONG residues, then ask for the row labeled 0."""
    chains = load_chains(PDB_PATH)
    long_chains = chains[chains["length"] > LONG]
    print(long_chains.loc[0, "entry"])


if __name__ == "__main__":
    main()
