import sqlite3
import csv

with open('absence_presence/spi.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    # for row in reader:
    #     print(row['first_name'], row['last_name'])

db_name = input("Please input database name: ")
con = sqlite3.connect(db_name+".db")
cur = con.cursor()
res = cur.execute(
    "SELECT sequence_id, gene_id, name, content FROM gene WHERE sequence_id == 'CBP-2196';")
con.commit()
print(type(res))
