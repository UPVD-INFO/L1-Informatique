# Yo ----
#2.1.1
library(tibble)
#2.1.2
tibble(x = 1:7)
#2.1.3
tibble_1 <- tibble(y = seq(from = 5, to = 26, by = 3))
#2.1.4
vecteur <- seq(from = 4, to = 14, by = 5)
#2.1.5
tibble_2 <− tibble(z = vecteur)
#2.1.6
tibble_3 <− tibble(etudiant = c("Dominique", "Camille", "Maxence"),
                   annee = c(2002, 2003, 2002),
                   licence = c("SVT", "Math", "Info"))

#Partie prof ----
library(tibble)
### 2.1
# Q 1.4.2
tibble(x = 1:7)
# Q 1.4.3
tibble_1 <− tibble(y = seq(from = 5, to = 26, by = 3))
# Q 1.4.4
vecteur <− seq(from = 4, to = 14, by = 5)
# Q 1.4.5
tibble_2 <− tibble(z = vecteur)
# Q 1.4.6
tibble_3 <− tibble(etudiant = c("Dominique", "Camille", "Maxence"),
                      annee = c(2002, 2003, 2002),
                      licence = c("SVT", "Math", "Info"))
# Q 1.4.7
tibble_4 <− tribble(~etudiant, ~annee, ~licence,
                       "Morgane", 2001, "SVT")

###2.2

library(tibble)

tibble_3 <− tibble(etudiant = c("Dominique", "Camille", "Maxence"),
                     annee = c(2002, 2003, 2002),
                     licence = c("SVT", "Math", "Info"))
tibble_4 <− tribble(~etudiant, ~annee, ~licence,
                      "Morgane", 2001, "SVT")

# Q 2.2.1
tibble_3[4, 1] <− "Louison"
# Q 2.2.2
tibble_3[4, 2] <− 2002
# Q 2.2.3
print(tibble_3)
# Q 2.2.4
NA
# Q 2.2.5
library(dplyr)
# Q 2.2.6
tibble_5 <− bind_rows(tibble_3, tibble_4)
# Q 2.2.7
tail(arrange(tibble_5, annee), n = 1)
# ou avec l'opérateur d'enchainement
tibble_5 %>%
  arrange(annee) %>%
  tail(n = 1)
# Q 2.2.8
resultat <− summarise(.data = tibble_5,
                         somme = sum(annee))

###2.3
library(readr)
library(dplyr)
tibble_6 <− read_csv("debut_tibble_3.csv")
tibble_6 <− tibble_6 %>%
  mutate(age = 2022 − annee)
resultat <− summarise(.data = tibble_6,
                        somme = sum(annee),
                        moyenne_d_age = mean(age))
### 2.4
#2.4.1
# Chaîne de caractères initiale
nom_de_la_matiere <- "tlnf2ri1"

# Utiliser str_to_upper pour convertir en majuscules
nom_de_la_matiere <- str_to_upper(nom_de_la_matiere)

#2.4.2
# Chaîne de caractères initiale
semaine <- "lundi mardi mercredi jeudi vendredi samedi dimanche"

# Utiliser str_to_title pour mettre en majuscules les premières lettres des mots
semaine <- str_to_title(semaine)

#2.4.3
# Vecteur initial avec les jours de la semaine
jours_de_la_semaine <- c("lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche")

# Utiliser str_sub pour ne contenir que les trois premières lettres en majuscules
jours_de_la_semaine <- str_to_upper(str_sub(jours_de_la_semaine, 1, 3))

# Affecter le résultat à la variable initiale
semaine <- jours_de_la_semaine

#2.4.4
# Vecteur de noms de fruits en anglais
fruit <- c("apple", "banana", "cherry", "date", "grape", "kiwi", "orange", "peach")

# Utiliser str_detect pour trouver les fruits avec au moins un "c"
fruits_avec_c <- fruit[str_detect(fruit, "c")]

# Nombre de fruits avec au moins un "c"
nombre_de_fruits_avec_c <- length(fruits_avec_c)

# Affecter le résultat à la variable reponse
reponse <- nombre_de_fruits_avec_c

#2.4.5
La fonction str_glue() fait partie du package stringr en R, 
et elle permet de créer des chaînes de caractères en incluant des 
expressions R à l'intérieur. Cela facilite la construction de chaînes 
complexes en interpolant des valeurs de variables ou d'expressions directement
dans la chaîne.