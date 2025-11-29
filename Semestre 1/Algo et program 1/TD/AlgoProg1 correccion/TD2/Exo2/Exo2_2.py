#Role: Créer un algorithme qui renvoie la valeur absolue d'un nombre
#Variabkes:
#valeur entier
#VA entier

valeur= int(input("Donne moi la valeur\n")) #On demande la valeur absolue

if valeur >= 0:
    print("La valeur absolue de", valeur ,"est", valeur)
if valeur < 0:
    VA= valeur*-1 #On calcule pour tourner la valeur dans son absolue
    print("La valeur absolue de", valeur ,"est", VA)
