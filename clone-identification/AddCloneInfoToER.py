import csv

# The input file must be the output of the error rate program
def find_clone(filename):
    to_identify_clone = []
    with open(filename, encoding='utf-8-sig') as speciesfile:
        csvreader = csv.DictReader(speciesfile)
        next(csvreader)
        for row in csvreader:
            to_identify_clone.append(row)

    with open('environment_data_add_clone_group.csv', encoding='utf-8-sig') as envfile:
        csv_env = csv.DictReader(envfile)
        next(csv_env)
        clone_group_dict = {}
        for row in csv_env:
            clone_group_dict[row["CBP_strain"]] = [row["Collection"], row["Collection_id"]]

    clone_pairs = []
    print(to_identify_clone)
    for elt in to_identify_clone:
        if clone_group_dict[elt["name1"]] and clone_group_dict[elt["name2"]] \
            and clone_group_dict[elt["name1"]] == clone_group_dict[elt["name2"]]:
            row = [elt["name1"], elt["name2"]] + \
                clone_group_dict[elt["name1"]] + [elt["without gap"]]
            clone_pairs.append(row)
            
    return clone_pairs


species = input("Please enter the species name: ")
clone_pairs = find_clone(species + '_errorrate.csv')
newfilename = species + '_clones.csv'
file1 = open(newfilename, "w")
writer = csv.writer(file1)
writer.writerow("name1", "name2", "LabName", "Collection_id", "without gap")
for row in clone_pairs:
    writer.writerow(row)
