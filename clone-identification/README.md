# clone-identification

Before identifying clones, you need
- error rate file - output of `ComputeER.py`
- environmental data file

Instructions for running clone-identification program
- Run `AddCollectionId.py` to get environmental data file with collection site ids
- Run `AddCloneInfoToER.py` to get clones.csv file needed to create matrix
- Run `CreateMatrix.py` to get strain pairwise distance matrix for each collection site. Copy collection ids list printed to terminal
- Paste collection ids in `Cluster.R`. Run `Cluster.R` and you'll get cluter of each collection site
- Run `AnalyzeCloneRes.py` to get list of strains and their clone information
