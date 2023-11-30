# Rarefaction Analysis
analyzes and plot graphs of rarefaction results

## Instructions
Before identifying clones, you need
- rarefaction results

Instructions for running rarefaction-analysis program
#### Ecotype Number Analysis
- Run `Parse.py` to get a csv file that contains name of each sample and its demarcated number of ecotype
- Run `Violin.R` to create a graph that displays distribution of demarcated number of ecotypes of each gene number
- `ViolinAll.R` is a back up program in case you want to put all species in a single plot

#### Supplementary analysis
- Run `ParseSeparate.py` to get csv files that contain information of npop, omega, sigma, and likelihood of each sample
- Run `Point.R` to create graphs that display trend of npop, omega, sigma, and likelihood information of each gene number
