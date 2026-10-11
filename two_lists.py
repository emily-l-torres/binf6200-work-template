"""Look up an amino acid with two lists that have to stay in step."""


def main() -> None:
    """Find TGG's amino acid, then sort one list and find it again."""
    codons = ["ATG", "TGG", "TAA"]
    amino_acids = ["Met", "Trp", "Stop"]
    print(amino_acids[codons.index("TGG")])
    codons.sort()
    print(amino_acids[codons.index("TGG")])


if __name__ == "__main__":
    main()
    