"""Compare the genes with variants in two patients' samples."""
SAMPLE_1 = {"BRAF", "KRAS", "FGFR4", "TP53"}
SAMPLE_2 = {"BRAF", "FGFR4", "EGFR", "TP53"}

print(sorted(SAMPLE_1.intersection(SAMPLE_2)))
print(sorted(SAMPLE_1.difference(SAMPLE_2)))
print(sorted(SAMPLE_2.difference(SAMPLE_1)))
print(sorted(SAMPLE_1.union(SAMPLE_2)))
print(sorted(SAMPLE_1.symmetric_difference(SAMPLE_2)))
