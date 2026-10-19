"""Join a table of named entries to their chain counts, and check for rows that vanish."""
import pandas as pd

from pdb_tools import load_chains

PDB_PATH = "data/pdb_protein.fasta"
ENTRIES_PATH = "data/entries.csv"
SUMMARY_PATH = "data/entry_summary.csv"


def main() -> None:
    """Merge the named entries with their chain counts, and count the rows in and out."""
    chains = load_chains(PDB_PATH)
    per_entry = chains.groupby("entry")["length"].agg(["count", "sum"])
    per_entry = per_entry.reset_index()
    proteins = pd.read_csv(ENTRIES_PATH)
    proteins["entry"] = proteins["entry"].str.upper()
    merged = proteins.merge(per_entry, on="entry", how="left")
    print(merged)
    missing = merged["count"].isna().sum()
    print(f"{len(proteins)} in, {len(merged)} out, {missing} unmatched")
    merged.to_csv(SUMMARY_PATH, index=False)


if __name__ == "__main__":
    main()
