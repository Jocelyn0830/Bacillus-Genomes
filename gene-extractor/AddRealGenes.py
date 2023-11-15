import sqlite3
import json
import sys
import os

cur_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(cur_dir))

from util import FastaToDict

def findHitFromPos(gene, subject_strain_name):
    genome = FastaToDict.fastaToDict(subject_strain_name + '.fasta').get('>' + subject_strain_name).lower()
    hit_from = genome.find(gene.lower())

    return hit_from

# parse gene position json file to get position of genes in core genome alignment
def parseGenePosJson(filename):
    gene_pos_json = open(filename)

    json_info_dict = {}

    data = json.load(gene_pos_json)

    try:
        blast_output = data["BlastOutput2"]
        blast_output_res = blast_output[0].get(
            'report').get('results').get('bl2seq')[0]

        hits = blast_output_res.get('hits')[0]
        hsps = hits.get('hsps')[0]
        description = hits.get('description')[0]
        subject_strain_name = description.get("title")

        query_gene_id, query_gene_name = blast_output_res.get('query_title').split('|')
        
        hseq = hsps.get('hseq') 
        align_len = hsps.get('align_len')

        hit_from = findHitFromPos(hseq, subject_strain_name)
        if hit_from == -1:
            print(query_gene_name, query_gene_id)
            
        hit_to = hit_from + align_len

        json_info_dict[query_gene_name] = \
            {"hit_from" : hit_from, "hit_to" : hit_to, "gene_length" : align_len}
    
    except Exception as e:
        print(e)
        print(filename)
    
    return json_info_dict

# parse all json files on the path
def parseAllJson():
    directory = input("Please type directory name: ")

    data = {}
    
    for filename in os.listdir(directory):
        if filename == ".DS_Store":
            continue
        f = os.path.join(directory, filename)
        if os.path.isfile(f):
            json_info_dict = parseGenePosJson(f)
            data = data | json_info_dict
    
    return data

# get real genes from core genome alignment
def getRealGenes(coregenefile):
    gene_pos_data = parseAllJson()
    core_genome_dict = FastaToDict.fastaToDict(coregenefile)

    all_real_genes = []

    for gene_name, gene_pos_dict in gene_pos_data.items():
        hit_from = gene_pos_dict["hit_from"]
        hit_to = gene_pos_dict["hit_to"]
        gene_length = gene_pos_dict["gene_length"]

        for strain_name, genome in core_genome_dict.items():
            strain_name = strain_name.replace('>', '').replace('-gff3','')
            gene_content = genome[hit_from:hit_to]
            # unique sequence gene identifier
            sequence_gene_id = strain_name + '_' + gene_name
            one_gene_one_cbp = (sequence_gene_id, strain_name, gene_name, gene_content, gene_length, )
            if gene_content and gene_length >= 500:
                all_real_genes.append(one_gene_one_cbp)
    
    return all_real_genes
            



db_name = input("Please type database name: ")
all_genes_data = getRealGenes("sp_rm_clones.fasta")
print(len(all_genes_data))
con = sqlite3.connect(db_name + ".db")
cur = con.cursor()


update_query = "INSERT or IGNORE INTO real_core_genes VALUES(?, ?, ?, ?, ?)"
con.executemany(update_query, all_genes_data)

# update_query = "UPDATE core_genes SET real_gene_content = ?, gene_length = ? WHERE sequence_id = ? and gene_id = ?"
# con.execute(update_query, all_genes_data[0])

con.commit()

con.close()