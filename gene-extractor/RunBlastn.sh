#!/bin/bash

# specify input directory
input_dir=/Users/jocelynwang/Desktop/WES/Fall2023/Cohan/Bacillus-Genomes/gene-extractor/reference

# specify input directory
output_dir=/Users/jocelynwang/Desktop/WES/Fall2023/Cohan/Bacillus-Genomes/gene-extractor/gene-pos

# specify blastn command
blastn_command="blastn -query QUERY-FILE -subject FILE -out OUTPUT_FILE -outfmt 15"

#for all files in input directory
for entry in "$input_dir"/*
    do
        # get file name in input directory without path
        file_name=$(basename "$entry")

        # your subject file
        file="CBP-1645.fasta"

        # your output file name
        output_file="$output_dir/${file_name%.fasta}_pos.json"

        # update blastn command wuth query filename
        blastn_cmd="${blastn_command/QUERY-FILE/$entry}"

        # update blastn command with subject filename
        blastn_cmd="${blastn_cmd/FILE/$file}"

        # update blastn command with output filename
        blastn_cmd="${blastn_cmd/OUTPUT_FILE/$output_file}"

        # execute blastn command
        $blastn_cmd
done
