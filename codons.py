"""Report how many whole codons fit in a DNA sequence of a given length."""
length_text = input("Sequence length in bases: ")
length = int(length_text)
codons = length // 3
leftover = length % 3
print(f"{length} bases hold {codons} whole codons")
if leftover != 0:
    print(f"{leftover} bases are left over at the end")
