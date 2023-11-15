import sys
import os
import csv



cur_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(cur_dir))

from util import FastaToDict

ap_clone_set = set()
sp_clone_set = set()
ia_clone_set = set()
with open("clone_summary.csv", encoding='utf-8-sig') as speciesfile:
    csvreader = csv.DictReader(speciesfile)
    for row in csvreader:
        ap_clone_set.add(row["ap"])
        sp_clone_set.add(row["sp"])
        ia_clone_set.add(row["ia"])

for species in ["ap", "ia", "sp"]:
    filename = species + ".fasta"
    gene_dict = FastaToDict.fastaToDict(filename)

    with open(species + '_rm_clones.fasta', 'w') as f:
        for key, value in gene_dict.items():
            strain_name = key.replace('>', '')
            if (species == "ap" and strain_name not in ap_clone_set) or \
               (species == "sp" and strain_name not in sp_clone_set) or \
               (species == "ia" and strain_name not in ia_clone_set):
                f.write(key + '\n')
                f.write(value + '\n')
            