# gene-extractor

To extract genes in core genome alignment
    (1) you need download all ffn files output by Prokka

Instructions for running gene-extractor program
- Run `CreateDB.py` to create a database and a table
- Run `GeneExtractor.py` to create put all_genes/core_genes in database
    - Which table do you want?
        - if you only want a database of core genes, answer `y` to the question
            Do you want to create a table that only includes core genes? (y/n)
        - if you want a database of all genes, answer `n` to the above question
    - Input your database name without the extension `.db` to this question
        Please type database name:
    - Input name of your directory that contains all ffn files (Your directory must be in the same directory where you put `GeneExtractor.py`)
        Please type database name:
- Run `CoreGeneExtractor.py` to create fasta files of all core genes (one for each) of your selected strain
- Run `GetOneCBP.py` to get fasta file of one strain in core genome alignment
- Run `./RunBlastn.sh` to run Blastn on all query core genes (output of `CoreGeneExtractor.py`) and your subject strain file (only one strain, output of `GetOneCBP.py`)
    - if you want to modify, run `chmod +x RunBlastn.sh` to complie it before running it
- Run `AddRealGenes.py`
    
