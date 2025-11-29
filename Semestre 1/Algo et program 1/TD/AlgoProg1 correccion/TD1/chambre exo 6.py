#Role: Créer un algorithme qui permet d'avoir les dimensions de la chambre et permet de donner le cout annuel et mensuel
#Variables:
#D entier
#l entier
#la entier
#h entier
#CA float/réel
#CM float/réel
#X entier
#Y int

l= int(input("Quel est la longueur de la chambre?\n"))
la= int(input("Quel est la largeur de la chambre?\n")) #On demande les dimensions de la chambre
h= int(input("Quel est la hauteur de la chambre?\n"))

D= l*la*h #On calcule la dimension grace aux valeurs données
print("votre chambre fait ", D ,"metre cube\n\n") #petit recap
X= int(input("Combien vous payez l'electricite par mettre cube?\n")) #ici on cherche a definir nos X et Y cad a savoir combien de mois on paye dans l'année et cmb on paye au mois (grace a un calcul apres)
Y= int(input("Pendant combien de mois dans l'année?\n"))

CA= D*X*Y
CM= CA/12

print("Dans annuellement vous payez ", CA ,"euros et au mois vous payez", CM ,"euros.")
#Affiche le message resumant toute la fin et en donnant les valeurs demandées et necessaires.
