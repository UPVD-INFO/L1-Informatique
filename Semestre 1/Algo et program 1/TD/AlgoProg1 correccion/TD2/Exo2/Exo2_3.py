#Role: ecrire un programme qui prend 2 valeurs entieres et affiche leur maximum
#Variables:
#v1 entier
#v2 entier


v1= int(input("Donne moi la premiere valeur\n"))
v2= int(input("Donne moi la deuxieme valeur\n")) #On demande les valeurs

if v1 > v2:
    print("Le maximum est", v1)

if v1 < v2:  #On les compares
    print("Le maximum est", v2)
#On affiche le resultat
