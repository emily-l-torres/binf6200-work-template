"""Time two ways of counting the chains in the first 20,000 headers."""
import time
from collections import Counter

from pdb_tools import read_entry_ids

HEADERS_TO_COUNT = 20000


def count_with_list_count(entry_ids: list[str]) -> dict[str, int]:
    """
    Count each entry ID by asking the whole list, once per distinct ID.
    @param entry_ids: a list of entry IDs
    @return: a dictionary of each entry ID to how many times it appears
    """
    counts = {}
    for entry_id in set(entry_ids):
        counts[entry_id] = entry_ids.count(entry_id)
    return counts


def main() -> None:
    """Time list.count against a Counter, and check they agree."""
    entry_ids = read_entry_ids("data/pdb_protein.fasta")[:HEADERS_TO_COUNT]
    start = time.perf_counter()
    slow = count_with_list_count(entry_ids)
    slow_seconds = time.perf_counter() - start
    start = time.perf_counter()
    fast = Counter(entry_ids)
    fast_seconds = time.perf_counter() - start
    print(f"list.count: {slow_seconds:.3f} seconds")
    print(f"Counter:    {fast_seconds:.5f} seconds")
    print(f"Counter was {slow_seconds / fast_seconds:.0f} times faster")
    print("Same answer:", slow == fast)


if __name__ == "__main__":
    main()
    