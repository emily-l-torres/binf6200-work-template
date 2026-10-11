"""Functions for reading the headers in a PDB FASTA file."""


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
