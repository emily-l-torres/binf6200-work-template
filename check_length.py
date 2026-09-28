"""Refuse a sequence length that cannot be real."""
length = int(input("Sequence length in bases: "))
if length <= 0:
    raise ValueError(f"the length has to be more than zero, and you gave {length}")
print(f"{length} bases hold {length // 3} whole codons")
