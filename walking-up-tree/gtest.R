library(dplyr)
library(RFLPtools)
library(DescTools)
setwd("/Users/jocelynwang/Desktop/WES/Fall2022-cohanlab/walking_up_tree/walking-up-tree")

options(scipen = 100)
# atro
# x <- c(1,3,5,17,27,28,29,30)
# sp
# x <- c(3,4,6,7,40,41,84,115,169,170,172,192)
# ia
x <- c(1,2,3,4,6,57,58,60,61,65)
gTest_ele <- c()
gTest_soil <- c()
# x <- c(3)
for (i in 1:length(x)) {
  s1 <- paste(as.character(x[i]), "_elevation", "_matrix.csv", sep ="")
  data <- read.csv(s1)
  gTest_ele[i] <- paste(as.character(x[i]), "_",
                        as.character(round(GTest(data,correct="none")$p.value, digits=8)), sep = "")
  s2 <- paste(as.character(x[i]), "_soil_type", "_matrix.csv", sep ="")
  data <- read.csv(s2)
  gTest_soil[i] <- paste(as.character(x[i]), "_",
                         as.character(round(GTest(data,correct="none")$p.value, digits=5)), sep = "")
}

atro = "atrophaeus"
sp = "spizizenii"
ia = "inaquosorum"
gTest_ele
gTest_soil
write(gTest_ele, paste(ia, "_elevation.txt", sep = ""))
write(gTest_soil, paste(ia, "_soil.txt", sep = ""))
