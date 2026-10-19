"""Draw a volcano plot of the genes that change between pregnancy and lactation in mice."""
import math

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

RESULTS_PATH = "data/pregnant_vs_lactating.tsv"
PLOT_PATH = "volcano.png"
FDR_CUTOFF = 0.01
LOG2_FOLD_CUTOFF = 0.58
COLORS = {"Not significant": "#BBBBBB", "Higher in pregnancy": "#D55E00",
          "Higher in lactation": "#0072B2"}


def main() -> None:
    """Mark the genes past both cutoffs, then plot fold change against certainty."""
    genes = pd.read_csv(RESULTS_PATH, sep="\t")
    genes["minus_log10_fdr"] = -genes["adj.P.Val"].apply(math.log10)
    significant = genes["adj.P.Val"] < FDR_CUTOFF
    higher_in_pregnancy = significant & (genes["logFC"] > LOG2_FOLD_CUTOFF)
    higher_in_lactation = significant & (genes["logFC"] < -LOG2_FOLD_CUTOFF)
    genes["change"] = "Not significant"
    genes.loc[higher_in_pregnancy, "change"] = "Higher in pregnancy"
    genes.loc[higher_in_lactation, "change"] = "Higher in lactation"
    print(genes["change"].value_counts())
    axes = sns.scatterplot(data=genes, x="logFC", y="minus_log10_fdr",
                           hue="change", palette=COLORS, s=4, linewidth=0)
    sns.move_legend(axes, "upper right", markerscale=4, title=None)
    axes.axvline(-LOG2_FOLD_CUTOFF, color="gray", linestyle="--")
    axes.axvline(LOG2_FOLD_CUTOFF, color="gray", linestyle="--")
    axes.axhline(-math.log10(FDR_CUTOFF), color="gray", linestyle="--")
    axes.set_xlabel("log2 fold change, pregnancy vs lactation")
    axes.set_ylabel("-log10 FDR (adjusted P value)")
    axes.set_title(f"{len(genes)} genes in mouse luminal cells")
    plt.savefig(PLOT_PATH)


if __name__ == "__main__":
    main()
