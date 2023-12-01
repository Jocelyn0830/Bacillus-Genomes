import csv

def TabulateNames(tree):
    names = {}
    for idx, clade in enumerate(tree.find_clades()):
        if clade.name:
            clade.name = "%d_%s" % (idx, clade.name)
        else:
            clade.name = str(idx)
        names[clade.name] = clade
    return names

def ParseCsv(filename):
    env_dict = {}
    with open (filename, encoding='utf-8-sig') as file:
        reader = csv.DictReader(file)
        for row in reader:
            strain = row['StrainName']
            if "*" not in strain:
                continue
            if row['Soil_Type'] == 'Free':
                soil_type = 'Free'
            else:
                soil_type = 'Not_Free'
            env_dict[strain.replace('*', '')] = {'Elevation': row['Elevation_class'], 'Soil_type': soil_type }
    
    return(env_dict)

def BranchGroupMatrix(env_dict, branch_dict):
    free_num_b0 = nfree_num_b0 = free_num_b1 = nfree_num_b1 = 0
    low_num_b0 = med_num_b0 = high_num_b0 = low_num_b1 = med_num_b1 = high_num_b1 = 0
    lis0 = branch_dict['0']
    for strain in lis0:
        strain_dict = env_dict[strain]
        elevation = strain_dict.get('Elevation',0)
        if elevation == 'Low':
            low_num_b0 += 1
        elif elevation == 'Medium':
            med_num_b0 += 1
        elif elevation == 'High':
            high_num_b0 += 1
        soil_type = strain_dict.get('Soil_type',0)
        if soil_type == 'Free':
            free_num_b0 += 1
        elif soil_type == 'Not_Free':
            nfree_num_b0 += 1

    lis1 = branch_dict['1']
    for strain in lis1:
        strain_dict = env_dict[strain]
        elevation = strain_dict.get('Elevation',1)
        if elevation == 'Low':
            low_num_b1 += 1
        elif elevation == 'Medium':
            med_num_b1 += 1
        elif elevation == 'High':
            high_num_b1 += 1
        soil_type = strain_dict.get('Soil_type',1)
        if soil_type == 'Free':
            free_num_b1 += 1
        elif soil_type == 'Not_Free':
            nfree_num_b1 += 1

    ele_matrix = [[low_num_b0, med_num_b0, high_num_b0], [low_num_b1, med_num_b1, high_num_b1]]
    soil_matrix = [[free_num_b0, nfree_num_b0], [free_num_b1, nfree_num_b1]]
    
    return (ele_matrix, soil_matrix)

def write_matrix(branch, matrix, type):
    newfilename = branch + '_' + type + '_matrix.csv'
    file = open(newfilename, "w")
    writer = csv.writer(file)
    if type == "elevation":
        writer.writerow(["low", 'medium', 'high'])
    if type == "soil_type":
        writer.writerow(['free', 'not_free'])
    for row in matrix:
        writer.writerow(row)


def writeBonCsv(species, variable):
    branch_p = {}
    with open (species + "_" + variable + ".txt") as file:
        for row in file:
            branch = row.split("_")[0]
            p_value = row.split("_")[1].replace("\n", '')
            branch_p[branch] = p_value

    branch_p = {k: v for k, v in sorted(branch_p.items(), key=lambda item: item[1])}
    k = len(branch_p)
    # k = 1

    new_values = []
    for branch, p in branch_p.items():
        alpha_value = 0.05 / k
        k -= 1
        # k += 1
        if float(p) < alpha_value:
            significant = "y"
        else: 
            significant = "n"
        temp_dict = { "branch_name" : branch, "p_value" : p, "alpha_value" : alpha_value, "significant?" : significant }
        new_values.append(temp_dict)

    newfilename = species + "_" + variable + "_bon.csv"
    file = open(newfilename, "w")
    writer = csv.DictWriter(file, fieldnames = ["branch_name", "p_value", "alpha_value", "significant?"])
    writer.writeheader()
    for elt in new_values:
        writer.writerow(elt)