setwd(dirname(rstudioapi::getActiveDocumentContext()$path))

library(ggplot2)
---- #Exercice 4.1----
# Q 4.4.1
load("passereau.Rdata")
# Q 4.4.2
ggplot(passereau) +
    aes(x = annee,
          y = population,
          group = f) +
    geom_line() +
    geom_point()
ggsave("suite_geom_ggplot_1.png")
# Q 4.4.3
ggplot(passereau) +
    aes(x = annee,
           y = population,
           color = f) +
    geom_line() +
    geom_point()
ggsave("suite_geom_ggplot_2.png")

---- #Exercice4.2----
#Q 4.5.1
library(tibble)
library(dplyr)
library(ggplot2)
n_0 <- 10
s_a <- 0.5
s_j <- 0.5
f <- 6
p_f <- 0.5
donnee <- tibble(annee = 0:10)
f <- 2
raison <- s_a + p_f * f * s_j
evolution <- mutate(donnee, population = n_0 * raison^annee)
# Q 4.5.2
evolution_0 <- mutate(evolution, f = f)
# Q 4.5.3
f <- 2.5
raison <- s_a + p_f * f * s_j
evolution <- mutate(donnee, population = n_0 * raison^annee)
evolution_1 <- mutate(evolution, f = f)
# Q 4.5.4
f <- 0.75
raison <- s_a + p_f * f * s_j
evolution <- mutate(donnee, population = n_0 * raison^annee)
evolution_2 <- mutate(evolution, f = f)
# Q 4.5.5
modele <- bind_rows(evolution_0, evolution_1, evolution_2)
# Q 4.5.6
ggplot(data = modele) +
  aes(x = annee,
         y = population,
         color = f,
         group = f) +
  geom_line() +
  geom_point()
ggsave("suite_geom_ggplot_3.png")
# Q 4.5.7
glimpse(modele)
# f est factorisé dans passereau
# Q 4.5.8
ggplot(data = modele) +
  aes(x = annee,
         y = population,
         color = factor(f)) +
  geom_line() +
  geom_point()
ggsave("suite_geom_ggplot_4.png")

---- #Exercice4.3----
library(tidyverse)

n_0 <- 10
s_a <- 0.5
s_j <- 0.5
f <- 1.7
p_f <- 0.5

# Avec une boucle for
raison_fixe <- s_a + p_f * f * s_j
donnee <- tibble(annee = 0:20) %>%
  mutate(raison = s_a +1.01^annee * s_j * p_f * f )
annee_vec <- pull(donnee, raison)
raison_vec <- pull(donnee, raison)
population = numeric(21)
population[1] <- n_0
for(annee in 1:20){
  population[annee + 1] <- raison_vec[annee+1] * population[annee]
  }
donnee <- donnee %>%
  mutate(rechauffement = population) %>%
  mutate(geometrique = n_0 * raison_fixe^annee) %>%
  mutate(ecart = abs(rechauffement − geometrique)) %>%
  pivot_longer(cols = c(rechauffement, geometrique),
                  values_to = "population",
                  names_to = "modele") %>%
  mutate(modele = factor(modele,
                            levels = c("rechauffement", "geometrique"),
                            labels = c("Avec réchauffement climatique", "Sans réchauffement
climatique")))


# Avec accumulate
raison_fixe <- s_a + p_f * f * s_j
donnee_2 <- tibble(annee = 0:20) %>%
  mutate(raison = s_a +1.01^annee * s_j * p_f * f ) %>%
  mutate(rechauffement = accumulate(.x = raison[−1],
                                       .f = prod,
                                       .init = 10)) %>%
  mutate(geometrique = n_0 * raison_fixe^annee) %>%
  mutate(ecart = abs(rechauffement − geometrique)) %>%
  pivot_longer(cols = c(rechauffement, geometrique),
                  values_to = "population",
                  names_to = "modele") %>%
  mutate(modele = factor(modele,
                            levels = c("rechauffement", "geometrique"),
                            labels = c("Avec réchauffement climatique", "Sans réchauffement
climatique")))

ggplot(data = donnee) +
  aes(x = annee,
         y = population,
         color = modele) +
  geom_point() +
  geom_line() +
  theme(legend.position = "bottom") +
  labs(color = "Modèle",
          x = "Année",
          y = "Population")
ggsave("temps.png")

valeur <- summarise(donnee, maximum = max(ecart)) %>%
  pull(maximum)
typeof(valeur) == "double"

donnee %>%
  filter(modele == "Avec réchauffement climatique") %>%
  slice_min(population)
