import csv

collection_ids = [12, 118, 122, 121, 63, 78, 81, 65, 67, 68, 70, 72, 73, 47, 119, 9, 10,
                  1, 3, 5, 6, 8, 43, 44, 46, 54, 57, 59, 60, 61, 74, 87, 89, 92, 93, 98, 100, 30, 31]
clone_res = []
for collection_id in collection_ids:
    with open('sp_data/sp_clone' + str(collection_id) + '.txt') as clone_file:
        next(clone_file)
        for row in clone_file:
            row = row.split()
            clone_res.append(
                [row[0].replace('"', ''), row[2].replace('"', '').replace("H1e-05_", '')])

with open('spi_clone_results.csv', 'w', newline='') as csvfile:
    clonewriter = csv.writer(csvfile)
    header = ['strain', 'clone_id']
    clonewriter.writerow(header)
    for entry in clone_res:
        clonewriter.writerow(entry)
