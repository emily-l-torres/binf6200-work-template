"""Read FASTA files whose sequences may wrap over several lines."""


def get_fasta_lists(path: str) -> tuple[list[str], list[str]]:
    """
    Read every header, and its sequence with any wrapped lines joined.

    @param path: the FASTA file to read
    @return: two lists in file order, the headers without their ">" and the sequences
    """
    headers = []
    sequences = []
    sequence = ""
    with open(path, encoding="utf-8") as handle:
        for line in handle:
            line = line.rstrip()
            if line.startswith(">"):
                if len(headers) > 0:
                    sequences.append(sequence)
                headers.append(line[1:])
                sequence = ""
            else:
                sequence += line
    if len(headers) > 0:
        sequences.append(sequence)
    return headers, sequences


def main() -> None:
    """Read the same three records wrapped and on one line, then a record with no sequence."""
    for path in ["data/wrapped3.fasta", "data/first3.fasta", "data/awkward.fasta"]:
        headers, sequences = get_fasta_lists(path)
        lengths = [len(sequence) for sequence in sequences]
        print(path, len(headers), "headers, lengths", lengths)


if __name__ == "__main__":
    main()
