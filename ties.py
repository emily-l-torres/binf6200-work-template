"""Break ties on purpose when sorting PDB entries by chain count."""


def main() -> None:
    """Sort four entries, in two ties, biggest count first, two ways."""
    counts = {"1P0T": 60, "3HF9": 56, "1OTZ": 60, "2APU": 56}
    reversed_ties = sorted(counts.items(), key=lambda pair: (pair[1], pair[0]),
                           reverse=True)
    print(reversed_ties)
    most_first = sorted(counts.items(), key=lambda pair: (-pair[1], pair[0]))
    print(most_first)


if __name__ == "__main__":
    main()
