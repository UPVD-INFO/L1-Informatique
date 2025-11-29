# Exercice TD3 ----
## Exercice 3.1 ----
### 3.1.1 ----
s_a <− 0.5
### 3.1.2 ----
s_j <− 0.5
### 3.1.3 ----
f <− 6
### 3.1.4 ----
p_f <− 0.5
### 3.1.5 ----
n_0 <− 10 # population à l'année 0
n_1 <− (s_a + p_f ∗ f ∗ s_j) ∗ n_0
### 3.1.6 ----
n_2 <− (s_a + p_f ∗ f ∗ s_j) ∗ n_1
### 3.1.7 ----
n_3 <− (s_a + p_f ∗ f ∗ s_j) ∗ n_2
## Exercice 3.2 ----
### 3.2.1 ----
# disponible
library(tibble)
library(dplyr)
raison <− s_a + p_f ∗ f ∗ s_j
### 3.2.2 ----
donnee <− tibble(annee = 0:10)
### 3.2.3 ----
evolution <− mutate(donnee, population = n_0 ∗ raison^annee)
# Q 2.2.4 La croissance de la population est exponentielle
# Q 2.2.5
head(evolution, n = 4)
# Q 2.2.6 Oui
# Q 2.2.7
exo_1 <− tibble(population = c(n_0, n_1, n_2, n_3))
exo_2 <− evolution %>%
select(population) %>%
head(n = 4)
all(exo_1 == exo_2)

## 3.3 ----
# disponible
library(tibble)
library(dplyr)
n_0 <− 10
s_a <− 0.5
s_j <− 0.5
f <− 6
p_f <− 0.5

 # Q 2.3.1
f_seuil <− 2 ∗ (1 − s_a)/s_j
# Q 2.3.2
raison <− s_a + p_f ∗ f_seuil ∗ s_j
# Q 2.3.3
donnee <− tibble(annee = 0:10)
# Q 2.3.4
evolution <− mutate(donnee, population = n_0 ∗ raison^annee)
# Q 2.3.5
summary(evolution)
# Q 2.3.6 La population n'évolue pas
# Q 2.3.7
calcul = select(evolution, population)
theorique = tibble(population = rep(10, 11))
setequal(calcul, theorique)
--------------------------------------------------------------------------------
# Q 2.3.7 Vérification de la constance de l'évolution de la population
evolution <- mutate(evolution, population_lag = lag(population))

# Afficher la réponse à la question
if(all(evolution$population == evolution$population_lag)) {
  cat("La population évolue de manière constante.\n")
} else {
  cat("La population n'évolue pas de manière constante.\n")
}
--------------------------------------------------------------------------------
#3.2.7
  # Chargement des bibliothèques
  library(tibble)
library(dplyr)

# Définition des variables
n_0 <- 10
s_a <- 0.5
s_j <- 0.5
f <- 6
p_f <- 0.5

# Calcul des seuils
f_seuil <- 2 * (1 - s_a) / s_j
raison <- s_a + p_f * f_seuil * s_j

# Création du dataframe
donnee <- tibble(annee = 0:10)

# Calcul de l'évolution de la population
evolution <- mutate(donnee, population = n_0 * raison^annee)

# Vérification de la constance de l'évolution de la population
resultat_constance <- evolution %>%
  head(1) %>%
  mutate(population_lag = lag(population)) %>%
  mutate(constante = population == population_lag) %>%
  pull(constante) %>%
  all()

# Affichage du résultat
if(resultat_constance) {
  cat("La population évolue de manière constante.\n")
} else {
  cat("La population n'évolue pas de manière constante.\n")
}
--------------------------------------------------------------------------------
# 3.3.7 met 1
  # Chargement des bibliothèques
  library(tibble)
library(dplyr)

# Définition des variables
n_0 <- 10
s_a <- 0.5
s_j <- 0.5
f <- 6
p_f <- 0.5

# Calcul des seuils
f_seuil <- 2 * (1 - s_a) / s_j
raison <- s_a + p_f * f_seuil * s_j

# Création du dataframe
donnee <- tibble(annee = 0:10)

# Calcul de l'évolution de la population
evolution <- mutate(donnee, population = n_0 * raison^annee)

# Vérification de la constance de l'évolution de la population
resultat_constance <- all(evolution$population == lag(evolution$population))

# Affichage du résultat
if(resultat_constance) {
  cat("La population évolue de manière constante.\n")
} else {
  cat("La population n'évolue pas de manière constante.\n")
}
--------------------------------------------------------------------------------
# 3.3.7
  # Chargement des bibliothèques
  library(tibble)
library(dplyr)

# Définition des variables
n_0 <- 10
s_a <- 0.5
s_j <- 0.5
f <- 6
p_f <- 0.5

# Calcul des seuils
f_seuil <- 2 * (1 - s_a) / s_j
raison <- s_a + p_f * f_seuil * s_j

# Création du dataframe
donnee <- tibble(annee = 0:10)

# Calcul de l'évolution de la population avec dplyr
evolution <- donnee %>%
  mutate(population = n_0 * raison^annee)

# Vérification de la constance de l'évolution de la population avec dplyr
resultat_constance <- evolution %>%
  mutate(population_lag = lag(population)) %>%
  filter(!is.na(population_lag)) %>%
  summarise(constante = all(population == population_lag)) %>%
  pull(constante)

# Affichage du résultat
if(resultat_constance) {
  cat("La population évolue de manière constante.\n")
} else {
  cat("La population n'évolue pas de manière constante.\n")
}