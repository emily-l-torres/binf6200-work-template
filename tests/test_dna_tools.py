"""Tests for dna_tools.py."""
import pytest
from dna_tools import gc_fraction

def test_gc_fraction_half():
    """Two of the four bases are G or C."""
    assert gc_fraction("ATGC") == 0.5


def test_gc_fraction_all():
    """Every base is G or C."""
    assert gc_fraction("GGCC") == 1.0


def test_gc_fraction_none():
    """No base is G or C."""
    assert gc_fraction("ATAT") == 0.0

def test_gc_fraction_lowercase():
    """Lowercase letters count the same as uppercase."""
    assert gc_fraction("atgc") == 0.5

def test_gc_fraction_empty():
    """An empty sequence has no GC fraction, so the function refuses it."""
    with pytest.raises(ValueError):
        gc_fraction("")
