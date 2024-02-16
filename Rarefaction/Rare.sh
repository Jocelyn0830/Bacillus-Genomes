#!/bin/bash

# Find the Java binary.
JAVA=$(which java)

ap_input_dir = /gene_with_name/ap_gene_with_name
sp_input_dir = /gene_with_name/sp_gene_with_name
ia_input_dir = /gene_with_name/ia_gene_with_name


# Run Ecotype Simulation.
for entry in "$input_dir"/*
do
	# java -jar ecosim.jar -n -s=rand/fake_gene$j/fake_gene${j}_$i.fasta -p=sp_tree.newick -o=result/fake$j/gene$j_$i.txt $ARGS
	java -jar ecosim.jar -n -s=$entry -p=sp_tree.newick -o=result/$entry $ARGS
done

