import re
import csv


ecotype_num, gene_number = [], []
for j in [1, 3, 7, 20, 100, 700]:
    for i in range(1, 501):
        with open("ap-fake/result/fake"+str(j)+"/gene"+str(j)+"_" + str(i) + ".txt", 'r') as file:
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
