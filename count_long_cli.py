"""Count FASTA sequences longer than a cutoff given on the command line."""
import argparse
import sys


def get_cli_args():
    """
    Read the command line.

    @return: the parsed arguments, with .fasta and .cutoff
    """
    parser = argparse.ArgumentParser(
        description="Count FASTA sequences longer than a cutoff")
    parser.add_argument("-f", "--fasta", default="data/pdb_protein.fasta",
                        help="the FASTA file to read")
    parser.add_argument("-c", "--cutoff", type=int, default=1000,
                        help="count sequences longer than this")
    return parser.parse_args()


def count_longer(path: str, cutoff: int) -> int:
    """
    Count the sequences in a FASTA file that are longer than a cutoff.

    @param path: the FASTA file to read
    @param cutoff: the length a sequence must be longer than
    @return: how many sequences are longer than the cutoff
    """
    count = 0
    with open(path, encoding="utf-8") as handle:
        for line in handle:
            line = line.rstrip()
            if line.startswith(">"):
                continue
            if len(line) > cutoff:
                count += 1
    return count


def main():
    """Read the command line, count, and report."""
    args = get_cli_args()
    try:
        count = count_longer(args.fasta, args.cutoff)
    except FileNotFoundError:
        print(f"Error: cannot find {args.fasta}", file=sys.stderr)
        sys.exit(1)
    print(f"Sequences longer than {args.cutoff}: {count}")


if __name__ == "__main__":
    main()
    