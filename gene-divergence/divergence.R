library(ggplot2)
require(RColorBrewer)

#######################################
################# ap ##################
#######################################

# avarage number of mismatch nucleotides
ap_data <- read.csv("ap_avg_mismatch_gene.csv")
# ap_data$avg_mismatch[ap_data$avg_mismatch >= 25] <- NA
# ap_data <- na.omit(ap_data)

ggplot(data=ap_data)+
  geom_point(aes(x=avg_mismatch, y=factor(ecotype_size)),
             size=1.5, alpha=0.5)+
  xlab("Average Pairwise Nucleotide Difference")+
  ylab("Ecotype Size")+
  ggtitle("Atrophaeus")
  
# avarage number of mismatch nucleotides
ap_data1 <- read.csv("ap_avg_mismatch_rate_gene.csv")
# ap_data1$avg_mismatch[ap_data1$avg_mismatch_rate >= 0.03] <- NA
# ap_data1 <- na.omit(ap_data1)

ggplot(data=ap_data1)+
  geom_point(aes(x=avg_mismatch_rate*100, y=factor(ecotype_size)), 
             size=1.5, alpha=0.5) +
  xlab("Average Pairwise Nucleotide Divergence Percentage")+
  ylab("Ecotype Size")+
  ggtitle("Atrophaeus")


#######################################
################# ia ##################
#######################################

# avarage number of mismatch nucleotides
ia_data <- read.csv("ia_avg_mismatch_gene.csv")
# ia_data$avg_mismatch[ia_data$avg_mismatch >= 25] <- NA
# ia_data <- na.omit(ia_data)

ggplot(data=ia_data)+
  geom_point(aes(x=as.numeric(avg_mismatch), 
                 y=factor(ecotype_size)),
             size=1.5, alpha=0.5)+
  xlab("Average Number of Nucleotide Difference")+
  ylab("Ecotype Size")+
  ggtitle("Inaquosorum")

# avarage number of mismatch nucleotides
ia_data1 <- read.csv("ia_avg_mismatch_rate_gene.csv")
# ia_data1$avg_mismatch[ia_data1$avg_mismatch_rate >= 0.03] <- NA
# ia_data1 <- na.omit(ia_data1)

ggplot(data=ia_data1)+
  geom_point(aes(x=as.numeric(avg_mismatch_rate)*100, 
                 y=factor(ecotype_size)), 
             size=1.5, alpha=0.5) +
  xlab("Average Pairwise Sequence Divergence Rate")+
  ylab("Ecotype Size")+
  ggtitle("Inaquosorum")

#######################################
################# sp ##################
#######################################

# avarage number of mismatch nucleotides
sp_data <- read.csv("sp_avg_mismatch_gene.csv")
# sp_data$avg_mismatch[sp_data$avg_mismatch >= 25] <- NA
# sp_data <- na.omit(sp_data)

ggplot(data=sp_data)+
  geom_point(aes(x=as.numeric(avg_mismatch), 
                 y=factor(ecotype_size)),
             size=1.5, alpha=0.5)+
  xlab("Average Number of Nucleotide Difference")+
  ylab("Ecotype Size")+
  ggtitle("Spizizenii")

# avarage number of mismatch nucleotides
sp_data1 <- read.csv("sp_avg_mismatch_rate_gene.csv")
# sp_data1$avg_mismatch[sp_data1$avg_mismatch_rate >= 0.03] <- NA
# sp_data1 <- na.omit(sp_data1)

ggplot(data=sp_data1)+
  geom_point(aes(x=as.numeric(avg_mismatch_rate), 
                 y=factor(ecotype_size)), 
             size=1.5, alpha=0.5) +
  xlab("Average Pairwise Sequence Divergence Rate")+
  ylab("Ecotype Size")+
  ggtitle("Spizizenii")

