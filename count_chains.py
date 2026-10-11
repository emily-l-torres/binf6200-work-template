"""Count the chains in each PDB entry, four ways, and check they agree."""
from collections import Counter, defaultdict

from pdb_tools import read_entry_ids


def count_with_if(entry_ids: list[str]) -> dict[str, int]:
    """
    Count each entry ID, asking first whether it's been seen.
    @param entry_ids: a list of entry IDs
    @return: a dictionary of each entry ID to how many times it appears
    """
    counts = {}
    for entry_id in entry_ids:
        if entry_id in counts:
            counts[entry_id] += 1
        else:
            counts[entry_id] = 1
    return counts


def count_with_get(entry_ids: list[str]) -> dict[str, int]:
    """
    Count each entry ID with .get(), which gives 0 for one not seen yet.
    @param entry_ids: a list of entry IDs
    @return: a dictionary of each entry ID to how many times it appears
    """
    counts = {}
    for entry_id in entry_ids:
        counts[entry_id] = counts.get(entry_id, 0) + 1
    return counts


def count_with_defaultdict(entry_ids: list[str]) -> dict[str, int]:
    """
    Count each entry ID with a defaultdict, which starts a new key at 0.
    @param entry_ids: a list of entry IDs
    @return: a dictionary of each entry ID to how many times it appears
    """
    counts = defaultdict(int)
    for entry_id in entry_ids:
        counts[entry_id] += 1
    return counts


def count_with_counter(entry_ids: list[str]) -> dict[str, int]:
    """
    Count each entry ID with a Counter, which does the whole loop itself.
    @param entry_ids: a list of entry IDs
    @return: a Counter of each entry ID to how many times it appears
    """
    return Counter(entry_ids)


def main() -> None:
    """Count the chains in every entry four ways, and compare the answers."""
    entry_ids = read_entry_ids("data/pdb_protein.fasta")
    by_if = count_with_if(entry_ids)
    by_get = count_with_get(entry_ids)
    by_defaultdict = count_with_defaultdict(entry_ids)
    by_counter = count_with_counter(entry_ids)
    print(len(entry_ids), "chains in", len(by_if), "entries")
    print("1OTZ has", by_if["1OTZ"], "chains")
    print(by_if == by_get == by_defaultdict == by_counter)


if __name__ == "__main__":
    main()
