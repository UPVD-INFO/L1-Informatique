#TD1

#EXERCICE 1
#1.1.1 
test <- 0
#1.1.2
autre <- 3
#1.1.3 
autre*5
#Non la valeur elle est pas dans environnement. Pour reutiliser le resultat
# il faut reecrire le calcul a nouveau dans l'operation souhaite
#1.1.4
numero <- 16
donnee <- 23
valeur <- (numero*7) + (donnee*4)
#1.1.5
print(valeur)

#EXERCICE 2
#1.2.1 ma methode a moi
vecteur_1 <- c(1,2,3,4,5) #c(1:5)
#1.2.2
vecteur_2 <- c(2,4,6,8,10,12,14) #c(seq(2,14,2))
#1.2.3
vecteur_2[2]

#EXERCICE 3
#1.3.1
nom <- "Modélisation"
#1.3.2
rien <- NA
#1.3.3
texte <- c("Cuscus","Tachin","Kebab")
#1.3.4
vrai_ou_faux <- c(TRUE,FALSE)
#1.3.5
print(vrai_ou_faux[1] & vrai_ou_faux[2])

#EXERCICE 4
#1.4.1
#is.numeric() indique si c'est un nombre. la fonction retourne un booleen
#as.numeric transforme une chaine de caracteres en valeur numerique
test <- "53"
valeur <- as.numeric(test)
#1.4.3
aucun_texte <- NA_character_
#1.4.4
un_entier <- as.integer(542.423)
#1.4.5
#la fonction as.character() converti toute valeur dans une chaine de caractere