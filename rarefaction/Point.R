library(ggplot2)
require(RColorBrewer)

setwd("/Users/jocelynwang/Desktop/WES/Spring2023-cohanlab/rarefication/ia")
data <- read.csv("rand_eco_npop_omega_result.csv")

data$gene_numebr = as.factor(data$gene_numebr)

gene_numebr.labs <- c('1 gene', '3 genes', '7 genes', '20 genes', '100 genes', '500 genes')
names(gene_numebr.labs) <- c('1', '3', '7', '20', '100', '500')

ggplot(data, aes(x = npop, y = ecotype_size)) +
  geom_point(color = "black") +
  facet_wrap(~ gene_numebr, ncol = 2, labeller = labeller(gene_numebr=gene_numebr.labs)) +
  ylab("Number of Ecotypes") +
  xlab("npop values")+
  theme_bw(base_size = 13)

ggplot(data, aes(x = omega, y = ecotype_size)) +
  geom_point(color = "black") +
  facet_wrap(~ gene_numebr, ncol = 2, labeller = labeller(gene_numebr=gene_numebr.labs)) +
  ylab("Number of Ecotypes") +
  xlab("npop values")+
  theme_bw(base_size = 13)
