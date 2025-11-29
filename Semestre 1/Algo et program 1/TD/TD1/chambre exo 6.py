#Role: Créer un algorithme qui permet d'avoir les dimensions de la chambre et permet de donner le cout annuel et mensuel
#Variables:
#D entier
#X entier
#Y entier
#Z entier
#CA float/réel
#CM float/réel
#E entier
#A int

X= int(input("Quel est la longueur de la chambre?\n"))
Y= int(input("Quel est la largeur de la chambre?\n"))
Z= int(input("Quel est la hauteur de la chambre?\n"))

D= X*Y*Z
print("votre chambre fait ", D ,"metre cube\n\n") 
E= int(input("Combien vous payez l'electricite par mettre cube?\n"))
A= int(input("Pendant combien de mois dans l'année?\n"))

CA= D*E*A
CM= CA/12

print("Dans ce cas vous payez ", CM ,"euros par mois et puisque cela est valable que pour\n", A ,"mois dans l'année, alors votre cout annuel est de", CA,"euros")


