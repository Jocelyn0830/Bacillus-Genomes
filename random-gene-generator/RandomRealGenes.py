from collections import defaultdict
import sqlite3
import random

con = sqlite3.connect("ap.db")
con.row_factory = lambda cursor, row: row[0]
cur = con.cursor()

# get all gene_names
gene_names_command = cur.execute("SELECT DISTINCT gene_name FROM real_core_genes")
gene_names = gene_names_command.fetchall()
sequence_ids_command = cur.execute("SELECT DISTINCT sequence_id FROM real_core_genes")
sequence_ids = sequence_ids_command.fetchall()
con.commit()
con.close()

con = sqlite3.connect("ap.db")
cur = con.cursor()

# Number of times to sample
num_samples = 500

# Number of genes to sample in each iteration
sample_size = 700

# List to store the results
sampled_gene_sets = []
gene_name_set = set()
for _ in range(num_samples):
    # Select 100 genes with replacement
    selected_genes = random.choices(gene_names, k=sample_size)
    gene_name_set.update(selected_genes)
    sampled_gene_sets.append(selected_genes)

gene_name_set = list(gene_name_set)

fetch_query = "SELECT gene_name, sequence_id, real_gene_content FROM real_core_genes WHERE gene_name IN ({})".format(", ".join(["?" for _ in gene_name_set]))

res = cur.execute(fetch_query, gene_name_set)
genes = res.fetchall()
con.commit()

sequence_gene_dict = {}
for gene_name, sequence_id, real_gene_content in genes:
    sequence_gene_dict[(gene_name, sequence_id)] = real_gene_content

def make_sample(gene_names, indicator):
    fasta_file_dict = defaultdict(str)
    for gene_name in gene_names:
        for sequence_id in sequence_ids:
            fasta_file_dict[sequence_id] += sequence_gene_dict.get((gene_name, sequence_id), "")
    
    len_of_content = len(fasta_file_dict[sequence_id])
    sample_name = "real_gene" + str(sample_size) + "_" + str(indicator) + ".fasta"

    with open(sample_name, 'w') as f:
        f.write('>amy' + '\n')
        f.write('-' * len_of_content + '\n')
        for sequence_id, content in fasta_file_dict.items():
            f.write('>' + sequence_id + '\n')
            f.write(content + '\n')

indicator = 1
for sample in sampled_gene_sets:
    make_sample(sample, indicator)
    indicator += 1