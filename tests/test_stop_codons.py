"""Tests for count_stop_codons in dna_tools.py, written before the function exists."""
from dna_tools import count_stop_codons


def test_one_stop():
    """ATG then TAA: one stop codon."""
    assert count_stop_codons("ATGTAA") == 1


def test_each_stop_counts():
    """TAA, TAG and TGA are all stop codons."""
    assert count_stop_codons("TAATAGTGA") == 3


def test_lowercase():
    """Case doesn't matter."""
    assert count_stop_codons("atgtaa") == 1


def test_out_of_frame():
    """The TAA in ATAAGC straddles two codons, ATA and AGC, so it isn't a stop codon."""
    assert count_stop_codons("ATAAGC") == 0


def test_leftover_bases():
    """Two bases left over after the last whole codon are ignored."""
    assert count_stop_codons("ATGTAATA") == 1


def test_empty():
    """No sequence, no stop codons."""
    assert count_stop_codons("") == 0
    