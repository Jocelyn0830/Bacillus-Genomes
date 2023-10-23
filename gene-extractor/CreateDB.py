import sqlite3

# create database
db_name = input("Please input database name: ")
con = sqlite3.connect(db_name+".db")
cur = con.cursor()
cur.execute("CREATE TABLE all_genes(sequence_id, gene_id, annotation, content)")
cur.execute("CREATE TABLE core_genes(sequence_id, gene_id, gene_name, annotation, content)")
