import csv

# Column D 'Collection' needs to be sorted alphabetically before running
def add_clone_names(filename):
    env_data = []
    with open (filename, encoding='utf-8-sig') as envfile:
        csvreader = csv.DictReader(envfile)
        for row in csvreader:
            env_data.append(row)

    clone_group_number = 1
    collection_name = env_data[0].get('Collection')
    first_row = env_data[0]
    first_row_add = [first_row.get('CBP_strain'), first_row.get('ChrisName'),
            first_row.get('LabName'), first_row.get('Collection'), 'Collection1', first_row.get('Species'),first_row.get('Soil_Type'), first_row.get('Elevation'), first_row.get('Lat_Degrees'), first_row.get('Lat_Min'), first_row.get('Lon_Degress'), first_row.get('Lon_Min'), first_row.get('Date')]
    env_data_add_group = [first_row_add]
    for i in range(1,len(env_data)):
        elt = env_data[i]
        one_row = [elt.get('CBP_strain'), elt.get('ChrisName'), elt.get('LabName'), elt.get('Collection'), elt.get('Species'), elt.get('Soil_Type'), elt.get('Elevation'), elt.get('Lat_Degrees'), elt.get('Lat_Min'), elt.get('Lon_Degrees'), elt.get('Lon_Min'), elt.get('Date')]
        if elt.get('Collection') == collection_name:
            one_row.insert(one_row.index(elt.get('Collection'))+1, 'Collection'+str(clone_group_number))
        else:
            collection_name = elt.get('Collection')
            clone_group_number += 1
            one_row.insert(one_row.index(elt.get('Collection'))+1, 'Collection'+str(clone_group_number))

        env_data_add_group.append(one_row)

    return(env_data_add_group)

data = add_clone_names("environment_data.csv")

header = ['CBP_strain', 'ChrisName','LabName','Collection', 'Collection_id','Species','Soil_Type', 'Elevation','Lat_Degrees','Lat_Min','Lon_Degrees','Lon_Min','Date']
newfilename = 'environment_data_add_clone_group.csv'
file1 = open(newfilename, "w")
writer = csv.writer(file1)
writer.writerow(header)
for elt in data:
    writer.writerow(elt)

