import sys
import os
import csv



cur_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(cur_dir))

from util import FastaToDict


gyra = FastaToDict.fastaToDict("sp_gyra_aligned.txt")


def compare(seq1, seq2):
    mismatch = 0
    gap = 0
    for i in range(len(seq1)):
        if (seq1[i] == "-" or seq2[i] == "-"):
            gap += 1
        elif (seq1[i] != seq2[i]):
            mismatch += 1
    return (mismatch, gap)


ecotype1 = ">CBP-2263"
ecotype2 = ">CBP-1811"
ecotype3 = ">CBP-2114"
ecotype4 = ">CBP-1647"
ecotype5 = ">CBP-1702"

# ecotype6 = ">_pos=388795-389651_CBP-1698"
# ecotype7 = ">_pos=388933-389789_CBP-1887"
# ecotype8 = ">_pos=388798-389654_CBP-2214"
# ecotype10 = ">_pos=388552-389408_CBP-2263"
ecotype_list = [ecotype1, ecotype2, ecotype3,
                ecotype4, ecotype5]

len_seq = len(gyra.get(ecotype1))

result = [[], [], [], [], []]
for key, val in gyra.items():
    if key in ecotype_list:
        continue
    i = 0
    for e in ecotype_list:
        mis = compare(gyra.get(e), val)
        mis_rate_gap = (mis[0] + mis[1]) / float(len_seq)
        mis_rate = (mis[0]) / float(len_seq)
        mismatch_num = mis[0]
        gap_num = mis[1]
        temp = [key[1:], mis_rate_gap, mis_rate, mismatch_num, gap_num]
        result[i].append(temp)
        i += 1

newfilename = "gyra_errorrate.csv"
file1 = open(newfilename, "w")
writer = csv.writer(file1)
temp = ["new_ecotype_1", "new_ecotype_2", "new_ecotype_3",
        "new_ecotype_4", "new_ecotype_5", 
        # "new_ecotype_6",
        # "new_ecotype_7", "new_ecotype_8", "new_ecotype_10"
        ]
header = []
header = []
for e in temp:
    header = header + [e, "rate_gap", "rate", "mismatch_num", "with_gap_mis"]

writer.writerow(header)
for i in range(len(result[0])):
    res = []
    for j in range(len(result)):
        res = res + result[j][i]
    writer.writerow(res)
