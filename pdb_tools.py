"""Functions for reading a PDB FASTA file."""
from collections.abc import Iterator

import pandas as pd

def read_entry_ids(path: str) -> list[str]:
    """
    Read the PDB entry ID from every header in a FASTA file.

    In >101M:A:sequence, 101M is the entry and A is the chain.
    @param path: the FASTA file to read
    @return: a list of entry IDs, one per header, such as "101M"
    """
    entry_ids = []
    with open(path, encoding="utf-8") as handle:
        for line in handle:
            line = line.rstrip()
            if line.startswith(">"):
                entry_ids.append(line[1:].split(":")[0])
    return entry_ids


def iter_chains(path: str) -> Iterator[tuple[str, str, int]]:
    """
    Yield each chain's entry ID, chain ID and length from a FASTA file.

    The file has to keep each sequence on one line, as pdb_protein.fasta does.
    @param path: the FASTA file to read
    @return: a generator of (entry ID, chain ID, length) tuples
    """
    entry_id = ""
    chain_id = ""
    with open(path, encoding="utf-8") as handle:
        for line in handle:
            line = line.rstrip()
            if line.startswith(">"):
                fields = line[1:].split(":")
                entry_id = fields[0]
                chain_id = fields[1]
            else:
                yield entry_id, chain_id, len(line)

def load_chains(path: str) -> pd.DataFrame:
    """
    Load every chain in a FASTA file into a table, one row per chain.

    @param path: the FASTA file to read, with each sequence on one line
    @return: a DataFrame with the columns entry, chain and length
    """
    return pd.DataFrame(iter_chains(path),
                        columns=["entry", "chain", "length"])
