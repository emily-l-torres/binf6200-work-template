"""Report how many whole codons fit in a DNA sequence of a given length."""
length_text = input("Sequence length in bases: ")
length = int(length_text)
codons = length // 3
leftover = length % 3
print(f"{length} bases hold {codons} whole codons")
if leftover == 0:
    print("The length is a whole number of codons")
elif leftover == 1:
    print("1 base is left over at the end")
else:
    print("2 bases are left over at the end")
