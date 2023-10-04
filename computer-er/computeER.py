import csv
# a function to convert fasta file to dict
def fasta2dict(file):
    dic = {}
    cur_id = ''
    cur_seq = []
    for line in open(file):
        if line.startswith(">") and cur_id == '':
            cur_id = line.split(' ')[0].strip()
        elif line.startswith(">") and cur_id != '':
            dic[cur_id] = ''.join(cur_seq)
            cur_id = line.split(' ')[0].strip()
            cur_seq = []
        else:
            cur_seq.append(line.rstrip())
    dic[cur_id] = ''.join(cur_seq)
    return dic

# a function to find the gap and mismatch
def compare(seq1,seq2):
    mismatch = 0
    gap = 0
    for i in range(len(seq1)):
        if (seq1[i] == "-" or seq2[i] == "-"):
            gap += 1
        elif (seq1[i] != seq2[i]):
            mismatch += 1
    return (mismatch, gap)

def compute_ER(filename):
    dic = fasta2dict(filename)
    # convert dict to list for pairwise comparison
    l = list(dic.items())
    len_seq = len(l[0][1])
    newfilename = filename+"_errorrate.csv"
    file1 = open(newfilename, "w")
    writer = csv.writer(file1)
    header = ["name", "counting gap", "without gap", "number of mismatched nucleotides", "number of gaps"]
    writer.writerow(header)
    for i in range(len(l)):
        for j in range(i+1, len(l)):
            seq1 = l[i][1]
            seq2 = l[j][1]
            mis = compare(seq1,seq2)
            mis_rate_gap = (mis[0] + mis[1]) / float(len_seq)
            mis_rate = (mis[0]) / float(len_seq)
            mismatch_num = mis[0]
            gap_num = mis[1]
            L = [(l[i][0] + " and " + l[j][0]), mis_rate_gap, mis_rate, mismatch_num, gap_num]
            writer.writerow(L)

def compute_ER_wEnv(filename):
    dic = fasta2dict(filename)
    # convert dict to list for pairwise comparison
    l = list(dic.items())
    len_seq = len(l[0][1])

    seq_env = []
    with open ("strain_env.csv", 'r') as envfile:
        csvreader = csv.reader(envfile)
        next(csvreader)
        for row in csvreader:
            seq_env.append(row)

    dic_seqenv = dict(seq_env)

    newfilename = filename + "_errorrate_wenv.csv"
    file1 = open(newfilename, "w")
    writer = csv.writer(file1)
    header = ["name", "environmental data", "counting gap", "without gap", "number of mismatched nucleotides", "number of gaps"]
    writer.writerow(header)
    for i in range(len(l)):
        for j in range(i+1, len(l)):
            seq1 = l[i][1]
            seq2 = l[j][1]
            mis = compare(seq1,seq2)
            mis_rate_gap = (mis[0] + mis[1]) / float(len_seq)
            mis_rate = (mis[0]) / float(len_seq)
            mismatch_num = mis[0]
            gap_num = mis[1]

            env1 = dic_seqenv.get(l[i][0].replace('>',''))
            env2 = dic_seqenv.get(l[j][0].replace('>',''))
            if (env1 != None) and (env2 != None):
                L = [(l[i][0] + " and " + l[j][0]), (env1 + " and " + env2), mis_rate_gap, mis_rate, mismatch_num, gap_num]
            elif (env1 == None) and (env2 == None):
                L = [(l[i][0] + " and " + l[j][0]), ("NA and NA"), mis_rate_gap, mis_rate, mismatch_num, gap_num]
            elif (env1 == None):
                L = [(l[i][0] + " and " + l[j][0]), ("NA and " + env2), mis_rate_gap, mis_rate, mismatch_num, gap_num]
            else:
                L = [(l[i][0] + " and " + l[j][0]), (env1 + " and NA"), mis_rate_gap, mis_rate, mismatch_num, gap_num]
            writer.writerow(L)

filename = input("Please type the filename to compute error rate: ")
user_choice = input("Please indicate if you want to include the environmental data (y/n): ")
if (user_choice == 'y'):
    compute_ER_wEnv(filename)
else:
    compute_ER(filename)
