# Random Gene Generator
- generates random fake gene/real gene samples for rarefaction analysis. All sample with replacement
- generate single gene samples of all genes in a given species

## Instructions
Before running the program, you need
- sql databases that store gene information created by `gene-extractor`

Instructions for running random gene generator program
- Run `DeleteClones.py` to dereplicate clones in your database if you haven't done so in gene-extractor step. This should be by default if you have clone results when you do that step.
- Run `RandomFakeGenes.py` to get random fake gene samples. You need to specify sample size and number of samples.
- Run `RandomRealGenes.py` to get random real gene samples. You need to specify sample size and number of samples.
- Run `AllOneGene.py` to generate single gene samples of all genes in a given species
- Run `./Rare.sh` to do rarefaction. You need to have  `Ecotype Simulation` installed and a tree generated using core genome alighment. (if you want to modify, run `chmod +x Rare.sh` to complie it before running it)
