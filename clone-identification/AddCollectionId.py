from collections import defaultdict
import csv

def addCollectionId(filename):

    env_data = defaultdict(list)
    
    # take environment file as input, must include "Collection" column
    with open (filename, encoding='utf-8-sig') as envfile:
        csvreader = csv.DictReader(envfile)

        # put all info in a dictionary in below structure
        # data is a dict that holds info of each row
        # { collection_name : data }
        for row in csvreader:
            collection_name = row["Collection"]
            env_data[collection_name].append(row)
    

    collection_id = 1
    result = []
    for collection_name, data in env_data.items():

        # data contains all strains in one collection site
        for strain in data:
            # make collection_id using collection name
            # structure:
            # { "Collection_id" : collection_id, other data in each csv row}
            result_dict = {"Collection_id" : collection_id}
            result_dict.update(strain)
            result.append(result_dict)
            
        collection_id += 1

    return result

addCollectionId("environment_data.csv")

# write result csv file
data = addCollectionId("environment_data.csv")
header = list(data[0].keys())
output = open("data_collection_id.csv", "w")
writer = csv.DictWriter(output, fieldnames=header)
writer.writeheader()
for elt in data:
    print(elt)
    writer.writerow(elt)

