import csv
import sys
import os
import xml.etree.ElementTree as ET 

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

def compute_ER(filename):
    dic = FastaToDict.fastaToDict(filename)
    del dic[">amy"]
    # convert dict to list for pairwise comparison
    l = list(dic.items())
    len_seq = len(l[0][1])
    
    total_cmp = 0
    total_mismatch = 0
    total_mismatch_rate = 0
    for i in range(len(l)):
        for j in range(i+1, len(l)):
            seq1 = l[i][1]
            seq2 = l[j][1]
            mismatch_num, gap_num = compare(seq1, seq2)
            mis_rate = mismatch_num / float(len_seq)
            total_cmp += 1
            total_mismatch += mismatch_num
            total_mismatch_rate += mis_rate
    
    avg_mismatch = total_mismatch / float(total_cmp)
    avg_mismatch_rate = total_mismatch_rate / float(total_cmp)
    
    return (avg_mismatch, avg_mismatch_rate)

def get_ecotype_size(filename):
    tree = ET.parse(filename) 
    root = tree.getroot() 
    ecotype_size = root.find("demarcation").find("ecotypes").get("size")

    return ecotype_size

avg_mismatch_list = []
avg_mismatch_rate_list = []

directory = "gene_with_name/sp_gene_with_name/"
ecosim_directory = "one-gene/sp"
for filename in os.listdir(directory):
    gene_name = filename.replace(".txt", "")
    f = os.path.join(directory, filename)
    (avg_mismatch, avg_mismatch_rate) = compute_ER(f)

    ecosim_f = os.path.join(ecosim_directory, filename)
    ecotype_size = get_ecotype_size(ecosim_f)

    avg_mismatch_list.append([gene_name, str(avg_mismatch), str(ecotype_size)])
    avg_mismatch_rate_list.append([gene_name, str(avg_mismatch_rate), str(ecotype_size)])
   
newfilename = 'avg_mismatch_gene.csv'
file = open(newfilename, "w")
writer = csv.writer(file)
writer.writerow(["gene_name", "avg_mismatch", "ecotype_size"])
for elt in avg_mismatch_list:
    writer.writerow(elt)

newfilename1 = 'avg_mismatch_rate_gene.csv'
file1 = open(newfilename1, "w")
writer1 = csv.writer(file1)
writer1.writerow(["gene_name", "avg_mismatch_rate", "ecotype_size"])
for elt in avg_mismatch_rate_list:
    writer1.writerow(elt)
