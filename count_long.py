"""Count FASTA sequences longer than a cutoff the user chooses."""
import sys

FASTA_PATH = "data/pdb_protein.fasta"

# Ask for a cutoff until it's a whole number above 0
while True:
    answer = input("Cutoff length: ")
    try:
        cutoff = int(answer)
    except ValueError:
        print(f"'{answer}' is not a whole number. Try again.")
    else:
        if cutoff > 0:
            break
        print("The cutoff has to be more than zero. Try again.")

# The count starts at 0
count = 0
try:
    # Open the file. If it isn't there, print an error and stop.
    with open(FASTA_PATH, encoding="utf-8") as handle:
        # Another line? Take off the newline
        for line in handle:
            line = line.rstrip()
            # A header: skip to the next line
            if line.startswith(">"):
                continue
            # A sequence longer than the cutoff: add 1 to the count
            if len(line) > cutoff:
                count += 1
except FileNotFoundError:
    print(f"Error: cannot find {FASTA_PATH}", file=sys.stderr)
    sys.exit(1)

# No more lines: print the count
print(f"Sequences longer than {cutoff}: {count}")
