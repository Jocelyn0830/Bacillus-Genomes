import csv
# sp
# collection_ids = [81, 82, 37, 38, 84, 40, 43, 87, 89, 91, 93, 94, 95, 96, 97, 98, 45, 99, 100, 101, 102, 105, 106, 51, 54, 112, 55, 56, 24, 57, 26, 115, 116, 65, 68, 120, 74, 70]

# ap
#collection_ids = [1, 36, 15, 37, 38, 40, 41, 42, 43, 19, 46, 47, 48, 52, 53, 54, 55, 56, 24, 58, 60, 62, 64, 67, 68, 69, 70, 72, 73, 75, 78, 35]

# ap
collection_ids = [3, 4, 5, 6, 13, 14, 16, 17, 18, 1, 20, 21, 22, 23, 24, 27, 29, 30, 33, 34, 35]

clone_res = []
for collection_id in collection_ids:
    with open('ap_clone' + str(collection_id) + '.txt') as clone_file:
        next(clone_file)
        for row in clone_file:
            row = row.split()
            clone_res.append(
                [row[0].replace('"', ''), row[2].replace('"', '').replace("H1e-05_", '')])

with open('ap_clone_results.csv', 'w', newline='') as csvfile:
    clonewriter = csv.writer(csvfile)
    header = ['strain', 'clone_id']
    clonewriter.writerow(header)
    for entry in clone_res:
        clonewriter.writerow(entry)
