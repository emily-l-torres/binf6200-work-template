"""A function that calls itself, with no case that stops it."""


def count_base(sequence: str, base: str) -> int:
    """Count a base, but never stop: there's no base case."""
    return sequence[:1].count(base) + count_base(sequence[1:], base)


def main() -> None:
    """Count the G's in a short sequence, and never finish."""
    print(count_base("GATTACAGG", "G"))


if __name__ == "__main__":
    main()
