"""Report how many sequences one or more FASTA files hold, and their total length."""
import argparse


def get_cli_args():
    """
    Read the command line.

    @return: the parsed arguments
    """
    parser = argparse.ArgumentParser(
        description="Count FASTA sequences, and their total length")
    parser.add_argument("fasta", nargs="+",
                        help="one or more FASTA files to read")
    parser.add_argument("--molecule", required=True,
                        choices=["dna", "protein"],
                        help="what the sequences are")
    parser.add_argument("-m", "--min-length", type=int, default=1,
                        help="leave out sequences shorter than this")
    parser.add_argument("-v", "--verbose", action="store_true",
                        help="say which file is being read")
    return parser.parse_args()


def measure(path, min_length):
    """
    Count the sequences in a FASTA file, and add up their lengths.

    Each sequence must be on one line, as in pdb_protein.fasta.

    @param path: the FASTA file to read
    @param min_length: leave out sequences shorter than this
    @return: a tuple of how many sequences, and their total length
    """
    count = 0
    total = 0
    with open(path, encoding="utf-8") as handle:
        for line in handle:
            line = line.rstrip()
            if line.startswith(">"):
                continue
            if len(line) >= min_length:
                count += 1
                total += len(line)
    return count, total


def main():
    """Read the command line, measure each file, and report."""
    args = get_cli_args()
    if args.molecule == "dna":
        unit = "bases"
    else:
        unit = "residues"
    for path in args.fasta:
        if args.verbose:
            print(f"Reading {path}")
        count, total = measure(path, args.min_length)
        print(f"{path}: {count} sequences, {total} {unit}")


if __name__ == "__main__":
    main()
    