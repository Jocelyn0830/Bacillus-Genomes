# Bootstrapped Ecotype
- calculates a bootstrapped score for each demarcated ecotype based on rarefaction results
- adds ecotype bootstrap score to the phylogenetic tree
- plots the phylogenetic tree with bootstrapped scores and ecotype annotation

## Instructions
Before bootstrapping ecotypes, you need
- rarefaction results (in .xml)

Instructions for running bootstrapped ecotype program
- Run `Bootstrapped.py` to caculate boostrap scores for all demarcated ecotypes based on rarefaction results
- Run `AddNodeLabel.py` to add bootstrapped ecotype scores to the phylogenetic tree and output an annotated tree in nhx format
- Run `PlotTree.R` to plot the phylogenetic tree with all additional information
