#Role: Trouver la vitesse moyen grace a la saisie de 2 valeurs temps et distance
#Variables:
#D entier
#T entier
#V entier

D= int(input("Combien de distance vous avez parcourue?\n"))
T=int(input("Combien de temps vous aviez mis?\n")) #On demande la distance et le temps en minutes

H= T/60 #On transforme les minutes en heures
V= D/H #on procede au calcul de la vitesse moyenne
#On arrondie le resultat au dixieme pres
print("Votre vitesse moyenne etait de", "{:.1f}".format(V) ,"km/h")

#On affiche le resultat arrondie aux dixieme pres
"'
