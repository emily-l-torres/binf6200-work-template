"""Build a pandas DataFrame from a list of dictionaries, and from a dictionary of lists."""
import pandas as pd


def main() -> None:
    """Make the same three-row table from each shape, and compare them."""
    rows = [
        {"entry": "103L", "chain": "A", "length": 167},
        {"entry": "104L", "chain": "A", "length": 166},
        {"entry": "104L", "chain": "B", "length": 166},
    ]
    columns = {
        "entry": ["103L", "104L", "104L"],
        "chain": ["A", "A", "B"],
        "length": [167, 166, 166],
    }
    from_rows = pd.DataFrame(rows)
    from_columns = pd.DataFrame(columns)
    print(from_rows)
    print(from_rows.equals(from_columns))
    print(type(from_rows["length"]))
    print(from_rows["length"].max())


if __name__ == "__main__":
    main()
