from Bio import Phylo
import util

species = input("Please input the species name: ")
tree = Phylo.read(species + ".nwk", "newick")


def MakeTerminalDict(curr_clade):
    clade_CBPs = []
    for clade in curr_clade.get_terminals():
        clade_name = str(clade)
        start_index = clade_name.find("CBP")
        strain = clade_name[start_index:]
        clade_CBPs.append(strain)
    return clade_CBPs

# The first branch is all other and the root
# Thus we just need to go to the all other branches and keep going,
# We can just keep making subtrees
clade_pos = [0]
curr_clade = Phylo.BaseTree.Tree.from_clade(tree.clade[0])
# print(curr_clade)
# print(len(curr_clade.get_terminals()))

names = util.TabulateNames(tree)


group_CBPs = {}
for name in names.keys():
    curr_clade = names[name]
    if (len(curr_clade.get_nonterminals()) < 2) or (len(curr_clade[0].get_terminals())< 5) or (len(curr_clade[1].get_terminals()) < 5):
        continue
    
    subclade_CBPs = {}
    subclade_0_list = MakeTerminalDict(curr_clade[0])
    subclade_CBPs['0'] = subclade_0_list
    subclade_1_list = MakeTerminalDict(curr_clade[1])
    subclade_CBPs['1'] = subclade_1_list
    group_CBPs[name] = subclade_CBPs
    print(name, subclade_0_list, subclade_1_list)


env_dict = util.ParseCsv('info.csv')

branch_names = ""
for elt in group_CBPs.keys():
    branch_names = branch_names + "," + elt
    
branch_names = branch_names[1:]
print(branch_names)

for branch, branch_dict in group_CBPs.items():
    (ele_matrix, soil_matrix) = util.BranchGroupMatrix(env_dict, branch_dict)
    util.write_matrix(branch, ele_matrix, "elevation")
    util.write_matrix(branch, soil_matrix, "soil_type")
