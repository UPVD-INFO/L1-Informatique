#Role: Changer les numeros entre eux mais sans de variable ttemporaire (intermediaire)
#Variables:
#X1 entier
#X2 entier
#X3 entier

X1= int(input("Saisissez la premiere valeur\n"))
X2= int(input("Saisissez la deuxieme valeur\n")) #On demande les trois valeurs a inverser
X3= int(input("Saisissez la troisieme valeur\n"))

print("Voici les valeurs au depart") #Introduction a la permutation

X1= X1+X2+X3
X2=X1-X2-X3
X3=X1-X2-X3 #Ici grace aux mathematiques on change les valeurs entre elles sans valeur intermediaire
X1=X1-X2-X3

print("Voici les valeurs a la fin", X1,X2,X3) #On affiche le resultat de la permutation
