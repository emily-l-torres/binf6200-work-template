"""A set keeps one of each."""
GENES_SEEN = ["BRAF", "KRAS", "BRAF", "TP53", "KRAS", "BRAF"]


def main():
    """Turn a list with repeats into a set, and look inside it."""
    unique = set(GENES_SEEN)
    print(len(GENES_SEEN))
    print(len(unique))
    print(sorted(unique))
    print(type(sorted(unique)))
    print("TP53" in unique)


if __name__ == "__main__":
    main()
    