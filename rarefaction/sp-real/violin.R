library(ggplot2)
require(RColorBrewer)

data <- read.csv("rand_ecotype_result.csv")
data$ecotype_size[data$ecotype_size >= 12] <- NA
# data$ecotype_size[data$ecotype_size < 12] <- NA
data <- na.omit(data)

data$gene_numebr = as.factor(data$gene_numebr)

gene_numebr.labs <- c('1 gene', '3 genes', '7 genes', '20 genes', '100 genes', '700 genes')
names(gene_numebr.labs) <- c('1', '3', '7', '20', '100', '700')

ggplot(data, aes(x = factor(ecotype_size))) +
  geom_bar(fill = "black",
                 color = "white") +
  facet_wrap(~ gene_numebr, ncol = 1, labeller = labeller(gene_numebr=gene_numebr.labs)) +
  ylab("number of Replicate Simulations (out of 500)") +
  xlab("number of Ecotypes")+
  theme_bw(base_size = 13)+
  ggtitle("Rarefaction analysis of the number of predicted ecotypes of Spizizenii,\n by sampling different numbers of real genes")

  # theme(axis.text.x=element_text(size=12),
  #     axis.text.y=element_text(size=12))

