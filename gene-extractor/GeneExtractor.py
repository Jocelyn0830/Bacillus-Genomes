import sqlite3
import os

from util import fasta_to_dict
# extract CBP and gene names

# parse ffn filenames from Roary to only include CBP numbers


def parseFilename(filename):
    only_fname = filename.split("/")[1]
    first_b = only_fname.find('[')
    sec_b = only_fname.find(']')
    fname = only_fname[first_b+1:sec_b]

    return fname

# create data entries for SQLite table


def createData(filename):
    gene_dict = fasta_to_dict.fastaToDict(filename)
    data = []
    for header, content in gene_dict.items():
        sequence_id = parseFilename(filename)
        header_split = header.split(" ")
        gene_id = header_split[0].replace(">", "")
        name = " ".join(header_split[1:])
        data.append((sequence_id, gene_id, name, content))

    return data


if __name__ == "__main__":
    directory = input("Please type directory name: ")
    db_name = input("Please type database name: ")
    # find all files from directory
    for filename in os.listdir(directory):
        if filename == ".DS_Store":
            continue
        f = os.path.join(directory, filename)
        if os.path.isfile(f):
            # connect to database and insert data
            data = createData(f)
            con = sqlite3.connect(db_name + ".db")
            cur = con.cursor()
            cur.executemany(
                "INSERT or IGNORE INTO gene VALUES(?, ?, ?, ?)", data)
            con.commit()
            # res = cur.execute("SELECT sequence_id FROM gene")
            # print(res.fetchall())
