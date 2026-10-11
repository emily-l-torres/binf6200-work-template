"""Tests for pdb_tools.py, each writing its own small FASTA file."""
from collections import Counter

from pdb_tools import read_entry_ids


def test_read_entry_ids_one_per_header(tmp_path):
    """Every header gives one entry ID, in the order of the file."""
    path = tmp_path / "small.fasta"
    path.write_text(">101M:A:sequence\nMV\n>1ABC:A:sequence\nMK\n>1ABC:B:sequence\nMK\n",
                    encoding="utf-8")
    assert read_entry_ids(path) == ["101M", "1ABC", "1ABC"]


def test_read_entry_ids_counts_chains(tmp_path):
    """Counting the IDs gives each entry's number of chains."""
    path = tmp_path / "small.fasta"
    path.write_text(">101M:A:sequence\nMV\n>1ABC:A:sequence\nMK\n>1ABC:B:sequence\nMK\n",
                    encoding="utf-8")
    assert Counter(read_entry_ids(path)) == {"101M": 1, "1ABC": 2}
    