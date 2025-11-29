#Role: Donner la valeur absolue d'un nombre
#Variables
#valeur entier
#VA entier

valeur= int(input("Donnez moi la valeur\n"))

if valeur >= 0:
    print("La valeur absolue est de", valeur)
else:
    VA= valeur*-1
    print("La valeur absolue est de", VA)
