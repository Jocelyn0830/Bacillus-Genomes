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
ia_tree <- read.nhx("ia/ia_bon.nhx")

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
  )+
  geom_label(aes(label=bon), fill='steelblue', hjust=-.5) 

ia_tree_graph+ 
  geom_cladelab(node=99, label="PE Z", align=TRUE)+
  geom_cladelab(node=103, label="PE AB 1 Clone", align=TRUE)+
  geom_cladelab(node=112, label="PE U", align=TRUE)+
  geom_cladelab(node=127, label="PE V", align=TRUE)+
  geom_cladelab(node=139, label="PE T", align=TRUE)+
  geom_cladelab(node=149, label="PE R", align=TRUE)+
  geom_cladelab(node=154, label="PE O", align=TRUE)+
  geom_cladelab(node=168, label="PE P", align=TRUE)+
  geom_cladelab(node=180, label="PE Q", align=TRUE)+
  geom_cladelab(node=185, label="PE S", align=TRUE)+
  geom_cladelab(node=194, label="PE W", align=TRUE)+
  geom_cladelab(node=202, label="PE X", align=TRUE)+
  geom_cladelab(node=203, label="PE Y", align=TRUE)+
  geom_cladelab(node=204, label="PE AA", align=TRUE)

# annotation
x <- as_tibble(ia_tree)
pull(filter(x, value > 90), node)


######################################
################# sp #################
######################################
sp_tree <- read.nhx("sp/sp_bon.nhx")

# annotation
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
  )+
  geom_label(aes(label=bon), fill='steelblue', hjust=-.5) 

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
ap_tree <- read.nhx("ap/ap_bon.nhx")

ap_tree_graph <- ggtree(ap_tree) +
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
          )+
  geom_label(aes(label=bon), fill='steelblue', hjust=-.5) 

ap_tree_graph+ 
  geom_cladelab(node=62, label="PE J", align=TRUE, fontsize=4)+
  geom_cladelab(node=86, label="PE H", align=TRUE, fontsize=4)+
  geom_cladelab(node=91, label="PE F", align=TRUE, fontsize=4)+
  geom_cladelab(node=120, label="PE G", align=TRUE, fontsize=4)+
  geom_cladelab(node=139, label="PE I", align=TRUE, fontsize=4)+
  geom_cladelab(node=144, label="PE L", align=TRUE, fontsize=4)+
  geom_cladelab(node=148, label="PE M 4 clones", align=TRUE, fontsize=4)+
  geom_cladelab(node=150, label="PE N\n4 clones", align=TRUE, fontsize=4)
# geom_hilight(node=333, fill="steelblue", alpha=.5)

# annotation
x <- as_tibble(ap_tree)
pull(filter(x, value > 50), node)
