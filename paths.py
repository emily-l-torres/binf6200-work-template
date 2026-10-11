"""Find the FASTA files in data, and take one path apart."""
from pathlib import Path


def main() -> None:
    """List the FASTA files in data, then look at one path's parts."""
    data_dir = Path("data")
    for path in sorted(data_dir.glob("*.fasta")):
        print(path)
    tiny = data_dir / "tiny.fasta"
    print(tiny.name, tiny.stem, tiny.suffix)
    print(tiny.exists(), (data_dir / "nothing.fasta").exists())


if __name__ == "__main__":
    main()
    