# Bacillus-Genomes
- a collection of programs written for Bacillus Genome projects
- detailed instructions for running the programs can be found in `README.md` of each folder

## Bootstrapped Ecotype
- calculates a bootstrapped score for each demarcated ecotype based on rarefaction results
- adds ecotype bootstrap score to the phylogenetic tree
- plots the phylogenetic tree with bootstrapped scores and ecotype annotation

## Clone Identification
- Identifies all possible clone strains in a core genome alignment file

## Compute ER
- Computes pairwise sequence divergence of all strains in the input fasta file

## Gene Divergence
- Computes average pairwise gene divergence/gene divergence percentage of all strains for a single gene
- Summarize single gene rarefaction results
- Plot a graph of the relationship between gene average divergence/gene divergence percentage and ecotype size for each species

## Gene Extractor
- creates sql databases to store information of genes for each species
- extract all genes of the given species
- extract all core genes in a given core genome alignment file

## Gene Length
- a small program that graphs the distribution of gene length in each species

## Random Gene Generator
- generates random fake gene/real gene samples for rarefaction analysis. All sample with replacement
- generate single gene samples of all genes in a given species

## Rarefaction Analysis
analyzes and plot graphs of rarefaction results

## Rename
matches the new ecotype demarcations with past ecotype demarcations (kept as backup in case we need it in the future)

## Util
util folder that contains utility functions used in other programs
