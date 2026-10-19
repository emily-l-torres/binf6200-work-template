"""Add up the residues in every PDB chain, and measure the memory it takes."""
import tracemalloc
from collections.abc import Iterator

PDB_PATH = "data/pdb_protein.fasta"


def iter_sequences(path: str) -> Iterator[str]:
    """
    Yield each sequence in a FASTA file that keeps each sequence on one line.

    @param path: the FASTA file to read
    @return: a generator of the sequences, one at a time, in file order
    """
    with open(path, encoding="utf-8") as handle:
        for line in handle:
            line = line.rstrip()
            if not line.startswith(">"):
                yield line


def main() -> None:
    """Total the residues, and print the most memory Python held at once."""
    tracemalloc.start()
    total = sum(len(sequence) for sequence in iter_sequences(PDB_PATH))
    peak = tracemalloc.get_traced_memory()[1]
    print(f"{total} residues, peak memory {peak / 1_000_000:.1f} MB")


if __name__ == "__main__":
    main()
