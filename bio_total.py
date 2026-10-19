"""Total the residues in pdb_protein.fasta with Biopython's FASTA reader."""
import tracemalloc

from Bio import SeqIO

PDB_PATH = "data/pdb_protein.fasta"


def main() -> None:
    """Look at the first record, then total every record's residues and print the peak memory."""
    first = next(SeqIO.parse(PDB_PATH, "fasta"))
    print(first.id, len(first.seq))
    tracemalloc.start()
    total = sum(len(record.seq) for record in SeqIO.parse(PDB_PATH, "fasta"))
    peak = tracemalloc.get_traced_memory()[1]
    print(f"{total} residues, peak memory {peak / 1_000_000:.1f} MB")


if __name__ == "__main__":
    main()
