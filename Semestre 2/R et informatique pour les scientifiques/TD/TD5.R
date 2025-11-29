setwd(dirname(rstudioapi::getActiveDocumentContext()$path))

# Exercice 5.1 ----
fun_efficacite <- function(annee, periode) {
  e_p <- 0.99 # Réduction des larves en absence de pommes de terre
  if (annee == 0){
    resultat = NA
    } else if (annee %% periode == 0) {
      resultat <- e_p # Année à céréales
      } else {
        resultat <- 0 # Année à pommes de terre
        }
  return(resultat)
  }

annee_1 <- fun_efficacite(annee = 1, periode = 2)
annee_2 <- fun_efficacite(annee = 2, periode = 2)
annee_3 <- fun_efficacite(annee = 3, periode = 2)
annee_4 <- fun_efficacite(annee = 4, periode = 2)

# Exercice 5.2 ----
library(tidyverse)

# Q 5.2.1
f <- 800
s_a <- 0.2
s_o <- 0.02
s_l <- 0.1

# Q 5.2.2
donnee_1 <- tibble(annee = 0:8,
                      efficacite = c(NA, rep(c(0, 0.99),4)))

# Q 5.2.3
donnee_1 <- tibble(annee = 0:8) %>%
  mutate(efficacite = map_dbl(annee, fun_efficacite, periode = 2))

# alternative non recommandée
# rowwise() allows you to compute on a data frame a row-at-a-time.
# This is most useful when a vectorised function doesn't exist.
# donnee_1 <- tibble(annee = 0:8) %>%
# rowwise() %>%
# mutate(efficacite = fun_efficacite(annee, 2)) %>%
# ungroup()

# Avec map, c'est une liste qu'on obtient
# > glimpse(donnee_1)
# Rows: 9
# Columns: 2
# $ annee <int> 0, 1, 2, 3, 4, 5, 6, 7, 8
# $ efficacite <list> NA, 0, 0.99, 0, 0.99, 0, 0.99, 0, 0.99

# Q 5.2.4
donnee_2 <- donnee_1 %>%
  mutate(raison = s_a + f * s_o * s_l * (1 - efficacite))

# Q 5.2.5
donnee_3 <- donnee_2 %>%
  mutate(population = c(100, rep(NA, 8)))

# Q 5.2.6
for (ligne in 2:9){
  donnee_3[ligne, 4] = donnee_3[ligne-1, 4] * donnee_3[ligne, 3]
  }

# Q 5.2.7
ggplot(donnee_3) +
  aes(x = annee,
         y = population) +
  geom_point() +
  geom_line()

ggsave("tibble.png")

# Exercice 5.3 ----
# Q 5.3.1
donnee_4 <- donnee_3 %>%
  filter(!is.na(raison))
# ou
donnee_4 <- drop_na(donnee_3)

# Q 5.3.2 puzzle
raison_huit_ans <- donnee_4 %>%
  summarise(raison_moyenne = prod(raison)^(1/8)) %>%
  pull(raison_moyenne)

# Q 5.3.3
vecteur_population = numeric(9)
vecteur_population[1] <- 100
for (annee in 2:9){
  vecteur_population[annee] = vecteur_population[annee-1] * raison_huit_ans
  }

# Q 5.3.4
donnee_5 <- tibble(annee = 0:8,
                      raison = rep(raison_huit_ans, 9),
                      population = vecteur_population)

# Q 5.3.5
donnee_4b <- mutate(donnee_3, modele = "alternance")
donnee_5b <- mutate(donnee_5, modele = "taux moyen")
donnee_plot <- bind_rows(donnee_4b, donnee_5b)

ggplot(data = donnee_plot) +
  aes(x = annee,
         y = population,
         color = modele) +
  geom_point() +
  geom_line()