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


def parse_filename(filename):
    only_fname = filename.split("/")[1]
    first_b = only_fname.find('[')
    sec_b = only_fname.find(']')
    fname = only_fname[first_b+1:sec_b]

    return fname


def createData(filename):
    gene_dict = fasta2dict(filename)
    data = []
    for header, content in gene_dict.items():
        sequence_id = parse_filename(filename)
        header_split = header.split(" ")
        gene_id = header_split[0].replace(">", "")
        name = " ".join(header_split[1:])
        data.append((sequence_id, gene_id, name, content))

    return data


if __name__ == "__main__":
    directory = input("Please type directory name: ")
    db_name = input("Please type database name: ")
    for filename in os.listdir(directory):
        if filename == ".DS_Store":
            continue
        f = os.path.join(directory, filename)
        if os.path.isfile(f):
            data = createData(f)
            con = sqlite3.connect(db_name + ".db")
            cur = con.cursor()
            cur.executemany(
                "INSERT or IGNORE INTO gene VALUES(?, ?, ?, ?)", data)
            con.commit()
            # res = cur.execute("SELECT sequence_id FROM gene")
            # print(res.fetchall())
