import sqlite3

# create database
db_name = input("Please input database name: ")
con = sqlite3.connect(db_name+".db")
cur = con.cursor()
cur.execute("CREATE TABLE gene(sequence_id, gene_id, name, content)")
