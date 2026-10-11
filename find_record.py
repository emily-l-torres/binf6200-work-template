"""Find one record's sequence in the two lists get_fasta_lists gives back."""
from read_wrapped import get_fasta_lists


def main() -> None:
    """Look up 102L's sequence by its header."""
    headers, sequences = get_fasta_lists("data/wrapped3.fasta")
    position = headers.index("102L:A:sequence")
    print(position, len(sequences[position]))


if __name__ == "__main__":
    main()
