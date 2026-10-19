"""Hold the same seven chains in three nested shapes."""
from pprint import pprint

from pdb_tools import iter_chains

SEVEN_CHAINS = "data/seven_chains.fasta"


def main() -> None:
    """Build a list of dictionaries, a dictionary of lists and a dictionary of dictionaries."""
    # A list of dictionaries: one dictionary per chain, a row
    rows = []
    for entry, chain, length in iter_chains(SEVEN_CHAINS):
        rows.append({"entry": entry, "chain": chain, "length": length})
    pprint(rows[:2], sort_dicts=False)

    # A dictionary of lists: one list per column
    columns = {"entry": [], "chain": [], "length": []}
    for entry, chain, length in iter_chains(SEVEN_CHAINS):
        columns["entry"].append(entry)
        columns["chain"].append(chain)
        columns["length"].append(length)
    pprint(columns, sort_dicts=False)

    # A dictionary of dictionaries: by entry, then by chain
    by_entry = {}
    for entry, chain, length in iter_chains(SEVEN_CHAINS):
        if entry not in by_entry:
            by_entry[entry] = {}
        by_entry[entry][chain] = length
    pprint(by_entry, sort_dicts=False)
    print(by_entry["104L"])
    print(by_entry["104L"]["B"])


if __name__ == "__main__":
    main()
