from ete3 import Tree

filename = "ap/ap_tree.newick"
tree_string = ""
with open(filename, encoding='utf-8-sig') as treefile:
    for row in treefile:
        tree_string += row

t = Tree(tree_string)
print(t)