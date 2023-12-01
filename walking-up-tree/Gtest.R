library(dplyr)
library(RFLPtools)
library(DescTools)

options(scipen = 100)
# atro
#x <- c(3,5,6,16,17,29,76)

# sp
x <- c(3,4,5,6,8,9,10,37,177,179,181,203)

# ia
# x <- c(5,6,7,8,62,80,89,90,93)

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

ap = "atrophaeus"
sp = "spizizenii"
ia = "inaquosorum"
gTest_ele
gTest_soil
write(gTest_ele, paste(sp, "_elevation.txt", sep = ""))
write(gTest_soil, paste(sp, "_soil.txt", sep = ""))

