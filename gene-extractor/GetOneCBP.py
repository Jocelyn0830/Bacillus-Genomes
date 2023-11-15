import sys
import os

cur_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(cur_dir))

from util import FastaToDict

filename = input("Please input filename: ")
gene_dict = FastaToDict.fastaToDict(filename)
strain_name = input("Please input strain name: ")

with open(strain_name + '.fasta', 'w') as f:
    f.write('>' + strain_name + '\n')
    f.write(gene_dict.get('>' + strain_name))
