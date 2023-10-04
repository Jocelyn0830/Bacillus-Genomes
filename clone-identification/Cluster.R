library(dplyr)
library(RFLPtools)
setwd("/Users/jocelynwang/Desktop/WES/Summer2022-cohan/genome/Clone-identification")

x <- c(13, 101, 102, 104, 109, 110, 111, 112, 113, 114, 115, 12, 15, 16, 18, 22, 23, 37, 60, 99)
# x <- c(3)
species = "atrophaeus"
for (val in x) {
  s <- paste(species, "_collection", as.character(val), "_matrix.csv", sep ="")
  temp = read.csv(s, sep=",", row.names=1)
  matrix <- as.matrix(temp) 
  matrix <- as.dist(matrix)
  clust <- hclust(matrix, method = "average")
  dend <- as.dendrogram(clust)
  par(mar=c(6.1, 4.1, 4.1, 2.1))
  plot(dend)
  s1 <- paste(species,"_clone",as.character(val),".txt", sep ="")
  pre <- paste(species,"_collection", as.character(val), sep ="")
  group <- write.hclust(clust, file = s1, prefix = pre,h = 0.00001)
}