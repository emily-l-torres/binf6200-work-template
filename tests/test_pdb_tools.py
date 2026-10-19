"""Tests for pdb_tools.py, each starting from the same small FASTA file."""
from collections import Counter

import pytest

from pdb_tools import iter_chains, read_entry_ids


@pytest.fixture(name="small_fasta")
def fixture_small_fasta(tmp_path):
    """Write three chains from two entries to a FASTA file, and return its path."""
    path = tmp_path / "small.fasta"
    path.write_text(">101M:A:sequence\nMV\n>1ABC:A:sequence\nMK\n>1ABC:B:sequence\nMK\n",
                    encoding="utf-8")
    return path


def test_read_entry_ids_one_per_header(small_fasta):
    """Every header gives one entry ID, in the order of the file."""
    assert read_entry_ids(small_fasta) == ["101M", "1ABC", "1ABC"]


def test_read_entry_ids_counts_chains(small_fasta):
    """Counting the IDs gives each entry's number of chains."""
    assert Counter(read_entry_ids(small_fasta)) == {"101M": 1, "1ABC": 2}


def test_iter_chains_one_tuple_per_chain(small_fasta):
    """Each chain comes back as its entry, its chain and its length."""
    expected = [("101M", "A", 2), ("1ABC", "A", 2), ("1ABC", "B", 2)]
    assert list(iter_chains(small_fasta)) == expected
