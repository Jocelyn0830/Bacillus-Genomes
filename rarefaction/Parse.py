import os
import re
import csv


ecotype_num, gene_number = [], []
for j in [1, 3, 7, 20, 100, 200, 400, 700]:
    for filename in os.listdir("sp-real/result/real"+str(j)):
        if ".txt" not in filename:
            continue
        with open("sp-real/result/real"+str(j)+ "/" + filename) as file:
            for row in file:
                if "<ecotypes size=" in row:
                    ecotype_num += (re.findall(
                        "[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?", row))
                    gene_number.append(j)

header = ["ecotype_size", "gene_number"]
with open('rand_ecotype_result.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(header)
    for i in range(len(ecotype_num)):
        data = [ecotype_num[i], gene_number[i]]
        writer.writerow(data)
