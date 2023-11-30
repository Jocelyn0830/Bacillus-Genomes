# Compute ER
Computes pairwise sequence divergence of all strains in the input fasta file

## Instructions
- Input file must be in fasta format
- Run `python3 computeER.py`
- Output file is a csv file that contains
  - names of strains
  - pairwise divergence of strains counting gap
  - pairwise divergence of strains without counting gap
  - number of mismatched nucleotides
  - number of gaps
