library(dplyr)
library(RFLPtools)

# sp
x <- c(12, 118, 122, 121, 63, 78, 81, 65, 67, 68, 70, 72, 73, 47, 119, 9, 10, 1, 3, 5, 6, 8, 43, 44, 46, 54, 57, 59, 60, 61, 74, 87, 89, 92, 93, 98, 100, 30, 31)
species = "sp"
for (val in x) {
  s <- paste(species, "_Collection", as.character(val), "_matrix.csv", sep ="")
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
