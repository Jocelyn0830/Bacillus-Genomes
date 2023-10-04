import csv
# Write an errorate dictionary
errorrate = {}
temp = []
species = input("Please enter the species name: ")
with open (species + "_errorrate.csv") as errfile:
    errreader = csv.reader(errfile)
    next(errreader)
    for row in errreader:
        temp.append(row)

for elt in temp:
    errorrate[(elt[0],elt[1])] = elt[5]

# The input csv file must be sorted alphabetically using Column D
data = []
with open (species + "_clones.csv") as file:
    csvreader = csv.reader(file)
    for row in csvreader:
        data.append(row)

collection_id = data[0][3]
strain = {collection_id : {(data[0][0],data[0][1]):data[0][4]}}
for i in range(1, len(data)):
    if data[i][3] == collection_id:
        to_add = strain[collection_id]
        to_add[(data[i][0],data[i][1])] = data[i][4]
        strain[collection_id] = to_add
    else:
        collection_id = data[i][3]
        strain[collection_id] = {(data[i][0],data[i][1]) : data[i][4]}

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
                if dic.get((elt,elt2)) != None:
                    entry.append(float((dic.get((elt,elt2)))))
                elif dic.get((elt2,elt)) != None:
                    entry.append(float((dic.get((elt2,elt)))))
                else:
                    if errorrate.get((elt,elt2)) != None:
                        entry.append(float((errorrate.get((elt,elt2)))))
                    else:
                        entry.append(float((errorrate.get((elt2,elt)))))
        matrix.append(entry)

    return matrix

def write_matrix(key):
    matrix = to_matrix(strain.get(key))
    newfilename = species + "_" +  key + '_matrix.csv'
    file = open(newfilename, "w")
    writer = csv.writer(file)
    for row in matrix:
        writer.writerow(row)

collection_id = []
for key in strain.keys():
    write_matrix(key)
    collection_id.append(int(key.replace('Collection','')))

print(collection_id)

