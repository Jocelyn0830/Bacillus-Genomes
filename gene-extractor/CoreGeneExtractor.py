import sqlite3

# with open('absence_presence/spi.csv', newline='') as csvfile:
#     reader = csv.DictReader(csvfile)
# for row in reader:
#     print(row['first_name'], row['last_name'])

# db_name = input("Please input database name: ")
con = sqlite3.connect("ap.db")
cur = con.cursor()
res = cur.execute(
    "SELECT gene_id, content FROM core_genes WHERE sequence_id == 'CBP-1645';")
genes = res.fetchall()
con.commit()

for gene_id, gene in genes:
    with open('reference/' + gene_id + '.fasta', 'w') as f:
        f.write('>' + gene_id + '\n')
        f.write(gene)
