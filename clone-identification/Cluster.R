library(dplyr)
library(RFLPtools)

# sp
# x <- c(81, 82, 37, 38, 84, 40, 43, 87, 89, 91, 93, 94, 95, 96, 97, 98, 45, 99, 100, 101, 102, 105, 106, 51, 54, 112, 55, 56, 24, 57, 26, 115, 116, 65, 68, 120, 74, 70)
# species = "sp"

# ia 
# x <- c(1, 36, 15, 37, 38, 40, 41, 42, 43, 19, 46, 47, 48, 52, 53, 54, 55, 56, 24, 58, 60, 62, 64, 67, 68, 69, 70, 72, 73, 75, 78, 35)
# species = "ia"

# ap
x <- c(3, 4, 5, 6, 13, 14, 16, 17, 18, 1, 20, 21, 22, 23, 24, 27, 29, 30, 33, 34, 35)
species = "ap"

for (val in x) {
  s <- paste(species, as.character(val), "_matrix.csv", sep ="")
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
