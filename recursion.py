"""Count one base in a DNA sequence with a function that calls itself."""


def count_base(sequence: str, base: str) -> int:
    """
    Count how many times a base appears in a sequence, one letter at a time.

    @param sequence: a DNA sequence
    @param base: the base to count, such as "G"
    @return: how many times base appears in sequence
    """
    if sequence == "":
        return 0
    if sequence[0] == base:
        return 1 + count_base(sequence[1:], base)
    return count_base(sequence[1:], base)


def main() -> None:
    """Count the G's in a short sequence, and check the answer against .count()."""
    print(count_base("GAG", "G"))
    print("GAG".count("G"))


if __name__ == "__main__":
    main()
