"""Keep asking for a sequence length until the answer is a positive whole number."""
while True:
    answer = input("Sequence length in bases: ")
    try:
        length = int(answer)
    except ValueError:
        print(f"'{answer}' is not a whole number. Try again.")
    else:
        if length > 0:
            break
        print("The length has to be more than zero. Try again.")
print(f"{length} bases hold {length // 3} whole codons")
