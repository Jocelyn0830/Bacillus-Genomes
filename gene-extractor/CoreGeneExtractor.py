import sqlite3

# with open('absence_presence/spi.csv', newline='') as csvfile:
#     reader = csv.DictReader(csvfile)
# for row in reader:
#     print(row['first_name'], row['last_name'])

# db_name = input("Please input database name: ")
con = sqlite3.connect("ia.db")
cur = con.cursor()
res = cur.execute(
    "SELECT gene_id, gene_name, content FROM core_genes WHERE sequence_id == 'CBP-1641';")
genes = res.fetchall()
con.commit()

gene_length_data = []
for gene_id, gene_name, gene in genes:
    gene_length_data.append((gene_name, len(gene)))
cur.executemany("INSERT or IGNORE INTO core_gene_with_length VALUES(?, ?)", gene_length_data)
con.commit()            
# add gene_name for easier later analysis
# for gene_id, gene_name, gene in genes:
#     with open('reference/' + gene_id + '.fasta', 'w') as f:
#         f.write('>' + gene_id + '|' + gene_name + '\n')
#         f.write(gene)
