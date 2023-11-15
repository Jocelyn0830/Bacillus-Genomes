from collections import defaultdict
import csv

# Write an errorate dictionary (clones.csv does not have all error rates)
errorrate = {}
with open("ap_errorrate.csv") as errfile:
    errreader = csv.DictReader(errfile)
    next(errreader)
    for row in errreader:
        errorrate[(row["name1"], row["name2"])] = row["without gap"]

# Find all pairs of strains
strain = defaultdict(dict)
with open("ap_clones.csv") as file:
    csvreader = csv.DictReader(file)
    for row in csvreader:
        collection_id = row["Collection_id"]
        names = (row["name1"], row["name2"])
        without_gap = row["without gap"]
        strain[collection_id][names] = without_gap

# Convert error rates into a matrix


def to_matrix(dic):
    strains = []
    for key in dic.keys():
        strains = strains + (list(key))
    strains = list(set(strains))

    matrix = [['']+strains]
    for elt in strains:
        entry = [elt]
        for elt2 in strains:
            if elt == elt2:
                entry.append(0)
            else:
                if dic.get((elt, elt2)):
                    entry.append(float(dic[(elt, elt2)]))
                elif dic.get((elt2, elt)):
                    entry.append(float(dic[(elt2, elt)]))
                else:
                    if errorrate.get((elt, elt2)):
                        entry.append(float(errorrate[(elt, elt2)]))
                    else:
                        entry.append(float(errorrate[(elt2, elt)]))
        matrix.append(entry)

    return matrix


def write_matrix(key):
    matrix = to_matrix(strain.get(key))
    newfilename = 'ap' + key + '_matrix.csv'
    file = open(newfilename, "w")
    writer = csv.writer(file)
    for row in matrix:
        writer.writerow(row)


collection_id = []
for key in strain.keys():
    write_matrix(key)
    collection_id.append(int(key.replace('Collection', '')))

print(collection_id)
