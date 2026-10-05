"""Borrow gc_fraction from dna_tools.py instead of writing it again."""
from dna_tools import gc_fraction

print(gc_fraction("GGCC"))