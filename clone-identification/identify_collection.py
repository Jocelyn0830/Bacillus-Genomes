import csv
# The input file must be the output of the error rate program
def find_clone(filename):
    to_identify_clone = []
    with open (filename, encoding='utf-8-sig') as speciesfile:
        csvreader = csv.reader(speciesfile)
        next(csvreader)
        for row in csvreader:
            to_identify_clone.append(row)

    with open ('environment_data_add_clone_group.csv', encoding='utf-8-sig') as envfile:
        csv_env = csv.reader(envfile)
        next(csv_env)
        clone_group_dict = {}
        for row in csv_env:
            clone_group_dict[row[0]] = [row[3],row[4]]

    clone_pairs = []
    clone_groups = []
    for elt in to_identify_clone:
        if clone_group_dict.get(elt[0]) == clone_group_dict.get(elt[1]):
            if clone_group_dict.get(elt[1]) != None:
                row = [elt[0], elt[1]] +  clone_group_dict.get(elt[1]) + [elt[5]]
                clone_pairs.append(row)

    return clone_pairs

species = input("Please enter the species name: ")
clone_pairs = find_clone(species + '_errorrate.csv')
newfilename = species + '_clones.csv'
file1 = open(newfilename, "w")
writer = csv.writer(file1)
for row in clone_pairs:
    writer.writerow(row)
