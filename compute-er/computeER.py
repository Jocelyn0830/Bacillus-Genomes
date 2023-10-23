import csv
import sys
import os

cur_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(cur_dir))

from util import FastaToDict

# a function to find the gap and mismatch


def compare(seq1, seq2):
    mismatch = 0
    gap = 0
    for i in range(len(seq1)):
        if (seq1[i] == "-" or seq2[i] == "-"):
            gap += 1
        elif (seq1[i] != seq2[i]):
            mismatch += 1
    return (mismatch, gap)


def compute_ER(filename, para):
    dic = FastaToDict.fastaToDict(filename)
    # convert dict to list for pairwise comparison
    l = list(dic.items())
    len_seq = len(l[0][1])

    if para == 'y':
        seq_env = []
        with open("strain_env.csv", 'r') as envfile:
            csvreader = csv.reader(envfile)
            next(csvreader)
            for row in csvreader:
                seq_env.append(row)

        dic_seqenv = dict(seq_env)

    newfilename = filename + "_errorrate_wenv.csv"
    file1 = open(newfilename, "w")
    writer = csv.writer(file1)
    header = ["name1", "name2",
              "counting gap", "without gap", "number of mismatched nucleotides", "number of gaps"]
    if para == 'y':
        header = header + ["environmental data1", "environmental data2"]

    writer.writerow(header)
    for i in range(len(l)):
        for j in range(i+1, len(l)):
            seq1 = l[i][1]
            seq2 = l[j][1]
            mis = compare(seq1, seq2)
            mis_rate_gap = (mis[0] + mis[1]) / float(len_seq)
            mis_rate = (mis[0]) / float(len_seq)
            mismatch_num = mis[0]
            gap_num = mis[1]

            strain_identifier1 = l[i][0].replace('>', '')
            strain_identifier2 = l[j][0].replace('>', '')

            L = [strain_identifier1, strain_identifier2,
                 mis_rate_gap, mis_rate, mismatch_num, gap_num]

            if para == 'y':
                env1 = dic_seqenv.get(strain_identifier1)
                env2 = dic_seqenv.get(strain_identifier2)
                L = L + [env1 if env1 else "NA", env2 if env2 else "NA"]

            writer.writerow(L)


filename = "sp_wo_amy.fasta"
# input("Please type the filename to compute error rate: ")
user_choice = input(
    "Please indicate if you want to include the environmental data (y/n): ")
compute_ER(filename, user_choice)
