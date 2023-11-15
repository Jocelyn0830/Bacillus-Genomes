from collections import defaultdict
import random
import sys
import os

cur_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(cur_dir))

from util import FastaToDict

filename = "ap_amy_new.fasta"

strain_dict = FastaToDict.fastaToDict(filename)
content_length = len(list(strain_dict.values())[0])

starting_pos = [i for i in range(0, content_length-100)]

# Number of times to sample
num_samples = 500

# Number of genes to sample in each iteration
sample_size = 3

# List to store the results
sampled_gene_pos = []
for _ in range(num_samples):
    # Select 100 genes with replacement
    selected_starting_pos_list = random.choices(starting_pos, k=sample_size)
    pos_list = [(starting_pos, starting_pos+1000) for starting_pos in selected_starting_pos_list]
    sampled_gene_pos.append(pos_list)

def make_sample(positions, indicator):
    fasta_file_dict = defaultdict(str)
    for starting_pos, ending_pos in positions:
        for sequence_id, content in strain_dict.items():
            fasta_file_dict[sequence_id] += content[starting_pos:ending_pos]

    sample_name = "fake_gene" + str(sample_size) + "_" + str(indicator) + ".fasta"

    with open(sample_name, 'w') as f:
        for sequence_id, content in fasta_file_dict.items():
            f.write(sequence_id + '\n')
            f.write(content + '\n')

indicator = 1
for sample in sampled_gene_pos:
    make_sample(sample, indicator)
    indicator += 1
            


