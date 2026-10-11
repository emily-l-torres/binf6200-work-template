"""Loop over a dictionary's keys, then its keys and values together."""


def main() -> None:
    """Print the codon table two ways."""
    codon_table = {"ATG": "Met", "TGG": "Trp", "TAA": "Stop"}
    for codon in codon_table:
        print(codon)
    for codon, amino_acid in codon_table.items():
        print(f"{codon} codes for {amino_acid}")


if __name__ == "__main__":
    main()
    