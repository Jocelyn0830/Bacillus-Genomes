import sqlite3
import os

# extract CBP and gene names


def fasta2dict(fil):
    """
    Read fasta-format file fil, return dict of form scaffold:sequence.
    Note: Uses only the unique identifier of each sequence, rather than the 
    entire header, for dict keys. 
    """
    dic = {}
    cur_scaf = ''
    cur_seq = []
    for line in open(fil):
        if line.startswith(">") and cur_scaf == '':
            cur_scaf = line.rstrip()
        elif line.startswith(">") and cur_scaf != '':
            dic[cur_scaf] = ''.join(cur_seq)
            cur_scaf = line.rstrip()
            cur_seq = []
        else:
            cur_seq.append(line.rstrip())
    dic[cur_scaf] = ''.join(cur_seq)
    return dic


def createData(filename, sequence_id):
    gene_dict = fasta2dict(filename)
    data = []
    for header, content in gene_dict.items():
        header_split = header.split(" ")
        gene_id = header_split[0].replace(">", "")
        name = " ".join(header_split[1:])
        data.append((sequence_id, gene_id, name, content))

    return data


if __name__ == "__main__":
    directory = input("Please type directory name: ")
    for filename in os.listdir(directory):
        if filename == ".DS_Store":
            continue
        f = os.path.join(directory, filename)
        if os.path.isfile(f):
            data = createData(f, filename.replace(".fasta", ""))
            con = sqlite3.connect("gene.db")
            cur = con.cursor()
            cur.executemany(
                "INSERT or IGNORE INTO gene VALUES(?, ?, ?, ?)", data)
            con.commit()
            res = cur.execute("SELECT sequence_id FROM gene")
            print(res.fetchall())
