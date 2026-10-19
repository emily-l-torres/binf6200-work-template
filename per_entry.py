"""Count the chains and add up the residues in each PDB entry, with groupby."""
from pdb_tools import load_chains

PDB_PATH = "data/pdb_protein.fasta"


def main() -> None:
    """Group the chains by entry, then look at four entries and the three largest."""
    chains = load_chains(PDB_PATH)
    per_entry = chains.groupby("entry")["length"].agg(["count", "sum"])
    print(per_entry.shape)
    print(per_entry.loc[["101M", "104L", "4HHB", "1OTZ"]])
    print(per_entry.sort_values("sum", ascending=False).head(3))


if __name__ == "__main__":
    main()
