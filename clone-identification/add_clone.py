import csv

ecotype_dic = {}
for species in ["atrophaeus", "inaquosorum", "spizizenii"]:
    eco_lis = []
    with open ("Ecotype/"+species+"_ecotype.csv") as ecofile:
        csvreader = csv.reader(ecofile)
        next(csvreader)
        for row in csvreader:
            eco_lis.append(row)
        for elt in eco_lis:
            ecotype_dic[elt[1]] = species + "_" + elt[0]



env_data = []
with open ('environment_data_add_clone_group.csv', encoding='utf-8-sig') as envfile:
    csvreader = csv.DictReader(envfile)
    for row in csvreader:
        env_data.append(row)

clone = []
sp = [1, 116, 117, 119, 120, 29, 3, 42, 43, 45, 46, 53, 59, 6, 60, 62, 64, 66, 67, 69, 72, 73, 76, 8, 85, 87, 9, 90, 91, 96, 98]
atro = [101, 102, 104, 109, 110, 111, 112, 113, 114, 115, 12, 13, 15, 16, 18, 22, 23, 37, 60, 99]
iaq = [119, 121, 122, 13, 14, 2, 24, 28, 30, 31, 33, 36, 37, 40, 48, 51, 53, 58, 59, 60, 62, 63, 64, 7, 74, 79, 80, 81, 86, 89, 96]

clone_dict = {}
species = {"spizizenii" : sp, "atrophaeus" : atro, "inaquosorum" : iaq}
for (spe,col_lis) in species.items():
    for col_id in col_lis:
        with open (spe+"_clone"+str(col_id)+".txt") as file:
            next(file)
            clone = []
            for row in file:
                clone.append(row.split('\t'))
            for elt in clone:
                clone_dict[elt[0].replace('"','')] = elt[2].replace('"','').replace("_H1e-05",'').replace("\n",'')

fieldnames = list(env_data[0].keys()) + ["Clone_id", "Ecotype_id"]
newfilename = "clone.csv"
file1 = open(newfilename, "w")
writer = csv.DictWriter(file1, fieldnames = fieldnames)
writer.writeheader()
for elt in env_data:
    if clone_dict.get(elt.get("CBP_strain")) == None and (elt.get("Species") in list(species.keys())):
        elt["Clone_id"] = elt.get("Species")+"_"+elt.get("Collection_id").replace("C","c")+"_1"
        if ecotype_dic.get(elt.get("CBP_strain")) == None:
            elt["Ecotype_id"] = ''
        else:
            elt["Ecotype_id"] =  ecotype_dic.get(elt.get("CBP_strain"))
        writer.writerow(elt)
    elif clone_dict.get(elt.get("CBP_strain")) == None:
        elt["Clone_id"] = ''
        if ecotype_dic.get(elt.get("CBP_strain")) == None:
            elt["Ecotype_id"] = ''
        else:
            elt["Ecotype_id"] =  ecotype_dic.get(elt.get("CBP_strain"))
        writer.writerow(elt)
    else:
        elt["Clone_id"] = clone_dict.get(elt.get("CBP_strain"))
        if ecotype_dic.get(elt.get("CBP_strain")) == None:
            elt["Ecotype_id"] = ''
        else:
            elt["Ecotype_id"] =  ecotype_dic.get(elt.get("CBP_strain"))
        writer.writerow(elt)
