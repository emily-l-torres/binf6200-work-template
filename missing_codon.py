"""Ask a dictionary for a key it doesn't have, three ways."""


def main() -> None:
    """Look up TTT, which isn't in the table."""
    codon_table = {"ATG": "Met", "TGG": "Trp", "TAA": "Stop"}
    print(codon_table.get("TTT"))
    print(codon_table.get("TTT", "unknown"))
    print(codon_table["TTT"])


if __name__ == "__main__":
    main()
    