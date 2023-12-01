from collections import defaultdict
import csv


soil_output = defaultdict(dict)
ele_output = defaultdict(dict)
with open('allstrains.csv', encoding='utf-8-sig') as infofile:
    csv_env = csv.DictReader(infofile)
    for row in csv_env:
        ecotype = row.get("Ecotype")
        if "sp" not in ecotype:
            continue
        # Soil
        soil_dict = soil_output.get(ecotype, {})

        soil_type = row.get("Soil_Type")
        if "Free" not in soil_dict:
            soil_dict["Free"] = 0
        if "Not Free" not in soil_dict:
            soil_dict["Not Free"] = 0  
        
        if soil_type =="Free":
            soil_dict[soil_type] += 1
        else:
            soil_dict["Not Free"] += 1
        
        soil_output[ecotype] = soil_dict
        
        # ele
        ele_dict = ele_output.get(ecotype, {})
        ele_type = row.get("Elevation_class")
        if not ele_type:
            continue
        if "Low" not in ele_dict:
            ele_dict["Low"] = 0
        if "Medium" not in ele_dict:
            ele_dict["Medium"] = 0
        if "High" not in ele_dict:
            ele_dict["High"] = 0

        ele_dict[ele_type] += 1
        ele_output[ecotype] = ele_dict


ele = []
for ecotype, env_info_dict in ele_output.items():
    if sum(env_info_dict.values()) < 5:
        continue
    ele.append(env_info_dict)
header = list(ele[0].keys())
output = open("ele.csv", "w")
writer = csv.DictWriter(output, fieldnames=header)
writer.writeheader()
for elt in ele:
    print(elt)
    writer.writerow(elt)

soil = []
for ecotype, env_info_dict in soil_output.items():
    if sum(env_info_dict.values()) < 5:
        continue
    soil.append(env_info_dict)
header = list(soil[0].keys())
output = open("soil.csv", "w")
writer = csv.DictWriter(output, fieldnames=header)
writer.writeheader()
for elt in soil:
    print(elt)
    writer.writerow(elt)