library(ggtree)
library(ape)
library(treeio)
library(dplyr)
library(ggplot2)
library(tidytree)
offspring.tbl_tree_item <- utils::getFromNamespace(".offspring.tbl_tree_item", "tidytree")

######################################
################# ia #################
######################################
ia_tree <- read.nhx("ia/ia_bootstrapped_ecotype.nhx")

x <- as_tibble(ia_tree)
child(ia_tree, 112)
offspring.tbl_tree_item

ia_tree_graph <- ggtree(ia_tree) +
  geom_text(aes(label = proof), hjust = -0.5, size = 2) +
  geom_point2(aes(subset=(value>=0), 
                  color = cut(value, 
                              breaks = c(0, 90, 100)),
  ), size = 3, alpha = 0.9)+
  scale_color_manual(
    values=c("Yellow Green", "Firebrick"),
    labels=c("0-90", "90-100"))+
  guides(alpha="none", 
         size="none", 
        color = guide_legend(title="Ecotype Bootstrapped Score"),
  )

ia_tree_graph+ 
  geom_cladelab(node=99, label="PE", align=TRUE)+
  geom_cladelab(node=103, label="test label", align=TRUE)+
  geom_cladelab(node=112, label="test label", align=TRUE)+
  geom_cladelab(node=127, label="test label", align=TRUE)+
  geom_cladelab(node=139, label="test label", align=TRUE)+
  geom_cladelab(node=149, label="test label", align=TRUE)+
  geom_cladelab(node=154, label="test label", align=TRUE)+
  geom_cladelab(node=168, label="test label", align=TRUE)+
  geom_cladelab(node=180, label="test label", align=TRUE)+
  geom_cladelab(node=185, label="test label", align=TRUE)+
  geom_cladelab(node=194, label="test label", align=TRUE)+
  geom_cladelab(node=202, label="test label", align=TRUE)+
  geom_cladelab(node=203, label="test label", align=TRUE)+
  geom_cladelab(node=204, label="test label", align=TRUE)

# annotation
x <- as_tibble(ia_tree)
pull(filter(x, value > 90), node)


######################################
################# sp #################
######################################
sp_tree <- read.nhx("sp/sp_bootstrapped_ecotype.nhx")
# sp_tree <- drop.tip(sp_tree, "amy")

# annotation
x <- as_tibble(sp_tree)
filter(x, value > 70)
pull(filter(x, value > 70), node)

sp_tree_graph <- ggtree(sp_tree) +
  geom_text(aes(label = proof), hjust = -0.5, size = 2) +
  geom_point2(aes(subset=(value>=0), 
                  color = cut(value, 
                              breaks = c(0, 70, Inf)),
  ), size = 3, alpha = 0.9)+
  scale_color_manual(
    values=c("Yellow Green", "Firebrick"), 
    labels=c("0-70", "70-100"))+
  guides(alpha="none", 
         size="none", 
         color = guide_legend(title="Ecotype Bootstrapped Score"),
  )

sp_tree_graph+ 
  geom_cladelab(node=164, label="PE D 1 clone", align=TRUE, fontsize=4)+
  geom_cladelab(node=173, label="PE A\n89 clones", align=TRUE, fontsize=4)+
  geom_cladelab(node=259, label="PE B\n72 clones", align=TRUE, fontsize=4)+
  geom_cladelab(node=330, label="PE C 4 clones", align=TRUE, fontsize=4)+
  geom_cladelab(node=333, label="PE E\n4 clones", align=TRUE, fontsize=4)
  # geom_hilight(node=333, fill="steelblue", alpha=.5)


######################################
################# ap #################
######################################
ap_tree <- read.nhx("ap/ap_bootstrapped_ecotype.nhx")

ggtree(ap_tree) +
  geom_text(aes(label = proof), hjust = -0.5, size = 2) +
  geom_point2(aes(subset=(value>=0), 
              color = cut(value, 
                          breaks = c(0, 50, 80, 90, Inf)),
              ), size = 3, alpha = 0.9)+
  scale_color_manual(
    values=c("Yellow Green", "Gold", "Dark Orange", "Firebrick"), 
    labels=c("0-50", "50-80", "80-90", "90-100"))+
  guides(alpha="none", 
         size="none", 
         color = guide_legend(title="Ecotype Bootstrapped Score"),
          )
