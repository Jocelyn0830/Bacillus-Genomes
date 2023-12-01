library(dplyr)
library(RFLPtools)
library(DescTools)

# ap
ap_ele <- read.csv("ap/ap_ele.csv")
GTest(ap_ele,correct="none")

ap_soil <- read.csv("ap/ap_soil.csv")
GTest(ap_soil,correct="none")

# sp
sp_ele <- read.csv("sp/sp_ele.csv")
GTest(sp_ele,correct="none")

sp_soil <- read.csv("sp/sp_soil.csv")
GTest(sp_soil,correct="none")

# ia 
ia_ele <- read.csv("ia/ia_ele.csv")
GTest(ia_ele,correct="none")

ia_soil <- read.csv("ia/ia_soil.csv")
GTest(ia_soil,correct="none")
