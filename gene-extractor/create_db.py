import sqlite3

# create database
con = sqlite3.connect("gene.db")
cur = con.cursor()
cur.execute("CREATE TABLE gene(sequence_id, gene_id, name, content)")
