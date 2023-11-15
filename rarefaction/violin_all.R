library(ggplot2)
require(RColorBrewer)
library(dplyr)

ap_data <- read.csv("ap/rand_ecotype_result.csv")
ap_data <- mutate(ap_data, species = "Atrophaeus")
sp_data <- read.csv("sp/rand_ecotype_result.csv")
sp_data <- mutate(sp_data, species = "Spizizenii")
ia_data <- read.csv("ia/rand_ecotype_result.csv")
ia_data <- mutate(ia_data, species = "Inaquosorum")

list <- list(ap_data, ia_data, sp_data)
data <- Reduce(function(x, y) merge(x, y, all=TRUE), list, accumulate=FALSE)
data$ecotype_size[
  (data$ecotype_size < 13 | data$ecotype_size >= 25) 
  & data$species == "Inaquosorum"] <- NA
data$ecotype_size[data$ecotype_size >= 11
                  & data$species == "Atrophaeus"] <- NA
data$ecotype_size[data$ecotype_size >= 14
                  & data$species == "Spizizenii"] <- NA

colnames(data)[2] <- "gene_number"

# data$ecotype_size[data$ecotype_size >= 12] <- NA
# data$ecotype_size[data$ecotype_size < 12] <- NA
data <- na.omit(data)

data$gene_number = as.factor(data$gene_number)

gene_number.labs <- c('1 gene', '3 genes', '7 genes', '20 genes', '100 genes', '400 genes', '700 genes')
names(gene_number.labs) <- c('1', '3', '7', '20', '100', '400', '700')

data <- group_by(data, species)
ggplot(data, aes(x = factor(ecotype_size))) +
  geom_bar(fill = "black",
                 color = "white") +
  facet_wrap(
    vars(species, gene_number),
    scales = "free_x",
    nrow=3,
    labeller = labeller(gene_number=gene_number.labs)
  ) +
  ylab("number of Replicate Simulations (out of 500)") +
  xlab("number of Ecotypes")+
  theme_bw(base_size = 13)+
  theme(
    plot.title = element_text(hjust = 0.5))+
  ggtitle(
    "Rarefaction analysis of the number of predicted ecotypes, by sampling different numbers of real genes"
  )
  # theme(axis.text.x=element_text(size=12),
  #     axis.text.y=element_text(size=12))


