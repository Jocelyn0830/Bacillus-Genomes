import sqlite3
import csv
import sys
import os

cur_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(cur_dir))

from util import FastaToDict

# take Roary's gene absence presence file as input


def findCoreGenes(filename):
    # find set of genes that are in core genome alignment
    with open(filename) as file:
        csvreader = csv.DictReader(file)
        core_gene_set = {}

        number_strains = 0
        for row in csvreader:
            number_strains = max(int(row["No. isolates"]), number_strains)
            core_gene_standard = number_strains * 0.99
            if int(row["No. isolates"]) >= core_gene_standard:
                row_list = list(row.items())
                # hard_coding start position of strains in Roary absence presence
                # can't figure out a better way to do this
                for strain, gene_id in row_list[14:]:
                        core_gene_set[gene_id] = row["Gene"]

    return core_gene_set


def parseFilename(filename):
    # parse ffn filenames from Roary to only include CBP numbers
    only_fname = filename.split("/")[1]
    first_b = only_fname.find('[')
    sec_b = only_fname.find(']')
    fname = only_fname[first_b+1:sec_b]

    return fname


def createData(filename, para):
    # create data entries for SQLite table
    gene_dict = FastaToDict.fastaToDict(filename)
    data = []
    if para == 'y':
        core_gene_set = findCoreGenes("sp_Absence_Presence.csv")

    for header, content in gene_dict.items():
        sequence_id = parseFilename(filename)
        header_split = header.split(" ")
        gene_id = header_split[0].replace(">", "")
        annotation = " ".join(header_split[1:])
        if para == 'y':
            if gene_id in core_gene_set:
                gene_name = core_gene_set[gene_id]
                data.append((sequence_id, gene_id, gene_name, annotation, content))
        else:
            data.append((sequence_id, gene_id, annotation, content))

    return data


if __name__ == "__main__":
    directory = input("Please type directory name: ")
    db_name = input("Please type database name: ")
    para = input(
        "Do you want to create a table that only includes core genes? (y/n)")
    # find all files from directory
    for filename in os.listdir(directory):
        if filename == ".DS_Store":
            continue
        f = os.path.join(directory, filename)
        if os.path.isfile(f):
            # connect to database and insert data
            data = createData(f, para)
            con = sqlite3.connect(db_name + ".db")
            cur = con.cursor()
            if para == 'y':
                cur.executemany(
                    "INSERT or IGNORE INTO core_genes VALUES(?, ?, ?, ?, ?)", data)
            else:
                cur.executemany(
                    "INSERT or IGNORE INTO all_genes VALUES(?, ?, ?, ?)", data)
            con.commit()
            # res = cur.execute("SELECT sequence_id FROM gene")
            # print(res.fetchall())
