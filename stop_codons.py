"""A tuple can't be changed once it's made."""
STOP_CODONS = ("TAA", "TAG", "TGA")

print(STOP_CODONS[0])
print("TGA" in STOP_CODONS)
STOP_CODONS[0] = "TTT"
