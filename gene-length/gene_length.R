library(ggplot2)

#### sp ####
sp_length_data <- read.csv("sp_gene_length.csv")
sp_length_data$length[sp_length_data$length >= 3000] <- NA
sp_length_data <- na.omit(sp_length_data)

# ggplot(data=length_data, aes(x=length))+
#   geom_histogram(aes(y=..density..), bins = 30)+
#   geom_density(alpha=.2, fill="#FF6666") 

ggplot(data=sp_length_data)+
  geom_histogram(aes(x=length), 
                 color="black", fill="lightblue",
                 bins = 25)+
  ggtitle("gene length distribution of Spizizenii")

#### ia ####
ia_length_data <- read.csv("ia_gene_length.csv")
ia_length_data$length[ia_length_data$length >= 3000] <- NA
ia_length_data <- na.omit(ia_length_data)

# ggplot(data=length_data, aes(x=length))+
#   geom_histogram(aes(y=..density..), bins = 30)+
#   geom_density(alpha=.2, fill="#FF6666") 

ggplot(data=ia_length_data)+
  geom_histogram(aes(x=length),
                 color="black", fill="lightblue",
                 bins = 25)+
  ggtitle("gene length distribution of Inaquosorum")

#### ap ####
ap_length_data <- read.csv("ap_gene_length.csv")
ap_length_data$length[ap_length_data$length >= 3000] <- NA
ap_length_data <- na.omit(ap_length_data)

# ggplot(data=length_data, aes(x=length))+
#   geom_histogram(aes(y=..density..), bins = 30)+
#   geom_density(alpha=.2, fill="#FF6666") 

ggplot(data=ap_length_data)+
  geom_histogram(aes(x=length),
                 color="black", fill="lightblue", bins = 25)+
  ggtitle("gene length distribution of Atrophaeus")
