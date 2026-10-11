"""Look up codons in a dictionary, then add one and change one."""


def main() -> None:
    """Build a small codon table, and look things up in it."""
    codon_table = {"ATG": "Met", "TGG": "Trp", "TAA": "Stop"}
    print(codon_table["TGG"])
    print(len(codon_table))
    codon_table["GCC"] = "Ala"
    codon_table["TAA"] = "Stop (ochre)"
    print(codon_table)
    print("GCC" in codon_table)
    print("Trp" in codon_table)


if __name__ == "__main__":
    main()
    