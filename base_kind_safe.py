"""Say whether a base is a purine or a pyrimidine, and refuse anything else."""
BASE = "N"
if BASE in ["A", "G"]:
    print("purine")
elif BASE in ["C", "T"]:
    print("pyrimidine")
else:
    raise ValueError(f"unknown base '{BASE}'")
