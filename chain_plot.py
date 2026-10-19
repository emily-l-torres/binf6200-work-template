"""Plot how long the chains in pdb_protein.fasta are."""
import matplotlib.pyplot as plt
import seaborn as sns

from pdb_tools import load_chains

PDB_PATH = "data/pdb_protein.fasta"
PLOT_PATH = "chain_lengths.png"


def main() -> None:
    """Draw a histogram of the chain lengths, and save it as a PNG file."""
    chains = load_chains(PDB_PATH)
    axes = sns.histplot(data=chains, x="length", log_scale=True)
    axes.set_xlabel("Chain length (residues, log scale)")
    axes.set_ylabel("Number of chains")
    axes.set_title(f"The {len(chains)} chains in pdb_protein.fasta")
    plt.savefig(PLOT_PATH)


if __name__ == "__main__":
    main()
