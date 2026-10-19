"""Join two small tables four ways, and see which rows each one keeps."""
import pandas as pd


def main() -> None:
    """Merge the same two tables with each value of how, and print each result."""
    proteins = pd.DataFrame({"entry": ["101M", "102L", "4hhb"],
                             "protein": ["myoglobin", "T4 lysozyme", "hemoglobin"]})
    per_entry = pd.DataFrame({"entry": ["101M", "102L", "104L"],
                              "count": [1, 1, 2],
                              "sum": [154, 165, 332]})
    for how in ["inner", "left", "right", "outer"]:
        print(f'how="{how}"')
        print(proteins.merge(per_entry, on="entry", how=how))


if __name__ == "__main__":
    main()
