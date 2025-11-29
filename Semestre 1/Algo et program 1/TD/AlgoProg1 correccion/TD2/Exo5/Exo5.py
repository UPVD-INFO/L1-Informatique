'''ROle: Demander deux nombres et sans faire le produit savoir si le resultat sera positif nulle ou negatif
Variables:
 n1,n2 entier
 '''

n1= int(input("Donne moi le premier nombre= ")) #On demande les valeur
n2= int(input("Donne moi le deuxieme nombre= "))

if n1 == 0:
    if n2 == 0:
        print("Le resultat est nulle") #On determine tout les posibilite d'un resultat nulle
    else:
        print("Le resultat est nulle")
else:
    if n2 == 0:
        print("Le resultat est nulle")

if n1 > 0:
    if n2 > 0:
        print("Le resultat est positive") #On determine tout les possibilite d'un resultat positive et negative
    else:
        if n2 < 0:
            print("Le resultat est negative")
else:
    if n2 > 0:
        if n1 != 0:
            print("Le resultat est negative")
    else:
        if n2 < 0:
            if n1 != 0:
                print("Le resultat est positive")
    
        
    
