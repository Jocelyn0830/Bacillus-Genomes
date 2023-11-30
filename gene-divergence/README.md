# Gene divergence
- Computes average pairwise gene divergence/gene divergence percentage of all strains for a single gene
- Summarize single gene rarefaction results
- Plot a graph of the relationship between gene average divergence/gene divergence percentage and ecotype size for each species

## Instructions
Before calculating gene divergence, you need
- fasta files of all single genes
- all single gene rarefaction results

Instructions for running gene-divergence program
- Run `computeGeneDiv.py` to generate a csv file that contains gene_name, average pairwise divergence/average pairwise divergence percentage, and demarcated ecotype size
- Run `divergence.R` to plot the graph
