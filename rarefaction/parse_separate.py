import re
import csv

npop, omega, sigma, likelihood, ecotype_num, gene_num = [], [], [], [], [], []

for j in [1, 3, 7, 20, 100, 700]:
    for i in range(1, 501):
        with open("result/real"+str(j)+"/gene"+str(j) + "_" + str(i) + ".txt", 'r') as file:
            for row in file:
                if "npop" in row and "omega" in row and "sigma" in row and "likelihood" in row:
                    temp = row.split(" ")
                    for elt in temp:
                        if "npop" in elt:
                            npop += (re.findall(
                                "[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?", elt))
                        elif "omega" in elt:
                            omega += (re.findall(
                                "[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?", elt))
                        elif "sigma" in elt:
                            sigma += (re.findall(
                                "[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?", elt))
                        elif "likelihood" in elt:
                            likelihood += (re.findall(
                                "[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?", elt))
                elif "<ecotypes size=" in row:
                    ecotype_num += (re.findall(
                        "[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?", row))
                    gene_num.append(j)

    header = ["ecotype_size", "npop", "omega", "sigma", "likelihood"]
    with open('real' + str(j) + '_result.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        for i in range(len(ecotype_num)):
            data = [ecotype_num[i], npop[i], omega[i], sigma[i], likelihood[i]]
            writer.writerow(data)

header = ["ecotype_size", "npop", "omega", "gene_numebr"]
with open('rand_eco_npop_omega_result.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(header)
    for i in range(len(ecotype_num)):
        data = [ecotype_num[i], npop[i], omega[i], gene_num[i]]
        writer.writerow(data)
