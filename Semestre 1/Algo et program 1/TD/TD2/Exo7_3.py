'''Role: Savoir si une année est bisextile en utilisant des operateurs logiques
Variables:
annee: entier
'''
from math import *

annee = int(input("Quel est l'annee= "))
a1 = annee
a2 = annee
while annee < 1582:
    print("l'annee ne peut pas etre calcule")

    annee = int(input("Quel est l'annee= "))
    
#Savoir si l'annee est bisextile ou non
    
if (annee % 4) == 0 and (annee % 100) != 0 or (annee % 400) == 0:
    print(f"l'annee {annee} est bisextile")
else:
    print(f"l'annee {annee} est pas bisextile")
    # On determine la prochaine annee bisextile
    ##while not((annee % 4) == 0) or not((annee % 100) != 0) and not((annee % 400) == 0):
    ##        annee = annee + 1
    ##print(f"l'annee la plus proche {annee}")

    while not((a1 % 4) == 0) or not((a1 % 100) != 0) and not((a1 % 400) == 0):
        a1 = a1 + 1

    while not((a2 % 4) == 0) or not((a2 % 100) != 0) and not((a2 % 400) == 0):
        a2 = a2 - 1

    if abs(a1 - annee) < abs(a2 - annee):
        print(f"L'annee la plus proche est {a1}")

    if abs(a1 - annee) > abs(a2 - annee):
        print(f"L'annee la plus proche est {a2}")

    if abs(a1 - annee) == abs(a2 - annee):
        print(f"Les annee les plus proche sont {a1} et {a2}")    

