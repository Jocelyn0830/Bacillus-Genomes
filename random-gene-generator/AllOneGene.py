from collections import defaultdict
import sqlite3

con = sqlite3.connect("ia.db")
cur = con.cursor()
fetch_query = "SELECT gene_name, sequence_id, real_gene_content FROM real_core_genes"

res = cur.execute(fetch_query)
genes = res.fetchall()
con.commit()

sequence_gene_dict = defaultdict(list)
for gene_name, sequence_id, real_gene_content in genes:
    sequence_gene_dict[gene_name].append((sequence_id, real_gene_content))

for gene_name, content_list in sequence_gene_dict.items():
    sample_name = "gene_with_name/" + gene_name + ".txt"
    len_of_content = len(content_list[0][1])
    with open(sample_name, 'w') as f:
        f.write('>amy' + '\n')
        f.write('-' * len_of_content + '\n')
        for sequence_id, content in content_list:
            f.write('>' + sequence_id + '\n')
            f.write(content + '\n')