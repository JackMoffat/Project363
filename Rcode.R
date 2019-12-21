library('dplyr')
library('ggplot2')
library('tidyr')
d <- read.csv("./dataFromPaper/csvfpsyg-06-01544.csv")
tbl_df(d)
oneback<-slice(d,11:12)
twoback<-slice(d,18:19)
threeback<-slice(d,25:26)

mean_sd <- bind_rows(oneback,twoback,threeback)

