import csv
import os
from collections import defaultdict
import xml.etree.ElementTree as ET 
from Bio import Phylo
from ete3 import Tree


def parse_result(filename):
    # built in function to parse xml tree
    try:
        tree = ET.parse(filename) 
        root = tree.getroot() 

        ecotype_dict = defaultdict(list)
        for item in root.find("demarcation").find("ecotypes"):
            ecotype_name = item.get("number")
            member_list = item.findall("member")
            name_list = []

            for member in member_list:
                name_list.append(member.get("name"))

            ecotype_dict[ecotype_name] = name_list
        
        return ecotype_dict
    except:
        print(f)
    # with open(filename) as result:
    #     for row in result:
    #         if "<ecotypes number=" in row:

def get_clade(treefile):
    tree = Phylo.read(treefile, "newick")

    node_list = []
    internal_nodes = tree.get_nonterminals()
    for idx, clade in enumerate(internal_nodes):
        leaves = clade.get_terminals()
        temp = []
        for leaf in leaves:
            if leaf.name == "amy":
                continue
            temp.append(leaf.name)

            # put all singleton leaves in node_list
            if idx == 0:
                node_list.append([leaf.name])

        node_list.append(temp)
  
    return node_list

node_list = get_clade("ia/ia_tree.newick")
directory = "ia/ia-real"

bootstrap_dict = defaultdict(int)

for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    ecotype_dict = parse_result(f)
    if not ecotype_dict:
        continue
    for ecotype_name, members in ecotype_dict.items():
        bootstrap_dict[node_list.index(members)] += 1


# newfilename = 'ia/ia_bootstrapped_ecotype.csv'
# file = open(newfilename, "w")
# writer = csv.writer(file)

result = []
for node_idx, chances in bootstrap_dict.items():
    # writer.writerow([node_list[node_idx], chances/500])
    result.append((node_list[node_idx], chances/500))


# Put info on tree
tree_filename = "ia/ia_tree.newick"
tree_string = ""
with open(tree_filename, encoding='utf-8-sig') as treefile:
    for row in treefile:
        tree_string += row

t = Tree(tree_string)
outgroup = t.search_nodes(name="amy")[0]
t.set_outgroup(outgroup)
all_names = t.get_leaf_names()
all_names.remove("amy")
t.prune(all_names)

for node in t.traverse():
  if node.support >= 25.0:
    node.add_feature("proof", node.support)

for leaf_names, value in result:
    if len(leaf_names) == 1:
        leaf = t.get_leaves_by_name(name=leaf_names[0])
        leaf = leaf[0]
        leaf.add_feature("value", value*100)
    else:
        node = t.get_common_ancestor(leaf_names)
        node.add_feature("value", value*100)

output = t.write(features=["proof", "value"])
with open("ia/ia_bootstrapped_ecotype.nhx", "w") as nhx_file:
    nhx_file.write(output)

