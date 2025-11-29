library(tidyverse)
library(readxl)

#tibble
#annee <dbl>
#gt_co2 <dbl>
#pays <fct>
#emission <fct>
p29 <- read_excel("chiffres_cles_climat_edition_2022_donnees_associees.xlsx",
                  sheet = "p29",
                  range = "A26:AE36")

donnee <- p29 |>
  rename(pays = 1,
         emission= 2)|>
  pivot_longer(cols= 3:31,
               names_to= "annee",
               values_to= "gt_co2")|>
  mutate(annee= as.numeric(annee))|>
  mutate(pays=  fct(pays))|>
  mutate(emission= fct(emission))

ggplot(data= donnee)+
  aes(x= annee,
      y= gt_co2,
      color= pays,
      linetype= emission)+
  geom_line(size= 0.7)+
  labs(linetype= NULL,
       color= "Zone Geographique")+
  scale_x_continuous(breaks= seq(1990,2018,2))+
  scale_y_continuous(breaks= seq(0,10,2))

# donnees |> ----
  arrange(emission,pays)|>
  ggplot()+
  aes(x= anneee,
      y= gt_co2,
      color=pays,
      linetype= emission,
      group= interaction(pa ys,emission))+